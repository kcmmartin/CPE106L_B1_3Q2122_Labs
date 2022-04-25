from tkinter import*
from tkinter import ttk
from time import strftime
import tkinter.messagebox
import pymysql
import smtplib


class ConnectorDB:
    def __init__(self, root):
        
        #============================================FRAME DESIGN============================================
        #Main Window
        self.root = root
        titlespace = " "
        self.root.title(125 * titlespace + "" + "Customer Registration (for Contact Tracing) ")
        self.root.geometry("1080x790+250+0")
        self.root.resizable(width = False, height = False)

        #Main Frame
        MainFrame = Frame(self.root, bd = 10, width = 1000, height = 720, relief = RIDGE, bg = 'powder blue')
        MainFrame.grid()

        #Title Frame
        TitleFrame = Frame(MainFrame, bd = 7, width = 1000, height = 300, relief = RIDGE)
        TitleFrame.grid(row = 0, column = 0)

        #Top Frame
        TopFrame = Frame(MainFrame, bd = 5, width = 1000, height = 500, relief = RIDGE)
        TopFrame.grid(row = 1, column = 0)

        #Left Frame
        LeftFrameA = Frame(TopFrame, bd = 5, width = 1000, height = 400, padx=2, relief = RIDGE, bg = 'powder blue')
        LeftFrameA.pack(side=LEFT)
        LeftFrameB = Frame(LeftFrameA, bd = 5, width = 800, height = 200, padx=2, pady=4, relief = RIDGE)
        LeftFrameB.pack(side=TOP, padx=0, pady=0)

        #Right Frame
        RightFrameA = Frame(TopFrame, bd = 5, width = 120, height = 400, padx=2, relief = RIDGE, bg = 'powder blue')
        RightFrameA.pack(side=RIGHT)
        RightFrameB = Frame(RightFrameA, bd = 5, width = 100, height = 250, padx=2, pady=2, relief = RIDGE)
        RightFrameB.pack(side=TOP)

        #Bottom Frame
        BottomFrame = Frame(LeftFrameA, bd = 5, width = 900, height = 100, padx=2, pady=4, relief = RIDGE)
        BottomFrame.pack(side=BOTTOM)
        #============================================VARIABLE DECLARAION============================================
        
        custID = StringVar()
        cName = StringVar()
        cSex = StringVar()
        cAge= StringVar()
        cAddress = StringVar()
        cEmail= StringVar()
        cNum = StringVar()
        DateTime = StringVar()
        cTemp = StringVar()

        mTo = StringVar()
        mSubj = StringVar()
        mBody = StringVar()

        #============================================FUNCTION DEFINITION ============================================
        def time():
            string = strftime('%I:%M:%S %p \n %m/%d/%Y')
            self.lbltime.config(text = string)
            self.lbltime.after(1000, time)


        def ExitProg():
            ExitProg=tkinter.messagebox.askyesno("Contact Tracing","Confirm if you want to exit")
            if ExitProg>0:
                root.destroy()
                return

        def Clear():
            self.tboxSurname.delete(0,END)
            self.tboxfirstname.delete(0,END)
            cSex.set("")
            self.tboxAge.delete(0,END)
            self.tboxAddress.delete(0,END)
            self.tboxEmail.delete(0,END)
            self.tboxNumber.delete(0,END)
            self.tboxCurrentDate.delete(0,END)
            self.tboxTemprature.delete(0,END)

        def AddData():
            if  cName.get() == "" or cSex.get() == "" or cAge.get() == "" or cSex.get() == "" or cAddress.get() == "" or DateTime.get() == "" or cEmail.get() == "" or cTemp.get() == "":
                tkinter.messagebox.showerror("Error Message", "Enter Correct Details")
            else:
                sqlCon = pymysql.connect(host ="localhost", user="root", password="admin123", database="custreg")
                cur = sqlCon.cursor()
                cur.execute("Insert into custreg(cName, cSex, cAge, cAddress, cEmail, cNum, DateTime, cTemp) values(%s, %s, %s, %s, %s, %s, %s, %s)",(
                    
                cName.get(),
                cSex.get(),
                cAge.get(),
                cAddress.get(),
                cEmail.get(),
                cNum.get(),
                DateTime.get(),
                cTemp.get(),
                ))
                sqlCon.commit()
                sqlCon.close()

                if float(cTemp.get()) >= 37.5:
                    tkinter.messagebox.showinfo("Registration Message", "Your Body Temperature is above normal. You are not allowed to enter our premises. Your data will still be recorded")
                else:
                    tkinter.messagebox.showinfo("Registration Message", "Recorded Successfully")
                ShowData()

        def ShowData():
            sqlCon = pymysql.connect(host ="localhost", user="root", password="admin123", database="custreg")
            cur = sqlCon.cursor()
            cur.execute("select * from custreg")
            result = cur.fetchall()
            if len(result) != 0:
                self.records.delete(*self.records.get_children())
                for row in result:
                    self.records.insert('',END,values=row)
            sqlCon.commit()
            sqlCon.close()

        def Info(ev):
            viewInfo = self.records.focus()
            learnerData=self.records.item(viewInfo)
            row=learnerData['values']
            custID.set(row[0])
            cName.set(row[1])
            cSex.set(row[2])
            cAge.set(row[3])
            cAddress.set(row[4])
            cEmail.set(row[5])
            cNum.set(row[6])
            DateTime.set(row[7])
            cTemp.set(row[8])
            mTo.set(row[5])

        def Update():
            sqlCon = pymysql.connect(host ="localhost", user="root", password="admin123", database="custreg")
            cur = sqlCon.cursor()
            try: 
                cur.execute("Update custreg set cName=%s, cSex=%s, cAge=%s, cAddress=%s, cEmail=%s, cNum=%s, DateTime=%s, cTemp=%s where custID=%s",(
                    
                cName.get(),
                cSex.get(),
                cAge.get(),
                cAddress.get(),
                cEmail.get(),
                cNum.get(),
                DateTime.get(),
                cTemp.get(),
                custID.get()
                ))
                sqlCon.commit()
                sqlCon.close()
                tkinter.messagebox.showinfo("Registration Message", "Updated Successfully")
            except:
                tkinter.messagebox.showinfo("Registration Message", "Error")
                
            ShowData()
        
        def Delete():
            sqlCon = pymysql.connect(host ="localhost", user="root", password="admin123", database="custreg")
            cur = sqlCon.cursor()
            cur.execute("Delete from custreg where custID=%s", custID.get())

            sqlCon.commit()
            sqlCon.close()
            tkinter.messagebox.showinfo("Registration Message", "Deleted Successfully")
            ShowData()

        def Search():
            try: 
                sqlCon = pymysql.connect(host ="localhost", user="root", password="admin123", database="custreg")
                cur = sqlCon.cursor()
                cur.execute("Select * from custreg where custID='%s'"%custID.get())

                row = cur.fetchone()

                custID.set(row[0])
                cName.set(row[1])
                cSex.set(row[2])
                cAge.set(row[3])
                cAddress.set(row[4])
                cEmail.set(row[5])
                cNum.set(row[6])
                DateTime.set(row[7])
                cTemp.set(row[8])

                sqlCon.commit()
            
            except:
                tkinter.messagebox.showinfo("Registration Message", "No Records Found")
                Clear()
            sqlCon.close()

        def Send():
            try:
                username = 'mdelrosproject@gmail.com'
                password = 'Mapua123'
                to = mTo.get()
                subject = mSubj.get()
                body = mBody.get()

                if to == "" or subject =="" or body == "":
                    tkinter.messagebox.showinfo("Registration Message", "Invalid Message Data")
                    return
                else:
                    finalMessage = 'Subject: {}\n\n{}'.format(subject, body)
                    server = smtplib.SMTP('smtp.gmail.com',587)
                    server.starttls()
                    server.login(username, password)
                    server.sendmail(username,to,finalMessage)
                    tkinter.messagebox.showinfo("Registration Message", "Message Sent!")
            except:
                tkinter.messagebox.showinfo("Registration Message", "Error Sending Message")




        #============================================TITLE AND LABELS============================================
        #Title Label
        self.lbltitle = Label(TitleFrame, font=('Tahoma',40, 'bold'), text = "Customer Registration", bd=7)
        self.lbltitle.grid(row = 0, column = 0, padx=210)

        #ID Textbox
        self.lblSurname = Label(LeftFrameB, font=('Tahoma',12, 'bold'), text = "Customer ID", bd=7)
        self.lblSurname.grid(row = 1, column = 0, sticky=W, padx=5)
        self.tboxSurname = Entry(LeftFrameB, font=('Tahoma',12, 'bold'), bd=5, width=15, justify = 'left', textvariable=custID)
        self.tboxSurname.grid(row = 1, column = 1, sticky=W, padx=5)

        #Customer Name Textbox
        self.lblfirstname = Label(LeftFrameB, font=('Tahoma',12, 'bold'), text = "Name", bd=7)
        self.lblfirstname.grid(row = 1, column = 3, sticky=W, padx=5)
        self.tboxfirstname = Entry(LeftFrameB, font=('Tahoma',12, 'bold'), bd=5, width=35, justify = 'left', textvariable=cName)
        self.tboxfirstname.grid(row = 1, column = 4, sticky=W, padx=5)

        #Sex Textbox
        self.lblSex = Label(LeftFrameB, font=('Tahoma',12, 'bold'), text = "Sex", bd=7)
        self.lblSex.grid(row = 2, column = 0, sticky=W, padx=5)
        self.cboxSex = ttk.Combobox(LeftFrameB,font=('Tahoma',12, 'bold'), width=14, state='readonly', textvariable=cSex)
        self.cboxSex['values'] = (' Male', ' Female')
        self.cboxSex.grid(row = 2, column = 1, sticky=W, padx=5)

        #Age Textbox
        self.lblAge = Label(LeftFrameB, font=('Tahoma',12, 'bold'), text = "Age", bd=7)
        self.lblAge.grid(row = 4, column = 0, sticky=W, padx=5)
        self.tboxAge = Entry(LeftFrameB, font=('Tahoma',12, 'bold'), bd=5, width=15, justify = 'left', textvariable=cAge)
        self.tboxAge.grid(row = 4, column = 1, sticky=W, padx=5)

        #Address Textbox
        self.lblAddress = Label(LeftFrameB, font=('Tahoma',12, 'bold'), text = "Address", bd=7)
        self.lblAddress.grid(row = 3, column = 0, sticky=W, padx=5)
        self.tboxAddress = Entry(LeftFrameB, font=('Tahoma',12, 'bold'), bd=5, width=60, justify = 'left', textvariable=cAddress)
        self.tboxAddress.grid(row = 3, column = 1, sticky=W, padx=5,columnspan=200)

        #Email Textbox
        self.lblEmail = Label(LeftFrameB, font=('Tahoma',12, 'bold'), text = "Email", bd=7)
        self.lblEmail.grid(row = 2, column = 3, sticky=W, padx=5)
        self.tboxEmail = Entry(LeftFrameB, font=('Tahoma',12, 'bold'), bd=5, width=35, justify = 'left', textvariable=cEmail)
        self.tboxEmail.grid(row = 2, column = 4, sticky=W, padx=5)

        #Contact Number Textbox
        self.lblNumber = Label(LeftFrameB, font=('Tahoma',12, 'bold'), text = "Contact Number", bd=7)
        self.lblNumber.grid(row = 4, column = 3, sticky=W, padx=5)
        self.tboxNumber = Entry(LeftFrameB, font=('Tahoma',12, 'bold'), bd=5, width=35, justify = 'left', textvariable=cNum)
        self.tboxNumber.grid(row = 4, column = 4, sticky=W, padx=5)

        #Current Date Textbox
        self.lblCurrentDate = Label(LeftFrameB, font=('Tahoma',12, 'bold'), text = "Time and Date", bd=7)
        self.lblCurrentDate.grid(row = 5, column = 3, sticky=W, padx=5)
        self.tboxCurrentDate = Entry(LeftFrameB, font=('Tahoma',12, 'bold'), bd=5, width=35, justify = 'left', textvariable=DateTime)
        self.tboxCurrentDate.grid(row = 5, column = 4, sticky=W, padx=5)

        #Temperature Textbox
        self.lblTemprature = Label(LeftFrameB, font=('Tahoma',12, 'bold'), text = "Temperature", bd=7)
        self.lblTemprature.grid(row = 5, column = 0, sticky=W, padx=5)
        self.tboxTemprature = Entry(LeftFrameB, font=('Tahoma',12, 'bold'), bd=5, width=15, justify = 'left', textvariable=cTemp)
        self.tboxTemprature.grid(row = 5, column = 1, sticky=W, padx=5)

        #Time Label
        self.lbltime = Label(TitleFrame, font = ('calibri', 14, 'bold'))
        self.lbltime.grid(row = 0, column = 0, sticky=W, padx=60)
        time()

        #Message Box
        self.msgTo = Label(BottomFrame, font=('Tahoma',12, 'bold'), text = "To", bd=7)
        self.msgTo.grid(row = 0, column = 0, sticky=W, padx=5)
        self.tboxTo = Entry(BottomFrame, font=('Tahoma',12, 'bold'), bd=5, width=30, justify = 'left', textvariable=mTo)
        self.tboxTo.grid(row = 0, column = 1, sticky=W, padx=5)

        self.msgSbj = Label(BottomFrame, font=('Tahoma',12, 'bold'), text = "Subject", bd=7)
        self.msgSbj.grid(row = 0, column = 2, sticky=W, padx=5)
        self.tboxSbj = Entry(BottomFrame, font=('Tahoma',12, 'bold'), bd=5, width=30, justify = 'left', textvariable=mSubj)
        self.tboxSbj.grid(row = 0, column = 3, sticky=W, padx=5)
        
        self.msgBody = Label(BottomFrame, font=('Tahoma',12, 'bold'), text = "Body", bd=7)
        self.msgBody.grid(row = 1, column = 0, sticky=W, padx=5)
        self.tboxBody = Entry(BottomFrame, font=('Tahoma',12, 'bold'), bd=5, width=74, justify = 'left', textvariable=mBody)
        self.tboxBody.grid(row = 1, column = 1, sticky=W, padx=5, columnspan=200)

        #============================================TABLE============================================
        scroll_y = Scrollbar(LeftFrameA, orient = VERTICAL)

        self.records=ttk.Treeview(LeftFrameA, height=15, columns=("custID","cName","cSex","cAge", "cAddress","cEmail","cNum","DateTime", "cTemp"), yscrollcommand=scroll_y.set)
        scroll_y.pack(side = RIGHT, fill=Y)

        self.records.heading("custID",text ="ID")
        self.records.heading("cName",text ="Name")
        self.records.heading("cSex",text ="Sex")
        self.records.heading("cAge",text ="Age")
        self.records.heading("cAddress",text ="Address")
        self.records.heading("cEmail",text ="Email")
        self.records.heading("cNum",text ="Number")
        self.records.heading("DateTime",text ="Date and Time")
        self.records.heading("cTemp",text ="Temp")

        self.records['show']='headings'

        self.records.column("custID",width= 40)
        self.records.column("cName",width= 110)
        self.records.column("cSex",width= 60)
        self.records.column("cAge",width= 40)
        self.records.column("cAddress",width= 170)
        self.records.column("cEmail",width= 170)
        self.records.column("cNum",width= 80)
        self.records.column("DateTime",width= 120)
        self.records.column("cTemp",width= 50)

        self.records.pack(fill=BOTH, expand = 0)
        self.records.bind("<ButtonRelease-1>", Info)
        ShowData()

        #============================================BUTTONS============================================
        self.btnAdd = Button(RightFrameB, font=('tahoma',16,'bold'), text = "Add New", bd=4, pady=1, padx=24, width=6, height=2, command = AddData).grid(row=0, column=0, padx=1)
        self.btnDisplay = Button(RightFrameB, font=('tahoma',16,'bold'), text = "Display", bd=4, pady=1, padx=24, width=6, height=2, command = ShowData).grid(row=1, column=0, padx=1)
        self.btnUpdate = Button(RightFrameB, font=('tahoma',16,'bold'), text = "Update", bd=4, pady=1, padx=24, width=6, height=2, command = Update).grid(row=2, column=0, padx=1)
        self.btnDelete = Button(RightFrameB, font=('tahoma',16,'bold'), text = "Delete", bd=4, pady=1, padx=24, width=6, height=2, command = Delete).grid(row=3, column=0, padx=1)
        self.btnSearch = Button(RightFrameB, font=('tahoma',16,'bold'), text = "Search", bd=4, pady=1, padx=24, width=6, height=2, command = Search).grid(row=4, column=0, padx=1)
        self.btnReset = Button(RightFrameB, font=('tahoma',16,'bold'), text = "Clear", bd=4, pady=1, padx=24, width=6, height=2, command = Clear).grid(row=5, column=0, padx=1)
        self.btnSend = Button(RightFrameB, font=('tahoma',16,'bold'), text = "Message", bd=4, pady=1, padx=24, width=6, height=2, command = Send).grid(row=6, column=0, padx=1)
        self.btnExit = Button(RightFrameB, font=('tahoma',16,'bold'), text = "Exit", bd=4, pady=1, padx=24, width=6, height=2, command = ExitProg).grid(row=7, column=0, padx=1)




if __name__=='__main__':
    #Creating Window
    root = Tk() 
    application = ConnectorDB(root)
    root.mainloop()