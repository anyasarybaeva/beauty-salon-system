# База данных салона красоты
## Базы данных
### Диагрмма базы данных

![alt text](https://github.com/anyasarybaeva/beauty-salon-system/raw/master/img/screen/1.png "Диграмма")​
---

База данных созданна в DataGrip с помощью PostgreSql. Для  подключение к базе данных используется используется модуль [psycopg2](https://www.psycopg.org/docs/usage.html).

Для выполнения запроса к базе, необходимо с ней соединиться и получить курсор.

```python
        import psycopg2

        conn = psycopg2.connect(dbname='салон красоты', user='annasarybaeva', host='localhost')
        cursor = conn.cursor()
```
Манипуляция с данными выполняется с помощью библиотеки [pandas](https://pandas.pydata.org/docs/index.html)


## Графический интерфейс

Графический интерфейс для удобного взаимодействия с базой данных салона красоты создан с помощью среды для разработки графических интерфейсов [Qt Designer](https://doc.qt.io/qt-5/qtdesigner-manual.html) и библиотеки [PyQt5](https://build-system.fman.io/pyqt5-tutorial).

#### Окно авторизации

Для входа в личный кабинет для работы с базой данных
![alt text](https://github.com/anyasarybaeva/beauty-salon-system/raw/master/img/screen/auth.png "Окно авторизации")
---
#### Личный кабинет мастера

![alt text](https://github.com/anyasarybaeva/beauty-salon-system/raw/master/img/screen/lk.png "Личный кабинет мастера")
---
#### Личный кабинет администратора

![alt text](https://github.com/anyasarybaeva/beauty-salon-system/raw/master/img/screen/lk_admin.png "Личный кабинет администратора")

## Источники

[pandas](https://pandas.pydata.org/docs/index.html)
[psycopg2](https://www.psycopg.org/docs/usage.html)
[Qt Designer](https://doc.qt.io/qt-5/qtdesigner-manual.html)
[PyQt5](https://build-system.fman.io/pyqt5-tutorial)
