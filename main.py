import os
import datetime

height = float(os.environ.get('HEIGHT', 1.75))
weight = float(os.environ.get('WEIGHT', 70))

bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Недостатня вага"
elif 18.5 <= bmi < 24.9:
    category = "Норма"
else:
    category = "Надлишкова вага"

result_string = f"[{datetime.datetime.now()}] Зріст: {height}м, Вага: {weight}кг -> ІМТ: {bmi:.2f} ({category})\n"

print("Результат обчислень:")
print(result_string)

with open("/app/data/results.txt", "a", encoding="utf-8") as file:
    file.write(result_string)

print("Результат успішно збережено у файл /app/data/results.txt")