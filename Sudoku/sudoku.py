from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import winsound

frequency = 2500
duration = 1000

timeleft = 300
Numbers = ['1','2','3','4','5']
a = random.randint(1,5)
b = random.randint(1,5)
e = random.randint(1,5)

def print_grid(arr):
    e1 = Button(root, text = arr[0][0],width =10)
    e1.grid(row=5,column=1,ipadx=10,ipady=10)
    e2 = Button(root, text = arr[0][1],width =10)
    e2.grid(row=5,column=2,ipadx=10,ipady=10)
    e3 = Button(root, text = arr[0][2],width =10)
    e3.grid(row=5,column=3,ipadx=10,ipady=10)
    e4 = Button(root, text = a,width =10)
    e4.grid(row=5,column=4,ipadx=4,ipady=4)
    e5 = Button(root, text = arr[0][4],width =10)
    e5.grid(row=5,column=5,ipadx=10,ipady=10)
    e6 = Button(root, text = b,width =10)
    e6.grid(row=6,column=1,ipadx=4,ipady=4)
    e7 = Button(root, text = arr[1][1],width =10)
    e7.grid(row=6,column=2,ipadx=10,ipady=10)
    e8 = Button(root, text = arr[1][2],width =10)
    e8.grid(row=6,column=3,ipadx=10,ipady=10)
    e9 = Button(root, text = arr[1][3],width =10)
    e9.grid(row=6,column=4,ipadx=10,ipady=10)
    e10 = Button(root, text = arr[1][4],width =10)
    e10.grid(row=6,column=5,ipadx=10,ipady=10)
    e11 = Button(root, text = arr[2][0],width =10)
    e11.grid(row=7,column=1,ipadx=10,ipady=10)
    e12 = Button(root, text = arr[2][1],width =10)
    e12.grid(row=7,column=2,ipadx=10,ipady=10)
    e13 = Button(root, text = arr[2][2],width =10)
    e13.grid(row=7,column=3,ipadx=10,ipady=10)
    e14 = Button(root, text = arr[2][3],width =10)
    e14.grid(row=7,column=4,ipadx=10,ipady=10)
    e15 = Button(root, text = arr[2][4],width =10)
    e15.grid(row=7,column=5,ipadx=10,ipady=10)
    e16 = Button(root, text = arr[3][0],width =10)
    e16.grid(row=8,column=1,ipadx=10,ipady=10)
    e17 = Button(root, text = arr[3][1],width =10)
    e17.grid(row=8,column=2,ipadx=10,ipady=10)
    e18 = Button(root, text = arr[3][2],width =10)
    e18.grid(row=8,column=3,ipadx=10,ipady=10)
    e19 = Button(root, text = arr[3][3],width =10)
    e19.grid(row=8,column=4,ipadx=10,ipady=10)
    e20 = Button(root, text = arr[3][4],width =10)
    e20.grid(row=8,column=5,ipadx=10,ipady=10)
    e21 = Button(root, text = arr[4][0],width =10)
    e21.grid(row=9,column=1,ipadx=10,ipady=10)
    e22= Button(root, text = arr[4][1],width =10)
    e22.grid(row=9,column=2,ipadx=10,ipady=10)
    e23 = Button(root, text = arr[4][2],width =10)
    e23.grid(row=9,column=3,ipadx=10,ipady=10)
    e24 = Button(root, text = arr[4][3],width =10)
    e24.grid(row=9,column=4,ipadx=10,ipady=10)
    e25 = Button(root, text = e,width =10)
    e25.grid(row=9,column=5,ipadx=4,ipady=4)

def printsudo():
    grid=[[0 for x in range(5)]for y in range(5)]
    grid=[[0,0,0,a,0],
          [b,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,e]]
    if solve_sudoku(grid):
        print_grid(grid);

def find_empty_location(arr,l):
    for row in range(5):
        for col in range(5):
            if(arr[row][col]==0):
                l[0]=row
                l[1]=col
                return True
    return False
def used_in_row(arr,row,num):
    for i in range(5):
        if(arr[row][i] == num):
            return True
    return False

def used_in_col(arr,col,num):
    for i in range(5):
        if(arr[i][col] == num):
            return True
    return False

def check_location_is_safe(arr,row,col,num):

    return not used_in_row(arr,row,num) and not used_in_col(arr,col,num)

def solve_sudoku(arr):

    l=[0,0]
    if(not find_empty_location(arr,l)):
        return True
    row=l[0]
    col=l[1]
    for num in range(1,6):
        if(check_location_is_safe(arr,row,col,num)):
            arr[row][col]=num
            if(solve_sudoku(arr)):
                return True
            arr[row][col] = 0
    return False


def startGame(event):
    if timeleft==300:
        countdown()
def on_button():
    if timeleft<=0 :
        messagebox._show("Result","TIMED OUT!!")
        EXIT(0)
    if (e1.get().strip() in Numbers and e2.get().strip() in Numbers and e3.get().strip() in Numbers and e5.get().strip() in Numbers and
       e7.get().strip() in Numbers and e8.get().strip() in Numbers and e9.get().strip() in Numbers and e10.get().strip() in Numbers and
       e11.get().strip() in Numbers and e12.get().strip() in Numbers and e13.get().strip() in Numbers and e14.get().strip() in Numbers and e15.get().strip() in Numbers and
       e16.get().strip() in Numbers and e17.get().strip() in Numbers and e18.get().strip() in Numbers and e19.get().strip() in Numbers and e20.get().strip() in Numbers and
       e21.get().strip() in Numbers and e22.get().strip() in Numbers and e23.get().strip() in Numbers and e24.get().strip() in Numbers):

       A=list();B=list();C=list();D=list();E=list();F=list();G=list();H=list();I=list();J=list();K=list();L=list()

       A.append(e1.get().strip())
       A.append(e2.get().strip())
       A.append(e3.get().strip())
       A.append(a)
       A.append(e5.get().strip())
       B.append(b)
       B.append(e7.get().strip())
       B.append(e8.get().strip())
       B.append(e9.get().strip())
       B.append(e10.get().strip())
       C.append(e11.get().strip())
       C.append(e12.get().strip())
       C.append(e13.get().strip())
       C.append(e14.get().strip())
       C.append(e15.get().strip())
       D.append(e16.get().strip())
       D.append(e17.get().strip())
       D.append(e18.get().strip())
       D.append(e19.get().strip())
       D.append(e20.get().strip())
       E.append(e21.get().strip())
       E.append(e22.get().strip())
       E.append(e23.get().strip())
       E.append(e24.get().strip())
       E.append(e)
       F.append(list(set(A)));F.append(list(set(B)));F.append(list(set(C)));F.append(list(set(D)));F.append(list(set(E)))
       G.append(e1.get().strip())
       H.append(e2.get().strip())
       I.append(e3.get().strip())
       J.append(a)
       K.append(e5.get().strip())
       G.append(b)
       H.append(e7.get().strip())
       I.append(e8.get().strip())
       J.append(e9.get().strip())
       K.append(e10.get().strip())
       G.append(e11.get().strip())
       H.append(e12.get().strip())
       I.append(e13.get().strip())
       J.append(e14.get().strip())
       K.append(e15.get().strip())
       G.append(e16.get().strip())
       H.append(e17.get().strip())
       I.append(e18.get().strip())
       J.append(e19.get().strip())
       K.append(e20.get().strip())
       G.append(e21.get().strip())
       H.append(e22.get().strip())
       I.append(e23.get().strip())
       J.append(e24.get().strip())
       K.append(e)
       flag=1

       L.append(list(set(G)));L.append(list(set(H)));L.append(list(set(I)));L.append(list(set(J)));L.append(list(set(K)))
       for i in range(len(F)):
           if(len(F[i])!=5 or len(L[i])!=5  ) :
               flag=0
               break
       if flag==1:
           messagebox._show("Result","YOU ARE THE REAL WINNER!!")
       else:
           messagebox._show("Result","WRONG!!")


    else :
        messagebox._show("Result","CHEATER!!")

def countdown():
    global timeleft

    if timeleft>0:
        timeleft-=1
        timeLabel.config(text = "Time left: "
                               + str(timeleft))
        timeLabel.after(1000, countdown)
        if (timeleft%100==0):
            winsound.Beep(frequency, duration)
        if timeleft < 3:
            winsound.Beep(frequency, duration)

def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e5.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)
    e9.delete(0,END)
    e10.delete(0,END)
    e11.delete(0,END)
    e12.delete(0,END)
    e13.delete(0,END)
    e14.delete(0,END)
    e15.delete(0,END)
    e16.delete(0,END)
    e17.delete(0,END)
    e18.delete(0,END)
    e19.delete(0,END)
    e20.delete(0,END)
    e21.delete(0,END)
    e22.delete(0,END)
    e23.delete(0,END)
    e24.delete(0,END)


root = Tk()
root.geometry('760x475')
root.configure(background="light yellow")
C = Canvas(root, bg="blue", height=150, width=200)
filename = PhotoImage(file = "1234.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.grid()
root.title('Sudoku By Abhishek Jaiswal')
label1=Label(root,text="*****WELCOME*****", font = ('Helvetica', 20),bg="light yellow")
label1.grid(row=0,column=0)
label2 = Label(root,text="Enter values between 1 and 5 only!", font = ('Helvetica', 12),bg="light yellow")
label2.grid(row=3,column=0)
scoreLabel = Label(root, text = "Press enter to start",
                                      font = ('Helvetica', 12),bg="light yellow")
scoreLabel.grid(row=1,column = 0)
timeLabel = Label(root, text = "Time left: " +
              str(timeleft), font = ('Helvetica', 12),bg="light yellow")

timeLabel.grid(row=2,column = 0)
root.bind('<Return>', startGame)
e1 = Entry(root, text = "",width =10,justify='center')
e1.grid(row=5,column=1,ipadx=10,ipady=10)
e2 = Entry(root, text = "",width =10,justify='center')
e2.grid(row=5,column=2,ipadx=10,ipady=10)
e3 = Entry(root, text = "",width =10,justify='center')
e3.grid(row=5,column=3,ipadx=10,ipady=10)
e4 = Button(root, text = a,width =10)
e4.grid(row=5,column=4,ipadx=4,ipady=4)
e5 = Entry(root, text = "",width =10,justify='center')
e5.grid(row=5,column=5,ipadx=10,ipady=10)
e6 = Button(root, text = b,width =10)
e6.grid(row=6,column=1,ipadx=4,ipady=4)
e7 = Entry(root, text = "",width =10,justify='center')
e7.grid(row=6,column=2,ipadx=10,ipady=10)
e8 = Entry(root, text = "",width =10,justify='center')
e8.grid(row=6,column=3,ipadx=10,ipady=10)
e9 = Entry(root, text = "",width =10,justify='center')
e9.grid(row=6,column=4,ipadx=10,ipady=10)
e10 = Entry(root, text = "",width =10,justify='center')
e10.grid(row=6,column=5,ipadx=10,ipady=10)
e11 = Entry(root, text = "",width =10,justify='center')
e11.grid(row=7,column=1,ipadx=10,ipady=10)
e12 = Entry(root, text = "",width =10,justify='center')
e12.grid(row=7,column=2,ipadx=10,ipady=10)
e13 = Entry(root, text = "",width =10,justify='center')
e13.grid(row=7,column=3,ipadx=10,ipady=10)
e14 = Entry(root, text = "",width =10,justify='center')
e14.grid(row=7,column=4,ipadx=10,ipady=10)
e15 = Entry(root, text = "",width =10,justify='center')
e15.grid(row=7,column=5,ipadx=10,ipady=10)
e16 = Entry(root, text = "",width =10,justify='center')
e16.grid(row=8,column=1,ipadx=10,ipady=10)
e17 = Entry(root, text = "",width =10,justify='center')
e17.grid(row=8,column=2,ipadx=10,ipady=10)
e18 = Entry(root, text = "",width =10,justify='center')
e18.grid(row=8,column=3,ipadx=10,ipady=10)
e19 = Entry(root, text = "",width =10,justify='center')
e19.grid(row=8,column=4,ipadx=10,ipady=10)
e20 = Entry(root, text = "",width =10,justify='center')
e20.grid(row=8,column=5,ipadx=10,ipady=10)
e21 = Entry(root, text = "",width =10,justify='center')
e21.grid(row=9,column=1,ipadx=10,ipady=10)
e22= Entry(root, text = "",width =10,justify='center')
e22.grid(row=9,column=2,ipadx=10,ipady=10)
e23 = Entry(root, text = "",width =10,justify='center')
e23.grid(row=9,column=3,ipadx=10,ipady=10)
e24 = Entry(root, text = "",width =10,justify='center')
e24.grid(row=9,column=4,ipadx=10,ipady=10)
e25 = Button(root, text = e,width =10)
e25.grid(row=9,column=5,ipadx=4,ipady=4)

button =Button(root, text="SUBMIT!", command=on_button)
button.grid(row=12,column=0,ipadx=5,ipady=5)

button2 = Button(root, text="Reset",command=clear)
button2.grid(row=2,column=5,ipadx=5,ipady=5)

button3 = Button(root, text="ANSWER",command=printsudo)
button3.grid(row=12,column=5,ipadx=5,ipady=5)



root.mainloop()
