str_time = input("What time is it now?")
str_wait_time = input("What is the number of nours to wait?")
time = int(str_time)
'''
Name error
wait_time = int(str_wait_time)
'''
wai_time = int(str_wait_time)

'''
Logic error :time_when_alarm_go_off is expressed as hours in (0-23)
time_when_alarm_go_off = (time+ wait_time) % 24

'''
time_when_alarm_go_off = time + wait_time
print(time_when_alarm_go_off)

#there is nothing wrong with this program
