# coding=utf-8
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import sys
reload(sys)

#中文和负号的正常显示
# plt.rcParams['font.sans-serif’]=['MicrosoftYaHei']
plt.rcParams['axes.unicode_minus']=False

