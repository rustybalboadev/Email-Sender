import smtplib
import PySimpleGUI as sg
layout = [
    [sg.Text("Enter your Email here")],
    [sg.InputText("",key=("EMAIL_INPUT"))],
    [sg.Text("Enter your Email Password here")],
    [sg.InputText("",password_char='*',key=("EMAIL_PASSWORD_INPUT"))],
    [sg.Text("Enter their Email Here")],
    [sg.InputText("",key=("THEIR_EMAIL"))],
    [sg.Text("Enter your Message here")],
    [sg.Multiline("",key=("MSG"))],
    [sg.Button("Send"),sg.Button("Spam"),sg.Button("Help"),sg.Button("Close")]
    
]
def spam():
    your_email = value['EMAIL_INPUT']
    your_email_password = value['EMAIL_PASSWORD_INPUT']
    their_email = value['THEIR_EMAIL']
    your_msg = value['MSG']
    amount = sg.popup_get_text("How many times do you want to spam them?",title=("Spam Amount"))
    amount = int(amount)
    print(type(amount))
    print(amount)
    iteration = 0
    while iteration != amount:
        print(iteration)
        print(amount)
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(your_email, your_email_password)
        s.sendmail(your_email, their_email, your_msg)
        iteration += 1
window = sg.Window("Email Sender", layout)
while True:
    event, value = window.Read()
    your_email = value['EMAIL_INPUT']
    your_email_password = value['EMAIL_PASSWORD_INPUT']
    their_email = value['THEIR_EMAIL']
    your_msg = value['MSG']
    if event == "Close":
        break
    elif event == "Send":
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(your_email, your_email_password)
        s.sendmail(your_email, their_email, your_msg)   
    elif event == "Spam":
        spam()
    elif event == "Help":
        sg.popup("If the email won't send you might need to enable Less Secure App Access on your google account and then enable the login attempt. When using spam don't click anything after the popup goes away. Unless the program will crash!",title="Help!")    
