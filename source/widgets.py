import tkinter
import tkinter.messagebox

#__class definition__
class Decimal_Binary_Convert:
    def __init__(self):
        #create main window
        self.i = 0
        self.j = 0
        self.divident = 100
        self.k = 0
    def do(self):
        
        self.mw = tkinter.Tk()
        self.mw.title('Decimal-Binary conversion')

        #create frames
        self.top =tkinter.Frame()
        

        self.bottom1 = tkinter.Frame() #default-applied to your only window attribute
        self.bottom2 = tkinter.Frame()

        #create widgets for top frame
        self.text = tkinter.Label(self.top, text = "To convert a decimal number to a binary number, you can follow these steps:\n\
1. Divide the decimal number by 2.\n2.Write down the remainder (either 0 or 1).\n3.Divide the quotient (the result of the division in step 1) by 2.\n\
4. Write down the remainder.\n5.Repeat steps 3 and 4 until the quotient becomes 0.\n6.Write the remainders in reverse order.\nLet's do some practice:\n")
        self.prompt = tkinter.Label(self.top, text = 'Enter a decimal number:')
        
        self.kentry = tkinter.Entry(self.top, width = 20) #for text entry
        self.prompt2 = tkinter.Label(self.bottom1, text = 'Enter the quotient: ')
        self.kentry2 = tkinter.Entry(self.bottom1, width = 8)
        self.prompt3 = tkinter.Label(self.bottom1, text = 'Enter the reminder: ')
        self.kentry3 = tkinter.Entry(self.bottom1, width = 8)

        #pack top widgets
        self.text.pack()
        self.prompt.pack(side = 'left')
        self.kentry.pack(side = 'left')
        self.prompt2.pack(side = 'left')
        self.kentry2.pack(side = 'left')
        self.prompt3.pack(side = 'left')
        self.kentry3.pack(side = 'left')

        #create bottom widgets
        self.check = tkinter.Button(self.bottom2, text = 'Check', command = self.check)
        self.quit = tkinter.Button(self.bottom2, text = 'Quit', command = self.mw.destroy)

        #pack bottom widgets
        self.check.pack(side = 'left')
        self.quit.pack(side = 'left')

        #pack frames
        self.top.pack()#default is the top
        self.bottom1.pack()
        self.bottom2.pack(side = 'bottom')


        #run the main loop
        tkinter.mainloop()
        
    def check(self):
        self.i += 1
        print(self.i)
        if self.divident == 1:
            self.bottom6 = tkinter.Frame()
            self.prompt = tkinter.Label(self.bottom6, text = "You are able to write the binary number now!")
            self.prompt.pack()
            self.bottom6.pack()
            self.bottom7 = tkinter.Frame()
            self.prompt2 = tkinter.Label(self.bottom7, text = "The binary number is: ")
            self.kentry5 = tkinter.Entry(self.bottom7, width = 15)
            self.prompt2.pack(side = 'left')
            self.kentry5.pack(side = 'left')
            self.bottom7.pack()
            self.k = 10
            self.divident = 0;
        elif self.k == 10:
            self.check2()
            
                                        
        elif self.j < 1:
            if self.i <= 1:
                decimal = int(self.kentry.get())
                self.initial = int(self.kentry.get())
                quotient = int(decimal / 2)
                reminder = decimal % 2
                answer = int(self.kentry2.get())
                answer2 = int(self.kentry3.get())
                self.bottom3 = tkinter.Frame()
                if answer == quotient and answer2 == reminder:
                    self.answer = tkinter.Label(self.bottom3, text = f"You are right!")
                    self.answer.pack()
                    self.bottom3.pack()
                    self.j += 1
                    self.divident = quotient
                   
                    self.append()
                else:
                    self.answer = tkinter.Label(self.bottom3, text = f"Sorry, you made it wrong.\nAnswer should be: \n quotient:{quotient}, Reminder: {reminder}")
                    self.answer.pack()
                    self.bottom3.pack()
            else:
                decimal = int(self.kentry.get())
                quotient = int(decimal / 2)
                reminder = decimal % 2
                answer = int(self.kentry2.get())
                answer2 = int(self.kentry3.get())
                self.answer.destroy()
                if answer == quotient and answer2 == reminder:
                    self.answer = tkinter.Label(self.bottom3, text = f"You are right!")
                    self.answer.pack()
                    self.j += 1
                    self.divident = quotient
                    self.append()
                else:
                    self.answer = tkinter.Label(self.bottom3, text = f"Sorry, you made it wrong.\nAnswer should be: \n quotient:{quotient}, Reminder: {reminder}")
                    self.answer.pack()
        else:
            if self.i <= 1:
                quotient = int(self.divident / 2)
                reminder = self.divident % 2
                answer = int(self.kentry2.get())
                answer2 = int(self.kentry3.get())
                self.bottom3 = tkinter.Frame()
                if answer == quotient and answer2 == reminder:
                    self.answer = tkinter.Label(self.bottom3, text = f"You are right!")
                    self.answer.pack()
                    self.bottom3.pack()
                    self.j += 1
                   
                    self.divident = quotient
                    self.append()
                else:
                    self.answer = tkinter.Label(self.bottom3, text = f"Sorry, you made it wrong.\nAnswer should be: \n quotient:{quotient}, Reminder: {reminder}")
                    self.answer.pack()
                    self.bottom3.pack()
            else:
                quotient = int(self.divident / 2)
                reminder = self.divident % 2
                answer = int(self.kentry2.get())
                answer2 = int(self.kentry3.get())
                self.answer.destroy()
                if answer == quotient and answer2 == reminder:
                    self.answer = tkinter.Label(self.bottom3, text = f"You are right!")
                    self.answer.pack()
                    self.j += 1
                    self.divident = quotient
                    self.append()
                else:
                    self.answer = tkinter.Label(self.bottom3, text = f"Sorry, you made it wrong.\nAnswer should be: \n quotient:{quotient}, Reminder: {reminder}")
                    self.answer.pack()

    def append(self):
        self.i = 0
        decimal = int(self.kentry2.get())
        self.bottom4 = tkinter.Frame()
        self.prompt = tkinter.Label(self.bottom4, text = f"Let's {decimal} divide by 2 now!")
        self.prompt.pack()
        self.bottom4.pack()
        self.bottom5 = tkinter.Frame()
        self.prompt2 = tkinter.Label(self.bottom5, text = "Enter the quotient: ")
        self.kentry2 = tkinter.Entry(self.bottom5, width = 8)
        self.prompt3 = tkinter.Label(self.bottom5, text = "Enter the reminder: ")
        self.kentry3 = tkinter.Entry(self.bottom5, width = 8)
        self.prompt2.pack(side = 'left')
        self.kentry2.pack(side = 'left')
        self.prompt3.pack(side = 'left')
        self.kentry3.pack(side = 'left')
        self.bottom5.pack()
    def check2(self):
        binary = int(self.kentry5.get())
        result = int(bin(self.initial)[2:])
        if result == binary:
            tkinter.messagebox.showinfo('Response','You got it right!')
        else:
            print('You are wrong')
        
        
    
        
        #displat result
        


#__driver portion__

#create an object
kc = Decimal_Binary_Convert()
kc.do()
