# Aplicacion Web


Crear el entorno virtual:



Repositorio con la app...

Para que funcione la aplicación se necesita:
* fastapi
* uvicorn
* PyAudio (Opcional)
* SpeechRecognition
* python-multipart

Si crea el entorno virtual por primera vez y no tiene el archivo ```requirements.txt```; dentro de este ejecute los siguientes comandos:

```
pip install fastapi
pip install "uvicorn[standard]"
pip install SpeechRecognition
pip install PyAudio
pip install python-multipart
pip install pandas
```

Por otro lado, en este caso se proporcina el archivo [requirements.txt](backend/requirements.txt) dentro de la carpeta [backend](backend/), lo primero que tiene que hacer es ingresar a esta carpeta:

```
cd backend
```

Y luego ejecutar los siguientes comandos:

```
python -m venv test_env
.\test_env\Scripts\activate 
pip install -r requirements.txt
```

Finalmente, para probar la aplicacion ejecute el comando:

```
uvicorn main:app --reload
```

## Instalación


```
python -m venv test_env
.\test_env\Scripts\activate 
pip install -r requirements.txt
```

## Referencias

* https://github.com/PacktPublishing/ChatGPT-Voice-Powered-ChatBot-Build-with-React-and-FastAPI/tree/main
* https://realpython.com/python-csv/
* https://realpython.com/python-classes/
* https://realpython.com/inheritance-composition-python/
* https://github.com/milaan9/06_Python_Object_Class
* https://cs50.harvard.edu/x/2023/problems/6/
* https://github.com/IrvKalb/Object-Oriented-Python-Code/
* https://realpython.com/pandas-read-write-files/
* https://realpython.com/quizzes/python-csv/viewer/
* https://realpython.com/python-interview-problem-parsing-csv-files/
