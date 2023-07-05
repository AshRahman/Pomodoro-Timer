import time


def single_pomodoro(t):
    while t:
        mins, secs = divmod(
            t,
        )
        timer = f"{mins:02}:{secs:02}"
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("take a break")


def second_converter(mins):
    seconds = mins * 60


t = input("Choose the practice time: \n 1. Hour \n 2. Mins")

single_pomodoro(int(t))
