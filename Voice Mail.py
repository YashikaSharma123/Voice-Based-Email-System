import pyttsx3 
import speech_recognition as sr 
import os 
import smtplib 
import datetime 

engine = pyttsx3.init('sapi5')#sapi5 parameter which help in initialization.and initialize the lib

voices = engine.getProperty('voices')#get property mai voices ko call krra hai

print(voices[0].id)#provide id to every voice

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)#it help in speaking
    engine.runAndWait()# run krega and wait krega jab tkk koi key ya shut down ni krte

def wishMe():
    hour = int(datetime.datetime.now().hour)#datetime module mai datetime cls mai now funct/method mai hour ko int mai dala
    if hour>=0 and hour<12:
        speak("Good Morning, My loard")

    elif hour>=12 and hour<18:
        speak("Good Afternoon, My loard")

    else:
        speak("Good Evening, My loard")

    speak("I am XYZ. Please tell me how may I help you")


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 #wait 
        r.energy_threshold=200 # for min. audio energy to consider for recording
        audio = r.listen(source)#convert into audiodata
        print("llll")

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')#conert it into eng
        print(f"User said: {query}\n")#print query

    except Exception as e:
        print(e)#if exception occur  it print
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)#bydefault
    server.ehlo()#it use to check the connection is establish or not
    print("Login work")
    server.starttls()#Put the SMTP connection in TLS (Transport Layer Security) mode. All SMTP commands that follow will be encrypted. You should then call ehlo() again.
    server.login("sender@gmail.com","Password")
    server.sendmail("sender@gmail.com", to, content)#sender reciver content
    server.quit()
def checkmail():
    EMAIL = 'sender@gmail.com'
    PASSWORD = 'password'
    SERVER = 'imap.gmail.com'

# connect to the server and go to its inbox
    mail = imaplib.IMAP4_SSL(SERVER)
    mail.login(EMAIL, PASSWORD)
# we choose the inbox but you can select others
    mail.select('inbox')
    status, response = mail.search(None, 'UNSEEN')
    unread_msg_nums = response[0].split()
    print(len(unread_msg_nums))
    for i in unread_msg_nums:
        status, data = mail.search(None, 'UNSEEN')
        mail_ids = []
        for block in data:
            mail_ids += block.split()
        for i in mail_ids:
            status, data = mail.fetch(i, '(RFC822)')
            for response_part in data:
                if isinstance(response_part, tuple):
                    message = email.message_from_bytes(response_part[1])
                    mail_from = message['from']
                    mail_subject = message['subject']
                    if message.is_multipart():
                        mail_content = ''
                        for part in message.get_payload():
                            if part.get_content_type() == 'text/plain':
                                mail_content += part.get_payload()
                    else:
                # if the message isn't multipart, just extract it
                        mail_content = message.get_payload()
                        
                    speak("Mail is from "+mail_from)
                    print(f'From: {mail_from}')
                    if mail_subject=='NoneType':
                        speak("Their is no subject")
                    else:
                        speak('Subject is' +mail_subject) 
                        print(f'Subject: {mail_subject}')
                        
            # and then let's show its result
                    #speak("Mail is from "+mail_from)
                    #print(f'From: {mail_from}')
                    #speak('Subject is' +mail_subject) 
                    #print(f'Subject: {mail_subject}')
                    speak('Mail body is'+mail_content)
                    print(f'Content: {mail_content}')



if __name__== "__main__": #it call by itself
    wishMe()
    while True:
  
        query = takeCommand().lower()#convert into lower case string


        if 'the time' in query:
            strtime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime}")
        elif 'check mail' in query:
            try:
                checkmail()
            except Exception as e:
                print(e)
                speak("Sorry my loard. I am not able to send get email ")


        elif 'send email' in query:
            try:
                speak("What should I send? ")
                content = takeCommand()
                print(content)
                speak("Do you wanna send this mail new or old user")

                b=takeCommand()
                b=str(b)
                print("Print: ",b)
                
                if b=="new":               
                    print(b)
                    speak("whom are you want to send this mail")
                    mail=takeCommand()
                    if "dot" in mail:
                        mail.replace("dot",".")
                    mail="".join(mail.split())
                    to=(mail+'@gmail.com')
                    sendEmail(to,content)
                    speak('Email has been new sent!')
                elif b=="old":              
                    print(b)
                    speak("You can send this mail single or all user also") 
                    to = {"Name":"xyz1@gmail.com","all":["xyz1@gmail.com","xyz2@gmail.com","xyz3@gmail.com"]}
                    speak("whom are you want to send this mail")
                    send=takeCommand()    
                    send=str(send)
                    print(send)
                    to=to[send]
                    sendEmail(to,content)
                    speak('Email has been old sent!')
                

    
            except Exception as e:
                print(e)
                



