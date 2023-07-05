import time


def single_pomodoro(t):
    t = t * 3600  # makes the hour into seconds
    while t:
        secs = t % 60  # makes the second not exceed 60 mark
        mins = int(t / 60) % 60  # makes the minute not exceed 60 mark
        hours = int(t / 3600)
        timer = f"{hours:02}:{mins:02}:{secs:02}"
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
        #####if (mins=)
    print("Times Up")


t = input("Choose the practice time Duration in hour:")

single_pomodoro(int(t))
