# HSE_HW_Streamlit
HomeWork 09, Streamlit

# Data:

https://www.kaggle.com/datasets/susanta21/student-attitude-and-behavior

# APP on Streamlit:

https://hsehwapp-qmq9my7ylxqxswmkyzzrbn.streamlit.app/

# P.S.:
1) to drop  - удаляет ненужные колонки из датасета
2) target - feature-importance какого признака хотим получить
3) Numerical features - числовые признаки, которые будут участвовать в анализе
4) Categorial features - категориальные пизнаки, которые будут участвовать в анализе (ВНИМАНИЕ: не выбирайте бинарные признаки - они почему-то не поддерживаются катбустом, это столбцы Certification Course, Department, daily studing time, Do you like your degree?, social medai & video, Travelling Time) 
5) далее фотрмируется итоговый датасет
6) Model type - регрессия или склассификация (в зависимости от выбранного таргета)
7) Show top-() features - сколько признаков вывести в таблицу feature-importance
8) Show plot - показать график важности всех признаков на таргет
