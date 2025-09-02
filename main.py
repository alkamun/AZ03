import random
import pandas as pd

names = ["Катя", "Саша", "Миша", "Наташа", "Коля", "Толя", "Женя", "Валя", "Сергей", "Антон"]
subjects = ["Математика", "Литература", "Русский", "Физика", "История"]
data = {
    "name": [],
    "subject": [],
    "rating": []
}

for name in names:
    for subject in subjects:
        data["name"].append(name)
        data["subject"].append(subject)
        data["rating"].append(random.randint(2, 5))

df = pd.DataFrame(data)
print(df.head(15))

df = df.groupby('subject')

print()
print('Средняя оценка:')
print(df['rating'].mean())

print()
print('Медианная оценка:')
print(df['rating'].median())

Q1_math = df['rating'].quantile(0.25)["Математика"]
print()
print(f"Математика Q1: {Q1_math}")

Q3_math = df['rating'].quantile(0.75)["Математика"]
print(f"Математика Q3: {Q3_math}")

print(f"Математика IQR: {Q3_math - Q1_math}")

print()
print('Стандартное отклонение:')
print(df['rating'].std())
