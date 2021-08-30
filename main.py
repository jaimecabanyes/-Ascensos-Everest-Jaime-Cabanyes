import collections
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import src.funciones_limpieza as fn

ascensos_everest = pd.read_csv("Mt_Everest_Ascent_Data.csv")

final = fn.cleaning_dataframe(ascensos_everest)
print(final)