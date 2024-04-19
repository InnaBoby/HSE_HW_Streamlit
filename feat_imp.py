import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from catboost import CatBoostRegressor, CatBoostClassifier
import matplotlib.pyplot as plt
import seaborn as sns



def Catboost_feature_importance(X, y, model_type, cat_features, num_features):
        
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=42)
    
    
    if model_type == 'CatBoostRegressor':
            model = CatBoostRegressor(iterations=500,
                              learning_rate=0.01,
                              depth=5,
                              cat_features=cat_features)
    
    elif model_type == 'CatBoostClassifier':
            model = CatBoostClassifier(iterations=500,
                              learning_rate=0.01,
                              depth=5,
                              cat_features=cat_features)

    model.fit(X_train, y_train)

    #Table
    importance = model.feature_importances_
    names = cat_features+num_features
    feat_imp = pd.DataFrame({'feature_importance': importance,
                             'feature_names': names})

    feat_imp = feat_imp.sort_values(by=['feature_importance'], ascending=False)

    #Plot
    fig, ax = plt.subplots(figsize=(10,8))
    sns.barplot(x=feat_imp['feature_names'], y=feat_imp['feature_importance'])
    ax.set_title(model_type + ' FEATURE IMPORTANCE')
    ax.set_xlabel('FEATURE NAMES')
    ax.set_ylabel('FEATURE IMPORTANCE')

    return feat_imp, fig


