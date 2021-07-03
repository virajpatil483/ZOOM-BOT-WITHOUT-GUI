import webbrowser as wb
from time import sleep
import schedule 

zoom_meet = "https://www.youtube.com/watch?v=_dZckj8FMx8"

def for_Join() :  
    sleep(5)
    wb.open_new_tab(zoom_meet)
             
schedule.every().day.at('10:45:05').do(for_Join()) 
 
while 1:
    schedule.run_pending()
    time.sleep(1)