from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox


GUI = Tk() #สร้างหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #ตั้งชื่อโปรแกรม
GUI.geometry('600x600')  #ตั้งขนาดโปรแกรม

#B2 = Button(GUI,text='เงินมีอยู่กี่บาท') :เป็นการสร้างปุ่มง่ายๆหน้าตาเวอร์ช่ัน98 555
#B2.pack()  : 
#B1 = ttk.Button(GUI,text='มีเงินอยู่เท่าไหร่')
#B1.pack(ipadx=20,ipady=20) #.pack :ไว้กำหนดให้อยู่ตรงกลาง

####################################

def Button1():
    text = 'ตอนนี้มีเงินในบัญชี  300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)
    #messagebox.showwarning('เงินในบัญชี',text)
    #messagebox.showerror('เงินในบัญชี',text)

#FB1 = Frame(GUI)  #เอาไว้สร้าง Frame
#FB1 = LabelFrame(GUI)  #เอาไว้สร้าง Frame
FB1 = LabelFrame(GUI,text='Money')  #เอาไว้สร้าง Frame 
FB1.place(x=100,y=50)

B2 = ttk.Button(FB1,text='ปุ่มสร้างจาก B2',command=Button1)
#B2.pack(ipadx=20,ipady=20)
B2.pack(ipadx=20,ipady=20,padx=30,pady=30) #ขยายความกว้างปุ่ม

#B2.place(x=50,y=200) #.place : ไว้กำหนดโลเคชั่น

####################################

GUI.mainloop()
