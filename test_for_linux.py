from datetime import datetime
import re
from os import path
import shutil
import subprocess


def get_data():
    with open("datafile", "r") as data_file:
        all_data = data_file.readlines()

    information_dict = {"trigger_date": "", "file_path": "", "actions": "", "bash": ""}

    for i in all_data:
        if "TRIGGER_DATE=" in i:
            information_dict["trigger_date"] = i[13:].strip()
        elif "PATH=" in i:
            information_dict["file_path"] = i[5:].strip()
        elif "BASH_CONDITION=" in i:
            bash_condition = i[15:].strip()
        elif "BASH_COMMANDS" in i and bash_condition == "Y":
            bash_checkpoint = all_data.index(i)
            for j in all_data[bash_checkpoint+1::]:
                if "[ACTIONS]" in j:
                    actions_checkpoint = all_data.index(j)
                    break
            commands = all_data[bash_checkpoint+1:actions_checkpoint]
            for l in commands:
                if re.search(r"^\r\n$", l):
                    continue
                else:
                    information_dict["bash"] += l.replace("\r\n", "; ")
        elif "[ACTIONS]" in i:
            checkpoint = all_data.index(i)
            information_dict["actions"] = all_data[checkpoint+1:]
            break

    if re.search(r"^([0-9]{4})-?(1[0-2]|0[1-9])-?(3[01]|0[1-9]|[12][0-9])?\s?(2[0-3]|[01][0-9]):?([0-5][0-9]):?([0-5][0-9])$", information_dict["trigger_date"]) and len(information_dict["trigger_date"]) == 19:
        format_check = True
    else:
        format_check = False
    if path.isfile(information_dict["file_path"]):
        path_check = True
    else:
        path_check = False

    return information_dict, format_check, path_check


def insert_new_data(information):
    i = True
    while i == True:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if current_time == information["trigger_date"]:
            file_name = path.basename(information["file_path"])
            shutil.copy(information["file_path"], "{file_name}-{current_time}".format(file_name=file_name, current_time=current_time.replace("-","")[2:-9]))
            with open(information["file_path"], "a") as file_for_changes:
                file_for_changes.writelines("\n\n")
                file_for_changes.writelines(information["actions"])
            subprocess.call(information["bash"], shell=True)
            i = False
        else:
            continue
    return


def main_function():
    information_dict, format_check, path_check = get_data()
    current_time_check = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if current_time_check < information_dict["trigger_date"] and format_check is True and path_check is True:
        print("Text will be inserted in {trigger_date}".format(trigger_date=information_dict["trigger_date"]))
        insert_new_data(information=information_dict)
    elif format_check is False:
        return "Invalid date format"
    elif path_check is False:
        return "Invalid file path"
    elif current_time_check > information_dict["trigger_date"]:
        return "Error, current time is greater than trigger time"
    return "The data in file has been inserted"


print(main_function())
