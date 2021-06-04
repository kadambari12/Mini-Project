#Make a list to hold onto items
shopping_list1 = []

# Print out instruction on how to use
print("Instruction 1: What items you would like to buy from store")
print("Instruction 2: Enter 'DONE' to stop adding items")

while True:
    new_item =  input("ENTER ITEM NAMES : ") #asks for new items
    
    if new_item == 'DONE': #be able to quit the app
        break
    
    shopping_list1.append(new_item) #add items to shopping list
    
# To print out the whole slected list
print("Here is your selected list :")
for item in shopping_list1:
    print(shopping_list1.index(item) + 1, end = ' ') # To print all the items in shopping list
    print(item)
    
 ########## OR WE CAN USE ENUMERATE FUNCTION TO GIVE NUMBER TO THE ITEMS ###  
# To print out the whole slected list
#print("Here is your selected list :")
#for number,item in enumerate(shopping_list1, 1):
#        print(number,item)    
   
    
   
    ######################### 2ND WAY ###################################

import pandas as pd
#Make a list to hold onto items
shopping_list = []


# Print out instruction on how to use
print("Instruction 1: What items you would like to buy from store")
print("Instruction 2: Enter 'DONE' to stop adding items")

while True:
    new_item =  input("ENTER ITEM NAMES : ") #asks for new items
    
    if new_item == 'DONE': #be able to quit the app
        break
    
    shopping_list.append(new_item) #add items to shopping list
    
# To print out the whole slected list
print("Here is your selected list :")
for item in shopping_list:
    print(item) # To print all the items in shopping list

#Create another list using range function for displaying length of first list(shopping list)
b = [x for x in range(len(shopping_list)+1)]
combine = pd.DataFrame(zip(b,shopping_list),columns=["Index","Fruits"], index=None)
print(combine)