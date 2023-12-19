from email.message import EmailMessage
import smtplib
import os

email_password = "Uff2021..*"
sender_email_address = "agudelojairo@hotmail.com"

def correo_usuarios(mensaje, Email, empresa_Idin, perfil, habilitado):
  email_subject = "Correo de prueba plataforma PODER" 
  receiver_email_address = Email 
  email_smtp = "smtp.office365.com" 

  # Create an email message object 
  message = EmailMessage() 

  # Configure email headers 
  message['Subject'] = email_subject 
  message['From'] = sender_email_address 
  message['To'] = receiver_email_address
  
  # Set email body text 
  URL = mensaje +": " + "http://127.0.0.1:8432/usuario/registro?email=" + receiver_email_address + "&nombre=" + "&empresa=" + empresa_Idin + "&perfil=" + perfil + "&habilitado=" + str(habilitado)
  print(URL)
  message.set_content(URL) 

  # Set smtp server and port 
  server = smtplib.SMTP(email_smtp, '587') 
  
  # Identify this client to the SMTP server 
  server.ehlo() 

  # Secure the SMTP connection 
  server.starttls() 

  # Login to email account 
  server.login(sender_email_address, email_password) 

  # Send email 
  server.send_message(message) 

  # Close connection to server 
  server.quit()
  


  # Secure the SMTP connection 
  server.starttls() 

  # Login to email account 
  server.login(sender_email_address, email_password) 

  # Send email 
  server.send_message(message) 

  # Close connection to server 
  server.quit()
