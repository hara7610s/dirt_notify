from email import message
import time
import line

def notify_entry(date, entry_dict, my_dict):
    message = str(date)
    for my_horse in my_dict:
        if my_horse in list(entry_dict.keys()):
            RaceCourse = entry_dict[my_horse][0].decode('utf-8')
            RaceNum = entry_dict[my_horse][1].decode('utf-8')
            RaceName = entry_dict[my_horse][2].decode('utf-8')
            HorseName = my_horse.decode('utf-8')
            
            message += f'\n{RaceCourse}{RaceNum} {RaceName} {HorseName}'
            time.sleep(1)
    
    line.notify_message(message)