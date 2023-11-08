import pickle
import pandas as pd
from functions import feature_encoder, target_encoder
from xgboost import XGBClassifier

df = pd.read_csv("static/data/users_data_cleaned_project2.csv")
#print(df.head())


encoding_cols = df.select_dtypes('object').columns.drop('TARGET')
df = feature_encoder(df, encoding_cols)
df = target_encoder(df, 'TARGET')

X, y = df.drop('TARGET', axis=1), df['TARGET']
xgb = XGBClassifier()
xgb.fit(X, y)

# Pickle model
pickle.dump(xgb, open("model.pkl", "wb"))
