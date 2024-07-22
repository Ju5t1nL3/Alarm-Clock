"""
The program starts a timer based off of user input then plays a sound when the timer is done
"""
import time
from playsound import playsound

CLEAR = "\033[2J"
RETURN = "\033[H"

def play_alarm(sec):
    """
    Starts the timer countdown until the time is over and plays the alarm sound
    """
    print(CLEAR)
    for i in range(answer_sec):
        new_time = answer_sec - i
        print(f"{RETURN}{(new_time//60):02d}:{(new_time%60):02d}")
        time.sleep(1)

    playsound("Alarm.mp3")
    print(f"{CLEAR}{RETURN}Timer done!")

#starts program
while True:
        try:
            answer = input("How many long would you like the alarm clock to last? (minutes:seconds format): ")
            answer_list = answer.split(":")
            answer_sec = (int(answer_list[0]) * 60) + int(answer_list[1])
            play_alarm(answer_sec)
            break
        except Exception as e:
            print(f"Error: {e}")
