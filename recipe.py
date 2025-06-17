from time import sleep
import pandas as pd
import mix
import heat
import add
class recipe:
    def __init__(self, name):
        self.name = name + '.csv'
        self.iter = 0
        print(self.name)
        self.actions = pd.read_csv(self.name, header = None)

    def realize_recipe(self):
        
        if self.actions.iloc[self.iter,0] == "mix":
            cook = mix.mix(self.actions.iloc[self.iter,1],self.actions.iloc[self.iter,2],self.actions,self.iter+1)
        if self.actions.iloc[self.iter,0] == "heat":
            cook = heat.heat(self.actions.iloc[self.iter,1],self.actions.iloc[self.iter,3],self.actions,self.iter+1)
        if self.actions.iloc[self.iter,0] == "add":
            cook = add.add(self.actions.iloc[self.iter,4],self.actions.iloc[self.iter,5],self.actions,self.iter+1)
  