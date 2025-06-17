import time
import tkinter as tk
from tkinter import *
import mix
import heat
import math

class add():

    def __init__(self, ingredient, amount, actions, iter):
        self.ingredient = ingredient
        self.amount = amount
        self.isDone = False
        self.actions = actions
        self.iter = iter

        self.expression = 'Dodaj ' + str(self.amount) + ' ' + self.ingredient
        self.addW = tk.Tk()

        self.addW.geometry("500x500")
        self.addW.title('Dodawanie')

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

        self.canvas = Canvas(self.addW,width=500, height=500)
        self.canvas.pack()
        self.base = self.canvas.create_rectangle(175,350,325,370, fill='black')
        self.vessel = self.canvas.create_polygon(self.x0+self.r4*math.cos(self.fi4+self.alfa),self.y0+self.r4*math.sin(self.fi4+self.alfa),self.x0+self.r1*math.cos(self.fi1+self.alfa),self.y0+self.r1*math.sin(self.fi1+self.alfa),self.x0-self.r3*math.cos(self.fi3+self.alfa),self.y0-self.r3*math.sin(self.fi3+self.alfa),self.x0+self.r2*math.cos(self.fi2+self.alfa),self.y0+self.r2*math.sin(self.fi2+self.alfa),fill='light gray')
        

        self.actionLabel = tk.Label(self.addW, text = self.expression)
        self.actionLabel.place(x=10,y=70)

        self.confButton = tk.Button(self.addW,text='Potwierdz', command = self.callbackConfirm)
        self.confButton.pack(padx=100,pady=30)
        self.confButton.place(x=100,y=30)

        self.addW.mainloop()

    def callbackConfirm(self):
        self.isDone = True
        self.addW.destroy()
        if self.iter<len(self.actions):
            if self.actions.iloc[self.iter,0] == "mix":
                cook = mix.mix(self.actions.iloc[self.iter,1],self.actions.iloc[self.iter,2],self.actions,self.iter+1)
            if self.actions.iloc[self.iter,0] == "heat":
                cook = heat.heat(self.actions.iloc[self.iter,1],self.actions.iloc[self.iter,3],self.actions,self.iter+1)
            if self.actions.iloc[self.iter,0] == "add":
                cook = add(self.actions.iloc[self.iter,4],self.actions.iloc[self.iter,5],self.actions,self.iter+1)
        