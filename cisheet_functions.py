
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
#Ring Settings
#-- values 1-26, can be duplicate (26x26x26)
#-- 3 columns, 1 value range(26) per column

ring_col = []
for i in range(31):
    ring_row = []    
    for j in range(3):
        ring_row.insert(j, random.choice(range(1, 26)))
    ring_col.insert(i, ring_row)
    
print(ring_col)


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


#%%
#kengruppen -- last columns
#-- can be repeating letters in sequence, for each selection
#-- 4 columns, 3 letters per column 

letter_opts = list(string.ascii_uppercase)

msg_col = []
for i in range(31):
    msg_row = []
    for j in range(4):
        msg_posi = []
        for k in range(3):
            msg_posi.insert(k, random.choice(letter_opts))
        msg_row.insert(j, msg_posi)
    msg_col.insert(i, msg_row)

print(msg_posi)
print(msg_row)
print(msg_col)


#%%
#Next -- to create the dataframe
