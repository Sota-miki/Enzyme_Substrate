import pandas as pd

def load_datasets(feats):
    dfs = [pd.read_feather(f'feature_variables/{f}_train.ftr') for f in feats]
    X_train = pd.concat(dfs, axis=1)
    dfs = [pd.read_feather(f'feature_variables/{f}_test.ftr') for f in feats]
    X_test = pd.concat(dfs, axis=1)
    return X_train, X_test

feats = ["BertzCT","Chi1"]
X_train, X_test = load_datasets(feats)

print(X_train.head())
print(X_test.head())