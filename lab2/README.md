# Звіт до роботи
## Тема: _Основи Python_
### Мета роботи: _Ознайомитись з основними конструкціями в Python_
---
### Виконання роботи
- Результати виконання завдання:
    1. Ознайомлено з основними типами даних. Практика з простими змінними, списками list, наборами set та словниками dict:
    ```python
    a = "змінна з текстом"
    b = 1 #числова Змінна
    c = ["a", 1, 1.25, "Слово"] #List
    d = {"a": "Слово", "b": 1} #Dict
    e = ("a", ) #Tuple
    f = {"ss", } #Set
    g = "додаткова змінна"
    ```

    2. Виведено вбудовані константи:
    ```python
    print("a", False)
    print("b", True)
    print("c", None)
    ```
    ![alt text](https://github.com/anastasiakohut/oop_kn320/raw/main/lab2/scr/scr1.jpg "Результат виконання програми")


    3. Виведено результат роботи вбудованих функцій:
    ```python
    print(pow(2,7))
    print(int(2362))
    ```
    ![alt text](https://github.com/anastasiakohut/oop_kn320/raw/main/lab2/scr/scr2.jpg "Результат виконання програми")

    4. Написано код, який демонструє роботу циклів:
    ```python
    chyslo = ["14", "1", "-24"]
    for i in range(len(chyslo)):
        print(f"На позиції {i} знаходиться  {chyslo[i]}")
    ```
    ![alt text](https://github.com/anastasiakohut/oop_kn320/raw/main/lab2/scr/scr3.jpg "Результат виконання програми")

    5. Написано код, який демонструє роботу розгалужень:
    ```python
    A = True
    print("Значить А=True" if A else "Значить А=False")
    
    if A == True:
        print("А - правда")
        elif A == False:
            print("А - брехня")
    ```
    ![alt text](https://github.com/anastasiakohut/oop_kn320/raw/main/lab2/scr/scr4.jpg "Результат виконання програми")

    6. Написано свій варіант коду з помилкою:
    ```python
    a = 0
    try:
        print("Що буде якщо", 10/a, "?")
        except Exception as e:
            print(e)
            finally:
                print("Число підходить" if a>0 else "Введіть інше значення а")
    ```
    ![alt text](https://github.com/anastasiakohut/oop_kn320/raw/main/lab2/scr/scr5.jpg "Результат виконання програми")

    7. Написано код з контекст-менеджером:
    ```python
    with open("test.txt", "w") as f:
        f.write("some_data")
        
    with open("test.txt", "r") as f:
        for line in f:
            print(line)
    ```
    ![alt text](https://github.com/anastasiakohut/oop_kn320/raw/main/lab2/scr/scr6.jpg "Результат виконання програми")

    8.  Написано код та як Ви розумієте Лямбди:
    ```python
    this_is_lambda = lambda first, last: f'Цей код написала: {first} {last}'
    print("Це просто функція:", this_is_lambda)
    print("Це її виклик:", this_is_lambda('Anastasiya', 'Kohut'))
    
    print("")
    lambda_second = lambda first, last: f'Сьогодні перша пара - {first}; а друга - {last}.'
    print(lambda_second('ООП', 'Бізнес-планування'))
    ```
    ![alt text](https://github.com/anastasiakohut/oop_kn320/raw/main/lab2/scr/scr7.jpg "Результат виконання програми")
   



### Висновок: 
У роботі було створено файли з розширенням .ipynb ; створено звіт в форматуванні MarkDown; запущено програму на Python. Мету роботи було досягнуто. При виконанні лабораторної роботи жодних питань чи складнощів не виникло. 

---