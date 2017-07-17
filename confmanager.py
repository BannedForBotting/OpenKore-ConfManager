#!/usr/bin/env python3
"""A simple GUI that allows OpenKore users to easily switch between configuration.

confManager allow any Ragnarok Online OpenKore user to quickly load a 'config.txt' in order to switch OpenKore's
configuration and automation pattern.
"""

import logging
import sys
import glob
import shutil
import tkinter
import time

__author__ = "Anis BENNABI"
__copyright__ = "Copyright 2017, Pikipoo"
__credits__ = ["Anis BENNABI", "Benjamin FOURCAULT"]

__license__ = "MIT"
__version__ = "1.0.2"
__maintainer__ = "Anis BENNABI"
__email__ = "anis.bennabi@epitech.eu"
__status__ = "Production"


CONF_MANAGER_REPO = '.\\confManager\\'
CONF_MANAGER_OLD = '.\\confManager\\old.txt'
CONF_MANAGER_FILE_PATTERN = '.\\confManager\\*.txt'
OPENKORE_CONF_FILE = '.\\control\\config.txt'

files = []

master = tkinter.Tk()
master.title("OpenKore Configuration Manager")
master.geometry('500x530')
master.resizable(width=False, height=False)

text_frame = tkinter.Frame(master, bd=1, height=20)
text_frame.pack(side=tkinter.BOTTOM, fill=tkinter.X)
text_info = tkinter.StringVar()
text_label = tkinter.Label(text_frame, textvariable=text_info)
text_label.pack()

list_frame = tkinter.Frame(master, bd=1)
list_frame.pack(side=tkinter.TOP, fill=tkinter.BOTH)
scrollbar = tkinter.Scrollbar(list_frame, orient=tkinter.VERTICAL)
listbox = tkinter.Listbox(list_frame, yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
listbox.config(width=50, height=29)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
listbox.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)


def close(event):
    """Handles the closing event when <Escape> button is pressed.

    :param event: Tkinter event.
    :return:
    """
    master.withdraw()
    print("Goodbye")
    sys.exit(1)


def copy_file(event=None):
    """Copies the selected file from '.\confManager\' to '.\control\config.txt'. Also performs a smart backup in
    '.\confManager\old.txt.

    :param event: Tkinter event.
    :return:
    """
    if listbox.size() <= 0:
        text_info.set("No file selected")
        logging.error("No file selected")
        return
    chosen_file = listbox.get(tkinter.ACTIVE)
    if chosen_file is None or len(chosen_file) <= 0:
        text_info.set("Wrong file name")
        logging.error("Wrong file name")
        return
    shutil.copy2(OPENKORE_CONF_FILE, CONF_MANAGER_OLD)
    shutil.copy2(CONF_MANAGER_REPO + chosen_file, OPENKORE_CONF_FILE)
    text_info.set("Configuration \"" + chosen_file + "\" loaded!")
    print("Configuration \"" + chosen_file + "\" loaded!")


def list_files():
    """Lists all '.txt' files found in '.\confManager' and returns it.

    :return: res_list: List of all configuration files found.
    """
    res_list = []
    files_list = glob.glob(CONF_MANAGER_FILE_PATTERN)
    print("Saved configuration files:")
    for i in files_list:
        tmp = i.split(CONF_MANAGER_REPO)
        if len(tmp) <= 0:
            text_info.set("Wrong file repository")
            time.sleep(5)
            sys.exit("Wrong file repository")
        tmp = tmp[1]
        res_list.append(tmp)
        print(tmp)
    return res_list


def conf_manager():
    """Inserts all configuration files found in '.\confManager' into a graphical Tkinter.Listbox.

    :return:
    """
    global files
    files = list_files()
    if len(files) <= 0:
        text_info.set("No .txt configuration file found in ./confManager/")
        time.sleep(5)
        sys.exit("No .txt configuration file found in ./confManager/")
    for j in files:
        listbox.insert(tkinter.END, j)
    listbox.select_set(0)
    listbox.activate(0)


if __name__ == '__main__':
    try:
        master.bind('<Escape>', close)
        button_frame = tkinter.Frame(master, bd=1)
        button_frame.pack(side=tkinter.BOTTOM, fill=tkinter.BOTH)
        btn = tkinter.Button(button_frame, text='Load!', command=copy_file, height=60, width=60)
        btn.pack()
        text_info.set("Welcome to OpenKore Conf Manager! Please select a file...")
        print("Welcome to OpenKore Conf Manager!")
        conf_manager()
        master.bind('<Return>', copy_file)
        master.mainloop()
    except Exception as e:
        logging.error(e)
        master.destroy()
        sys.exit(e.__cause__)
