import time


class Timer:
    def __init__(self, t) -> None:
        self.t = t

    def single_pomodoro(self, t):
        t = t * 3600  # makes the hour into seconds
        while t:
            """an if else statement needs to be written for 25 and 5 min
            mark where it will then go to the break_start function to star the
            break procedure
            25 min = 1500 sec
            55 min = 3300 sec + 1800
            1 hour 25 min = 5100 sec + 1800
            1 hour 55 min =  6900 sec
            
            """
            if()
            secs = t % 60  # makes the second not exceed 60 mark
            mins = int(t / 60) % 60  # makes the minute not exceed 60 mark
            hours = int(t / 3600)
            timer = f"{hours:02}:{mins:02}:{secs:02}"
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
            #####if (mins=)
        print("Times Up")

    def break_start(self, start_time):
        """this function will take input from single pomodoro where one sprint
        is finished and start a timer of its own for 5 minutes then after its
        finished it will add the 5 mins with the recieved start timer of pomodoro
        and return it back to single pomodoro function
        """
        pass


t = int(input("Choose the practice time Duration in hour:"))

timer1 = Timer()
timer1.single_pomodoro(t)
