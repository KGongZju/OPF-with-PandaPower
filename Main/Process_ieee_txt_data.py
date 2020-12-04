import pandas as pd
import numpy as np
import os

def ieee_get_data():
    #column_name = ['from', 'to', 'P', 'Q', 'rohm', 'xohm', 'maxi']
    column_name1 = ['from', 'to', 'rohm', 'xohm', 'maxi']
    column_name2 = ['BusNo', 'P', 'Q']
    column_name3 = ['No', 'BusNo', 'Pg', 'Pmax', 'Pmin', 'Qmax', 'Qmin', 'vm', 'gencost']
    #path = r'C:\Users\wkb16122\Dropbox\python\padapower'
    #data_33 = 'ieee33bus.txt'
    #data_69 = 'ieee69bus.txt'
    data_118_bus = 'ieee118bus.txt'
    data_118_line= 'ieee118line.txt'
    data_118_gen = 'ieee118gen.txt'
    #file33 = os.path.join(path, data_33)
    #file69 = os.path.join(path, data_69)

    #fo = open(file33, 'r')
    fo = open(data_118_bus, 'r')
    #data33 = []
    databus = []
    for line in fo:
        #data33.append(line.rstrip().split(' '))
        databus.append(line.rstrip().split('\t'))
        # print line.split(' ')
        #df_33 = pd.DataFrame(data33, columns=column_name)
    Bus_118 = pd.DataFrame(databus, columns=column_name2)

    #data69 = []
    #fo = open(file69, 'r')
    fo = open(data_118_line, 'r')
    dataline = []
    for line in fo:
        #data69.append(line.rstrip().split(' '))
        dataline.append(line.rstrip().split('\t'))
        #df_69 = pd.DataFrame(data69, columns=column_name)
    Line_118 = pd.DataFrame(dataline, columns=column_name1)

    #fo = open(file33, 'r')
    fo = open(data_118_gen, 'r')
    #data33 = []
    datagen = []
    for line in fo:
        #data33.append(line.rstrip().split(' '))
        datagen.append(line.rstrip().split('\t'))
        # print line.split(' ')
        #df_33 = pd.DataFrame(data33, columns=column_name)
    Gen_118 = pd.DataFrame(datagen, columns=column_name3)

    return Bus_118, Line_118, Gen_118
