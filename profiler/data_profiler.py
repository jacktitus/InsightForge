import pandas as pd
# from scipy.stats import skew

def profile_dataset(df,targetcol):
    profile = {}

#number of rows and columns
    profile['rows'] = df.shape[0]
    profile['columns'] = df.shape[1]

# column types
    numerical = df.select_dtypes(include =['int64','float64']).columns.tolist()
    categorical = df.select_dtypes(include =['object','category']).columns.tolist()
    profile['numerical_columns'] = numerical
    profile['categorical_columns'] = categorical
    
# missing values
    missing = {}
    for col in df.columns:
        missing[col] = float(round(df[col].isnull().mean()*100,2))

    profile['missing_values_percentage'] = missing

# target and imbalance
    profile['target'] = targetcol

    if targetcol in df.columns:
        count = df[targetcol].value_counts(normalize=True)
        imbalance_ratio = round(count.max(),2)

        profile['imbalance_ratio'] = imbalance_ratio
    
    return profile