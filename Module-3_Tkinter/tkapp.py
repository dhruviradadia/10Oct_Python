import tkinter
from tkinter import ttk,messagebox

window=tkinter.Tk()
window.config(background='blue')
window.title("Firstapp")
window.geometry("500x600")

"""lbl_fnm=tkinter.Label(text="Firstname:",bg='blue',fg='red',font='Dubai 15 bold')
#lbl_fnm.pack()
#lbl_fnm.place(x=0,y=0)
lbl_fnm.grid(row=0,column=0,sticky=0)"""

"""lbl_fnm=tkinter.Label(text="Lastname:",bg='blue',fg='dubai 15 bold',)
lbl_fnm.pack()
lbl_fnm.place(x=0,y=0)
lbl_fnm.grid(row=1,column=0,sticky='w')"""

txt_fnm=tkinter.Entry(font='Dubai 12 bold')
txt_fnm.grid(row=0,column=1,sticky='w')

txt_lnm=tkinter.Entry(font='Dubai 12 bold')
txt_lnm.grid(row=1,colimn=1,sticky='w')

male=tkinter.Radiobutton(value=0,text="male",bg='blue',fg='black',font='Dubai 115 bold')
male.grid(row=2,column=0,sticky='w')

female=tkinter.Radiobutton(value=1,text="Female",bg='blue',fg='black',font='Dubai 15 bold')
female.grid(row=2,column=1,sticky='w')

opt1=tkinter.Checkbutton(text="python",bg='blue',fg='red',font='Dubai 15 bold')
opt1.grid(row=3,column=0,sticky='w')

opt2=tkinter.Checkbutton(text="PHP",bg='blue',fg='red',font='Dubai 15 bold')
opt2.grid(row=4,column=0,sticky='w')

opt3=tkinter.Checkbutton(text="JAVA",bg='blue',fg='red',font='Dubai 15 bold')
opt3.grid(row=5,column=0,sticky='w')

opt4=tkinter.Checkbutton(text="HTML",bg='blue',fg='red',font='Dubai 15 bold')
opt4.grid(row=6,column=0,sticky='w')


city=['Ahmedabad','Rajkot','Baroda','Surat','Jamnagar','BHavnagar']
citycombo=ttk.Checkbutton(values=city)
citycombo.grid(row=7,column=0,sticky='w')

def btnclick():
    #print("button clicked!")
    fnm=txt_fnm.get()
    lnm=txt_lnm.get()

    print("Firstname:",fnm)
    print("Lastname:",lnm)

    #messagebox.showerror("Error","Somthing went wrong...try again!")
    #messagebox.showinfo("Success","Your data has been saved!")
    messagebox.showwarning("Warning","your disk is full!")

btn=tkinter.Button(text="submit",font='Dubai 15 bold',command=btnclick)
#btn.grid(row=9,column=0)
btn.place(x=170,y=380)

window.mainloop()










