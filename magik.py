from tkinter import *
import random

root=Tk()
root.title("Mutidimensional Arrays")
root.geometry("500x500")

label = Label(root)

OURarray = [[["",25,33,48,54,60,91],["@","#"],["WD","BH","YA","DZ","EX","JL","GQ","VP"]]]
print(OURarray[0])

def gimmynewpassword():
    rn1 = random.randint(0,6)
    rn2 = random.randint(0,1)
    rn3 = random.randint(0,7)
    rn4 = random.randint(0,7)
    rn5 = random.randint(0,7)
    label["text"]=str(OURarray[0][0][rn1]) + OURarray[0][1][rn2] + OURarray[0][2][rn3] + OURarray[0][2][random.randint(0,7)] + OURarray[0][2][rn5] + str(OURarray[0][0][random.randint(0,6)]) + OURarray[0][2][rn4]
    
btn = Button(root, text = 'Show new password', command = gimmynewpassword)
btn.place(relx=0.5,rely=0.5,anchor = CENTER)

label.place(relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()

#this code is totoally not scuffed and totally not copied off of byju's future school