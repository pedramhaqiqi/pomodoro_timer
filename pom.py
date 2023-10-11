import time
import signal

BOLD = "\033[1m"
GREEN = "\033[32m"
RESET = "\033[0m"

def signal_handler(signal, frame):
    print("\n")
    print("Have a good day!")
    exit(0)

def pomodoro_timer(duration):
    print("Pomodoro Timer Started")
    for i in range(duration, 0, -1):
        minutes = i // 60
        seconds = i % 60
        print(f"Time remaining: {BOLD}{GREEN} {minutes:02d}:{seconds:02d} minutes{RESET}", end='\r')
        time.sleep(1)
    print("Pomodoro Timer Completed")

def main():
    print("Welcome to Pomodoro Timer")
    duration = 25  # 25 minutes in seconds

    while True:
        action = input("Enter 's' to start the timer with default, 'd' to set duration (mins) default = 25 mins, or 'q' to quit: ")
        if action == "d":
            duration = input("Enter Duration: ")
            print("Duration set to: " + duration)
        elif action.lower() == 's':
            pomodoro_timer(int(duration) * 60)
        elif action.lower() == 'q':
            print("Thank you for using Pomodoro Timer. Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main()
