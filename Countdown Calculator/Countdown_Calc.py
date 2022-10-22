
import time


def countdown(t):
	print ("\nHurry. The clock has started to tick !")
	while t:
		mins, secs = divmod(t, 60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		print(timer, end="\r")
		time.sleep(1)
		t -= 1
	
	print('Time is up :)')


t = input("Enter the time in seconds: ")

countdown(int(t))
# Payel - AIML