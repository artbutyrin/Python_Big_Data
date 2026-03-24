# Лекція 10. Data Visualization

---

## 1. Що таке Data Visualization і навіщо вона потрібна

**Data Visualization** — це перетворення сирих числових даних у зрозумілі візуальні об'єкти (графіки, діаграми), щоб швидко донести ідею.

Візуалізація допомагає:

- показати тренд, порівняння або структуру даних;
- спростити складну інформацію;
- зробити аналітику більш зрозумілою для інших.

---

## 2. Приклади поганих візуалізацій і головні правила

У лекції розібрано приклади невдалих графіків та висновки, як покращувати якість візуалізації.

### Базові правила з прикладів

1. Додавайте заголовок (`title`), щоб одразу було зрозуміло, про що графік.
2. Перевіряйте, чи справді видно тренд/ідею, яку хочете показати.
3. Використовуйте порівнювані вимірювання та коректний масштаб.
4. Для більшості порівнянь осі краще починати з 0 (щоб не спотворювати сприйняття).
5. Обирайте адекватний тип графіка під задачу.
6. Заголовки мають бути короткі й прості.
7. Не перевантажуйте графік кольорами; використовуйте стриману палітру.
8. Для категорій краще не робити занадто багато груп (орієнтовно до 10).
9. Перевіряйте читабельність: людина має зрозуміти сенс за 10-15 секунд.
10. Дотримуйтесь єдиного стилю (корпоративні кольори, 1-2 шрифти, однакові назви категорій).
11. Підписуйте осі й одиниці виміру.
12. Перевіряйте орфографію, підписи, сітку та посилання.

Корисний каталог типів графіків: [Data Viz Catalogue](https://datavizcatalogue.com/).

---

## 3. Який графік коли використовувати

### 1) Line graph (лінійний графік)

- для **безперервних числових даних у часі**;
- коли важливо бачити зміну показника (тренд).

### 2) Scatter plot (діаграма розсіювання)

- для зв'язку між **двома безперервними змінними**;
- дозволяє побачити кореляцію, кластери, викиди.

### 3) Bar chart (стовпчикова діаграма)

- для порівняння **категорій** і числових значень;
- коли категорії не є безперервною шкалою.

### 3a) Histogram (гістограма)

- спеціальний випадок bar chart;
- показує розподіл безперервної змінної по інтервалах (`bins`).

### 4) Pie chart (кругова діаграма)

- для показу часток категорій у загальному цілому;
- сума часток має дорівнювати 1 або 100%.

---

## 4. Matplotlib і `pyplot`: основи

Посилання з лекції:

- [Matplotlib Quick Start](https://matplotlib.org/stable/tutorials/introductory/quick_start.html)
- [Real Python: Matplotlib Guide](https://realpython.com/python-matplotlib-guide/)

Імпорт:

```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
```

Найпростіший приклад:

```python
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()
```

### Figure та Axes

- `Figure` — зовнішній контейнер (весь малюнок);
- `Axes` — конкретний графік всередині `Figure`;
- елементи графіка (лінії, легенда, підписи, тики) — керовані об'єкти.

Створення полотна:

```python
fig = plt.figure()                 # порожній Figure
fig, ax = plt.subplots()           # Figure + 1 Axes
fig, axs = plt.subplots(2, 2)      # сітка 2x2 Axes
```

---

## 5. Практика Matplotlib з лекції

### Підготовка даних

```python
X = np.random.randint(low=1, high=11, size=50)
Y = X + np.random.randint(1, 5, size=X.size)
data = np.column_stack((X, Y))
```

### Два графіки в одному Figure

```python
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))

ax1.scatter(x=X, y=Y, marker='*', c='r', edgecolor='b')
ax1.set_title('Scatter: $x$ versus $y$')
ax1.set_xlabel('$x$')
ax1.set_ylabel('$y$')
ax1.grid(color='g', linestyle='-', linewidth=1)

ax2.hist(data, bins=np.arange(data.min(), data.max()), label=('x', 'y'))
ax2.legend(loc=(0.7, 0.8))
ax2.yaxis.tick_right()
```

### Кастомне розташування subplot через `subplot2grid`

```python
gridsize = (3, 2)
fig = plt.figure(figsize=(12, 8))
ax1 = plt.subplot2grid(gridsize, (0, 0), colspan=2, rowspan=2)
ax2 = plt.subplot2grid(gridsize, (2, 0))
ax3 = plt.subplot2grid(gridsize, (2, 1))
```

### Pie chart

```python
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15.5, 30, 45, 10]
explode = (0, 0.1, 0, 0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
plt.show()
```

Приклад із сортуванням категорій перед побудовою:

```python
labels_sizes_dict = {'Frogs': 15.5, 'Hogs': 30, 'Dogs': 45, 'Logs': 10}
labels_sizes_dict_sorted = dict(sorted(labels_sizes_dict.items(), key=lambda item: item[1]))
```

---

## 6. Seaborn: статистичні графіки поверх Matplotlib

Посилання з лекції: [Seaborn Introduction](https://seaborn.pydata.org/tutorial/introduction.html)

Seaborn будується поверх Matplotlib і добре інтегрується з `pandas`-структурами.

Імпорт:

```python
import seaborn as sns
```

Завантаження вбудованих датасетів:

```python
tips = sns.load_dataset("tips")
penguins = sns.load_dataset("penguins")
```

### Приклади графіків із лекції

```python
sns.scatterplot(x=tips["total_bill"], y=tips["tip"])
plt.show()
```

```python
sns.regplot(x="total_bill", y="tip", data=tips)  # linear regression
```

```python
sns.relplot(data=tips, x="total_bill", y="tip", hue="smoker")
```

```python
sns.boxplot(x="day", y="total_bill", data=tips, hue="smoker", palette=["m", "g"])
```

```python
sns.violinplot(
    data=tips, x="day", y="total_bill", hue="smoker",
    split=True, inner="quart", linewidth=1,
    palette={"Yes": "b", "No": ".85"}
)
```

```python
sns.histplot(penguins, x="flipper_length_mm", bins=200)
```

```python
sns.pairplot(penguins, hue="species")
```

---

## 7. Що запам'ятати після лекції

- Візуалізація має комунікувати ідею швидко й однозначно.
- Спочатку визначаємо задачу (тренд, порівняння, розподіл, частки), потім тип графіка.
- Якісний графік має: зрозумілий заголовок, підписані осі, коректний масштаб, читабельні кольори.
- `Matplotlib` дає повний контроль над елементами графіка (`Figure`, `Axes`, підписи, легенда, сітка).
- `Seaborn` спрощує статистичні візуалізації і пришвидшує EDA.

---

## 8. Додаткові приклади EDA з лекції

1. [Kaggle: Awesome Data Visualisation (Student Results)](https://www.kaggle.com/code/joshuaswords/awesome-data-visualisation-student-results?scriptVersionId=57181038)
2. [Kaggle: Netflix Data Visualization](https://www.kaggle.com/code/joshuaswords/netflix-data-visualization)
3. [Kaggle: Python Data Visualizations](https://www.kaggle.com/code/benhamner/python-data-visualizations)
