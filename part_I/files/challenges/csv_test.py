'''
@Project ：tstp-master 
@File    ：csv_test.py
@IDE     ：PyCharm 
@Date    ：2023/3/20 12:21 
'''

import csv

with open("/Users/aoyufei/Desktop/929.xlsx", 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=",")
    for row in spamreader:
        print(",".join(row))