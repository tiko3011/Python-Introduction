import time

myTimeMin = int(input("Enter time in minutes: "))
myTimeSec = int(input("Enter time in seconds: "))
myTime = myTimeMin * 60 + myTimeSec

for i in range(myTime, 0, -1):
    minutes = i // 60
    seconds = i % 60
    print(f"00:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Times Up!")
