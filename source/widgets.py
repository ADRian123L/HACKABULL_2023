import tkinter
import tkinter.messagebox

#__class definition__
class Decimal_Binary_Convert:
    def __init__(self, base: int = 10, quotient: int = 0, i: int = 0):
        self.base = base
        self.quotient = quotient
        self.i = i

    def do(self):
        
        self.mw = tkinter.Tk()
        self.mw.title('Decimal_Binary converter')

        #create frames
        self.top =tkinter.Frame()

        self.bottom1 = tkinter.Frame() #default-applied to your only window attribute
        self.bottom2 = tkinter.Frame()

        #create widgets for top frame
        self.prompt = tkinter.Label(self.top, text = 'Enter a decimal number:')
        
        self.kentry = tkinter.Entry(self.top, width = 20) #for text entry
        self.prompt2 = tkinter.Label(self.bottom1, text = 'Enter the quotient: ')
        self.kentry2 = tkinter.Entry(self.bottom1, width = 8)
        self.prompt3 = tkinter.Label(self.bottom1, text = 'Enter the reminder: ')
        self.kentry3 = tkinter.Entry(self.bottom1, width = 8)

        #pack top widgets
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
        
    def store_base(self) -> int:
        """store the decimal number"""
        self.base = int(self.kentry.get())
        return self.decimal
    
    def store_quotient(self) -> int:
        """store the quotient"""
        self.quotient = int(self.kentry2.get())
        return self.quotient
    
    def calculate(self) -> int:
        """calculate the quotient and reminder"""
        self.quotient = int(self.base / 2)
        self.reminder = self.base % 2
        return self.quotient, self.reminder

    def check_input(self) -> bool:
        """check if the input is correct"""
        if self.quotient == int(self.kentry2.get()) and self.reminder == int(self.kentry3.get()):
            return True
        else:
            return False
        
    def loop_game(self) -> None:
        """"This function will loop the game"""



    def check(self):
        self.i += 1
        print(self.i)
    
        if self.i <= 1:
            self.store_base()
            self.calculate()
            answer = int(self.kentry2.get())
            answer2 = int(self.kentry3.get())
            self.bottom3 = tkinter.Frame()

            if self.check_input():
                self.answer = tkinter.Label(self.bottom3, text = f"You are right!")
                self.answer.pack()
                self.bottom3.pack()
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
                self.append()
            else:
                self.answer = tkinter.Label(self.bottom3, text = f"Sorry, you made it wrong.\nAnswer should be: \n quotient:{quotient}, Reminder: {reminder}")
                self.answer.pack()

    def append(self):
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
        
    
        
        #displat result
        


#__driver portion__

#create an object
kc = Decimal_Binary_Convert()
kc.do()
