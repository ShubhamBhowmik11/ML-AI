import json
#14 dec 2025
def readJson(filename):
        with open(filename,"r") as r:
         data = json.load(r)
        return data 

def CleaningData(filename):
        with open(filename,"r") as r:
         data = json.load(r)
         print(type(data))
        for ele in data:
        #  dummy_name = ele["name"]
         print(ele["id"])
          
        return 'hey'
print(CleaningData("data.json"))