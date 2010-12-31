import os, time

def within(mins):
    if mins > 19 and mins < 25:
	return True
    return False

while not within(time.localtime().tm_min):
    time.sleep(2)
os.system("cvlc -Lf ~/Music/Symphony_of_Science-The_Poetry_of_Reality.mp3 ~/Videos/strobe.dvd")
