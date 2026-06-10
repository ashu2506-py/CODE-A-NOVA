import smtplib
from email.message import EmailMessage

sender_address= "codewithcodex2106@gmail.com"
app_password="abrfmczyvbyksiig"

reciever=input("Enter reciever email:")
subject=input("Enter subject: ")
message=input("Enter message: ")

email=EmailMessage()

email["From"]=sender_address
email["To"]=reciever
email["Subject"]=subject

email.set_content(message)

try:

    smtp=smtplib.SMTP_SSL("smtp.gmail.com",465)

    smtp.login(sender_address,app_password)
    smtp.send_message(email)
    print("Email sent successfully")
    
    with open("Email-Services/logs.txt","a") as file:
        file.write(f"To: {reciever}\n")
        file.write(f"Subject: {subject}\n")
        file.write(f"Message: {message}\n")
        file.write("-"*40+"\n")
        

except Exception as e:
    print("Failed to send Email")
    print(e)
    

