import streamlit as st
from io import StringIO
from feat_imp import *

st.header('Feature Importance')

data = pd.read_csv('Student Attitude and Behavior.csv')
if st.button('Показать данные'):
    st.table(data.head())
data.fillna(0)
data=data[['Gender',	'Height(CM)',	'Weight(KG)',	'10th Mark',	'12th Mark',	'college mark',	'hobbies',	'prefer to study in',	'salary expectation']]

#Choose target, numerical features, categorical features and columns to drop
to_drop = st.multiselect(
    'To drop', data.columns.to_list())
data.drop(columns=to_drop, inplace = True)

target = st.multiselect(
    'Target', data.columns.to_list())
y = data[target]
data.drop(columns=target, inplace=True)

num_features = st.multiselect(
    'Numerical features', data.select_dtypes(exclude='object').columns.to_list())
cat_features = st.multiselect(
    'Categorial features', data.select_dtypes(include='object').columns.to_list())
X = data[cat_features + num_features]

st.table(X.head())

model_type = st.selectbox('Model type',
                          ('CatBoostRegressor', 'CatBoostClassifier'),
                          placeholder="What kind of model would to use...")

feat_imp, fig = Catboost_feature_importance(X, y, model_type, cat_features, num_features)

n = st.select_slider('Show top-() features',
                         options=np.arange(1, len(X.columns.to_list())+1)
                        )
st.table(feat_imp.head(n))
    
plot = st.checkbox('Show plot')
if plot:
    st.write(fig)



