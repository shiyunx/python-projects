# Import time module
import time

# Create function with second
def countdown_timer(second):
    # Create a while loop to count down
    while second:
        minutes, seconds = divmod(second, 60)
        timeformat = "{:02}:{:02}".format(minutes, seconds)
        print(timeformat)

        # 1min = 60sec, delay time
        time.sleep(1)
        second = second - 1
    print("Stop")

# Call function
countdown_timer(10)