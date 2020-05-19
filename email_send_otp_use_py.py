import random
import smtplib
import tkinter as tk
from tkinter import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def CreateWidget():
    emailLabel = Label(root, text ="Enter Your Email_ID : ", bg = "Deepskyblue3")
    emailLabel.grid(row= 0, column = 1, padx = 5, pady = 5)
    
    emailEntry = Entry(root, textvariable = emailid, width =30)
    emailEntry.grid(row= 0, column = 2, padx = 5, pady = 5)
    
    sendOTPbutton = Button(root, text ="Send OTP", command = sendOTP, width =20)
    sendOTPbutton.grid(row= 0, column = 3, padx = 5, pady = 5)

    root.msgLabel = Label(root,bg = "deepskyblue3")
    root.msgLabel.grid(row=0, column=1, padx=5, pady=5,columnspan = 30)

    otpLabel = Label(root, text="Enter The OTP: ", bg= "deepskyblue3")
    otpLabel.grid(row = 2, column =2, padx=5, pady=5)

    root.otpEntry = Entry(root, textvariable=otp, width=30, show="*")
    root.otpEntry.grid(row=2, column=2, padx=5, pady=5)

    validOTPbutton = Button(root, text="Validate OTP", command = validOTP, width=20)
    validOTPbutton.grid(row=2, column=3, padx=5, pady=5)

    root.otpLabel= Label(root, bg="deepskyblue3")
    root.otpLabel.grid(row=3, column=1, padx=5, pady=5, columnspan=30)

def sendOTP():
    numbers = "0123456789"
    root.genOTP = ""
    receiverEmail = emailid.get()

    for i in range(6):
        root.genOTP += numbers[int(random.random()*10)]
    otpMSG = "Your OTP Is :" + root.genOTP

    message = MIMEMultipart()
    message['FROM'] = "OTP VALIDATOR (Python_Scripts)"
    message['To'] = receiverEmail
    message['Subject'] = "OTP VALIDATION"
    message.attach(MIMEText(otpMSG))

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login("sender's email-id", "sender's password")
    smtp.sendmail("sender's email-id", receiverEmail, message.as_string())
    smtp.quit()

    receiverEmail= '{}********{}'.formate(receiverEmail[0:2], receiverEmail[-10:])
    root.msgLabel.config(text = "OTP has been to SENT To"+ receiverEmail)

def validOTP():
    userInputOTP = otp.get()
    systemOTP = root.genOTP

    if userInputOTP == systemOTP:
        root.otpLabel.config(text="OTP Validated Successfully")
    else:
        root.otpLabel.config(text = "Inavalid OTP")

root = tk.Tk()

root.title("EmailOTP")
root.resizable(False, False)
root.config(background = "deepskyblue3")

emailid = StringVar()
otp = StringVar()

root.mainloop()
