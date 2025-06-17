import pandas as pd
class recipe_list:
    def __init__(self, listName):
       self.list = pd.read_csv(listName,header=None)
    
    def getList(self):
        return self.list
    
    def popFromList(self, recipeName):
        self.list.drop(recipeName)

    def addToList(self,recipeName):
        newRecipe = pd.DataFrame([recipeName])
        self.list = pd.concat([self.list,newRecipe])
    
    def saveList(self):
        self.list.to_csv("lista.csv",index=False,header=None)

    def __del__(self):
        self.list.to_csv("lista.csv",index=False,header=None)