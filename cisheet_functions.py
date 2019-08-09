
"""
Created on Fri Aug  9 2019

@author: jossammil
"""


#%%

import random

#create function for creating a rotor list

def make_rotor_list():
    rotors = ['I', 'II', 'III', 'IV', 'V']
    rotorlist = []
    rotorlist.insert(0, random.choice(rotors))
    rotorlist.insert(1, random.choice([i for i in rotors if i not in rotorlist]))
    rotorlist.insert(2, random.choice([i for i in rotors if i not in rotorlist]))
    return rotorlist


#%%
    
#Just for testing the rotor list    
my_rotorlist = make_rotor_list()
print(my_rotorlist)




#%%
#now create a rotor list for 31 days that does not repeat consecutive days 

rotors_month = []
for x in range(30):
    inter_rotor = make_rotor_list()
    if x == 0:
        rotors_month.append(inter_rotor)
    else:
        while inter_rotor == rotors_month[len(rotors_month)-1]:
            inter_rotor = make_rotor_list()
        rotors_month.append(inter_rotor)
        

        
#%%
#Testing the 31 day rotorlist
        
print(rotors_month)      



#%%
#Creating the plugboard setup

import string

pluglist_A = []
pluglist_B = []
letter_opts = list(string.ascii_uppercase)
for i in range(10):
    pluglist_A.insert(i, random.choice([j for j in letter_opts if j not in pluglist_A]))
for i in range(10):
    pluglist_B.insert(i, random.choice([j for j in letter_opts if j not in pluglist_B and j not in pluglist_A]))
    
pluglist_JOIN = []
for i in range(10):
    pluglist_JOIN.insert(i, list((pluglist_A[i], pluglist_B[i])))

    
#%%
#Test the pluglist
    
print(pluglist_JOIN)

    


