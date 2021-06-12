import time
from tkinter import *
import random

class TypingTest:
    prompt_lst = ['The quick brown fox jumps over the lazy dog', 'Look for opportunities in every change in your life','The story of life is quicker than the wink of an eye',\
    'A politician is someone who promises a bridge even when there’s no water', 'The important thing to remember is not to forget', 'A perfect summer day is when the sun is shining, the breeze is blowing, the birds are singing, and the lawn mower is broken',\
    'Don’t tell people your plans. Show them your results', 'We can do anything we want to if we stick to it long enough']
 
    def __init__(self):
        self.root = Tk()
        self.root.title('Typing Speed Test')
        self.root.state('zoomed')
        self.title =Label(self.root, text='Typing Speed Test', font=('Arial', 60),padx=40, pady=50)
        self.title.pack()
        self.start_button = Button(self.root, text='START', padx=50, pady=35, bg='#5a8b59', font=('', 16), command=self.Play)
        self.again_button = Button(self.root, text='Play again', padx=40, pady=25, bg='#5a8b59', font=('', 16), command=self.Again)

        self.start_button.pack()

        self.root.mainloop()

    def Play(self):
        self.start_button.destroy()
        self.message = Label(self.root, text='Write this following prompt to check your typing speed (press "Enter" after completion)',padx=40, pady=20, font=('', 20))
        self.message.pack()
        self.prompt_line = random.choice(TypingTest.prompt_lst)
        self.prompt = Label(self.root, text=self.prompt_line, pady=20, font=('', 18), fg='Blue')
        self.prompt.pack()
        self.CountDown()
        
        

    def Again(self):
        self.root.destroy()
        TypingTest()

    def CountDown(self):
        count = Label(self.root, text='3..2..1..START', font=('', 16, 'bold'))
        count.pack()
        self.root.after(3000, self.InputProcess)


    def InputProcess(self):
        #global start_time
        def GetInput(event):
            #global end_time, user_input
            self.end_time = time.time()
            self.user_input = self.input_box.get()
            self.input_box['state']= 'disabled'
            self.ResultGen()
        self.root.bind('<Return>', GetInput)

        self.input_box = Entry(self.root, width=50, border=5, bg='#BFD1FD', font=('', 16))
        self.input_box.focus_set() #the cursor is set in the box and will take input immediately. no need to click the box.
        self.input_box.pack()
        self.start_time = time.time()

    def ResultGen(self):
        self.WPMCalc()
        self.Accuracy()
        wpm_label = Label(self.root, text=f"WPM: {self.wpm}", font=('', 20, 'bold'), pady=10)
        accuracy_label = Label(self.root, text=f"Accuracy: {self.accuracy} %", font=('', 20, 'bold'), pady=10)
        wrong_word_label = Label(self.root, text=f"Wrong words are: {', '.join(self.wrong_word)}", font=('', 16))
        wpm_label.pack()
        accuracy_label.pack()
        wrong_word_label.pack()
        self.again_button.pack()

    def WPMCalc(self):
        #global wpm, prompt_word, user_word, time_taken
        self.prompt_word = self.prompt_line.split(' ')
        self.user_word = self.user_input.split(' ')
        time_taken = self.end_time - self.start_time
        self.wpm = format(((len(self.user_word)/time_taken)*60),".0f")

    def Accuracy(self):
        global accuracy
        correct_word = []
        self.wrong_word =[]
        if len(self.prompt_word) == len(self.user_word):
            for i in range(len(self.prompt_word)):
                if self.prompt_word[i] == self.user_word[i]:
                    correct_word.append(self.prompt_word[i])
                else:
                    self.wrong_word.append(self.user_word[i])

            self.accuracy = format((len(correct_word)/len(self.prompt_word)*100), '.0f')
        else:
            self.accuracy = 'N/A'
            self.wrong_word = self.user_word

if __name__ == "__main__":
    TypingTest()
