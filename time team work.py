currentTimeStr = input("What is the current time (in hours 0-23)?")
waitTimeStr = input("How many hours do you want to wait") #a closing parenthesis was missing

'''
Name errors found
currenTimeInt = int(currentTimeStr)
waitTimeInt = int(waitTimeStr)
'''

currentTimeInt = int(current_time_str)
waitTimeInt = int(wait_time_str)

'''
Logic error: The final time is represented in hours(0-23). 
finalTimeInt = (currentTimeInt + waitTimeInt) % 24
'''
finalTimeInt = currentTimeInt + waitTimeInt

'''
Name error found
print(finalTimeInt)
'''
print(finalTime_Int)
