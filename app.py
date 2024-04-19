import streamlit as st
from io import StringIO
from feat_imp import *

st.header('Feature Importance')

uploaded_file = st.file_uploader('Загрузите данные')
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
        # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode('utf-8'))
        # To read file as string:
    string_data = stringio.read()
        # Can be used wherever a "file-like" object is accepted:
    data = pd.read_csv(uploaded_file)


if st.button('Показать данные'):
    st.table(data)

#Choose target, numerical features, categorical features and columns to drop
to_drop = st.multiselect(
    'To drop', data.columns.to_list())
data.drop(columns=to_drop, inplace = True)

target = st.multiselect(
    'Target', data.columns.to_list())
y = data[target]

num_features = st.multiselect(
    'Numerical features', data.columns.to_list())
cat_features = st.multiselect(
    'Categorial features', data.columns.to_list())
X = data[cat_features + num_features]

model_type = st.selectbox('Model type',
                          ('CatBoostRegressor', 'CatBoostClassifier'),
                          placeholder="What kind of model would to use...")

feat_imp, fig = Catboost_feature_importance(X, y, model_type, cat_features, num_features)

n = st.select_slider('Show top-() features',
    options=[range(len(cat_features+num_features))])
st.table(feat_imp.head(n))

plot = st.checkbox('Show plot')
if plot:
    st.write(fig)



