greeting = input("Hello, possible pirate! What's the password?")  # a quotation mark was missing at the end
if greeting in ["Arrr!"]:  #used the same parenthesis intead of different ones
	print("Go away, pirate.")
   

'''
for not matching case, the following message is printed.

else:
     print("Greetings, hater of pirates!")
''''

elif greeting in ["Not pirate"]:  #Added a new phrase in fornt of th elif with the right quotes and parenthesis
    print("Greetings, hater of pirates!") #all we added was just make the right indentation
