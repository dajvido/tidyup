#! /usr/bin/env python
# -*- coding:utf-8 -*-

import os
import shutil


def get_list_of_files(path):
    """ Return list of files. """
    return [elem for elem in os.listdir(path) if os.path.isfile(
        os.path.join(path, elem))
    ]


def get_list_of_folders(path):
    """ Return list of folders. """
    return [folder for folder in os.listdir(path) if os.path.isdir(
        os.path.join(path, folder))
    ]


def get_list_of_files_and_folders(path):
    """ Return list of folders. """
    return [folder for folder in os.listdir(path)]


def create_new_folders(folders_name, target):
    """ Create folders by given list of names. """
    for name in folders_name:
        path = os.path.join(target, name)
        if not os.path.isdir(path):
            os.mkdir(path)


def move_all(list_of_tuples, source, target):
    """
        Move all files and folders by given list of tuples (object, catalog).
    """
    for obj_tuple in list_of_tuples:
        obj, catalog = obj_tuple
        try:
            shutil.move(
                os.path.join(source, obj),
                os.path.join(target, catalog, obj)
            )
        except shutil.Error:
            print "Catalog", catalog + "/" + obj, "already exist."
