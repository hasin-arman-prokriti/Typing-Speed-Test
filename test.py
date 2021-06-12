import time
from tkinter import *
import random

prompt_lst = ['The quick brown fox jumps over the lazy dog', 'Look for opportunities in every change in your life','The story of life is quicker than the wink of an eye',\
    'A politician is someone who promises a bridge even when there’s no water', 'The important thing to remember is not to forget', 'A perfect summer day is when the sun is shining, the breeze is blowing, the birds are singing, and the lawn mower is broken'\
    'Don’t tell people your plans. Show them your results', 'We can do anything we want to if we stick to it long enough']
    
root = Tk()
root.title('Typing Speed Test')
root.state('zoomed')

title =Label(root, text='Typing Speed Test', font=('Arial', 60),padx=40, pady=50)
title.pack()

def InputProcess():
    global start_time
    def GetInput(event):
        global end_time, user_input
        end_time = time.time()
        user_input = input_box.get()
        input_box['state']= 'disabled'
        ResultGen()
        
    
    root.bind('<Return>', GetInput)
    input_box = Entry(root, width=50, border=5, bg='#BFD1FD', font=('', 16))
    input_box.focus_set() #the cursor is set in the box and will take input immediately. no need to click the box.
    input_box.pack()
    start_time = time.time()
    
def WPMCalc():
    global wpm, prompt_word, user_word, time_taken
    prompt_word = prompt_line.split(' ')
    user_word = user_input.split(' ')
    time_taken = end_time - start_time
    wpm = format(((len(user_word)/time_taken)*60),".0f")

def Accuracy():
    global accuracy
    correct_word = []
    if len(prompt_word) == len(user_word):
        for i in range(len(prompt_word)):
            if prompt_word[i] == user_word[i]:
                correct_word.append(prompt_word[i])

        accuracy = format((len(correct_word)/len(prompt_word)*100), '.0f')
    else:
        accuracy = 'N/A'

def Play():
    global prompt_line, wpm
    start_button.destroy()
    message = Label(root, text='Write this following prompt to check your typing speed (press "Enter" after completion)',padx=40, pady=20, font=('', 20))
    message.pack()
    prompt_line = random.choice(prompt_lst)
    prompt = Label(root, text=prompt_line, pady=20, font=('', 18), fg='Blue')
    prompt.pack()
    time.sleep(0.7)
    InputProcess()

def ResultGen():
    WPMCalc()
    Accuracy()
    wpm_label = Label(root, text=f"WPM: {wpm}", font=('', 20, 'bold'), pady=10)
    accuracy_label = Label(root, text=f"Accuracy: {accuracy} %", font=('', 20, 'bold'), pady=10)
    wpm_label.pack()
    accuracy_label.pack()
    again_button.pack()

def Again():
    root.destroy()

start_button = Button(root, text='START', padx=50, pady=35, bg='#5a8b59', font=('', 16), command=Play)
again_button = Button(root, text='Play again', padx=40, pady=25, bg='#5a8b59', font=('', 16), command=Again)

start_button.pack()

root.mainloop()