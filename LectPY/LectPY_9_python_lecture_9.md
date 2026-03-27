# Лекція 9. Pandas: Series, DataFrame та обробка табличних даних

---

## 1. Вступ: що вивчаємо в лекції

Лекція присвячена базовому і практичному використанню `pandas` для аналізу табличних даних:

- `Series` та `DataFrame`;
- читання/запис CSV;
- очищення даних (дублікати, пропуски);
- індексація, фільтрація;
- створення нових колонок;
- агрегування, `groupby`, сортування;
- об'єднання таблиць (`join`).

Імпорт у ноутбуці:

```python
import pandas as pd
import numpy as np
```

---

## 2. `Series` — одномірна структура

`Series` — це одномірний масив значень з підписами індексів.

Приклад із лекції:

```python
sequence = [1, 2, 3, 4, 5]
new_ser = pd.Series(sequence, dtype=np.float32)
```

Корисно пам'ятати:

- `Series` має `values`, `index`, `dtype`;
- операції між серіями вирівнюються за індексами;
- це базовий "будівельний блок" для `DataFrame`.

---

## 3. `DataFrame` — двовимірна таблиця

`DataFrame` — це таблична структура: рядки + колонки (можуть бути різних типів).

Приклад створення:

```python
data = {
    'age': [22, 31, 25],
    'name': ['Hannah', 'Mike', 'John'],
    'is_employed': [True, False, True]
}
df = pd.DataFrame(data)
```

`DataFrame` можна створювати з:

- словників;
- списків списків;
- `numpy`-масивів;
- інших `Series` / `DataFrame`.

---

## 4. Читання та запис даних (I/O)

У лекції використано датасет `adult.data`.

### Читання CSV

```python
data_path = '/content/.../adult.data'
df = pd.read_csv(data_path, sep=', ', header=None, na_values='?')
```

Пояснення параметрів:

- `sep=', '` — роздільник;
- `header=None` — у файлі немає заголовка колонок;
- `na_values='?'` — символ `?` трактуємо як пропуск (`NaN`).

### Задання схеми (імен колонок)

```python
column_names = [
    'age', 'workclass', 'fnlwgt', 'education', 'education-num',
    'marital-status', 'occupation', 'relationship', 'race', 'sex',
    'capital-gain', 'capital-loss', 'hours-per-week', 'native-country',
    'annual_income'
]
df.columns = column_names
```

### Запис у файл

У лекції також розглянуто зворотну операцію `to_csv()` (запис `DataFrame` у CSV).

---

## 5. Інспекція `DataFrame`

Перед будь-якою обробкою треба подивитись на структуру даних:

```python
df.head()
df.info()
df.describe()
df.shape
df.dtypes
```

Що дає інспекція:

- розмір таблиці;
- типи колонок;
- кількість непорожніх значень;
- базову статистику для числових полів.

---

## 6. Робота з колонками (refining columns)

### Перейменування колонок

```python
df.rename(
    columns={'Age': 'age_of_person', 'Workclass': 'workclass_of_person'},
    inplace=True
)
```

### Зміна типів

```python
typed_df = df.astype({'Capital-Gain': 'float'})
df['Capital-Loss'] = df['Capital-Loss'].astype(float)
```

### Видалення колонок

```python
dropped_df = df.drop('Capital-Loss', axis='columns')
```

---

## 7. Дублікати

### Пошук дублікатів

```python
df.duplicated()
df.duplicated(subset=['Education'])
```

### Видалення дублікатів

```python
dropped_df_1 = df.drop_duplicates()                  # дублікати по всіх колонках
dropped_df_2 = df.drop_duplicates(subset=['Education'])  # дублікати по конкретній колонці
```

---

## 8. Пропуски (`NaN`, `None`, `NULL`)

### Виявлення пропусків

```python
df.isna()                  # те саме, що .isnull()
df.isna().any(axis=1)      # рядки, де є хоча б один NaN
df[df.isna().any(axis=1)]  # показати такі рядки
```

### Заповнення пропусків

```python
na_filled_df = df.fillna('THIS IS NA')
```

### Видалення рядків із пропусками

```python
na_dropped_df = df.dropna()
na_subset_dropped_df = df.dropna(subset=['workclass_of_person'])
```

---

## 9. Індексація: `[]`, `iloc`, `loc`

### Базовий доступ до колонок

```python
df['Education']   # безпечний спосіб
df.Education      # коротко, але менш надійно
```

### `iloc` — доступ за позиціями (індексами)

```python
df.iloc[45:70, [3, 8, 2]]
df.iloc[3]
df.iloc[:3]
df.iloc[2:5, 4:10]
df.iloc[2, 4]
```

### `loc` — доступ за мітками (іменами)

```python
df.loc[:]
df.loc[:3]
df.loc[2:5, 'workclass_of_person']
df.loc[2:5, 'workclass_of_person':'Occupation']
df.loc[3, 'Education']
```

---

## 10. Фільтрація даних

Фільтрація будується на булевих умовах:

```python
df[df['age_of_person'] == 18]
```

Складні умови поєднуються через `&`, `|`, `~`:

```python
complicated_condition = (
    ((~df['age_of_person'] <= 25) & (df['Education'] == 'Masters'))
    | (df['Education'].isin(['Assoc-acdm', 'Doctorate']))
)
df[complicated_condition]
```

### `.where()`

`where()` залишає значення, де умова істинна, і підставляє інше там, де хибна.

```python
df['Sex'].where(df['Sex'] == 'Female')
df['Sex'].where(df['Sex'] == 'Female', 'man')
df['age_of_person'].where(df['age_of_person'] >= 18, 18)
```

### Скидання індексу після фільтрації

```python
df[df['age_of_person'] == 18].reset_index(drop=True)
```

---

## 11. Створення нових колонок

### На основі арифметики

```python
df['this_is_new_col'] = df['Capital-Loss'] - 100
```

### Через `map` + `lambda`

```python
df['annual_income_num'] = df['Annual_Income'].map(
    lambda val: 1 if val == '<=50K' else 2
)
```

### Через `apply(axis=1)` і власну функцію

```python
def is_eligible(row):
    # умова з лекції
    if ...:
        return True
    return False

df['is_scholarship_eligible'] = df.apply(is_eligible, axis=1)
```

---

## 12. Агрегування

Типові агрегати:

```python
df.count()     # кількість non-null
df.min()
df.max()
df.mean()
df.median()
df.sum()
```

Агрегування кількома функціями:

```python
df.agg([min, max])
df.agg({'age_of_person': min, 'Education-Num': max})
```

---

## 13. Групування (`groupby`)

Групування дозволяє рахувати метрики по категоріях.

```python
df.groupby('Sex')
df[['Sex', 'Occupation']].groupby('Sex').count()
df.groupby(['Sex', 'Marital-Status']).count()
df.groupby('Sex').age_of_person.agg([min, 'mean', max])
```

---

## 14. Сортування

```python
df.sort_values('age_of_person')
df.sort_values('age_of_person', ascending=False)
df.sort_values(['age_of_person', 'Education-Num'], ascending=[True, False])
```

---

## 15. Об'єднання таблиць

У лекції показано об'єднання через `join()`:

```python
df.join(other, lsuffix='_caller', rsuffix='_other')
```

Це корисно, коли потрібно додати колонки з іншого `DataFrame` за спільним індексом.

---

## Короткі висновки

- `Series` і `DataFrame` — базові структури `pandas`.
- Типовий пайплайн: **читання → інспекція → очищення → фільтрація/трансформація → агрегування**.
- Для пропусків і дублікатів: `isna`, `fillna`, `dropna`, `duplicated`, `drop_duplicates`.
- Для доступу до даних: `iloc` (позиції) і `loc` (мітки).
- Для аналітики: `groupby`, `agg`, `sort_values`, створення нових колонок через `map/apply`.
- Для злиття таблиць: `join` (і загалом інструменти об'єднання у `pandas`).
