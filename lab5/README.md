# Звіт до лабораторної роботи
## Тема: _Тестування програм_
### Мета: _Перевірити правильність роботи програм, їх функцій та поведінки при різних умовах роботи шляхом створення штучних ситуацій або сценаріїв_
---
### Перевірка assert

Програма з тестами assert:

![alt text](https://github.com/anastasiakohut/oop_kn320/raw/main/lab5/scr/scr1.jpg "Результат виконання програми")

Якщо ввести змінну не int, то програма видає:

```
Введіть свій рік народження -> qwerty
AssertionError: Ви впевнені що це "qwerty" число ?)
```

При введенні слова з маленької літери, прогама видасть наступне:

```
Введіть свій рік народження -> 2003
Введіть Прізвище Імя по Батькові (через пробіл, з великої літери) -> kohut
AssertionError: Схоже ви допустились помилки у слові "kohut"
```

При виконанні наступного коду, програма вивела:

![alt text](https://github.com/anastasiakohut/oop_kn320/raw/main/lab5/scr/scr2.jpg "Результат виконання програми")


Результат роботи програмки з файлу f3.py:

![alt text](https://github.com/anastasiakohut/oop_kn320/raw/main/lab5/scr/scr3.jpg "Результат виконання програми")

---
### Юніт тести

При введені коду програма видає наступне:

![alt text](https://github.com/anastasiakohut/oop_kn320/raw/main/lab5/scr/scr4.jpg "Результат виконання програми")

### test.py

```python
import unittest
from random import choice, randint

from app import Figure  # назва файлу з нашим класом повинна бути app.py


class TestFigure(unittest.TestCase):
    def setUpClass():
        """Виконається лише раз на початку тестів
        """
        pass

    def setUp(self) -> None:
        """Виконується кожного разу коли запускається тест
        """
        self.figure = choice(Figure.FIGURES)
        self.length = randint(1, 10)
        self.color = choice(Figure.COLORS)
        self.obj = Figure(self.figure, self.length, self.color)
        return super().setUp()

    def tearDown(self) -> None:
        del self.obj
        return super().tearDown()

    def test_figure_type(self):
        print(
            f"Тестуємо вивід, має бути: {self.figure} == {self.obj.get_figure_type}")
        self.assertEqual(self.figure, self.obj.get_figure_type,
                         "Властивість get_figure_type повертає непривильну фігуру!")

    def test_figure_lengh(self):
        self.assertEqual(self.length, self.obj.get_figure_length,
                         "Властивість get_figure_length повертає непривильну довжину!")

    def test_figure_color(self):
        self.assertEqual(self.color, self.obj.get_figure_color,
                         "Властивість get_figure_length повертає непривильний колір!")

    def test_obj(self):
        with self.assertRaises(AssertionError):
            # Спробуємо створити обєкт з недозволеними параметрими, в нас має бути помилка AssertionError
            Figure("коло", 1)


if __name__ == '__main__':
    # unittest.main(verbosity=2) щоб був більш детальний вивід
    unittest.main(verbosity=2)
```

При запуску тестів програма вивела:

```
test_figure_color (__main__.TestFigure) ... ok
test_figure_lengh (__main__.TestFigure) ... FAIL
test_figure_type (__main__.TestFigure) ... Тестуємо вивід, має бути: прямокутник == прямокутник
ok
test_obj (__main__.TestFigure) ... ok

======================================================================
FAIL: test_figure_lengh (__main__.TestFigure)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\Labs\Labs 3.1\ООП\github\OOP\Lab5\Test_app.py", line 33, in test_figure_lengh
    self.assertEqual(self.length, self.obj.get_figure_length,
AssertionError: 5 != 'прямокутник' : Властивість get_figure_length повертає непривильну довжину!

----------------------------------------------------------------------
Ran 4 tests in 0.002s

FAILED (failures=1)
```
---
### Юніт тести з використання бібліотеки PyTest


Cтворено віртуальне середовище та інстальовано туди бібліотеку `PyTest`
  До арр.ру додано таку функцію:

```python
def test_app_triangle():
    """Test if we create triangle figure.
    """
    fig = "трикутник"
    len = 4
    col = 'blue'

    triangle = Figure(fig, len, col)
    assert triangle.type == fig, f"Фігура має бути {fig}"
```

Ось що виводить `PyTest`:

```
================== test session starts ==================
platform win32 -- Python 3.10.6, pytest-7.1.3, pluggy-1.0.0
rootdir:C:\Users\Nastia\Desktop\Навчання\Об'єктно-орієнтоване програмування\oop_kn320\lab5
collected 1 item

app.py .              [100%]

================== 1 passed in 0.02s ==================
```

А це вивід після запуску `test.py`:

```
================== test session starts ==================
platform win32 -- Python 3.10.6, pytest-7.1.3, pluggy-1.0.0
rootdir: C:\Users\Nastia\Desktop\Навчання\Об'єктно-орієнтоване програмування\oop_kn320\lab5
collected 4 items

test.py .F..   [100%]

================== FAILURES ==================
__________________ TestFigure.test_figure_lengh __________________

self = <test.TestFigure testMethod=test_figure_lengh>

    def test_figure_lengh(self):
>       self.assertEqual(self.length, self.obj.get_figure_length,
                         "Властивість get_figure_length повертає непривильну довжину!")
E       AssertionError: 4 != 'квадрат' : Властивість get_figure_length повертає непривильну довжину!

test.py:33: AssertionError
================== short test summary info ==================
FAILED test.py::TestFigure::test_figure_lengh - AssertionError: 4 != 'квадрат' : Властивість get_figure_length повертає непривильну довжину!
================== 1 failed, 3 passed in 0.10s ==================
```

### Візуалізація результатів та покриття коду Coverage (pytest-cov)

Встановлено плагін `PyTest-Cov` та `Coverage`, щоб потестити який з тестів краще тестить

  Вивід трошки гарніший. В таблиці гарно виглядає, але щось мало інформації про помилку.

```
Name     Stmts   Miss  Cover
----------------------------
app.py      25      5    80%
----------------------------
TOTAL       25      5    80%
```

---

### Висновок: 
У роботі було створено файли з розширенням .py; створено звіт в форматуванні MarkDown; отримано навички у тестуванні. Мету роботи було досягнуто. При виконанні лабораторної роботи жодних складнощів не виникло.
---