# AZ01_Employee_Data
### Задания к уроку AZ01

#### 1. Скачайте любой датасет с сайта https://www.kaggle.com/datasets

1.1. Загрузите набор данных из CSV-файла в DataFrame. 

1.2.Выведите первые 5 строк данных, чтобы получить представление о структуре данных. 

1.3. Выведите информацию о данных (.info()) и статистическое описание (.describe()).

#### 2. Определите среднюю зарплату (Salary) по городу (City) - используйте файл приложенный к дз - dz.csv

### Задание 1

Файл c кодом: part1.py 

Файл с данными: employee_data.csv

#### О наборе данных
Набор данных с именем employee_data.csv содержит смоделированные данные о 400 сотрудниках, работающих на различных должностях, связанных с ИТ. Данные включают сведения о поле каждого сотрудника, годах опыта, должности и заработной плате. Цель набора данных - отразить реальное распределение и различия в ИТ-отрасли, в частности то, как зарплаты, как правило, увеличиваются с увеличением опыта работы и конкретной должностной роли. Этот набор данных был сгенерирован с использованием библиотеки Faker на Python, которая позволяет создавать реалистичные поддельные данные для различных приложений.

1) ID: уникальный идентификатор для каждого сотрудника (от 1 до 400).
2) Gender: пол сотрудника. Значения задаются либо "M" (мужчина), либо "F" (женщина).
3) Опыт (годы): количество лет профессионального опыта, которое имеет сотрудник, в диапазоне от 0 до 20 лет.
4) Должность: название должности сотрудника. Должности, включенные в набор данных, следующие:

ИТ-менеджер
Инженер-программист
Сетевой администратор
Системный администратор
Администратор базы данных (DBA)
Веб-разработчик
Специалист по ИТ-поддержке
Системный аналитик
Аналитик по ИТ-безопасности
Инженер DevOps
Архитектор облачных решений
5) Заработная плата: годовая заработная плата сотрудника в долларах США. Заработная плата рассчитывается с учетом реальной компенсации в ИТ-отрасли и увеличивается как с увеличением должности, так и с годами опыта.

### Задание 2
Файл с кодом: part2.py

Файл с данными: dz.py
