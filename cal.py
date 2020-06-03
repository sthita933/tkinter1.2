from tkinter import *
top=Tk()
top.title('calculator')
operator=""
var=StringVar()
e1=Entry(top,font=('arial',20,'bold'),bd=30,bg="powder blue",insertwidth=4,justify='right',textvariable=var).grid(columnspan=4)

def click(numbers):
    global operator
    operator=operator + str(numbers)
    var.set(operator)
    
def clear():
    global operator
    operator=""
    var.set("")

def equal():
    global operator
    sumup=str(eval(operator))
    var.set(sumup)
    operator=""
##################################################################################################################

#btn 7,8,9,add :text 7,8,9,+ : col 0,1,2,3

btn7=Button(top,padx=16,pady=16,bd=8,fg="black",command=lambda:click(7),bg="powder blue",font=('arial',20,'bold'),text="7").grid(row=1,column=0)
btn8=Button(top,padx=16,pady=16,bd=8,fg="black",command=lambda:click(8),bg="powder blue",font=('arial',20,'bold'),text="8").grid(row=1,column=1)
btn9=Button(top,padx=16,pady=16,bd=8,fg="black",command=lambda:click(9),bg="powder blue",font=('arial',20,'bold'),text="9").grid(row=1,column=2)
addition=Button(top,padx=16,pady=16,bd=8,fg="black",command=lambda:click("+"),bg="powder blue",font=('arial',20,'bold'),text="+").grid(row=1,column=3)
###################################################################################################################

#btn 4,5,6,sub : text 4,5,6 : row 2,2,2 

btn4=Button(top,padx=16,pady=16,bd=8,fg="black",bg="powder blue",command=lambda:click(4),font=('arial',20,'bold'),text="4").grid(row=2,column=0)
btn5=Button(top,padx=16,pady=16,bd=8,fg="black",bg="powder blue",command=lambda:click(5),font=('arial',20,'bold'),text="5").grid(row=2,column=1)
btn6=Button(top,padx=16,pady=16,bd=8,fg="black",bg="powder blue",command=lambda:click(6),font=('arial',20,'bold'),text="6").grid(row=2,column=2)
sub=Button(top,padx=16,pady=16,bd=8,fg="black",bg="powder blue",command=lambda:click("-"),font=('arial',20,'bold'),text="-").grid(row=2,column=3)
###################################################################################################################

#btn 1,2,3,mul : text 1,2,3 : row 3,3,3,3

btn1=Button(top,padx=16,bd=8,pady=16,fg="black",bg="powder blue",command=lambda:click(1),font=('arial',20,'bold'),text="1").grid(row=3,column=0)
btn2=Button(top,padx=16,bd=8,pady=16,fg="black",bg="powder blue",command=lambda:click(2),font=('arial',20,'bold'),text="2").grid(row=3,column=1)
btn3=Button(top,padx=16,bd=8,pady=16,fg="black",bg="powder blue",command=lambda:click(3),font=('arial',20,'bold'),text="3").grid(row=3,column=2)
mul=Button(top,padx=16,bd=8,pady=16,fg="black",bg="powder blue",command=lambda:click("*"),font=('arial',20,'bold'),text="*").grid(row=3,column=3)
###################################################################################################################


#btn 0,clear,equals,div : text 0,c,=,/  : row 4,4,4,4

btn0=Button(top,padx=16,bd=8,pady=16,fg="black",bg="powder blue",command=lambda:click(0),font=('arial',20,'bold'),text="0").grid(row=4,column=0)
clear=Button(top,padx=16,pady=16,bd=8,fg="black",bg="powder blue",command=clear,font=('arial',20,'bold'),text="c").grid(row=4,column=1)
equals=Button(top,padx=16,pady=16,bd=8,fg="black",bg="powder blue",command=equal,font=('arial',20,'bold'),text="=").grid(row=4,column=2)
div=Button(top,padx=16,pady=16,bd=8,fg="black",bg="powder blue",command=lambda:click("/"),font=('arial',20,'bold'),text="/").grid(row=4,column=3)
###################################################################################################################

top.mainloop()






















