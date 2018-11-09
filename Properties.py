
# coding: utf-8

# In[4]:


import json

with open('monopoly.json') as json_data:
    d = json.load(json_data)
    print(d)


# In[3]:


print(d['properties'])


# In[12]:


for element in d:
    print(element)


# In[6]:


properties = d['properties']
print(properties[0])


# In[7]:


type(properties)


# In[9]:


attributes = list(properties[0])


# In[16]:


print(list(properties[0][attributes[12]]))


# In[27]:


class Property:
    def __init__(self, name, id, posistion, price, rent, multpliedrent, housecost, group, ownedby, 
                 buildings, mortgaged, probability, rel, ohousecost, oprice, averageProbability):
        self.name = name
        self.id = id
        self.posistion = posistion
        self.price = price
        self.rent = rent
        self.multpliedrent = multpliedrent
        self.housecost = housecost
        self.group = group
        self.ownedby = ownedby
        self.buildings = buildings
        self.mortgaged = mortgaged
        self.probability = probability
        self.rel = rel
        self.ohousecost = ohousecost
        self.oprice = oprice
        self.averageProbability = averageProbability

MedAve = Property(**properties[0])
print(MedAve.rel)

#class propertyList:
    
        

