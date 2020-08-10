

from tkinter import *
from pytube import YouTube

init = Tk()

init.geometry('400x350')
init.title('YouTube video downloader application')

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

Label(init,text="Welcome to YouTube\n Downloader Application",font='Consolas 15 bold').pack()
myVar = StringVar()
myVar.set("Enter the link below:")
Entry(init, textvariable=myVar, width=40).pack(pady=10)
link = StringVar()
Entry(init, textvariable=link, width=40).pack(pady=10)
Button(init, text="Download video", command=download).pack()
init.mainloop()