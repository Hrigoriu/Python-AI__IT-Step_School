from datetime import date

# Створимо дорожню карту як markdown-текст
notion_template = """
# 🧭 Дорожня карта: Від ЛОР-лікаря до Deep Learning Engineer

## 📅 Дата початку: {start_date}

---

## 🔹 Фаза 1: Закладення основ (0–6 місяців)
### 🎯 Цілі:
- Освоїти Python + бібліотеки (NumPy, Pandas, Matplotlib)
- Вивчити базову математику для ML
- Вивчити англійську до рівня B1
- Зробити 1-2 pet-проєкти (медична тематика)

### 📘 Ресурси:
- Python: RealPython, freeCodeCamp
- Математика: 3Blue1Brown, Khan Academy
- DeepLearning.AI: Neural Networks and Deep Learning
- Англійська: Duolingo, EnglishClass101, speaking clubs

---

## 🔹 Фаза 2: Профільне заглиблення (6–18 місяців)
### 🎯 Цілі:
- Вивчити PyTorch/TensorFlow, CNN, RNN, Transformers
- Побудувати 3-5 проєктів
- Писати README англійською
- Дослідити медичні дані (DICOM, MedNIST, HuggingFace)

### 📘 Ресурси:
- DeepLearning.AI спеціалізація
- Kaggle Competitions
- GitHub Projects
- HuggingFace Courses

---

## 🔹 Фаза 3: Вихід на ринок (18–36 місяців)
### 🎯 Цілі:
- Вийти на позицію Junior DL Engineer
- Пройти технічні інтерв’ю
- Використовувати Docker, FastAPI, MLflow
- Створити блог або менторський курс

### 📘 Ресурси:
- Interviewing.io, LeetCode (базовий рівень)
- YouTube-канали: Henry AI Labs, AI Coffee Break
- Medium, Towards Data Science

---

## 🔚 Принцип:
**"Не змінюй минуле — інтегруй його."**
Ти не просто вчишся — ти трансформуєш професійний досвід у нову форму.

"""

# Дата створення
today = date.today().strftime("%Y-%m-%d")

# Підставляємо дату
final_doc = notion_template.format(start_date=today)

# Зберігаємо як текстовий файл
file_path = "files/DL_Transition_Roadmap_UKR.txt"
with open(file_path, "w", encoding="utf-8") as f:
    f.write(final_doc)

file_path
