import os
import sys
import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))

df = pd.read_csv("data/l2_conventional_data_202611042047.csv")

print(df.info())