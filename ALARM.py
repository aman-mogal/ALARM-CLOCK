import datetime
import time
import pygame
import msvcrt  

def set_alarm():
    
    hours = int(input("Enter the number of hours: "))
    minutes = int(input("Enter the number of minutes: "))
    seconds = int(input("Enter the number of seconds: "))

    alarm_time = datetime.datetime.now() + datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)
    alarm_time = alarm_time.strftime("%H:%M:%S")

    pygame.mixer.init()

    pygame.mixer.music.load("C:/Users/AMAN/Documents/STUDY/song.mp3")  

    alarm_triggered = False

    while True:
        now = datetime.datetime.now().strftime("%H:%M:%S")

        if now >= alarm_time and not alarm_triggered:
            print("Wake up!")
            play_song()
            alarm_triggered = True

        if alarm_triggered and msvcrt.kbhit():  
            key = msvcrt.getch()
            if key == b'q' or key == b'Q':  
                stop_song()
                break

        time.sleep(1)

def play_song():
    pygame.mixer.music.play()

def stop_song():
    pygame.mixer.music.stop()

    pygame.mixer.quit()

set_alarm()
