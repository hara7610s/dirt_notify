import time
import line
import find_race
import find_horse
import datetime
import spreadsheet
import checking_entry

def main():
    # find race pages tomorrow
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    race_id_list = find_race.get_race_list(tomorrow)
    
    # make a list of horses entered tomorrow
    if len(race_id_list) == 0:
        pass
    else:
        entry_dict = {}
        for race_id in race_id_list:
            each_race = find_horse.make_entry_dict(race_id)

            entry_dict.update(each_race)

        # call my horse list
        my_dict = spreadsheet.read_spreadsheet()
        
        # match entry list and my horse list
        checking_entry.notify_entry(tomorrow, entry_dict, my_dict)

if __name__ == "__main__":
    main()
