import pandas as pd

data_path = r"..\data\Iris_Data.csv"
data_frame = pd.read_csv(data_path)
data_frame['species'] = data_frame.species.apply(lambda input_str: input_str.replace('Iris-', ''))

############################################################################

import numpy as np
grouped_df = data_frame.groupby(['species'])
print(grouped_df.agg([np.mean, np.median]))
