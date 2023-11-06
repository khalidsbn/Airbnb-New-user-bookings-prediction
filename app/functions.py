""" Build functions to automatize the process in model.py and app.py """

from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import LabelEncoder

def feature_encoder(df, cols):
    """
    Processing object features with OrdinalEncoder
    """
    ordinal_encoder = OrdinalEncoder()
    df[cols] = ordinal_encoder.fit_transform(df[cols])
    return df

def target_encoder(df, column_name):
    """"
    Process the Target alone
    """
    label_encoder = LabelEncoder()
    df[column_name] = label_encoder.fit_transform(df[column_name])
    return df