from time import sleep
import tkinter as tk
class weight():
    def __init__(self, ingredient, weight):
        self.ingredient = ingredient
        self.weight = weight
        self.prompt = 'Waga ' + self.ingredient +' to '+ str(self.weight)+ ' kg'

        self.weightW = tk.Tk()

        self.weightW.geometry("500x500")
        self.weightW.title('Ważenie')

        self.weightLabel = tk.Label(self.weightW, text = self.prompt)
        self.backButton = tk.Button(self.weightW,text="Wroc", command = self.callbackBack)

        self.weightLabel.place(x=50,y=30)
        self.backButton.place(x=100,y=30)
        self.backButton.pack(padx=100,pady=30)
        self.weightW.mainloop()

    def updateWeight(self,w):
        self.weight = w

    def do_cooking(self):
        if(self.weight != 0):
            print('weight of ', self.ingredient ,' is ', self.weight, ' kg')
            print("Done!")
        else:
            print("nie położono produktu")
    
    def callbackBack(self):
        self.weight = 0
        self.weightW.destroy()