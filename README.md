# 🏭 Проект: Бинарная классификация для предиктивного обслуживания оборудования

![Predictive Maintenance](https://img.shields.io/badge/Predictive-Maintenance-blue) ![Machine Learning](https://img.shields.io/badge/Machine-Learning-orange) ![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-green)

## Описание

**Цель:** Построить ML-модель для предсказания отказа оборудования:
- ✅ Target = 0 — оборудование работает
- ❌ Target = 1 — ожидается отказ

Результат — интерактивное Streamlit-приложение с удобной навигацией.

**Преимущества:** Предиктивное обслуживание снижает простои и затраты, позволяя планировать ТО по необходимости.

## 📊 Датасет

Используется [AI4I 2020 Predictive Maintenance Dataset](https://archive.ics.uci.edu/dataset/601/predictive+maintenance+dataset) (10 000 строк, 14 признаков).

| Категория         | Переменные                                                                 |
|-------------------|----------------------------------------------------------------------------|
| Идентификаторы    | UDI, Product ID                                                            |
| Признаки          | Type (L/M/H), Air temperature [K], Process temperature [K], Rotational speed [rpm], Torque [Nm], Tool wear [min] |
| Целевые           | Machine failure (0/1), TWF, HDF, PWF, OSF, RNF                             |

## 📂 Структура проекта

```
predictive_maintenance_project/
├── app.py                # Streamlit-приложение
├── analysis_and_model.py # Анализ данных и модели
├── presentation.py       # Презентация проекта
├── requirements.txt      # Зависимости
├── model_handler.py      # Логика моделей
├── data/                 # Датасеты
├── models/               # Сохранённые модели
└── README.md             # Документация
```

## 🚀 Быстрый старт

```bash
git clone https://github.com/RatmirTech/KAI.PrediMaint
cd predictive_maintenance_project
pip install -r requirements.txt
streamlit run app.py
```

## 🖥️ Возможности приложения

### 1. 📊 Анализ и модель
- Загрузка данных (файл или UCI)
- Предобработка: удаление столбцов, кодирование, масштабирование
- Обучение моделей: Логистическая регрессия, Случайный лес, XGBoost, SVM
- Оценка: Accuracy, Precision, Recall, F1, ROC-AUC, матрица ошибок, важность признаков
- Предсказание на новых данных

### 2. 🎤 Презентация
- Описание задачи
- Методология
- Результаты
- Выводы и улучшения

## 🔧 Пример предобработки
```python
from sklearn.preprocessing import LabelEncoder, StandardScaler
# Удаление лишних столбцов
data.drop(['UDI', 'Product ID'], axis=1, inplace=True)
# Кодирование категориальных переменных
le = LabelEncoder()
data['Type'] = le.fit_transform(data['Type'])
# Масштабирование
scaler = StandardScaler()
data[['Air temperature [K]', 'Process temperature [K]']] = scaler.fit_transform(data[['Air temperature [K]', 'Process temperature [K]']])
```

## 🤖 Модели
| Модель                | Преимущества                 |
|-----------------------|------------------------------|
| Логистическая регрессия | Простота, интерпретируемость |
| Случайный лес           | Устойчивость к переобучению  |
| XGBoost                 | Высокая точность             |
| SVM                     | Эффективность на сложных данных |

## 📈 Метрики
```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print(f"Precision: {precision_score(y_test, y_pred):.2f}")
print(f"Recall: {recall_score(y_test, y_pred):.2f}")
print(f"F1-score: {f1_score(y_test, y_pred):.2f}")
print(f"ROC-AUC: {roc_auc_score(y_test, y_pred):.2f}")
```

## 🛠️ Технологии
- Python
- Streamlit
- Scikit-learn
- XGBoost
- Pandas
- Plotly

## 📬 Контакты
Автор: Ратмир Ишгулов  
Email: ishgulov.ratmir@gmail.com  
GitHub: [github.com/RatmirTech](https://github.com/RatmirTech/KAI.PrediMaint)

<div align="center">
  <img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg" alt="Made with Python">
  <img src="https://img.shields.io/badge/Open%20Source-%E2%9D%A4-blue" alt="Open Source">
</div>
