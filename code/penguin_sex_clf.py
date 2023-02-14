# "code/penguin_sex_clf.py"

import pandas as pd
penguins = pd.read_csv('data/penguins_cleaned.csv')

penguins_df = penguins[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'sex']]

# Ordinal feature encoding
# https://www.kaggle.com/pratik1120/penguin-dataset-eda-classification-and-clustering
df = penguins_df.copy()

target_mapper = {'male':0, 'female':1}
def target_encode(val):
    return target_mapper[val]

df['sex'] = df['sex'].apply(target_encode)

# Separating X and Y
X = df.drop('sex', axis=1)
Y = df['sex']

# Build random forest model
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X, Y)

