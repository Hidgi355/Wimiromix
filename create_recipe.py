import pandas as pd
import tkinter as tk
import csv

class create_recipe:
    def __init__(self, list):
       self.isCreated = 0
       self.isDone = 0
       self.create = tk.Tk()
       self.create.geometry("500x500")
       self.create.title('Stwórz przepis')
       self.list = list
       self.recipeName = ''
       self.recipe = pd.DataFrame()

       self.mixButtonCr = tk.Button(self.create,text='Miks', command = self.callbackMixAdd)
       self.heatButtonCr = tk.Button(self.create,text='Grzej', command = self.callbackHeatAdd)
       self.addButtonCr = tk.Button(self.create,text='Dodaj', command = self.callbackAddAdd)
       self.confirmButtonCr = tk.Button(self.create,text='Potwierdz', command = self.callbackConfirm)
       self.endButtonCr = tk.Button(self.create,text='Zakoncz', command = self.callbackEnd)
       self.timeFieldCr = tk.Text(self.create, height = 1, width = 10)
       self.speedFieldCr = tk.Text(self.create, height = 1, width = 10)
       self.tempFieldCr = tk.Text(self.create, height = 1, width = 10)
       self.ingFieldCr = tk.Text(self.create, height = 1, width = 10)
       self.amountFieldCr = tk.Text(self.create, height = 1, width = 10)
       self.nameFieldCr = tk.Text(self.create, height = 1, width = 10)

       self.mixButtonCr.place(x=100,y=30)
       self.heatButtonCr.place(x=150,y=30)
       self.addButtonCr.place(x=200,y=30)
       self.timeFieldCr.place(x=100,y=70)
       self.speedFieldCr.place(x=100,y=110)
       self.tempFieldCr.place(x=100,y=150)
       self.ingFieldCr.place(x=100,y=190)
       self.amountFieldCr.place(x=100,y=230)
       self.nameFieldCr.place(x=100,y=270)
       self.confirmButtonCr.place(x=100,y=310)
       self.endButtonCr.place(x=100,y=350)
    
       self.actionLabel = tk.Label(self.create, text = "czynnosc")
       self.timeLabel = tk.Label(self.create, text = "czas")
       self.speedLabel = tk.Label(self.create, text = "predkosc")
       self.tempLabel = tk.Label(self.create, text = "temperatura")
       self.ingLabel = tk.Label(self.create, text = "skladnik")
       self.amountLabel = tk.Label(self.create, text = "ilosc")
       self.nameLabel = tk.Label(self.create, text = "nazwa przepisu")

       self.actionLabel.place(x=10,y=30)
       self.timeLabel.place(x=10,y=70)
       self.speedLabel.place(x=10,y=110)
       self.tempLabel.place(x=10,y=150)
       self.ingLabel.place(x=10,y=190)
       self.amountLabel.place(x=10,y=230)
       self.nameLabel.place(x=10,y=270)
       
       self.create.mainloop()
    
    def callbackMixAdd(self):
        if (self.timeFieldCr.get("1.0", "1.15") != 0) and(self.timeFieldCr.get("1.0", "1.15") != '') and (self.speedFieldCr.get("1.0", "1.15") != 0) and(self.speedFieldCr.get("1.0", "1.15") != '') and (self.tempFieldCr.get("1.0", "1.15") == '') and(self.ingFieldCr.get("1.0", "1.15") == '') and (self.amountFieldCr.get("1.0", "1.15") == '')and(self.isDone == 1):
            self.row = pd.DataFrame([["mix",self.timeFieldCr.get("1.0", "1.15"),self.speedFieldCr.get("1.0", "1.15"),self.tempFieldCr.get("1.0", "1.15"),self.ingFieldCr.get("1.0", "1.15"),self.amountFieldCr.get("1.0", "1.15")]])
            self.recipe = pd.concat([self.recipe,self.row],ignore_index=True)
        else:
            print("zle parametry")

    def callbackHeatAdd(self):
        if (self.timeFieldCr.get("1.0", "1.15") != 0) and (self.timeFieldCr.get("1.0", "1.15") != '')and (self.speedFieldCr.get("1.0", "1.15") == '') and (self.tempFieldCr.get("1.0", "1.15") != 0) and (self.tempFieldCr.get("1.0", "1.15") != '')and(self.ingFieldCr.get("1.0", "1.15") == '') and (self.amountFieldCr.get("1.0", "1.15") == '')and(self.isDone == 1):
            self.row = pd.DataFrame([["heat",self.timeFieldCr.get("1.0", "1.15"),self.speedFieldCr.get("1.0", "1.15"),self.tempFieldCr.get("1.0", "1.15"),self.ingFieldCr.get("1.0", "1.15"),self.amountFieldCr.get("1.0", "1.15")]])
            self.recipe = pd.concat([self.recipe,self.row],ignore_index=True)
        else:
            print("zle parametry")
    def callbackAddAdd(self):
        if (self.timeFieldCr.get("1.0", "1.15") == '') and (self.speedFieldCr.get("1.0", "1.15") == '') and (self.tempFieldCr.get("1.0", "1.15") == '') and(self.ingFieldCr.get("1.0", "1.15") != '') and (self.amountFieldCr.get("1.0", "1.15") != '')and (self.amountFieldCr.get("1.0", "1.15") != 0)and(self.isDone == 1):
            self.row = pd.DataFrame([["add",self.timeFieldCr.get("1.0", "1.15"),self.speedFieldCr.get("1.0", "1.15"),self.tempFieldCr.get("1.0", "1.15"),self.ingFieldCr.get("1.0", "1.15"),self.amountFieldCr.get("1.0", "1.15")]])
            self.recipe = pd.concat([self.recipe,self.row],ignore_index=True)
        else:
            print("zle parametry")

    def callbackConfirm(self):
        if self.nameFieldCr.get("1.0", "1.15") != '':
            self.recipeName = self.nameFieldCr.get("1.0", "1.15") + ".csv"
            with open(self.recipeName, mode='w', newline='') as file:
                writer = csv.writer(file)
            self.recipe = pd.DataFrame() 
            self.isDone = 1
            self.list.addToList(self.nameFieldCr.get("1.0", "1.15"))
            self.list.saveList()

    def callbackEnd(self):
        if self.recipeName != '':
            self.recipe.to_csv(self.recipeName,index=False,header=None)
        self.create.destroy()

    def __del__(self):
        self.recipe.to_csv(self.recipeName,index=False,header=None)