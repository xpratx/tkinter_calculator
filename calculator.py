from tkinter import *
from customtkinter import *
import math

root = CTk()
root.minsize(700,500)
root.maxsize(700,500)
root.title("Calculator")


var = StringVar()
eqn = ""



def btn(no):
    global eqn
    eqn += str(no)
    var.set(eqn)

def calculation():
    global eqn
    expression = area.get()
    expression_with_e = expression.replace('e', str(math.e))

    b = eval(expression_with_e, {'sin': math.sin, 'cos': math.cos, 'tan':math.tan, 'sqrt': math.sqrt, 'fact':math.factorial, 'log':math.log10})
    eqn = str(b)
    area.delete(0, END)
    area.insert(0, eqn)

def clear():
    area.delete(0, END)
    global eqn
    eqn = ""
    var.set(eqn)


custom_font = ("Arial",18)

area = CTkEntry(root, textvariable= var,  font=custom_font, height=60, width=660)
area.place(x=20, y=30)


gap = 30
button_size = 70


def simulate_nums_press(event):
    key = event.char
    if key.isdigit:
        btn(int(key))
        
for i in range(10):
    root.bind(f"<Key-{i}>", simulate_nums_press)

def simulate_plus(event):
    btn("+")

root.bind('<Key-plus>', simulate_plus)

def simulate_minus(event):
    btn("-")

root.bind('<Key-minus>', simulate_minus)

def simulate_mul(event):
    btn("*")

root.bind('<Key-asterisk>', simulate_mul)

def simulate_div(event):
    btn("/")

root.bind('<Key-slash>', simulate_div)

def simulate_enter(event):
    calculation()

root.bind("<Return>", simulate_enter)

def simulate_clear(event):
    clear()

root.bind("<BackSpace>", simulate_clear)

def simulate_openParenthesis(event):
    btn("(")

root.bind("<Key-parenleft>", simulate_openParenthesis)

def simulate_closeParenthesis(event):
    btn(")")

root.bind("<Key-parenright>", simulate_closeParenthesis)


b1 = CTkButton(root, text='1', command=lambda : btn(1), font=custom_font, height=button_size,width=button_size, fg_color="#B33F62")      #you have to use the lambda function, or else all the buttons are
b1.place(x=20, y=110, )            #pre pressed when you start the program

b2 = CTkButton(root, text='2', command=lambda : btn(2), font=custom_font, height=button_size,width=button_size, fg_color="#B33F62" )
b2.place(x=20+button_size+gap, y=110, )

b3 = CTkButton(root, text='3', command=lambda : btn(3), font=custom_font, height=button_size,width=button_size, fg_color="#B33F62" )
b3.place(x=20+(2*button_size)+(2*gap), y=110, )

b4 = CTkButton(root, text='4', command=lambda : btn(4), font=custom_font, height=button_size,width=button_size, fg_color="#B33F62")
b4.place(x=20, y=110+button_size+gap, )

b5 = CTkButton(root, text='5', command=lambda : btn(5) , font=custom_font, height=button_size,width=button_size, fg_color="#B33F62")
b5.place(x=20+button_size+gap, y=110+button_size+gap, )

b6 = CTkButton(root, text='6', command=lambda : btn(6), font=custom_font, height=button_size,width=button_size, fg_color="#B33F62")
b6.place(x=20+(2*button_size)+(2*gap), y=110+button_size+gap, )

b7 = CTkButton(root, text='7',command=lambda : btn(7), font=custom_font, height=button_size,width=button_size, fg_color="#B33F62" )
b7.place(x=20, y=110+(2*button_size)+(2*gap), )

b8 = CTkButton(root, text='8', command=lambda : btn(8), font=custom_font, height=button_size,width=button_size, fg_color="#B33F62")
b8.place(x=20+button_size+gap, y=110+(2*button_size)+(2*gap), )

b9 = CTkButton(root, text='9',command=lambda : btn(9), font=custom_font, height=button_size,width=button_size, fg_color="#B33F62" )
b9.place(x=20+(2*button_size)+(2*gap), y=110+(2*button_size)+(2*gap), )

b0 = CTkButton(root, text='0',command=lambda : btn(0), font=custom_font, height=button_size,width=button_size, fg_color="#B33F62" )
b0.place(x=20+button_size+gap, y=110+(3*button_size)+(3*gap), )

b_add = CTkButton(root, text="+", command=lambda : btn("+"), font=custom_font, height=button_size,width=button_size, fg_color="#F9564F")
b_add.place(x=20+(3*button_size)+(3*gap), y=110)

b_sub = CTkButton(root, text="-", command=lambda : btn("-"), font=custom_font, height=button_size,width=button_size, fg_color="#F9564F")
b_sub.place(x=20+(4*button_size)+(4*gap), y=110)

b_mul = CTkButton(root, text="x", command=lambda : btn("*"), font=custom_font, height=button_size,width=button_size, fg_color="#F9564F")
b_mul.place(x=20+(3*button_size)+(3*gap), y=110+button_size+gap)

b_div = CTkButton(root, text="/", command=lambda : btn("/"), font=custom_font, height=button_size,width=button_size, fg_color="#F9564F")
b_div.place(x=20+(4*button_size)+(4*gap), y=110+button_size+gap)

b_equals = CTkButton(root, text="=", command=calculation, font=custom_font, height=button_size,width=2*button_size+gap, fg_color="#F9564F")
b_equals.place(x=20+(3*button_size)+(3*gap), y=110+(3*button_size)+(3*gap))

b_decimal = CTkButton(root, text=".", command=lambda : btn("."), font=custom_font, height=button_size,width=button_size, fg_color="#F9564F")
b_decimal.place(x=20+(2*button_size)+(2*gap), y=110+(3*button_size)+(3*gap), )

b_clear = CTkButton(root, text="AC", command=clear, font=custom_font, height=button_size,width=button_size, fg_color="#F9564F")
b_clear.place(x=20, y=110+(3*button_size)+(3*gap), )

b_openParenthesis = CTkButton(root, text="(", command=lambda : btn("("), font=custom_font, height=button_size, width=button_size, fg_color="#F9564F" )
b_openParenthesis.place(x=20+(3*button_size)+(3*gap), y=110+(2*button_size)+(2*gap))

b_closeParenthesis = CTkButton(root, text=")", command=lambda : btn(")"), font=custom_font, height=button_size, width=button_size, fg_color="#F9564F" )
b_closeParenthesis.place(x=20+(4*button_size)+(4*gap), y=110+(2*button_size)+(2*gap))

b_sin = CTkButton(root, text="sin", command=lambda : btn('sin('), font=custom_font, height=button_size, width=button_size,  fg_color="#F9564F")
b_sin.place(x=20+(5*button_size)+(5*gap), y=110)

b_cos = CTkButton(root, text="cos", command=lambda : btn('cos('), font=custom_font, height=button_size, width=button_size,  fg_color="#F9564F")
b_cos.place(x=20+(6*button_size)+(6*gap), y=110)

b_tan = CTkButton(root, text="tan", command=lambda : btn("tan("), font=custom_font, height=button_size,width=button_size, fg_color="#F9564F")
b_tan.place(x=20+(5*button_size)+(5*gap), y=110+button_size+gap)

b_pow = CTkButton(root, text="^", command=lambda : btn("**"), font=custom_font, height=button_size,width=button_size, fg_color="#F9564F")
b_pow.place(x=20+(6*button_size)+(6*gap), y=110+button_size+gap)

b_sqrt = CTkButton(root, text="sqrt", command=lambda : btn("sqrt("), font=custom_font, height=button_size,width=button_size, fg_color="#F9564F")
b_sqrt.place(x=20+(5*button_size)+(5*gap), y=110+(2*button_size)+(2*gap))

b_fact = CTkButton(root, text="fact", command=lambda : btn("fact("), font=custom_font, height=button_size,width=button_size, fg_color="#F9564F")
b_fact.place(x=20+(6*button_size)+(6*gap), y=110+(2*button_size)+(2*gap))

b_e = CTkButton(root, text="e", command=lambda : btn("e"), font=custom_font, height=button_size,width=button_size, fg_color="#F9564F")
b_e.place(x=20+(5*button_size)+(5*gap), y=110+(3*button_size)+(3*gap))

b_fact = CTkButton(root, text="log", command=lambda : btn("log("), font=custom_font, height=button_size,width=button_size, fg_color="#F9564F")
b_fact.place(x=20+(6*button_size)+(6*gap), y=110+(3*button_size)+(3*gap))
root.mainloop()
