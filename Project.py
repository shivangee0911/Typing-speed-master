words = ['Disney','Mango','Dictionary','Harry','Amazon','Ronaldo','Christmas','Nile','Mountain']
def labelSlider():
    global count, sliderwords
    text = 'Welcome to typing speed increaser game'
    if(count >= len(text)):
        count = 0
        sliderwords = ''
    sliderwords += text[count]
    count += 1
    fontLabel.configure(text=sliderwords)
    fontLabel.after(150,labelSlider)


def time():
     global timeleft,score,miss
     if(timeleft >= 11):
         pass
     else:
         timeLabelCount.configure(fg='red')
     if(timeleft > 0):
         timeleft -= 1
         timeLabelCount.configure(text = timeleft)
         timeLabelCount.after(1000,time)

     else:
         gamePlayDetaiLabel.configure(text ='Hit ={} |Miss = {} |Total score ={}'.format(score,miss,score-1))
         rr = messagebox.askretrycancel('Notification','For play again hit retry button')
         if(rr == True):
           score = 0
           timeleft = 14
           miss = 0
           timeLabelCount.configure(text = timeleft)
           wordLabel.configure(text = words[0])
           scoreLabelCount.configure(text = score)

def startGame(event):
    global score ,miss
    if(timeleft == 14):
       time()
    gamePlayDetaiLabel.configure(text='')
    if (wordEntry.get() == wordLabel['text']):
        score += 1
        scoreLabelCount.configure(text=score)
    else:
         miss += 1
         print('Miss =',+miss)
    random.shuffle(words)
    wordLabel.configure(text=words[0])
    wordEntry.delete(0,END)

from tkinter import *
import random
from tkinter import messagebox

################################ Root Method
root = Tk()
root.geometry('800x600+400+100')
root.configure(bg= 'black')
root.title('Typing Speed Increaser Game')
##########################################Variable

score  =0
timeleft = 14
count = 0
sliderwords =''
miss = 0
##############################Label Methods

random.shuffle(words)

wordLabel = Label(root, text=words[0],font=('airal',40,'italic bold'),
                  bg = 'powder blue')
wordLabel.place(x=350,y=200)

scoreLabel =Label(root, text='YOUR SCORE :',font=('airal',10,'italic bold'),
                  bg = 'yellow',fg='black')
scoreLabel.place(x=10,y=100)

scoreLabelCount = Label(root, text=score,font=('airal',15,'italic bold'),
                  bg = 'black',fg='white')
scoreLabelCount.place(x=60,y=150)

timerLabel =Label(root, text='Time Left:' ,font=('airal',10,'italic bold'),
                  bg = 'yellow',fg='black')
timerLabel.place(x=600,y=100)

timeLabelCount = Label(root, text=timeleft,font=('airal',15,'italic bold'),
                  bg = 'black',fg='purple')
timeLabelCount.place(x=600,y=150)

gamePlayDetaiLabel = Label(root, text='Type word and Hit enter button',font=('arial',25,'italic bold'),)
gamePlayDetaiLabel.place(x=120,y=450)
######################entry method
#################################################
root.bind('<Return>',startGame)
root.mainloop()