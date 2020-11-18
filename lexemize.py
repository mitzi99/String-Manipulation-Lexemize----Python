from tkinter import *
import tkinter.font as font

root = Tk()
root.title('Lexemize')


myFont1 = font.Font(family='Times New Roman', size=20, weight='bold')
myFont2 = font.Font(family='Times New Roman', size=10, weight='bold')


eLabel = Label(root, text="Enter Arithmetic Expression")
eLabel['font'] = myFont1
entry = Entry(root, width=30)
entry['font'] = myFont1
eLabel.grid(row=0, column=0, padx=10)
entry.grid(row=0, column=1)


def lexemize():

	v = entry.get()
	li = []
	lis = []

	for i in v:
		if i == '-' or i == '+' or i == '*' or i == '/' or i == ')' or i == '(':
			a = ""
			for j in lis:
				a = a + j		
			li.append(a)
			li.append(i)
			lis.clear()
		elif i == ' ':
			pass

		else:

			lis.append(i)


	a = ""
	for j in lis:
		a = a + j		
	li.append(a)

	ans = str(li)

	expression=Label(root,text=entry.get())
	expression['font'] = myFont1
	expression.grid(row=3, column=1)
	
	myLabel = Label(root, text=ans )
	myLabel['font'] = myFont1
	myLabel.grid(row=4, column=1)

	entry.delete(0, END)

myButton = Button(root, text="Lexemize Expression", command=lexemize)
myButton['font'] = myFont2
myButton.grid(row=2, column=0, pady=10)



root.mainloop()
