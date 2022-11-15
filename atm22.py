from tkinter import*
from tkinter import ttk
import tkinter.messagebox
bal=150000



class  atm:
    
    def __init__(self, root) :
        self.root = root
        blank_space = " "
        self.root.title(82 * blank_space + "ATM System")
        self.root.geometry("634x620+280+0")
        self.root.configure(bg='gainsboro')

        #_______________________________FRAME________________________________________

        MainFrame  =  Frame(self.root, bd=20,  width = 620, height=634, relief=RIDGE)
        MainFrame.grid()

        TopFrame1= Frame(MainFrame, bd=7, width = 620, height=280, relief=RIDGE)
        TopFrame1.grid(row=1, column=0, padx=12)

        TopFrame2= Frame(MainFrame, bd=7, width = 620, height=280, relief=RIDGE)
        TopFrame2.grid(row=0, column=0, padx=8)


        TopFrame2Left= Frame(TopFrame2, bd=5, width = 190, height=280, relief=RIDGE)
        TopFrame2Left.grid(row=0, column=0, padx=2)

        TopFrame2Mid= Frame(TopFrame2, bd=5, width = 200, height=280, relief=RIDGE)
        TopFrame2Mid.grid(row=0, column=1, padx=2)

        TopFrame2Right= Frame(TopFrame2, bd=5, width = 190, height=280, relief=RIDGE)
        TopFrame2Right.grid(row=0, column=2, padx=2)
        #_________________________________FUNCTIONS__________________________________

        def enter_pin():
            pinNo = self.txtReceipt.get("1.0", "end-1c")
            if((pinNo == str("2213"))):
                self.txtReceipt.delete("1.0", END)

                self.txtReceipt.insert(END,'\t\t   ATM' + "\n\n") 
                self.txtReceipt.insert(END,'Withdraw Cash\t\t\t Loan' + "\n\n\n\n") 
                self.txtReceipt.insert(END,'Cash with Receipt\t\t\t Deposit' + "\n\n\n\n") 
                self.txtReceipt.insert(END,'Balance\t\t\t Request New Pin' + "\n\n\n\n") 
                self.txtReceipt.insert(END,'Mini Statement\t\t\t Print Statement' + "\n\n\n\n")

                self.btnArrowL1=Button(TopFrame2Left, width=90, height=50, state = NORMAL,
                command= withdrawcash, image=self.img_arrow_left).grid(row=0,column =0, padx=2, pady=2)

                self.btnArrowL2=Button(TopFrame2Left, width=90, height=50, state = NORMAL,
                command= withdrawcash, image=self.img_arrow_left).grid(row=1,column =0, padx=2, pady=2)

                self.btnArrowL3=Button(TopFrame2Left, width=90, height=50, state = NORMAL,
                command= Balance, image=self.img_arrow_left).grid(row=2,column =0, padx=2, pady=2)

                self.btnArrowL4=Button(TopFrame2Left, width=90, height=50, state = NORMAL,
                command= statement, image=self.img_arrow_left).grid(row=3,column =0, padx=2, pady=2)

                #____________________________________________________________________________


                self.btnArrowL1=Button(TopFrame2Right, width=90, height=50, state = NORMAL,
                command= Loan,image=self.img_arrow_Right).grid(row=0,column =0, padx=2, pady=2)

                self.btnArrowL2=Button(TopFrame2Right, width=90, height=50, state = NORMAL,
                command= deposit, image=self.img_arrow_Right).grid(row=1,column =0, padx=2, pady=2)

                self.btnArrowL3=Button(TopFrame2Right, width=90, height=50, state = NORMAL,
                command= request_new_pin, image=self.img_arrow_Right).grid(row=2,column =0, padx=2, pady=2)

                self.btnArrowL4=Button(TopFrame2Right, width=90, height=50, state = NORMAL,
                command= statement, image=self.img_arrow_Right).grid(row=3,column =0, padx=2, pady=2)

            else:
                self.txtReceipt.delete("1.0", END)

                self.txtReceipt.insert(END,'Invalid Pin Number' + "\n\n") 
                



        def clear():
                self.txtReceipt.delete("1.0", END)
                


                self.btnArrowL1=Button(TopFrame2Left, width=90, height=50, state = DISABLED,
                command= withdrawcash, image=self.img_arrow_left).grid(row=0,column =0, padx=2, pady=2)

                self.btnArrowL2=Button(TopFrame2Left, width=90, height=50, state = DISABLED,
                command= Loan, image=self.img_arrow_left).grid(row=1,column =0, padx=2, pady=2)

                self.btnArrowL3=Button(TopFrame2Left, width=90, height=50, state = DISABLED,
                image=self.img_arrow_left).grid(row=2,column =0, padx=2, pady=2)

                self.btnArrowL4=Button(TopFrame2Left, width=90, height=50, state = DISABLED,
                image=self.img_arrow_left).grid(row=3,column =0, padx=2, pady=2)

                #____________________________________________________________________________


                self.btnArrowL1=Button(TopFrame2Right, width=90, height=50, state = DISABLED,
                image=self.img_arrow_Right).grid(row=0,column =0, padx=2, pady=2)

                self.btnArrowL2=Button(TopFrame2Right, width=90, height=50, state = DISABLED,
                image=self.img_arrow_Right).grid(row=1,column =0, padx=2, pady=2)

                self.btnArrowL3=Button(TopFrame2Right, width=90, height=50, state = DISABLED,
                image=self.img_arrow_Right).grid(row=2,column =0, padx=2, pady=2)

                self.btnArrowL4=Button(TopFrame2Right, width=90, height=50, state = DISABLED,
                image=self.img_arrow_Right).grid(row=3,column =0, padx=2, pady=2)

        def input_value():
            global bal
            cash = self.txtReceipt.get("1.0", "end-1c")
            bal= bal-int(cash)
            self.txtReceipt.insert(END, "\n\n" + 'The cash withdrawn: '+ cash )

        def input_value2():
            global bal
            cash = self.txtReceipt.get("1.0", "end-1c")
            bal= bal+int(cash)
            self.txtReceipt.insert(END, "\n\n" + 'The cash deposited: '+ cash )
            
        def input_value3():
            global bal
            cash = self.txtReceipt.get("1.0", "end-1c")
            bal= bal+int(cash)
            self.txtReceipt.insert(END, "\n\n" + 'Loaned Rupees: '+ cash )    

        def insert0():
            Value0 = 0
            self.txtReceipt.insert(END, Value0)

        def insert1():
            Value1 = 1
            self.txtReceipt.insert(END, Value1)

        def insert2():
            Value2 = 2
            self.txtReceipt.insert(END, Value2)

        def insert3():
            Value3 = 3
            self.txtReceipt.insert(END, Value3)

        def insert4():
            Value4 = 4
            self.txtReceipt.insert(END, Value4)


        def insert5():
            Value5 = 5
            self.txtReceipt.insert(END, Value5)

        def insert6():
            Value6 = 6
            self.txtReceipt.insert(END, Value6)

        def insert7():
            Value7 = 7
            self.txtReceipt.insert(END, Value7)

        def insert8():
            Value8 = 8
            self.txtReceipt.insert(END, Value8)

        def insert9():
            Value9 = 9
            self.txtReceipt.insert(END, Value9)

        def cancel():
            Cancel = tkinter.messagebox.askyesno("ATM", "Confirm if you want to cancel")
            if Cancel > 0:
                self.root.destroy()
                return

        def withdrawcash():
            #input_value()
            self.txtReceipt.delete("1.0", END)
            #global bal
            #self.txtReceipt.insert(END, 'Withdraw Rupees: ' )
            
            
            
            

           
            self.txtReceipt.focus_set()


        def withdrawcash2():
            input_value()
            self.txtReceipt.delete("1.0", END)
            self.txtReceipt.insert(END, 'Withdraw Rupees: ' )
            
            self.txtReceipt.focus_set()

        def Loan2():
            enter_pin()
            self.txtReceipt.delete("1.0", END)
            self.txtReceipt.insert(END, 'Loan Rupees: ' )
            self.txtReceipt.focus_set()

        def Loan():
            self.txtReceipt.delete("1.0", END)

            self.txtReceipt.focus_set()           

        def deposit():
            
            self.txtReceipt.delete("1.0", END)

            self.txtReceipt.focus_set()

        def request_new_pin():
            enter_pin()
            self.txtReceipt.delete("1.0", END)
            self.txtReceipt.insert(END, '\t\tWelcome to ABC Bank' + "\n\n" )
            self.txtReceipt.insert(END, 'New Pin will be send to your home address.' + "\n\n" )
            self.txtReceipt.insert(END,'Withdraw Cash\t\t\t Loan' + "\n\n\n\n") 
            self.txtReceipt.insert(END,'Cash with Receipt\t\t\t Deposit' + "\n\n\n\n") 
            self.txtReceipt.insert(END,'Balance\t\t\t Request New Pin' + "\n\n\n\n") 
            self.txtReceipt.insert(END,'Mini Statement\t\t\t Print Statement' + "\n\n\n\n")
            self.txtReceipt.insert(END, 'Thanks for using ABC Bank' )

        def Balance():
            self.txtReceipt.delete("1.0", END)
            self.txtReceipt.insert(END, '\t\tWelcome to ABC Bank' + "\n\n")
            

            self.txtReceipt.insert(END, 'Your total Balance is ₹' + str(bal) + "\n" )
            self.txtReceipt.insert(END,'Withdraw Cash\t\t\t Loan' + "\n\n\n\n") 
            self.txtReceipt.insert(END,'Cash with Receipt\t\t\t Deposit' + "\n\n\n\n") 
            self.txtReceipt.insert(END,'Balance\t\t\t Request New Pin' + "\n\n\n\n") 
            self.txtReceipt.insert(END,'Mini Statement\t\t\t Print Statement' + "\n\n\n\n")
            self.txtReceipt.insert(END, 'Thanks for using ABC Bank' )


        def statement():
            global bal
            self.txtReceipt.delete("1.0", END)

            self.txtReceipt.insert(END, '\tAccount Balance ₹' + str(bal) + "\t\t\n\n")
            self.txtReceipt.insert(END,'Rent \t\t\t\t ₹30000' + "\n\n") 
            self.txtReceipt.insert(END,'Auto \t\t\t\t ₹20' + "\n\n") 
            self.txtReceipt.insert(END,'Fruits \t\t\t\t ₹180' + "\n\n") 
            self.txtReceipt.insert(END,'Auto \t\t\t\t ₹20' + "\n\n")
            self.txtReceipt.insert(END,'Fees \t\t\t\t ₹80000' + "\n\n")
            self.txtReceipt.insert(END,'Auto \t\t\t\t ₹20' + "\n\n")
            self.txtReceipt.insert(END,'clothes \t\t\t\t ₹2000' + "\n\n")
            self.txtReceipt.insert(END,'Auto \t\t\t\t ₹20' + "\n\n")
            self.txtReceipt.insert(END,'Auto \t\t\t\t ₹20' + "\n\n")

        def statement2():
            pinNo1 = str(self.txtReceipt.get("1.0", "end-1c"))
            pinNo2 = str(pinNo1)
            pinNo3 = float(pinNo2)
            pinNo4 = float(150000 - (pinNo3))
            self.txtReceipt.delete("1.0", END)
            self.txtReceipt.insert(END, '\n\t' + str(pinNo4) + "\t\t")
            self.txtReceipt.insert(END, '\t\t\t\t Account Balance ₹' + str(pinNo4) + "\t\t\n\n")
            self.txtReceipt.insert(END,'Rent \t\t\t\t ₹30000' + "\n\n") 
            self.txtReceipt.insert(END,'Auto \t\t\t\t ₹20' + "\n\n") 
            self.txtReceipt.insert(END,'Fruits \t\t\t\t ₹180' + "\n\n") 
            self.txtReceipt.insert(END,'Auto \t\t\t\t ₹20' + "\n\n")
            self.txtReceipt.insert(END,'Fees \t\t\t\t ₹80000' + "\n\n")
            self.txtReceipt.insert(END,'Auto \t\t\t\t ₹20' + "\n\n")
            self.txtReceipt.insert(END,'clothes \t\t\t\t ₹2000' + "\n\n")
            self.txtReceipt.insert(END,'Auto \t\t\t\t ₹20' + "\n\n")
            self.txtReceipt.insert(END,'Auto \t\t\t\t ₹20' + "\n\n")
            
        #_________________________________WIDGET_____________________________________

        self.txtReceipt = Text(TopFrame2Mid, height=17, width= 42, bd=12, font=('arial', 9, 'bold'))
        self.txtReceipt.grid(row=0, column=0)

        self.img_arrow_left = PhotoImage(file="lArrow.png")

        self.btnArrowL1=Button(TopFrame2Left, width=90, height=50, state = DISABLED,
        command= withdrawcash,image=self.img_arrow_left).grid(row=0,column =0, padx=2, pady=2)

        self.btnArrowL2=Button(TopFrame2Left, width=90, height=50, state = DISABLED,
        command= withdrawcash, image=self.img_arrow_left).grid(row=1,column =0, padx=2, pady=2)

        self.btnArrowL3=Button(TopFrame2Left, width=90, height=50, state = DISABLED,
        command= Balance, image=self.img_arrow_left).grid(row=2,column =0, padx=2, pady=2)

        self.btnArrowL4=Button(TopFrame2Left, width=90, height=50, state = DISABLED,
        command= statement, image=self.img_arrow_left).grid(row=3,column =0, padx=2, pady=2)

        #____________________________________________________________________________

        self.img_arrow_Right = PhotoImage(file="rArrow.png")


        self.btnArrowL1=Button(TopFrame2Right, width=90, height=50, state = DISABLED,
        command= Loan, image=self.img_arrow_Right).grid(row=0,column =0, padx=2, pady=2)

        self.btnArrowL2=Button(TopFrame2Right, width=90, height=50, state = DISABLED,
        command= deposit, image=self.img_arrow_Right).grid(row=1,column =0, padx=2, pady=2)

        self.btnArrowL3=Button(TopFrame2Right, width=90, height=50, state = DISABLED,
        command= request_new_pin, image=self.img_arrow_Right).grid(row=2,column =0, padx=2, pady=2)

        self.btnArrowL4=Button(TopFrame2Right, width=90, height=50, state = DISABLED,
        command= statement, image=self.img_arrow_Right).grid(row=3,column =0, padx=2, pady=2)


        #________________________________PIN_________________________________________

        self.img_1 = PhotoImage(file="one.png")


        self.btn1=Button(TopFrame1, width=90, height=50, command= insert1,
        image=self.img_1).grid(row=2,column =0, padx=4, pady=4)
        
        self.img_2 = PhotoImage(file="two.png")
        self.btn2=Button(TopFrame1, width=90, height=50, command= insert2,
        image=self.img_2).grid(row=2,column =1, padx=4, pady=4)

        self.img_3 = PhotoImage(file="three.png")
        self.btn3=Button(TopFrame1, width=90, height=50, command= insert3,
        image=self.img_3).grid(row=2,column =2, padx=4, pady=4)

        self.img_CE = PhotoImage(file="cancel.png")
        self.btn3=Button(TopFrame1, width=90, height=50, command= cancel,
        image=self.img_CE).grid(row=2,column =3, padx=4, pady=4)

        #__________________________________________________________________________

        self.img_4 = PhotoImage(file="four.png")
        self.btn4=Button(TopFrame1, width=90, height=50, command= insert4,
        image=self.img_4).grid(row=3,column =0, padx=4, pady=4)

        self.img_5 = PhotoImage(file="five.png")
        self.btn4=Button(TopFrame1, width=90, height=50, command= insert5,
        image=self.img_5).grid(row=3,column =1, padx=4, pady=4)
 

        self.img_6 = PhotoImage(file="six.png")
        self.btn4=Button(TopFrame1, width=90, height=50, command= insert6,
        image=self.img_6).grid(row=3,column =2, padx=4, pady=4)
 
        self.img_C1 = PhotoImage(file="clear.png")
        self.btn4=Button(TopFrame1, width=90, height=50, command= clear,
        image=self.img_C1).grid(row=3,column =3, padx=4, pady=4)

        #__________________________________________________________________________
 
        self.img_7 = PhotoImage(file="seven.png")
        self.btn4=Button(TopFrame1, width=90, height=50, command= insert7,
        image=self.img_7).grid(row=4,column =0, padx=4, pady=4)

        self.img_8 = PhotoImage(file="eight.png")
        self.btn4=Button(TopFrame1, width=90, height=50, command= insert8,
        image=self.img_8).grid(row=4,column =1, padx=4, pady=4)
 

        self.img_9 = PhotoImage(file="nine.png")
        self.btn4=Button(TopFrame1, width=90, height=50, command= insert9,
        image=self.img_9).grid(row=4,column =2, padx=4, pady=4)
 
        self.img_Enter = PhotoImage(file="enter.png")
        self.btn4=Button(TopFrame1, width=90, height=50, command= enter_pin,
        image=self.img_Enter).grid(row=4,column =3, padx=4, pady=4)


       #=============================================================================


        self.imgSp1 = PhotoImage(file="empty.png")
        self.btn4=Button(TopFrame1, width=90, height=50, command= input_value,
        image=self.imgSp1).grid(row=5,column =0, padx=4, pady=4)

        self.img_0 = PhotoImage(file="zero.png")
        self.btn4=Button(TopFrame1, width=90, height=50, command= insert0,
        image=self.img_0).grid(row=5,column =1, padx=4, pady=4)
 

        self.img_Sp2 = PhotoImage(file="empty.png")
        self.btn4=Button(TopFrame1, width=90, height=50, command=input_value2,
        image=self.img_Sp2).grid(row=5,column =2, padx=4, pady=4)
 
        self.img_Sp3 = PhotoImage(file="empty.png")
        self.btn4=Button(TopFrame1, width=90, height=50, command= input_value3,
        image=self.img_Sp3).grid(row=5,column =3, padx=4, pady=4)
 










if __name__ =='__main__':
    root = Tk()
    application= atm(root)
    root.mainloop()
        
