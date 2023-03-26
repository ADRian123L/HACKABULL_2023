import tkinter
import tkinter.messagebox

#__class definition__
class kiloConvert:
    def __init__(self):
        """The constructor initializes the object with the API key and the model."""
        self.i = 0

    def do(self) -> None:
        """The method creates the main window."""
        self.mw = tkinter.Tk() #main window
        self.mw.title('kilometer conversion') #title of the window

        self.top =tkinter.Frame() #default-applied to your only window attribute
        self.bottom1 = tkinter.Frame() #default-applied to your only window attribute
        self.bottom2 = tkinter.Frame() #default-applied to your only window attribute

        self.prompt = tkinter.Label(self.top, text = 'Enter a decimal number:') #for text entry
        self.kentry = tkinter.Entry(self.top, width = 20) #for text entry
        self.prompt2 = tkinter.Label(self.bottom1, text = 'Enter the quotient: ') #for text entry
        self.kentry2 = tkinter.Entry(self.bottom1, width = 8) #for text entry
        self.prompt3 = tkinter.Label(self.bottom1, text = 'Enter the reminder: ') #for text entry
        self.kentry3 = tkinter.Entry(self.bottom1, width = 8) #for text entry   

        # Pack the top widgets
        self.prompt.pack(side = 'left')
        self.kentry.pack(side = 'left')
        self.prompt2.pack(side = 'left')
        self.kentry2.pack(side = 'left')
        self.prompt3.pack(side = 'left')
        self.kentry3.pack(side = 'left')

        # Pack the bottom widgets
        self.check = tkinter.Button(self.bottom2, text = 'Check', command = self.check)
        self.quit = tkinter.Button(self.bottom2, text = 'Quit', command = self.mw.destroy)

        # Pack the buttons
        self.check.pack(side = 'left')
        self.quit.pack(side = 'left')
        
        # Pack the frames
        self.top.pack()#default is the top
        self.bottom1.pack()
        self.bottom2.pack(side = 'bottom')

        # Enter the tkinter main loop
        tkinter.mainloop()
        
    def check(self) -> None:
        """The method checks the answer."""
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

if __name__ == "__main__":
    kc = kiloConvert()
    kc.do()
