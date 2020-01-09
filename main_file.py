#!/usr/bin/env python
import os
import datetime
import shutil
import time
import sys

def create_directory_dict(begin_date, end_date):
    """
    To create the dictionary to hold the dates
    :param: begin date - datetime object for begin date
    :param: end date - datetime object for end date
    :return: directory dictionary
    """
    date_directory = {}
    dates_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
    for d in dates_generated:
        year = str(d.year)
        month = str(d.month)
        day = str(d.day)
        # Check if the year is in there
        if year not in date_directory.keys():
            date_directory[year] = {}
        # Check if the month is in there
        if month not in date_directory[year].keys():
            date_directory[year][month] = []
        # Check if the day is in there
        if day not in date_directory[year][month]:
            # Go ahead and put the day in the list
            date_directory[year][month].append(day)
        else:
            print("This should not have happened, something wrong with the datetime method")
    return date_directory


start = datetime.datetime.strptime(sys.argv[1], "%d-%m-%Y")
end = datetime.datetime.strptime(sys.argv[2], "%d-%m-%Y")
keep_flag = False
if(len(sys.argv) == 4 and sys.argv[3] == "-keep"):
    keep_flag = True

directory_dict = create_directory_dict(start, end)

def build_directories(dict):
    try:
        # Years
        for y in dict:
            year_directory = str(y)
            os.mkdir(year_directory)
            if keep_flag: open(year_directory+"\\.keep", "w")
            # Months
            for m in dict[y]:
                month_directory = year_directory + "\\" + str(m)
                os.mkdir(month_directory)
                if keep_flag: open(month_directory + "\\.keep", "w")
                #Days
                for d in dict[y][m]:
                    day_directory = month_directory + "\\" + str(d)
                    os.mkdir(day_directory)
                    if keep_flag: open(day_directory + "\\.keep", "w")
    except FileExistsError:
        print("The folders already exist")


def delete_directories(dict):
    for y in dict.keys():
        shutil.rmtree(y)


def time_method(method, parameters):
    tic = time.process_time()
    method(parameters)
    toc = time.process_time()
    print(method.__name__, toc - tic)


time_method(build_directories, directory_dict)
#time_method(delete_directories, directory_dict)
