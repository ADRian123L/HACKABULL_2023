import tkinter
import tkinter.messagebox

#__class definition__
class kiloConvert:
    def __init__(self):
        #create main window
        self.i = 0
    def do(self):
        
        self.mw = tkinter.Tk()



        self.mw.title('kilometer conversion')

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
        
    def check(self):
        self.i += 1
        print(self.i)
        if self.i <= 1:
            decimal = int(self.kentry.get())
            quotient = int(decimal / 2)
            reminder = decimal % 2
            answer = int(self.kentry2.get())
            answer2 = int(self.kentry3.get())
            self.bottom3 = tkinter.Frame()
            if answer == quotient and answer2 == reminder:
                self.answer = tkinter.Label(self.bottom3, text = f"You are right!")
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
             
            if answer == quotient and answer2 == reminder:
                self.answer = tkinter.Label(self.bottom3, text = f"You are right!")
                self.answer.pack()
            else:
                self.answer = tkinter.Label(self.bottom3, text = f"Sorry, you made it wrong.\nAnswer should be: \n quotient:{quotient}, Reminder: {reminder}")
                self.answer.pack()

        #displat result
        


#__driver portion__

#create an object
kc = kiloConvert()
kc.do()
