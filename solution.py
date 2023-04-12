import pandas as pd
import numpy as np
import statsmodels.stats.weightstats as w


chat_id = 1152225195 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    _, pvalue = w.ztest(x, value=500, alternative='larger')
    return pvalue <= 0.06
