import os
from tkinter import *
from pygame import mixer
import tkinter.messagebox
from tkinter import filedialog

root = Tk()
mixer.init()


#menu bar====================
menubar=Menu(root)
root.config(menu=menubar)


#====================submenubar=========================
def browser_file():
    global filename
    filename = filedialog.askopenfilename()


submenubar=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File", menu=submenubar)
submenubar.add_command(label="Open" ,command=browser_file)
submenubar.add_command(label="Exit" ,command=root.destroy)


def about_us():
    tkinter.messagebox.showinfo('Music Player','If any error please Call or Email us.')


submenubar=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help", menu=submenubar)
submenubar.add_command(label="Contuct Us",command=about_us)



#root.geometry('500x400')
root.title("Music Player")
root.iconbitmap(r'title.ico')


statusbar=Label(root,text="Welcome To Music Player", height=5, relief=SUNKEN)
statusbar.pack(side=TOP,fill=X)

def play_btn():
    try:
        paused
    except NameError:
        try:
            mixer.music.load(filename)
            mixer.music.play()
            statusbar['text']="Playing" + ' ' + os.path.basename(filename)
        except:
            tkinter.messagebox.showerror('File Not Found!','Sorry Sir Could not find the file. Please check again.')
    else:
        mixer.music.unpause()
        statusbar['text']="Playing" + ' ' + os.path.basename(filename)

def stop_btn():
    mixer.music.stop()
    statusbar['text']="Stopped" + ' ' + os.path.basename(filename)

def pause_btn():
    global paused
    paused= TRUE
    mixer.music.pause()
    statusbar['text']="Paused" + ' ' + os.path.basename(filename)
         
def repeat_btn():
    mixer.music.rewind() 
    statusbar['text']="Playing" + ' ' + os.path.basename(filename)  
def set_vol(val):
    volume=int(val)/100
    mixer.music.set_volume(volume)

middlefram = Frame(root,pady=10)
middlefram.pack()

previoussongphoto = PhotoImage(file  = 'previous.png')
btnprevioussong = Button(middlefram, image=previoussongphoto, command=repeat_btn)
btnprevioussong.pack(side=LEFT,padx=10)

stopphoto = PhotoImage(file='stop.png')
btnstop = Button(middlefram, image=stopphoto, command=stop_btn)
btnstop.pack(side=LEFT,padx=10)

playphoto = PhotoImage(file='play.png')
btnplay = Button(middlefram, image=playphoto, command=play_btn)
btnplay.pack(side=LEFT,padx=10)

pausephoto = PhotoImage(file='pause.png')
btnpause = Button(middlefram, image=pausephoto, command=pause_btn)
btnpause.pack(side=LEFT,padx=10)

repeatphoto = PhotoImage(file='repeat.png')
btnrepeat = Button(middlefram, image=repeatphoto, command=repeat_btn)
btnrepeat.pack(side=LEFT,padx=10)

nextsongphoto = PhotoImage(file='next.png')
btnnextsong = Button(middlefram, image=nextsongphoto, command=repeat_btn)
btnnextsong.pack(side=LEFT,padx=10)

scaler=Scale(root,from_=0,to=100, orient=HORIZONTAL, width= 10, command= set_vol)
scaler.set(50)
mixer.music.set_volume(0.5)
scaler.pack(side=BOTTOM,fill=X,padx=15)




root.mainloop()
