Win+R --> Пишемо: cmd --> Переходимо в командний рядок, щоб відкрити термінал

як в командному рядку перейти 
з C:\Users\User> 
до D:\IT school\Projects\Projects_IT_School\Jupyter-AI_IT_School

cd /d "D:\IT school\Projects\Projects_IT_School\Python-AI__IT-Step_School"

Лапки потрібні, бо в назві є пробіли (IT school).
Тут ключ /d каже команді cd, що потрібно ще й змінити диск (з C: на D:).
Після цього ви одразу опинитесь у папці/.

Вводимо в терміналі: python --version 		(провірка чи встановлений python)
Вводимо в термінал:  pip install notebook 	(установка jupyter)
Вводимо в термінал:  jupyter notebook 		(запускаємо локально сервер з jupyter)
Автоматично відкриється браузер з шляхом: http://localhost:8888/tree

Потім для зручності:
	Win+R --> Пишемо: cmd
	cd /d "D:\IT school\Projects\Projects_IT_School\Python-AI__IT-Step_School"
	jupyter notebook

!!! Не закриваємо термінал, бо він має бути активним, через нього працює локальний сервер.
Зупинити його можна: 	поставивши курсор на індикатор мигаючий у терміналі , 
			потім комбінація кнопок Ctrl+C

=====================================================================================
як в jupyter писати тексти, абзаци, виділяти текст та інше
У Jupyter Notebook (або JupyterLab) є два основні типи комірок:

Code cell – для коду (Python та ін.)
Markdown cell – для тексту, абзаців, форматування
Щоб писати текст, абзаци, заголовки, виділення, потрібно:

🔹 Як перейти в текстовий режим
Натисніть на комірку.
У меню вгорі виберіть Cell → Cell Type → Markdown
або просто натисніть M у командному режимі (синя рамка навколо комірки).
Тепер у цій комірці можна писати Markdown.

🔹 Приклади форматування в Markdown
# Заголовок 1
## Заголовок 2
### Заголовок 3

📌 Абзаци:
Просто пишете текст у кілька рядків.
Порожній рядок = новий абзац.

📌 Виділення:
*курсив* або _курсив_  
**жирний текст**  
***жирний курсив***  

📌 Списки:
- Перший пункт
- Другий пункт
  - Підпункт
1. Нумерований
2. Список

📌 Цитата:
> Це приклад цитати

📌 Код у тексті:
`print("Hello")`

📌 Блок коду:
```python
print("Hello Jupyter")
```

📌 Посилання та зображення:
[Google](https://google.com)  
![Картинка](https://jupyter.org/assets/homepage/main-logo.svg)

✅ Щоб побачити результат – після написання тексту натисніть Shift + Enter.


==============================================================================================================
Give me 80/20 information about
[Answers to my questions from the Python exercises].
As an expert in the topic [teacher of the Python programming language].
Don't forget to use these :
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import plot_tree
import xgboost as xgb
"""
Think harder and make the right decision.
Stick to the principles:
“Don't make things up if you're not sure.”
“Don't invent if the information is not verified.“
“If the answer is inaccurate, say so directly.”
“Use only relevant and verified data.”
“Answer briefly, to the point, and clearly.“
Explain it step-by-step so that a beginner can understand it
Explain this to me like I’m 5
Answer in Ukrainian


py -3.12 -m venv venv
venv\Scripts\activate
python --version
Має бути: Python 3.12.10





