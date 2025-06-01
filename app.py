import streamlit as st
from streamlit_option_menu import option_menu
import analysis_and_model
import presentation

st.set_page_config(
    page_title="Предиктивное обслуживание",
    page_icon="🛠️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main-header {
        font-size: 2.6rem;
        font-weight: 700;
        color: #0A81D1;
        text-align: center;
        padding-bottom: 0.5rem;
    }
    .sub-header {
        text-align: center;
        font-size: 1.1rem;
        color: #444;
    }
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">Предиктивное обслуживание оборудования</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Интерактивный проект по бинарной классификации с использованием машинного обучения</div>', unsafe_allow_html=True)
st.markdown("")

with st.sidebar:
    st.image("https://img.icons8.com/ios-filled/100/maintenance.png", width=100)
    st.markdown("## 🔍 Навигация")
    selected = option_menu(
        menu_title=None,
        options=["📊 Анализ и Модель", "🧾 Презентация"],
        icons=["graph-up", "easel"],
        default_index=0
    )

if selected == "📊 Анализ и Модель":
    analysis_and_model.show()
elif selected == "🧾 Презентация":
    presentation.show()

st.markdown("---")
st.markdown("### ℹ️ О проекте")
st.info("""
Данный проект демонстрирует применение алгоритмов машинного обучения 
для предиктивного технического обслуживания оборудования.

🔹 Используемый датасет: *AI4I 2020 Predictive Maintenance Dataset*  
🔹 Цель: прогнозировать потенциальные отказы оборудования (бинарная классификация)  
🔹 Методы: анализ данных, обучение моделей, визуализация
""")
