#! /usr/bin/env python
# -*- coding:utf-8 -*-

import os
import datetime
import operations


def date_to_string(date):
    """ Convert date to string 'Month-Year'. """
    date = datetime.datetime(date.year, date.month, date.day)
    date = date.strftime("%B-%Y")
    return date


def get_dates_of_item(item, path):
    """ Return created and modified date of folder or file. """
    cdate = datetime.datetime.fromtimestamp(
        os.path.getctime(
            os.path.join(path, item)
        )
    )
    mdate = datetime.datetime.fromtimestamp(
        os.path.getmtime(
            os.path.join(path, item)
        )
    )
    cdate = date_to_string(cdate)
    mdate = date_to_string(mdate)
    return cdate, mdate


def get_sets_of_dates(path):
    """ Return set of created dates and set of modified dates. """
    list_of_files_and_folders = operations.get_list_of_files_and_folders(path)

    list_of_cdates, list_of_mdates = [], []
    for item in list_of_files_and_folders:
        cdate, mdate = get_dates_of_item(item, path)

        list_of_cdates.append(cdate)
        list_of_mdates.append(mdate)

    return set(list_of_cdates), set(list_of_mdates)


def get_names_of_new_folders(mdate, path):
    """ Return list of names of folders to create. """
    list_of_cdates, list_of_mdates = get_sets_of_dates(path)
    return list_of_mdates if mdate else list_of_cdates


def move_files_and_folders(mdate, source, target):
    """ Move all files and folders to given target. """
    files_and_folders = operations.get_list_of_files_and_folders(source)

    list_of_tuples = []
    if mdate:
        for obj in files_and_folders:
            _, obj_mdate = get_dates_of_item(obj, source)
            list_of_tuples.append((obj, obj_mdate))
    else:
        for obj in files_and_folders:
            obj_cdate, _ = get_dates_of_item(obj, source)
            list_of_tuples.append((obj, obj_cdate))

    operations.move_all(list_of_tuples, source, target)


def by_cdate(source, target):
    """ Group files and folders by created date. """
    folders_name = get_names_of_new_folders(False, source)
    operations.create_new_folders(folders_name, target)
    move_files_and_folders(False, source, target)


def by_mdate(source, target):
    """ Group files and folders by modified date. """
    folders_name = get_names_of_new_folders(True, source)
    operations.create_new_folders(folders_name, target)
    move_files_and_folders(True, source, target)
