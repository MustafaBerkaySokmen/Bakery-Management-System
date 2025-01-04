#This file is for the Bakery Management question.
print("Good morning, welcome to the bakery!")
print("-----------------")
mufst=int(input("How many muffins do we have in stock for today?:"))
mufcost=float(input("How much does each muffin cost?:"))
cupcst=int(input("How many cupcakes do we have in stock for today?:"))
cupccost=float(input("How much does each cupcake cost?:"))
print("Great! Let’s start accepting customers..")
print("-----------------")
j=1
revenue=0
soldmuf=0
soldcupc=0
while j>0:
        print("Welcome customer",j,"!")
        j=j+1
        custmuf=int(input("How many muffins do you want?:"))
        custcupc=int(input("How many cupcakes do you want?:"))
        if custmuf==(-1) or custcupc==(-1):
             print("-----------------")
             break
        else:
            if custmuf>mufst:
                print("Not enough muffins left to serve this customer.")
                print("-----------------")
                continue
            elif custcupc>cupcst:
                print("Not enough cupcakes left to serve this customer.")
                print("-----------------")
                continue
            else:    
                cost=mufcost*custmuf+cupccost*custcupc
                revenue+= cost
                soldmuf+=custmuf
                soldcupc+=custcupc
                print("Cost for customer is:",cost)
                print("Thanks for coming to our bakery, please visit again.")
                mufst -= custmuf
                cupcst -= custcupc
                print("-----------------")
                
print("End of the day waas reached. Summary:") 
print("Our total revenue today :",revenue)
totalmuf=soldmuf+mufst
totalcupc=soldcupc+cupcst
print("Initially, we had",totalmuf,"muffins.We were not able to sell",mufst,"of them.")               
print("Initially, we had",totalcupc,"cupcakes.We were not able to sell",cupcst,"of them.")           
                
    

    








