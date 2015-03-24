#! /usr/bin/env python
# -*- coding:utf-8 -*-

import os
import operations


EXTENSIONS = {
    ('',): "others",
    ('pdf',): "pdfs",
    ('jpg', 'jfif', 'jpe', 'gif', 'png', 'bmp', 'tiff', 'tif', 'pcx', 'emf',
        'rle', 'dib', 'wbm'): "images",
    ('py', 'rb', 'cpp', 'c', 'erl', 'cs', 'java', 'perl', 'groovy',
        'clojure'): "programs",
    ('html', 'css', 'js', 'php'): "web",
    ('odt', 'doc', 'docx', 'docm', 'dot', 'dotx', 'docb'): "words",
    ('ods', 'xlsx', 'xlsm', 'xlsb', 'xltx', 'xls', 'xlt', 'xls', 'xlam', 'xla',
        'xlw'): "excels",
    ('odp', 'ppt', 'pptx', 'pot', 'pps'): "presentations",
    ('xml', 'xsd', 'xps'): "xml",
    ('txt', 'rtf'): "texts",
    ('psd', 'ai', 'eps', 'ptl', 'prtl', ''): "adobe",
    ('mov', 'mp4', 'avi', 'rvm', 'flv', 'f4v'): "videos",
    ('aac', 'aif', 'aiff', 'ac3', 'm4a', 'mp3', 'mpeg', 'mpg', 'wma',
        'wmp'): "audios",
    ('xcf',): "gimp"
}


def get_extensions(files):
    """ Return list of occurring extensions. """
    extensions = [os.path.splitext(f)[1] for f in files]
    extensions = set(extensions)
    return [ext[1:].lower() for ext in extensions]


def move_folders(source, target):
    """ Move all folders to "foldery" folder in new path. """
    folders = operations.get_list_of_folders(source)
    if folders:
        if not os.path.isdir(os.path.join(target, "folders")):
            os.mkdir(os.path.join(target, "folders"))

        list_of_tuples = [(folder, "folders") for folder in folders]
        operations.move_all(list_of_tuples, source, target)


def get_names_of_new_folders(extensions):
    """ Create new folders by extensions. """
    folders_name = []
    for extension in extensions:
        if extension == "":
            folders_name.append("others")
        else:
            for ext_key in EXTENSIONS:
                if extension in ext_key:
                    folders_name.append(EXTENSIONS[ext_key])
                    break
    return folders_name


def move_files(source, target, list_of_files):
    """ Move all files to specific folders in new path. """
    list_of_tuples = []
    for f in list_of_files:
        extension = os.path.splitext(f)[1][1:]
        for ext_key in EXTENSIONS:
            if extension in ext_key:
                list_of_tuples.append((f, EXTENSIONS[ext_key]))
                break
    operations.move_all(list_of_tuples, source, target)


def by_extension(source, target):
    """ Group files and folders by extension. """
    list_of_files = operations.get_list_of_files(source)
    extensions = get_extensions(list_of_files)
    folders_name = get_names_of_new_folders(extensions)
    move_folders(source, target)
    operations.create_new_folders(folders_name, target)
    move_files(source, target, list_of_files)
