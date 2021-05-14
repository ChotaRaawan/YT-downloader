from tkinter import *    #for GUI
from pytube import YouTube   #for youtube module

# defining the window
root = Tk()
root.configure(bg='#BEBEBE')
root.geometry('500x250')
root.resizable(0,0)
root.title("YouTube Downloader")


Label(root,text = 'Youtube Downloader', font ='Verdana 20 bold').pack()

# accepting link as a string
link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'Verdana 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)



#function for downloading video

def Downloader():
     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'Download Complete', font = 'arial 15').place(x= 180 , y = 210)


Button(root,text = 'Download', font = 'arial 15 bold' ,bg = 'green', padx = 2, command = Downloader).place(x=180 ,y = 170)



root.mainloop()
