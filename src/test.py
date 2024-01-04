import os
import pandas as pd

data_dir = "/media/zetlin/Data2/Argoverse2/train_sample/02ecafff-012c-45f8-bb6e-5ace2c6e3d88/scenario_02ecafff-012c-45f8-bb6e-5ace2c6e3d88.parquet"

data = pd.read_parquet(data_dir)
print(data.head())