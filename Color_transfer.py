from tkinter import *
from tkinter.font import Font
from PIL import ImageTk,Image
import PIL.Image, PIL.ImageTk
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import filedialog
from color_transfer import color_transfer
import numpy as np
import argparse
import cv2
import os
import time
import glob
import sys
import argparse
import datetime

fimg = 'Harish'
fimg2 = 'Kumawat'
some = 'some'
def sub(var):
	def show_image(title, image, width = 300):
		# resize the image to have a constant width, just to
		# make displaying the images take up less screen real
		# estate
		r = width / float(image.shape[1])
		dim = (width, int(image.shape[0] * r))
		resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
		# show the resized image
		cv2.imshow(title, resized)




	source = cv2.imread(fimg)
	target = cv2.imread(fimg2)
	transfer = color_transfer(source, target)

	'''if args["output"] is not None:
		cv2.imwrite(args["output"], transfer)'''
	show_image("Source", source)
	show_image("Target", target)
	show_image("Transfer", transfer)
	cv2.waitKey(0)
	choice=messagebox.askquestion("Confirmation","Save ?:")
	if choice=='yes':
		cv2.imwrite('color_change.jpg', transfer)
	else:
		print("you exit")
def open_file():
	global fimg
	result=filedialog.askopenfile(initialdir=os.getcwd()+"/dataset_images/",title="Select file",filetypes=(("text",".jpg"),("all file","*.*")))
	img=os.path.abspath(result.name)
	print(img)
	fimg = img
	print(fimg)

def open_file2():
	global fimg2
	result=filedialog.askopenfile(initialdir=os.getcwd()+"/dataset_images/",title="Select file",filetypes=(("text",".jpg"),("all file","*.*")))
	img1=os.path.abspath(result.name)
	fimg2 =img1

root = Tk()
root.title("Color_transfer")

topframe=Frame(root)
my_font=Font(family="Rekha",size=30,weight="bold",slant="italic")
label=Label(root,text="color_transfer_images",font=my_font,foreground="red").pack()
topframe.pack(side=TOP)

bottomframe=Frame(root)
my_font=Font(family="Rekha",size=30,weight="bold",slant="italic")
label=Label(bottomframe,text="Select Image 1 --->",font=my_font,foreground="#283142").grid(row=0)


Bt4=Button(bottomframe,text="Select file 1",width=10,command=open_file,activebackground="green",bg='#6E9AFF')
Bt4.grid(row=0,column=1,pady=5,padx=15)

my_font=Font(family="Rekha",size=30,weight="bold",slant="italic")
label=Label(bottomframe,text="Select Image 2 --->",font=my_font,foreground="#283142").grid(row=1)
Bt5=Button(bottomframe,text="Select file 2",width=10,command=open_file2,activebackground="green",bg='#6E9AFF')
Bt5.grid(row=1,column=1,pady=5,padx=15)
boldFont = Font (size = 10, weight = "bold")
Bt6=Button(bottomframe,text="Submit",width=10,command=lambda: sub(some),activebackground="red",bg='green',font = boldFont,fg='white')
Bt6.grid(columnspan=2,pady=20)
bottomframe.pack()


root.geometry()
root.mainloop()
