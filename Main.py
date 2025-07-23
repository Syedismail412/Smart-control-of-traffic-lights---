from tkinter import messagebox
from tkinter import *
from tkinter import simpledialog
import tkinter
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from traffic_simulation import *
from yolo_traffic import *

main = tkinter.Tk()
main.title("Smart Control of Traffic Light Using Artificial Intelligence")
main.geometry("1300x1200")

global filename

def yoloTrafficDetection():
    global filename
    filename = filedialog.askopenfilename(initialdir="Videos")
    pathlabel.config(text=filename)
    text.delete('1.0', END)
    text.insert(END,filename+" loaded\n");
    runYolo(filename)
   
def runSimulation():
    sim = Simulation()
    sim.runSimulation()

def exit():
    main.destroy()

    
font = ('times', 16, 'bold')
title = Label(main, text='Smart Control of Traffic Light Using Artificial Intelligence')
title.config(bg='light cyan', fg='pale violet red')  
title.config(font=font)           
title.config(height=3, width=120)       
title.place(x=0,y=5)

font1 = ('times', 14, 'bold')
simulationButton = Button(main, text="Run Traffic Simulation", command=runSimulation)
simulationButton.place(x=50,y=100)
simulationButton.config(font=font1)  

pathlabel = Label(main)
pathlabel.config(bg='light cyan', fg='pale violet red')  
pathlabel.config(font=font1)           
pathlabel.place(x=460,y=100)

yoloButton = Button(main, text="Run Yolo Traffic Detection & Counting", command=yoloTrafficDetection)
yoloButton.place(x=50,y=150)
yoloButton.config(font=font1) 

exitButton = Button(main, text="Exit", command=exit)
exitButton.place(x=460,y=150)
exitButton.config(font=font1) 


font1 = ('times', 12, 'bold')
text=Text(main,height=20,width=150)
scroll=Scrollbar(text)
text.configure(yscrollcommand=scroll.set)
text.place(x=10,y=250)
text.config(font=font1)


main.config(bg='snow3')
main.mainloop()
