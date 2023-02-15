Данный проект - уневерсальный парсер вакансий для составления статистики 



# 2.3.2

![image](https://user-images.githubusercontent.com/104368430/209503074-20ca9c0a-e6f0-4834-b073-ebbb8a8f772c.png)
<img width="183" alt="image" src="https://user-images.githubusercontent.com/104368430/209503109-fa29d5d2-8c2d-4d66-97f6-03755c2121f8.png">


# 2.3.3
Запустила профилизатор в PyCharm. Одним из самых трудозатратных методов является 'update', который обновляет значениия в словарях лдя составления статистики
<img width="960" alt="image" src="https://user-images.githubusercontent.com/104368430/209527713-1c182c2c-e762-41c6-936a-421e7e529a95.png"> 

В моем коде нет метода для форматирования даты (вместо этого я работаю со строкой, а точнее 'обрезаю' лишнее) ->

### 1-ая реализация: форматирование даты с помощью строк (в моем коде это реализовано в 1 строчку)
``` python
row[naming_dic.get('published_at')][:4]
```
Но чтобы замерить скорост выполнения я создала метод 'parse_date_with_str'

<img width="749" alt="image" src="https://user-images.githubusercontent.com/104368430/209534219-41a0b2fd-a4db-4818-a7a8-82f52bdcbc50.png">

``` python
def parse_date_with_str(date_vac: str) -> str:
    """Форматирует дату публикации к нужному формату 'обрезая' строку

    :param date_vac: Дата публикации
    :return: Отформатированная дата публикации
    """
    return date_vac[:4]
```
### 2-ая реализация: форматирование даты с помощью datetime
Работает значительно дольше, нежели первая реализация
<img width="753" alt="image" src="https://user-images.githubusercontent.com/104368430/209533888-4e2ef512-3d25-4c43-92bd-74486e261b82.png">

``` python
def parse_date_with_datetime(date_vac: str) -> str:
    """Форматирует дату публикации к нужному формату используя datetime

    :param date_vac: Дата публикации
    :return: Отформатированная дата публикации
    """
    return datetime.datetime.strptime(date_vac, '%Y-%m-%dT%H:%M:%S%z').strftime('%Y')
```
### 3-я реализация: форматирование даты с помощью dateutil
Работает намного дольше первых 2ух реализаций
<img width="753" alt="image" src="https://user-images.githubusercontent.com/104368430/209535480-d9611ed3-9ae0-4a8c-ae63-9b3788b76a0f.png">

``` python
def parse_date_with_dateutil(date_vac: str) -> str:
    """Форматирует дату публикации к нужному формату используя dateutil

    :param date_vac: Дата публикации
    :return: Отформатированная дата публикации
    """
    return parse(date_vac).strftime('%Y')
```
## В своем коде я оставила функцию 'parse_date_with_str' - наименее затратную по времени функцию преобразования


# 3.2.1
<img width="960" alt="image" src="https://user-images.githubusercontent.com/104368430/209541301-c7e98d73-628c-4986-90d0-ecab5de1ab89.png">


# 3.2.2

Без использования multiprocessing
<img width="960" alt="image" src="https://user-images.githubusercontent.com/104368430/209811587-7c826cb4-896e-47a0-a06d-d747ce8fa704.png">

С multiprocessing
<img width="960" alt="image" src="https://user-images.githubusercontent.com/104368430/209811492-8a6a8f4d-2717-48cb-abcb-371d5ddc34ed.png">

## С multiprocessing работает быстрее


# 3.2.3

C Concurrent futures
<img width="960" alt="image" src="https://user-images.githubusercontent.com/104368430/209812220-46a7f9fc-e9c3-47e1-b739-9093d11f640f.png">

С multiprocessing
<img width="960" alt="image" src="https://user-images.githubusercontent.com/104368430/209811492-8a6a8f4d-2717-48cb-abcb-371d5ddc34ed.png">


# 3.3.1

<img width="774" alt="image" src="https://user-images.githubusercontent.com/104368430/209898655-b9b19b39-c470-4fea-87a6-a01a7de70690.png">
<img width="906" alt="image" src="https://user-images.githubusercontent.com/104368430/209899102-9c6dde63-c4b9-4d3c-a947-fb3cec941d2a.png">


# 3.3.2

Первые 100 результатов

<img width="722" alt="image" src="https://user-images.githubusercontent.com/104368430/209950469-49294451-80f9-4f83-b0f2-a19351ce147a.png">
<img width="719" alt="image" src="https://user-images.githubusercontent.com/104368430/209950520-dbe4fca9-a8ba-4a94-9ea0-cda041ed3bef.png">
<img width="720" alt="image" src="https://user-images.githubusercontent.com/104368430/209950547-a0beab01-e5cf-4ef4-8703-ceb6997689b3.png">
<img width="721" alt="image" src="https://user-images.githubusercontent.com/104368430/209950568-ed4b76b1-27d2-4e3d-9df7-06796576d837.png">
<img width="727" alt="image" src="https://user-images.githubusercontent.com/104368430/209950592-0f06751a-60b0-4834-9936-7c7fbecdebe8.png">


# 3.5.1

<img width="960" alt="image" src="https://user-images.githubusercontent.com/104368430/210037204-9edce4a3-9b19-4ee2-877d-d1dc110ea7fc.png">
