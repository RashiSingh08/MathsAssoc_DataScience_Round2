import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Was it really necessary to give us such a large dataset??
# Like, the Task_train.csv was 950mb and it took 10-15 minutes just to extract and open
# The code too takes atleast 5 minutes to run on laptop. 
# AND, I will say, The damn clean normalised dataset refuses to open. 
# Like, I understand that data is usually large, but this was really hard to work on a laptop.

df = pd.read_csv('DataProcessingTask/Final_Task/Task_train.csv', header=None)

print("---- Initial Data Preview ----")
print(df.head(15))

df = df.replace(0.0, np.nan)

df = df.fillna(df.mean())

print(df.head(15)) 

# This is the meat of this particular task.

scaler = MinMaxScaler()
df_normalised = pd.DataFrame(scaler.fit_transform(df), columns = df.columns)

df_normalized.to_csv("cleaned_normalized_dataset.csv", index=False, compression="gzip")
print("\nDataset successfully cleaned, normalized, and saved.")