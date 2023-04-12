import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 1152225195 # Ваш chat ID, не меняйте название переменной

def solution(x, y) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    statistic, pvalue = ttest_ind(x, y, equal_var=False, alternative="less")
    alpha = 0.06
    return pvalue < alpha
