import tkinter as tk
import time
from tkinter import *
import heat
import add
import math

class mix():
    def __init__(self, givenTime, speed, actions, iter):
        self.isDone = False
        self.time = givenTime
        self.elapsedTime = 0
        self.status = "Czekam na start"
        if speed >=10 and speed<=300:
            self.speed = speed
        elif speed<10:
            self.speed = 10
        elif speed>300:
            self.speed = 300
        self.actions = actions
        self.iter = iter

        self.expression = 'Miksujemy przez ' + str(self.time) + ' minut z predkoscia ' + str(self.speed) + ' obr/min'
        self.mixW = tk.Tk()

        self.mixW.geometry("500x500")
        self.mixW.title('Miksowanie')

        self.mark = 1
        self.alfa = 0
        self.x0 = 250
        self.y0 = 350
        self.r1 = 25
        self.fi1 = 0
        self.r2 = 158
        self.fi2 = 1.3975*math.pi
        self.r3 = 158
        self.fi3 = 0.6025*math.pi
        self.r4 = 25
        self.fi4 = math.pi

        self.canvas = Canvas(self.mixW,width=500, height=500)
        self.canvas.pack()
        self.base = self.canvas.create_rectangle(175,350,325,370, fill='black')
        self.vessel = self.canvas.create_polygon(self.x0+self.r4*math.cos(self.fi4+self.alfa),self.y0+self.r4*math.sin(self.fi4+self.alfa),self.x0+self.r1*math.cos(self.fi1+self.alfa),self.y0+self.r1*math.sin(self.fi1+self.alfa),self.x0-self.r3*math.cos(self.fi3+self.alfa),self.y0-self.r3*math.sin(self.fi3+self.alfa),self.x0+self.r2*math.cos(self.fi2+self.alfa),self.y0+self.r2*math.sin(self.fi2+self.alfa),fill='light gray')
        
        self.actionLabel = tk.Label(self.mixW, text = self.expression)
        self.actionLabel.place(x=10,y=70)

        self.timeLabelTxt = tk.Label(self.mixW, text = "czas")
        self.timeLabelTxt.place(x=10,y=30)

        self.startButton = tk.Button(self.mixW,text='Start', command = self.callbackStart)
        self.confButton = tk.Button(self.mixW,text='Potwierdz', command = self.callbackConfirm)
        self.startButton.pack(padx=100,pady=30)
        self.confButton.pack(padx=100,pady=30)
        self.startButton.place(x=300,y=30)
        self.confButton.place(x=300,y=70)

        self.timeLabelNum = tk.Label(self.mixW, text = str(round(self.elapsedTime,2)))
        self.timeLabelNum.place(x=100,y=30)

        self.statusLabelTxt = tk.Label(self.mixW, text = "Status:")
        self.statusLabelTxt.place(x=10,y=110)

        self.statusLabel = tk.Label(self.mixW, text = self.status)
        self.statusLabel.place(x=50,y=110)

        self.mixW.mainloop()

    def callbackStart(self): 
        self.start = time.time()
        self.callbackRefresh()
            
    def callbackRefresh(self):
        if self.elapsedTime <= self.time:
            self.elapsedTime = time.time() - self.start
            self.timeLabelNum.config(text = str(round(self.elapsedTime,2)))
            self.status = "W trakcie"
            self.statusLabel.config(text = self.status)
            self.vessel = self.canvas.create_polygon(self.x0+self.r4*math.cos(self.fi4+self.alfa),self.y0+self.r4*math.sin(self.fi4+self.alfa),self.x0+self.r1*math.cos(self.fi1+self.alfa),self.y0+self.r1*math.sin(self.fi1+self.alfa),self.x0-self.r3*math.cos(self.fi3+self.alfa),self.y0-self.r3*math.sin(self.fi3+self.alfa),self.x0+self.r2*math.cos(self.fi2+self.alfa),self.y0+self.r2*math.sin(self.fi2+self.alfa),fill='#f0f0f0')
            self.alfa = self.mark*0.03 + self.alfa
            if self.alfa > 0.1 or self.alfa < -0.1:
                self.mark = self.mark*(-1)
            self.canvas.create_polygon(self.x0+self.r4*math.cos(self.fi4+self.alfa),self.y0+self.r4*math.sin(self.fi4+self.alfa),self.x0+self.r1*math.cos(self.fi1+self.alfa),self.y0+self.r1*math.sin(self.fi1+self.alfa),self.x0-self.r3*math.cos(self.fi3+self.alfa),self.y0-self.r3*math.sin(self.fi3+self.alfa),self.x0+self.r2*math.cos(self.fi2+self.alfa),self.y0+self.r2*math.sin(self.fi2+self.alfa),fill='light gray')
            self.base = self.canvas.create_rectangle(175,350,325,370, fill='black')
            self.mixW.after(10, self.callbackRefresh)
        else:    
            self.isDone = True
            self.status = "Zrobione"
            self.statusLabel.config(text = self.status)

    def callbackConfirm(self):
        if self.isDone:
            self.mixW.destroy()
            if self.iter<len(self.actions):
                if self.actions.iloc[self.iter,0] == "mix":
                    cook = mix(self.actions.iloc[self.iter,1],self.actions.iloc[self.iter,2],self.actions,self.iter+1)
                if self.actions.iloc[self.iter,0] == "heat":
                    cook = heat.heat(self.actions.iloc[self.iter,1],self.actions.iloc[self.iter,3],self.actions,self.iter+1)
                if self.actions.iloc[self.iter,0] == "add":
                    cook = add.add(self.actions.iloc[self.iter,4],self.actions.iloc[self.iter,5],self.actions,self.iter+1)