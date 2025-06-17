import time
import tkinter as tk
from tkinter import *
import mix
import add
import math
import colorsys

class heat():
    def __init__(self, givenTime, temp, actions, iter):
        self.isDone = False
        self.time = givenTime
        self.elapsedTime = 0
        self.status = "Czekam na start"
        if temp>=30 and temp<=200:
            self.temp = temp
        elif temp<30:
            self.temp = 30
        elif temp>200:
            self.temp = 200
        self.actions = actions
        self.iter = iter

        self.expression = 'Grzejemy przez ' + str(self.time) + ' minut w temperaturze ' + str(self.temp) + ' ℃'
        self.heatW = tk.Tk()

        self.heatW.geometry("500x500")
        self.heatW.title('Grzanie')

        self.tempStep = 0.1
        self.tempStep2 = self.tempStep*(211/44)
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
        self.color = ''
        self.colorChange = 0
        self.colorChange2 = 0

        self.canvas = Canvas(self.heatW,width=500, height=500)
        self.canvas.pack()
        self.base = self.canvas.create_rectangle(175,350,325,370, fill='black')
        self.vessel = self.canvas.create_polygon(self.x0+self.r4*math.cos(self.fi4+self.alfa),self.y0+self.r4*math.sin(self.fi4+self.alfa),self.x0+self.r1*math.cos(self.fi1+self.alfa),self.y0+self.r1*math.sin(self.fi1+self.alfa),self.x0-self.r3*math.cos(self.fi3+self.alfa),self.y0-self.r3*math.sin(self.fi3+self.alfa),self.x0+self.r2*math.cos(self.fi2+self.alfa),self.y0+self.r2*math.sin(self.fi2+self.alfa),fill='light gray')
        
        self.actionLabel = tk.Label(self.heatW, text = self.expression)
        self.actionLabel.place(x=10,y=70)

        self.timeLabelTxt = tk.Label(self.heatW, text = "czas")
        self.timeLabelTxt.place(x=10,y=30)

        self.startButton = tk.Button(self.heatW,text='Start', command = self.callbackStart)
        self.confButton = tk.Button(self.heatW,text='Potwierdz', command = self.callbackConfirm)
        self.startButton.pack(padx=100,pady=30)
        self.confButton.pack(padx=100,pady=30)
        self.startButton.place(x=300,y=30)
        self.confButton.place(x=300,y=70)

        self.timeLabelNum = tk.Label(self.heatW, text = str(round(self.elapsedTime,2)))
        self.timeLabelNum.place(x=100,y=30)

        self.statusLabelTxt = tk.Label(self.heatW, text = "Status:")
        self.statusLabelTxt.place(x=10,y=110)

        self.statusLabel = tk.Label(self.heatW, text = self.status)
        self.statusLabel.place(x=50,y=110)

        self.heatW.mainloop()

    def callbackStart(self): 
        self.start = time.time()
        self.callbackRefresh()
            
    def callbackRefresh(self):
        if self.elapsedTime <= self.time:
            self.elapsedTime = time.time() - self.start
            self.timeLabelNum.config(text = str(round(self.elapsedTime,2)))
            self.status = "W trakcie"
            self.statusLabel.config(text = self.status)
            self.color = '#%02x%02x%02x' % (211+round(self.colorChange), 211-round(self.colorChange2), 211-round(self.colorChange2))
            if((self.colorChange+211)<255-self.tempStep):
                self.colorChange = self.colorChange+self.tempStep
            if((211-self.colorChange2)>(0+self.tempStep2)):
                self.colorChange2 = self.colorChange2+self.tempStep2
            self.canvas.create_polygon(self.x0+self.r4*math.cos(self.fi4+self.alfa),self.y0+self.r4*math.sin(self.fi4+self.alfa),self.x0+self.r1*math.cos(self.fi1+self.alfa),self.y0+self.r1*math.sin(self.fi1+self.alfa),self.x0-self.r3*math.cos(self.fi3+self.alfa),self.y0-self.r3*math.sin(self.fi3+self.alfa),self.x0+self.r2*math.cos(self.fi2+self.alfa),self.y0+self.r2*math.sin(self.fi2+self.alfa),fill=self.color)
            self.heatW.after(10, self.callbackRefresh)
        else:   
            self.isDone = True 
            self.status = "Zrobione"
            self.statusLabel.config(text = self.status)

    def callbackConfirm(self):
        if self.isDone:
            self.heatW.destroy()
            if self.iter<len(self.actions):
                if self.actions.iloc[self.iter,0] == "mix":
                    cook = mix.mix(self.actions.iloc[self.iter,1],self.actions.iloc[self.iter,2],self.actions,self.iter+1)
                if self.actions.iloc[self.iter,0] == "heat":
                    cook = heat(self.actions.iloc[self.iter,1],self.actions.iloc[self.iter,3],self.actions,self.iter+1)
                if self.actions.iloc[self.iter,0] == "add":
                    cook = add.add(self.actions.iloc[self.iter,4],self.actions.iloc[self.iter,5],self.actions,self.iter+1)
        