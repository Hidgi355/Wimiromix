import mix
import heat
import create_recipe
import open_recipe
import recipe_list
import tkinter as tk
class interface():
    

    def __init__(self, list):
        self.conf = False
        self.mass = 0
        self.list = list
        self.a = False
        self.weightPrompt = ''
        self.root = tk.Tk()

        self.root.geometry("500x500")
        self.root.title('Wimiromix')

        self.timeField = tk.Text(self.root, height = 1, width = 10)
        self.speedField = tk.Text(self.root, height = 1, width = 10)
        self.tempField = tk.Text(self.root, height = 1, width = 10)
        self.ingField = tk.Text(self.root, height = 1, width = 10)

        self.timeField.place(x=100,y=30)
        self.speedField.place(x=100,y=70)
        self.tempField.place(x=100,y=110)
        self.ingField.place(x=100,y=150)

        self.timeLabel = tk.Label(self.root, text = "czas")
        self.speedLabel = tk.Label(self.root, text = "predkosc")
        self.tempLabel = tk.Label(self.root, text = "temperatura")
        self.ingLabel = tk.Label(self.root, text = "skladnik")
        
        self.timeLabel.place(x=10,y=30)
        self.speedLabel.place(x=10,y=70)
        self.tempLabel.place(x=10,y=110)
        self.ingLabel.place(x=10,y=150)

        self.mixing = tk.Button(self.root,text='Miksuj', command = self.callbackMix)
        self.heating = tk.Button(self.root,text='Grzej', command = self.callbackHeat)
        self.weighting = tk.Button(self.root,text='Waż', command = self.callbackWeight)
        self.put = tk.Button(self.root,text='Połóż produkt',command = self.callbackPut)
        self.doRecipe = tk.Button(self.root,text='Wybierz przepis',command = self.callbackDoRecipe)
        self.createRecipe = tk.Button(self.root,text='Stwórz przepis',command = self.callbackCreateRecipe)

        self.mixing.pack(padx=100,pady=30)
        self.heating.pack(padx=100,pady=30)
        self.weighting.pack(padx=100,pady=30)
        self.doRecipe.pack(padx=100,pady=30)
        self.createRecipe.pack(padx=100,pady=30)
        self.put.pack(padx=100,pady=30)

        self.put.place(x=300,y=30)
        self.mixing.place(x=300,y=70)
        self.heating.place(x=300,y=110)
        self.weighting.place(x=300,y=150)
        self.doRecipe.place(x=300,y=190)
        self.createRecipe.place(x=300,y=230)
        

        self.root.mainloop()
    
    def callbackConf(self):
        global conf
        conf = not conf
    def callbackPut(self):
        self.mass = self.mass + 0.25
    def callbackMix(self):
        self.time = self.timeField.get("1.0", "1.15")
        self.speed = self.speedField.get("1.0", "1.15")
        self.action = mix.mix(int(self.time), int(self.speed),'',1)
        self.next = self.action.isDone
        del self.action
    
    def callbackHeat(self):
        self.time = self.timeField.get("1.0", "1.15")
        self.temp = self.tempField.get("1.0", "1.15")
        self.action = heat.heat(int(self.time), int(self.temp),'',1)
    
    def callbackWeight(self):
        self.ingredient = self.ingField.get("1.0", "1.15")
        self.weightPrompt = 'Waga ' + self.ingredient +' to '+ str(self.mass)+ ' kg'
        self.weightLabel2 = tk.Label(self.root, text = "                                                                         ")
        self.weightLabel2.place(x=10,y=190)
        if self.mass != 0 and self.ingredient != '':
            self.weightLabel = tk.Label(self.root, text = self.weightPrompt)
            self.weightLabel.place(x=10,y=190)
        self.mass = 0

    def callbackDoRecipe(self): 
        self.openRecipe = open_recipe.open_recipe(self.list)
    def callbackCreateRecipe(self):
        self.create = create_recipe.create_recipe(self.list)
        self.list = self.create.list