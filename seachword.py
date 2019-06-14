#coding: utf8
from Tkinter import *
root = Tk()
text = Text()
text.grid(row = 1)
def start2(event):
	txt = text.get(1.0, END)
	word = str(seach_word.get())
	if word in txt:
		result.grid(row = 0)
	else:
		result["text"] = "Здесь слова нет"
		result.grid(row = 0)
result = Label(root, text = "Слово здесь")		 
label = Label(root, text = "Введите слово: ")
label.grid(row = 2)
seach_word = Entry(root)
seach_word.grid(row = 3)
start = Button(root, text = "Нажмите")
start.grid(row = 3, column = 2)
start.bind("<Button-1>", start2)
root.mainloop()