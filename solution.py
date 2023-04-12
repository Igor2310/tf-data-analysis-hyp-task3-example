import pandas as pd
import numpy as np
from scipy import stats

chat_id = 1152225195 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool: 
    return x.mean() - stats.norm.ppf(0.94)*x.std()/(np.sqrt(x.shape[0])) >= 500
