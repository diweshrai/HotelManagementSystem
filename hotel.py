from report import report
from tkinter import*

from PIL import Image,ImageTk  

from customer import cust_win

from room import Roombooking

from tkinter import messagebox

from details import RoomDetails

class hotelmanagementsystem:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1530x800+0+0")


                   # upper image                      


        img1=Image.open(r"H:\WhatsApp\1.png")
        img1=img1.resize((1530,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lbling=Label(self.root,image=self.photoimg1,bd=10,relief=RIDGE)
        lbling.place(x=0,y=0,width=1530,height=140)


                 #logo

        img2=Image.open(r"H:\WhatsApp\2.png")
        img2=img2.resize((140,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbling=Label(self.root,image=self.photoimg2,bd=10,relief=RIDGE)
        lbling.place(x=0,y=0,width=140,height=140)

        #title


        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1530,height=50)



        # main frame 
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1530,height=620)



        #menu
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)
 
                  # button frame 
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=212)


        #buttons


        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,cursor="hand1")
        cust_btn.grid(row=0,column=0)

        room_btn=Button(btn_frame,text="ROOM",command=self.roombooking,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,cursor="hand1")
        room_btn.grid(row=1,column=0)

        details_btn=Button(btn_frame,text="DETAILS",command=self.RoomDetail,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,cursor="hand1")
        details_btn.grid(row=2,column=0)

        report_btn=Button(btn_frame,text="REPORT",command=self.rep,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,cursor="hand1")
        report_btn.grid(row=3,column=0)

        log_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,cursor="hand1")
        log_btn.grid(row=4,column=0)



        img3=Image.open(r"H:\WhatsApp\3.jpg")
        img3=img3.resize((1300,590),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)


        lbling=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lbling.place(x=225,y=0,width=1300,height=590)

# down images 

        img4=Image.open(r"H:\WhatsApp\4.jpg")
        img4=img4.resize((230,210),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)


        lbling=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lbling.place(x=0,y=250,width=230,height=210)


        img5=Image.open(r"H:\WhatsApp\5.jpg")
        img5=img5.resize((230,190),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)


        lbling=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lbling.place(x=0,y=420,width=230,height=190)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=cust_win(self.new_window)

    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)

    
    def RoomDetail(self):
        self.new_window=Toplevel(self.root)
        self.app=RoomDetails(self.new_window)


    def logout(self):
        #self.new_window=Toplevel(self.root)   
        root.quit()


    def rep(self):
        self.new_window=Toplevel(self.root)
        self.app=report(self.new_window)    
    

        



if __name__ == "__main__":
    root=Tk()
    obj=hotelmanagementsystem(root)
    root.mainloop()