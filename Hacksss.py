#FraserHacks application
#By Rick and Lindsay
#Last edited Dec 11 2019

from tkinter import *
import time

level = 0

window = Tk()
print("hi")
f0 = Frame(window)
f1 = Frame(window)
f2 = Frame(window)
f3 = Frame(window)
f4 = Frame(window)
f5 = Frame(window)
f6 = Frame(window)

fhImage = PhotoImage(file="FraserHacks-logo.png")

def levelTwo(event):
    refresh(1)

def refresh(state):
    if state == 0:
        c=Canvas(f0, width=1080, height=700)
        click = Label(c,text="Click", font=(60), fg="blue")
        click.place(relx=0.436, rely=0.7)
        underline = c.create_line(475,523,520,523,fill="blue")

        register = Label(c, text="to register", font=60)
        register.bind("<Button-1>",levelTwo)
        register.place(relx=0.48, rely=0.7)

        labForImage = Label(c,image=fhImage)
        labForImage.place(relx=0.5, rely=0.4, anchor=CENTER)
        c.pack()

    elif state == 1:
        f0.destroy()
        c=Canvas(f1, width=1080, height=700)
        name=Label(c, text="Fill in name:", font=60)
        name.place(relx=0.4, rely=0.5)
        nameentry=Entry(c)
        nameentry.place(relx=0.6,rely=0.5)
        c.pack()
        input = ""
        def submitu(event):
            input = nameentry.get()
            print(input)
            if (not(any(x.isupper() for x in input) and any(x.islower() for x in input) and any(x.isdigit() for x in input) and len(input) >= 7 and hasSpecial(input))):
                no=Label(c, text='Name must include at least one uppercase letters, one special character,\n one number and be over 7 characters in length', fg='red', font=11)
                no.place(relx=0.1, rely=0.65)
            else:
                refresh(2)
        submit = Button(c,text="submit", font=60)
        submit.bind("<Button-1>",submitu)
        submit.place(relx=0.3,rely=0.7)
        def hasSpecial(input):
            if(any(not x.isalpha() and not x.isdigit() for x in input)):
                return 1
            else:
                return 0

    elif state == 2:
        f1.destroy()
        c=Canvas(f2, width=1080, height=700)
        stopped = 0
        def stop():
            stopped = 1


        def counter_label(count):
            counter = 0
            def count():
                global counter
                counter += 1
                print(counter)
                count.config(text=str(counter))
                count.after(1000, count)
            if not stopped:
                count()
        count = Label(c,font=60)
        count.place(relx=0.5,rely=0.5)
        counter_label(count)
        stopButton = Button(c,text="STOP",font=60,command=stop)
        stopButton.place(relx=0.5,rely=0.7)
        c.pack()


refresh(2)
#f0.pack()
#f1.pack()
f2.pack()
f3.pack()
f4.pack()
f5.pack()
f6.pack()
window.mainloop()
