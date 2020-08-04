from tkinter import *
from chatterbot import ChatBot
import tkinter.font as font
from chatterbot.trainers import ListTrainer
import os
import pyttsx3
import speech_recognition as sr
import win32api

root = Tk()
root.title("CHATBOT")
root.configure(bg='#1b1c25')

img = PhotoImage(file="chat3.png")

PhotoL = Label(root ,image=img)

PhotoL.grid(row=0, column=0)
bot=ChatBot("Friday")
tr=ListTrainer(bot)

kk=pyttsx3.init()
kk.setProperty('rate', 100)

voices = kk.getProperty('voices')

kk.setProperty('voice',voices[1].id)



chats=open('chat.txt','r').readlines()
tr.train(chats)

def send():
    
    
    

    while True:
        #    text=input(name+':')
        query=e.get()

        if(query=="exit"):
            
            root.destroy()
            return
        try:
      
 
             txt.insert(END,'You: '+str(query)+'\n\n')  
             response=bot.get_response(query)
             kk.say(response)
             txt.insert(END,'Friday:'+str(response)+'\n\n')
             kk.runAndWait()
        except:
            response=bot.get_response("sorry")
            kk.say(response)
            txt.insert(END,'Friday:'+str(response)+'\n\n')
            kk.runAndWait()
         # txt.insert(END,"\n"+send)
        e.delete(0,END)
        break


myFont = font.Font(family='Merriweather', size=20, weight='bold')

txt=Text(root,bg="#1f4068",fg="#ebecf1")
txt.grid(row=1,column=0,columnspan=2)
txt['font'] = myFont

txt.insert(END,"\n Friday: Hello\n\n")

e=Entry(root,width=100,bg="#1f4068",fg="#ebecf1")
e['font'] = myFont
e.grid(row=2,column=0)


response=Button(root,text="Send",command=send,bg="#1f4068",fg="#ebecf1")
response.grid(row=2,column=1)
response['font'] = myFont



root.mainloop()





















