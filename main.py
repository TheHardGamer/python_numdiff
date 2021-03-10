from tkinter import *
import tkinter.ttk as ttk

base = Tk()

base.title("Difference checker")
base.geometry("800x600")
base.configure(bg="black")

main = Frame(base)
main.pack(pady=10)
main.configure(bg="black")

def getstring():
	nums = numbers.get("1.0","end")
	return nums

def getdiff():
	diffwant = diff.get("1.0","end")
	return int(diffwant)

def convertstrtoint():
	inputnum = getstring()
	differencereq = [getdiff()]
	for i in inputnum.split():
		diglist = [int(i) for i in i]
		result = [abs(diglist[0] - diglist[1])]
		if (result == differencereq):
			k = ''.join(str(e) for e in diglist)
			finalresult = str(k)
			resultbox.insert(INSERT, finalresult + '\n')

numbers = Text(main, bg="lightgreen", fg="red")
numbers.configure(height=10)
numbers.grid(row=0, column=0, pady=5)

diff = Text(main, bg="lightgreen", fg="red")
diff.insert(INSERT, "Enter the difference you want to find")
diff.configure(height=1)
diff.grid(row=3, column=0, pady=5)

resultbox = Text(main, bg="lightgreen", fg="red")
resultbox.configure(height=10)
resultbox.grid(row=4, column=0, pady=5)

butframe = Frame(main)
butframe.grid(row=2, column=0, pady=5)
butframe.configure(bg="black")
but_button = Button(butframe, text="YES", command=convertstrtoint)
but_button.grid(row=2, column=0, padx=2)

base.mainloop()