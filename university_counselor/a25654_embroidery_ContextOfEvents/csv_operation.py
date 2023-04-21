import os
import pickle
import pprint
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import csv


def csv_reader(filename, directory="./"):
    with open(os.path.join(directory, filename), newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter="\n", quotechar="|")
        mylist = []
        for row in reader:
            if len(row) > 0 and row[0] != '"':
                mylist.append(row[0].split("\t"))
        return mylist


def read_csv_data(filepath):
    data = []
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data