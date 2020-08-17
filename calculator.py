from tkinter import *

root=Tk()
root.title("Calculator")
root.geometry("310x460")

############################################################


countertext = StringVar()


def click(event):
	text = event.widget.cget('text')
	print(text)
	if text == "=":
		try:
			if countertext.get().isdigit():
				value = int(countertext.get())
			else:
				value = eval(counter.get())

			countertext.set(value)
			counter.update()
		except:
			countertext.set("ERROR")

	elif text == "AC":
		countertext.set("")
		counter.update()


	else:
		countertext.set(countertext.get() + text)




############## GUI ######################

########## Base  DISPLAY ##############

display = Frame(root)
display.place(x=5,y=10,height=150,width=300)

counter = Entry(display,textvariable=countertext,font=('digital-7',30,'bold'))
counter.pack(fill=X,ipady=20)



########## KEYPAD ###########
##################################
aci = PhotoImage(file='res\\ac.png')
zimg = PhotoImage(file='res\\0.png')
onimg = PhotoImage(file='res\\1.png')
twimg = PhotoImage(file='res\\2.png')
thrimg = PhotoImage(file='res\\3.png')
fimg = PhotoImage(file='res\\4.png')
fvimg = PhotoImage(file='res\\5.png')
sximg = PhotoImage(file='res\\6.png')
seimg = PhotoImage(file='res\\7.png')
eimg = PhotoImage(file='res\\8.png')
nimg = PhotoImage(file='res\\9.png')

doimg = PhotoImage(file='res\\dot.png')
eqimg = PhotoImage(file='res\\=.png')
pimg = PhotoImage(file='res\\+.png')
mimg = PhotoImage(file='res\\-.png')
mulimg = PhotoImage(file='res\\x.png')
dvimg = PhotoImage(file='res\\divide.png')

#########################################

keypad = Frame(root)
keypad.place(x=5,y=80,height=370,width=300)

ac = Button(keypad,text="AC",bd=0,image=aci)
ac.bind("<Button-1>",click)
ac.grid(row=0,columnspan=4,pady=7)



######## ROW 1 ########


seven = Button(keypad,text="7",bd=0,image=seimg)
seven.bind("<Button-1>",click)
seven.grid(row=1,column=0,padx=4,pady=4)

eight = Button(keypad,text="8",bd=0,image=eimg)
eight.bind("<Button-1>",click)
eight.grid(row=1,column=1,padx=4,pady=4)

nine = Button(keypad,text="9",bd=0,image=nimg)
nine.bind("<Button-1>",click)
nine.grid(row=1,column=2,padx=4,pady=4)

plus = Button(keypad,text="+",bd=0,image=pimg)
plus.bind("<Button-1>",click)
plus.grid(row=1,column=3,padx=4,pady=4)


######## ROW 2 ########

four = Button(keypad,text="4",bd=0,image=fimg)
four.bind("<Button-1>",click)
four.grid(row=2,column=0,padx=4,pady=4)

five = Button(keypad,text="5",bd=0,image=fvimg)
five.bind("<Button-1>",click)
five.grid(row=2,column=1,padx=4,pady=4)

six = Button(keypad,text="6",bd=0,image=sximg)
six.bind("<Button-1>",click)
six.grid(row=2,column=2,padx=4,pady=4)

minus = Button(keypad,text="-",bd=0,image=mimg)
minus.bind("<Button-1>",click)
minus.grid(row=2,column=3,padx=4,pady=4)


######## ROW 3 ########


one = Button(keypad,text="1",bd=0,image=onimg)
one.bind("<Button-1>",click)
one.grid(row=3,column=0,padx=4,pady=4)

two = Button(keypad,text="2",bd=0,image=twimg)
two.bind("<Button-1>",click)
two.grid(row=3,column=1,padx=4,pady=4)

three = Button(keypad,text="3",bd=0,image=thrimg)
three.bind("<Button-1>",click)
three.grid(row=3,column=2,padx=4,pady=4)

multiply = Button(keypad,text="*",bd=0,image=mulimg)
multiply.bind("<Button-1>",click)
multiply.grid(row=3,column=3,padx=4,pady=4)


######## ROW 4 ########

dot = Button(keypad,text=".",bd=0,image=doimg)
dot.bind("<Button-1>",click)
dot.grid(row=4,column=0,padx=4,pady=4)

zero = Button(keypad,text="0",bd=0,image=zimg)
zero.bind("<Button-1>",click)
zero.grid(row=4,column=1,padx=4,pady=4)

equal = Button(keypad,text="=",bd=0,image=eqimg)
equal.bind("<Button-1>",click)
equal.grid(row=4,column=2,padx=4,pady=4)

divide = Button(keypad,text="/",bd=0,image=dvimg)
divide.bind("<Button-1>",click)
divide.grid(row=4,column=3,padx=4,pady=4)



root.resizable(0,0)
root.mainloop()