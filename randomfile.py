Python 3.8.10 (default, Mar 15 2022, 12:22:08) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> import random
>>> 
>>> tk = Tk()
>>> canvas = Canvas(tk, width=400, height=400)
>>> canvas.pack()
>>> 
>>> def random_rectangle(width, height):
	x1 = random.randrange(width)
	y1 = random.randrange(height)
	x2 = x1 + random.randrange(width)
	y2 = y1 + random.randrange(height)
	canvas.create_rectangle(x1, y1, x2, y2)

	
>>> 
================================================ RESTART: Shell ================================================
>>> from tkinter import *
>>> import random
>>> 
>>> tk = Tk()
>>> canvas = Canvas(tk, width=400, height=400)
>>> canvas.pack()
>>> 
>>> def random_rectangle(width, height):
	x1 = random.randrange(width)
	y1 = random.randrange(height)
	x2 = x1 + random.randrange(width)
	y2 = y1 + random.randrange(height)
	canvas.create_rectangle(x1, y1, x2, y2)

colors = ("green", "red", "blue", "orange", "yellow",
	  "pink", "purple", "violet", "magenta", "cyan")
	
>>> for _ in range(100):
	random_retangle(400, 400)

	
SyntaxError: multiple statements found while compiling a single statement
>>> 
================================================ RESTART: Shell ================================================
>>>  from tkinter import *
>>> import random
SyntaxError: unexpected indent
>>> form tkinter import *
SyntaxError: invalid syntax
>>> from tkinter import *
>>> import random
>>> tk = Tk()
>>> canvas = Canvas(tk, width=400, height=400)
>>> canvas.pack()
>>> 
>>> def random_rectangle(width, height):
	x1 = random.randrange(width)
	y1 = random.randrange(height)
	x2 = x1 + random.randrange(width)
	y2 = y1 + random.randrange(height)
	canvas.create_rectangle(x1, y1, x2, y2)

colors = ("green", "red", "blue", "orange", "yellow",
	  "pink", "purple", "violet", "magenta", "cyan")

	
SyntaxError: invalid syntax
>>> def random_rectangle(width, height):
	x1 = random.randrange(width)
	y1 = random.randrange(height)
	x2 = x1 + random.randrange(width)
	y2 = y1 + random.randrange(height)
	canvas.create_rectangle(x1, y1, x2, y2)

	
>>> colors = ("green", "red", "blue", "orange", "yellow",
	  "pink", "purple", "violet", "magenta", "cyan")

>>> for _ in range(100):
	random_retangle(400, 400)
	