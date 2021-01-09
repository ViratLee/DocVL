import time
count = 0
while True:
    time.sleep(5) # Delay for 5 seconds.
    print("This prints every 5 seconds. 5 times")
    count += 1
    print('count:{}'.format(count))
    if count >= 5:
    	break    