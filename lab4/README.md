# Звіт до лабораторної роботи
## Тема: _Робота у віртуальних середовищах_
### Мета роботи: _Ознайомитись з віртуальним середовищем_
---
### Основи роботи зі сторонніми бібліотеками
1. Встановлення PIP. Перевірка бібліотек встановдених на комп'ютері

![alt text](https://github.com/anastasiakohut/oop_kn320/raw/main/lab4/scr/scr1.jpg "Результат виконання програми")

2. Встановлення бібліотеки requests

![alt text](https://github.com/anastasiakohut/oop_kn320/raw/main/lab4/scr/scr2.jpg "Результат виконання програми")
![alt text](https://github.com/anastasiakohut/oop_kn320/raw/main/lab4/scr/scr3.jpg "Результат виконання програми")

4. Ознайомлення та використання методів із бібліотеки

![alt text](https://github.com/anastasiakohut/oop_kn320/raw/main/lab4/scr/scr4.jpg "Результат виконання програми")
![alt text](https://github.com/anastasiakohut/oop_kn320/raw/main/lab4/scr/scr5.jpg "Результат виконання програми")

---
### Робота у віртуальному середовищі
1. Для створення VENV та його активації було виконано такі команди:

```
python -m venv ./my_env
source my_env/Scripts/activate
pip install requests
deactivate
pip show requests 
```
2. Остання команда вивела опис бібліотеки:

![alt text](https://github.com/anastasiakohut/oop_kn320/raw/main/lab4/scr/scr6.jpg "Результат виконання програми")
---
### Робота з Pipenv
1. Команди, які можна виконувати за допомогою pipenv:

![alt text](https://github.com/anastasiakohut/oop_kn320/raw/main/lab4/scr/scr7.jpg "Результат виконання програми")

2. Створення нового середовища:

![alt text](https://github.com/anastasiakohut/oop_kn320/raw/main/lab4/scr/scr8.jpg "Результат виконання програми")

3. Створення файлів Pipfile та Pipfile.lock:

![alt text](https://github.com/anastasiakohut/oop_kn320/raw/main/lab4/scr/scr9.jpg "Результат виконання програми")
![alt text](https://github.com/anastasiakohut/oop_kn320/raw/main/lab4/scr/scr10.jpg "Результат виконання програми")

4. Коли пропробувала запустити код, то в командному рядку виводилось лише таке, і я не зрозуміла, що потрібно робити далі:

![alt text](https://github.com/anastasiakohut/oop_kn320/raw/main/lab4/scr/scr11.jpg "Результат виконання програми")

5. Для встановлення я обрала біблотеку NumPy. Вона містить багатовимірні масиви та матричні структури даних.

![alt text](https://github.com/anastasiakohut/oop_kn320/raw/main/lab4/scr/scr12.jpg "Результат виконання програми")

```python
>>> import numpy as np
>>> x = np.linspace(-5, 5, 11)
>>> x
array([-5., -4., -3., -2., -1.,  0.,  1.,  2.,  3.,  4.,  5.])
```

6. Доступні інтерпретатори:

![alt text](https://github.com/anastasiakohut/oop_kn320/raw/main/lab4/scr/scr13.jpg "Результат виконання програми")


### Робота зі змінними середовища
Після виконання коду, мені вивело:
```
KeyError: 'HELLO'
```

### Висновок: 
У роботі було створено файли з розширенням .py та .env; створено звіт в форматуванні MarkDown; встановлено бібліотеку requests; створено віртуальне середовище. Мету роботи було досягнуто. При виконанні лабораторної роботи виникли деякі складнощі, пов'язані з віртуальним середовищем.

---