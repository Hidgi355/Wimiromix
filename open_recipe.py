import tkinter as tk
import pandas as pd
import recipe
class open_recipe:
    def __init__(self, list):
        self.list = pd.DataFrame
        self.list = list.getList()
        self.openW = tk.Tk()
        self.openW.geometry("500x500")
        self.openW.title('Otwórz przepis')
        self.k = 30
        self.j = 10
        self.name = ''
        self.names = []
        self.buttons = []
        self.backButton = tk.Button(self.openW,text="Wroc", command = self.callbackBack)
        self.backButton.pack(padx=100,pady=30)
        for i in range(len(self.list)):
            self.name = self.list.iloc[i,0]
            self.names.append(self.list.iloc[i,0])
            self.openButton=tk.Button(self.openW,text=self.name, command = lambda i=i: self.callbackOpen(i))#
            self.openButton.pack(padx=100,pady=30)
            self.buttons.append(self.openButton)

        for i in self.buttons:
            i.place(x=self.k,y=self.j)
            self.j=self.j+40
            if self.j>400:
                self.j = 30
                self.k = self.k+100
            
            
        self.backButton.place(x=10,y=450)
        self.openW.mainloop()
       
    def callbackOpen(self,j):
        self.doRecipe = recipe.recipe(self.names[j])
        self.doRecipe.realize_recipe()
    
    def callbackBack(self):
        self.openW.destroy()