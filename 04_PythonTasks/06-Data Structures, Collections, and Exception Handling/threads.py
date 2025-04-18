import threading
from datetime import datetime
import time
import os

def display_time():
  """
  Displays the current time every second in real time.
  This function runs continuously to show the updated time.
  """
  current_date = datetime.now().strftime("%Y-%m-%d")
  current_time = datetime.now().strftime("%H:%M:%S")
  return [current_date,current_time]
print(display_time())

def log_time_to_file():
  """
  Logs the current time to a file every 5 seconds.
  The time is logged in the format: YYYY-MM-DD HH:MM:SS.
  """
  current_date,current_time = display_time()
  with open("time_log.txt","a") as file:
    file.write(f"Date : {current_date}  Time: {current_time}\n")
  print(f"Logged time :{current_date}, {current_time} to file")
  time.sleep(5)

# Function to delete the log file at the start of the program
def delete_log_file():
    """
    Deletes the 'time_log.txt' file if it exists.
    This ensures a fresh start every time the program runs.
    """
    if os.path.exists("time_log.txt"):
        os.remove("time_log.txt")
        print("Previous log file deleted.")

def main():
  delete_log_file()

  start_time = time.time()
  try:
    end_time = int(input("Enter the time you want the program to exit: "))
  except:
     print("You have entered an invalid number! We will exit after 10 seconds")
     end_time = 10
  while(1):
    if(time.time()-start_time<end_time):
        display_thread = threading.Thread(target=display_time)

        log_thread = threading.Thread(target=log_time_to_file)

        display_thread.start()
        log_thread.start()

        display_thread.join()
        log_thread.join()
    else:
      print("End logging  exiting the program")
      character = input("Do you want to delete the file? press y for yes: ")
      if(character=='y' or character =='Y'):
         delete_log_file()
      break

if __name__ =="__main__":
  main()




