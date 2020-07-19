# -*- coding: utf-8 -*-
import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


# 每四個點預測下一個點
train_size, predict_size = 4, 1

# 要用來訓練的資料欄位，只取特定欄位，總共10個
data_column = ['lat', 'lon', 'x_gyro', 'y_gyro', 'z_gyro', 'x_acc', 'y_acc', 'z_acc', 'wind_speed', 'wind_direction']

path = r'DroneFlightData/WithoutTakeoff'


def window_data(data, window_size):
    X = []
    y = []
    i = 0
    while (i + window_size) <= len( data ) - 1:
        X.append( data[i:i + window_size] )
        y.append( data[i + window_size] )
        i += 1
    assert len( X ) == len( y )
    return X, y


# 讀取資料夾底下所有csv檔，把檔名存在csv_file_list
def get_all_csv_file_list(path):
    csv_file_list = []
    for root, dirs, files in os.walk(path):
        for f in files:
            if os.path.splitext(f)[1] == '.csv':
                csv_file_list.append(os.path.join(root, f))
    return csv_file_list


# 獲得所有train data, label
def get_all_train_data_and_label_data(csv_file_list):
    global count
    all_train_data = []
    all_label = []
    for csv_file in csv_file_list:
        df = pd.read_csv( csv_file )
        dataset = df.loc[:, data_column].values
        sc = MinMaxScaler( feature_range=(0, 1) )
        training_set_scaled = sc.fit_transform( dataset )
        x, y = window_data( training_set_scaled, train_size )

        for a in x:
            all_train_data.append(a)
        for b in y:
            all_label.append(b)

    return np.array(all_train_data), np.array(all_label)








