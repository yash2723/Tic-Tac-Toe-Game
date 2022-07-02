from tkinter import *
from tkinter import messagebox
from pygame import mixer
from tkinter import ttk

def active1(event):
    ent_name1.focus()

def active2(event):
    ent_name2.focus()

def click1():
    #mixer.music.load("Click Click.mp3")
    #mixer.music.play()
    if btn1['text']==" ":
        if turn.get()%2==0 :
            btn1.config(text="0")
            status.config(text=name1.get() + " is your turn")
        else:
            btn1.config(text="x")
            status.config(text=name2.get() + " is your turn")
        a=turn.get()
        a=a+1
        turn.set(a)
        check()

def click2():
    #mixer.music.load("Click Click.mp3")
    #mixer.music.play()
    if btn2['text']==" ":
        if turn.get()%2==0 :
            btn2.config(text="0")
            status.config(text=name1.get() + " is your turn")
        else:
            btn2.config(text="x")
            status.config(text=name2.get() + " is your turn")
        a=turn.get()
        a=a+1
        turn.set(a)
        check()

def click3():
    #mixer.music.load("Click Click.mp3")
    #mixer.music.play()
    if btn3['text']==" ":
        if turn.get()%2==0 :
            btn3.config(text="0")
            status.config(text=name1.get() + " is your turn")
        else:
            btn3.config(text="x")
            status.config(text=name2.get() + " is your turn")
        a=turn.get()
        a=a+1
        turn.set(a)
        check()

def click4():
    #mixer.music.load("Click Click.mp3")
    #mixer.music.play()
    if btn4['text']==" ":
        if turn.get()%2==0 :
            btn4.config(text="0")
            status.config(text=name1.get() + " is your turn")
        else:
            btn4.config(text="x")
            status.config(text=name2.get() + " is your turn")
        a=turn.get()
        a=a+1
        turn.set(a)
        check()

def click5():
    #mixer.music.load("Click Click.mp3")
    #mixer.music.play()
    if btn5['text']==" ":
        if turn.get()%2==0 :
            btn5.config(text="0")
            status.config(text=name1.get() + " is your turn")
        else:
            btn5.config(text="x")
            status.config(text=name2.get() + " is your turn")
        a=turn.get()
        a=a+1
        turn.set(a)
        check()

def click6():
    #mixer.music.load("Click Click.mp3")
    #mixer.music.play()
    if btn6['text']==" ":
        if turn.get()%2==0 :
            btn6.config(text="0")
            status.config(text=name1.get() + " is your turn")
        else:
            btn6.config(text="x")
            status.config(text=name2.get() + " is your turn")
        a=turn.get()
        a=a+1
        turn.set(a)
        check()

def click7():
    #mixer.music.load("Click Click.mp3")
    #mixer.music.play()
    if btn7['text']==" ":
        if turn.get()%2==0 :
            btn7.config(text="0")
            status.config(text=name1.get() + " is your turn")
        else:
            btn7.config(text="x")
            status.config(text=name2.get() + " is your turn")
        a=turn.get()
        a=a+1
        turn.set(a)
        check()

def click8():
    #mixer.music.load("Click Click.mp3")
    #mixer.music.play()
    if btn8['text']==" ":
        if turn.get()%2==0 :
            btn8.config(text="0")
            status.config(text=name1.get() + " is your turn")
        else:
            btn8.config(text="x")
            status.config(text=name2.get() + " is your turn")
        a=turn.get()
        a=a+1
        turn.set(a)
        check()

def click9():
    #mixer.music.load("Click Click.mp3")
    #mixer.music.play()
    if btn9['text']==" ":
        if turn.get()%2==0 :
            btn9.config(text="0")
            status.config(text=name1.get() + " is your turn")
        else:
            btn9.config(text="x")
            status.config(text=name2.get() + " is your turn")
        a=turn.get()
        a=a+1
        turn.set(a)
        check()

def check():
    '''
    if btn1['text']==btn2['text']==btn3['text']:
        btn1['text']='---'
        btn2['text']='---'
        btn3['text']='---'
        #or btn1['text']==btn4['text']==btn7['text'] or btn3['text']==btn6['text']==btn9['text'] or btn7['text']==btn8['text']==btn9['text'] or btn1['text']==btn5['text']==btn9['text'] or btn3['text']==btn5['text']==btn7['text'] :
    '''

    if btn1['text']==btn2['text']==btn3['text']=='x' or btn1['text']==btn4['text']==btn7['text']=='x' or btn3['text']==btn6['text']==btn9['text']=='x' or btn7['text']==btn8['text']==btn9['text']=='x' or btn1['text']==btn5['text']==btn9['text']=='x' or btn3['text']==btn5['text']==btn7['text']=='x' or btn4['text']==btn5['text']==btn6['text']=='x' or btn2['text']==btn5['text']==btn8['text']=='x' :
        mixer.music.load("end-music.mp3")
        mixer.music.play()
        messagebox.showinfo("Result","Player " + name1.get() + " is Win . Congratulations ! ")
        root.destroy()

    if btn1['text']==btn2['text']==btn3['text']=='0' or btn1['text']==btn4['text']==btn7['text']=='0' or btn3['text']==btn6['text']==btn9['text']=='0' or btn7['text']==btn8['text']==btn9['text']=='0' or btn1['text']==btn5['text']==btn9['text']=='0' or btn3['text']==btn5['text']==btn7['text']=='0' or btn4['text']==btn5['text']==btn6['text']=='0' or btn2['text']==btn5['text']==btn8['text']=='0' :
        mixer.music.load("end-music.mp3")
        mixer.music.play()
        messagebox.showinfo("Result","Player " + name2.get() + " is Win . Congratulations ! ")
        root.destroy()

    if btn1['text']!=" " and btn2['text']!=" " and btn3['text']!=" " and btn4['text']!=" " and btn5['text']!=" " and btn6['text']!=" " and btn7['text']!=" " and btn8['text']!=" " and btn9['text']!=" ":
        mixer.music.load("end-music.mp3")
        mixer.music.play()
        messagebox.showinfo("Result","Match has been tied . Try Next Time ! ")
        root.destroy()

def start():
    temp.set(1)
    import time
    progressbar['value']=10
    load['text']=" Loading... 10% " 
    root1.update_idletasks()
    time.sleep(3)

    progressbar['value']=25
    load['text']=" Loading... 25% " 
    root1.update_idletasks()
    time.sleep(2)

    progressbar['value']=35
    load['text']=" Loading... 35% " 
    root1.update_idletasks()
    time.sleep(1)

    progressbar['value']=40
    load['text']=" Loading... 40% " 
    root1.update_idletasks()
    time.sleep(4)
    
    progressbar['value']=50
    load['text']=" Loading... 50% " 
    root1.update_idletasks()
    time.sleep(2)

    progressbar['value']=65
    load['text']=" Loading... 65% " 
    root1.update_idletasks()
    time.sleep(3)

    progressbar['value']=80
    load['text']=" Loading... 80% " 
    root1.update_idletasks()
    time.sleep(1)

    progressbar['value']=90
    load['text']=" Loading... 90% " 
    root1.update_idletasks()
    time.sleep(2)

    progressbar['value']=100
    load['text']=" Loading... 100% " 
    root1.update_idletasks()
    time.sleep(1)

    root1.destroy()

root1=Tk()
root1.title("ProgressBar")
root1.geometry("400x200")
#root1.maxsize(40
root1.config(background="white")
root1.wm_iconbitmap("game.ico")

temp=IntVar()
temp.set(0)

mixer.init()
mixer.music.load("entry-music.mp3")
mixer.music.play(loops=10)

top_frame=Frame(root1,background="white")
top_frame.grid(pady=40)

progressbar=ttk.Progressbar(top_frame,orient=HORIZONTAL,length=300,mode='determinate')
progressbar.grid(padx=50,pady=10)

btn=Button(top_frame,text="Ready",command=start)
btn.grid(pady=10)

bottom_frame=Frame(root1,background="medium purple",width=350,height=30)
bottom_frame.grid()

load=Label(bottom_frame,text=" Loading... 0% ")
load.grid(padx=160,pady=5)

root1.mainloop()

if temp.get()==0:
    exit()

root=Tk()

turn=IntVar()
turn.set(1)

mixer.init()
mixer.music.load("music.mp3")
mixer.music.play(loops=20)

root.title("Tic-Tac-Toi")
root.geometry("500x570")
root.maxsize(500,570)
root.minsize(500,570)
root.config(background="black")
root.wm_iconbitmap("game.ico")

top_frame=Frame(root,background="white",width=500,height=75)
top_frame.grid(pady=10)

title=Label(top_frame,text="Tic - Tac - Toi",font=" Arial 50 bold")
title.grid(padx=30)

info_frame=Frame(root,background="cyan",width=500,height=100)
info_frame.grid(pady=10)

name1=StringVar()
name1.set("X")
name2=StringVar()
name2.set("0")

lab_name1=Label(info_frame,text="Enter the name of first person : ")
lab_name1.grid(row=1,column=1,pady=20,padx=10)
lab_name1.bind('<Button-1>',active1)
ent_name1=Entry(info_frame,textvariable=name1)
ent_name1.grid(row=1,column=2,pady=20,padx=10)

lab_name2=Label(info_frame,text="Enter the name of second person : ")
lab_name2.grid(row=2,column=1,pady=20,padx=10)
lab_name2.bind('<Button-1>',active2)
ent_name2=Entry(info_frame,textvariable=name2)
ent_name2.grid(row=2,column=2,pady=20,padx=10)

main_frame=Frame(root,background="yellow",width=500,height=100)
main_frame.grid(pady=10)

btn1=Button(main_frame,text=" ",width=10,height=5,command=click1)
btn1.grid(row=1,column=1)

btn2=Button(main_frame,text=" ",width=10,height=5,command=click2)
btn2.grid(row=1,column=2)

btn3=Button(main_frame,text=" ",width=10,height=5,command=click3)
btn3.grid(row=1,column=3)

btn4=Button(main_frame,text=" ",width=10,height=5,command=click4)
btn4.grid(row=2,column=1)

btn5=Button(main_frame,text=" ",width=10,height=5,command=click5)
btn5.grid(row=2,column=2)

btn6=Button(main_frame,text=" ",width=10,height=5,command=click6)
btn6.grid(row=2,column=3)

btn7=Button(main_frame,text=" ",width=10,height=5,command=click7)
btn7.grid(row=3,column=1)

btn8=Button(main_frame,text=" ",width=10,height=5,command=click8)
btn8.grid(row=3,column=2)

btn9=Button(main_frame,text=" ",width=10,height=5,command=click9)
btn9.grid(row=3,column=3)

statusbar=Frame(root,background="yellow",width=500,height=50)
statusbar.grid()

status=Label(statusbar,text=name1.get() + " is your turn.",font="serifan 15 bold")
status.grid(padx=150,pady=8)

root.mainloop()


