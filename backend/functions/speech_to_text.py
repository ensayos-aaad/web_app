# Get rid of ALSA lib error messages in Linux
import platform

if  platform.system() == "Linux":
    from ctypes import CFUNCTYPE, c_char_p, c_int, cdll
    
    # Define error handler
    error_handler = CFUNCTYPE\
	(None, c_char_p, c_int, c_char_p, c_int, c_char_p)
    # Don't do anything if there is an error message
    def py_error_handler(filename, line, function, err, fmt):
      pass
    # Pass to C
    c_error_handler = error_handler(py_error_handler)
    asound = cdll.LoadLibrary('libasound.so')
    asound.snd_lib_error_set_handler(c_error_handler)
	
# Now define the voice_to_text() function for all platforms    


import speech_recognition as sr

speech = sr.Recognizer()

def voice_to_text(file):
    print("pasa por aca")
    audio_file = sr.AudioFile(file)
    with audio_file as source:
        #speech.adjust_for_ambient_noise(source)        
        try:
            audio = speech.record(source)
            transcript = speech.recognize_google(audio, language='es-CO')
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass        
        except sr.WaitTimeoutError:
            pass
    return transcript

if __name__ =='__main__':
    print("Test")
    text = voice_to_text("trabalenguas.wav")
    print(text)