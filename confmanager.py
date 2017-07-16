#!/usr/bin/env python3

import logging
import sys
import glob
import shutil
import tkinter


master = tkinter.Tk()
master.title("OpenKore Configuration Manager")
master.geometry('500x500')

listbox = tkinter.Listbox(master)
listbox.config(width=50, height=29)
listbox.pack()

CONF_MANAGER_REPO = './confManager\\'
CONF_MANAGER_OLD = './confManager/old.txt'
CONF_MANAGER_FILE_PATTERN = './confManager/*.txt'
OPENKORE_CONF_FILE = './control/config.txt'

files = []


def close(event):
    master.withdraw()
    print("Goodbye")
    sys.exit(1)


def copy_file():
    chosen_index = listbox.curselection()
    print(chosen_index)
    chosen_file = files[chosen_index[0]]
    print(chosen_file)
    if chosen_file is None or len(chosen_file) <= 0:
        print("Wrong file name")
        return
    shutil.copy2(OPENKORE_CONF_FILE, CONF_MANAGER_OLD)
    shutil.copy2(CONF_MANAGER_REPO + chosen_file, OPENKORE_CONF_FILE)
    print("Configuration loaded!")


def list_files():
    res_list = []
    files_list = glob.glob(CONF_MANAGER_FILE_PATTERN)
    print("Saved configuration files:")
    for i in files_list:
        tmp = i.split(CONF_MANAGER_REPO)
        if len(tmp) <= 0:
            sys.exit("Wrong file repository")
        tmp = tmp[1]
        res_list.append(tmp)
        print(tmp)
    return res_list


def conf_manager():
    global listbox
    global files
    files = list_files()
    if len(files) <= 0:
        sys.exit("No .txt configuration file found in ./confManager/")
    for j in files:
        listbox.insert(tkinter.END, j)
        # chosen_file = input("Which file do you wish to load? :")
        # if chosen_file is None or len(chosen_file) <= 0:
        #     print("Wrong file name")
        #     return
        # if chosen_file[-4:] != '.txt':
        #     print("PD")
        #     chosen_file += ".txt"
        # for i in files:
        #     if chosen_file == i:
        #         copy_file(chosen_file)
        #         sys.exit("Configuration file loaded!")
        # print("Configuration file not found! Try again...")


if __name__ == '__main__':
    try:
        master.bind('<Escape>', close)
        btn = tkinter.Button(master, text='Load!', command=copy_file)
        btn.pack()
        print("Welcome to OpenKore Conf Manager!")
        conf_manager()
        master.mainloop()
    except Exception as e:
        logging.error(e)
        master.destroy()
        sys.exit(e.__cause__)
