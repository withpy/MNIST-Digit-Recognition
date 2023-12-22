import tkinter as tk
import win32gui
from PIL import ImageGrab, Image,ImageDraw
import numpy as np
import joblib
import os
import matplotlib.pyplot as plt


os.chdir('D:\Python\py\Machine Learning\Project 2 digit recognition using MNIST')

root=tk.Tk()
root.geometry('700x400')  
model=joblib.load('clf.joblib')


def draw_fun(event):
    x=event.x
    y=event.y
    r=5
    canvas.create_rectangle(x-r,y-r,x+r,y+r,fill='black')
    draw.line([x-r,y-r,x+r,y+r],fill='black',width=8)
def hand_writing():
    x=canvas.winfo_id()
    # print(x)
    rect=win32gui.GetWindowRect(x)
    rect=list(rect)
    rect[0],rect[1]=rect[0]+100,rect[1]+10
    rect[2],rect[3]=rect[2]+100,rect[3]+100
    img=ImageGrab.grab(rect)
    print(rect)
    # print(img)
    predict_fun(img,image1)
def predict_fun():
    image=np.invert(image1.resize((28,28))).reshape([1,-1])
    var.set(*model.predict(image))
    label.config(font='lucida 80')
def clear_fun():
    canvas.delete('all')
    w=image1.width
    h=image1.height
    draw.rectangle([0,0,w,h],fill='white')

var=tk.StringVar()
var.set('Predicted\nValue')
canvas=tk.Canvas(root,bg='white',height=300,width=300,highlightbackground='black')
canvas.grid(padx=20,pady=20)
label=tk.Label(root,textvariable=var,font='lucida 50')
label.grid(row=0,column=1,padx=20,pady=20)
clear_button=tk.Button(root,text='Clear',command=clear_fun)
clear_button.grid(row=1,column=0)
recognise_button=tk.Button(root,text='Recognise',command=predict_fun)
recognise_button.grid(row=1,column=1)
canvas.bind('<B1-Motion>',draw_fun)

image1=Image.new('L',(300,300),(255))
draw=ImageDraw.Draw(image1)

root.mainloop()
# image1.show()
plt.imshow(np.invert(image1.resize((28,28))))
# plt.show()
