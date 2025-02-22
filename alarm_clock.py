# Import te playsound module. 

from playsound import playsound
import time     # to be used to regulate time to have 1s for each iteration
from datetime import datetime

# get user's preferred format in 12/24 hrs
def get_time_format():
    while True:
        format_choice = input("Choose time format:\n1. 12-hour (AM/PM)\n2. 24-hour\nEnter 1 or 2 (or 'quit' to exit): ")
        if format_choice.lower() in ['quit', 'exit', 'q']:
            return 'quit'
        if format_choice in ['1', '2']:
            return format_choice
        print("Invalid choice. Please enter 1 or 2.")

def set_alarm():
    while True:  # Main loop for the entire alarm setting process
        try:
            # Get user's preferred time format
            format_choice = get_time_format()
            
            if format_choice == 'quit':
                return False
            
            if format_choice == '1':
                alarm_time = input("Enter alarm time in 'HH:MM AM/PM' format (e.g., 07:30 PM) or 'quit' to exit: ")
                if alarm_time.lower() in ['quit', 'exit', 'q']:
                    return False
                # Convert am/pm to uppercase and remove extra spaces
                alarm_time = alarm_time.strip().upper()
                # Convert 12-hour format to 24-hour format
                alarm_datetime = datetime.strptime(alarm_time, '%I:%M %p')
                alarm_time = alarm_datetime.strftime('%H:%M')
            else:
                alarm_time = input("Enter alarm time in 'HH:MM' format (24-hour) or 'quit' to exit: ")
                if alarm_time.lower() in ['quit', 'exit', 'q']:
                    return False
                datetime.strptime(alarm_time, '%H:%M')
            
            print(f"Alarm set for {alarm_time}")
            
            while True:
                current_time = datetime.now().strftime('%H:%M')
                print(f"Current time: {current_time} (Press Ctrl+C to exit)", end='\r')
                
                if current_time == alarm_time:
                    print("\nTime to wake up!")
                    playsound("alarm.mp3")
                    break
                
                time.sleep(1)
            break  # Exit the main loop after alarm goes off
            
        except ValueError:
            while True:
                choice = input("Invalid time format! Would you like to try again? (yes/no/quit): ").lower()
                if choice in ['quit', 'exit', 'q']:
                    return False
                if choice in ['yes', 'no']:
                    if choice == 'no':
                        return False
                    break  # Break the inner loop to try again
                print("Please enter 'yes' or 'no' or 'quit'")
    return True

if __name__ == "__main__":
    print("Welcome to Simple Alarm Clock!")
    if set_alarm():
        print("Alarm completed successfully!")
    print("Thank you for using our alarm clock! Have a great day!")



