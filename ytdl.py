#Youtube downloader in python3
# @python.hub insta
#import tkinter
from tkinter import *
#import the YouTube module from pytube
from pytube import YouTube
#initialize tkinter
init = Tk()
#specify the dimensions and title of the GUI
init.geometry('400x350')
init.title('YouTube video downloader application')
#download defined for execution without errors
def download():
    try:
        myVar.set('Downloading...')
        init.update()
        YouTube(link.get()).streams.first().download()
        link.set('Video downloaded succesfully.')
    except Exception as e:
        myVar.set('Mistake')
        init.update()
        link.set('Enter correct link.')
#label widget to welcome the user
Label(init,text="Welcome to YouTube\n Downloader Application",\
      font='Consolas 15 bold').pack()
#first StringVar variable defined
myVar = StringVar()
#set the default text
myVar.set("Enter the link below:")
#Entry widget for the user to enter the url 
Entry(init, textvariable=myVar, width=40).pack(pady=10)
#second StringVar type variable to get the link for download
link = StringVar()
#entry widget to get the link
Entry(init, textvariable=link, width=40).pack(pady=10)
#button to initiate the download
Button(init, text="Download video", command=download).pack()
#to just keep the loop going as long as the GUI is open
init.mainloop()
