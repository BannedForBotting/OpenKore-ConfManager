#!/usr/bin/env python3

import logging
import sys
import glob
import shutil
# import tkinter


# master = tkinter.Tk()
# e = tkinter.Entry(master)
# e.pack()
# e.focus_set()

CONF_MANAGER_REPO = './confManager\\'
CONF_MANAGER_OLD = './confManager/old.txt'
CONF_MANAGER_FILE_PATTERN = './confManager/*.txt'
OPENKORE_CONF_FILE = './control/config.txt'


def close():
    master.withdraw()
    print("Goodbye")
    sys.exit(1)


def copy_file(chosen_file):
    shutil.copy2(OPENKORE_CONF_FILE, CONF_MANAGER_OLD)
    shutil.copy2(CONF_MANAGER_REPO + chosen_file, OPENKORE_CONF_FILE)


def list_files():
    res_list = []
    files = glob.glob(CONF_MANAGER_FILE_PATTERN)
    print("Saved configuration files:")
    for i in files:
        tmp = i.split(CONF_MANAGER_REPO)
        if len(tmp) <= 0:
            sys.exit("Wrong file repository")
        tmp = tmp[1]
        res_list.append(tmp)
        print(tmp)
    return res_list


def conf_manager():
    try:
        files = list_files()
        if len(files) <= 0:
            sys.exit("No .txt configuration file found in ./confManager/")
        chosen_file = input("Which file do you wish to load? :")
        if chosen_file is None or len(chosen_file) <= 0:
            print("Wrong file name")
            return
        if chosen_file[-4:] != '.txt':
            print("PD")
            chosen_file += ".txt"
        for i in files:
            if chosen_file == i:
                copy_file(chosen_file)
                sys.exit("Configuration file loaded!")
        print("Configuration file not found! Try again...")
    except Exception as e:
        logging.error(e)
        sys.exit(e.__cause__)

if __name__ == '__main__':
    # master.bind('<Escape>', close)
    print("Welcome to OpenKore Conf Manager!")
    while True:
        conf_manager()
