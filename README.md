# brigada_test_assignment

Задача, найденная на просторах интернета. Описание находится в папке [task/](https://github.com/AndyPlo/brigada_test_assignment/blob/main/task/task.md) Задание мне показалось интересным для изучения особенностей работы post запросов в django и дало возможность поиграться с ветвлениями для заполнения списков (select) во вьюхе.

В задании особо были выделены следующие условия:

> При выборе поля А, должно подгружаться поле Б, только те объекты
> которые входят в текущий выбранный объект А. Так же, если есть
> дочерние объекты В, для выбранного поля Б, то они тоже должны
> подгружаться. При выборе данных из формы, лишних данных не должно
> быть, только те, которые относятся к тем или иным объектам.
>
> Очень важно, после выбора объектов А, Б и если есть дочерние объекты
> Б, то и В, после перезагрузки страницы (например пользователь нажал
> f5) должны поля select и другие в текущей момент поля text, number
> помнить свое состояние, то есть не сбрасываться (можно использовать
> localStorage в js), так же можно использовать постраничный вывод,
> например /1, /1/2, /1/2/3 (где 1, 2, 3 объекты А, Б, В).

а так же рекомендация использовать ajax и jQuery. Так как в настоящий момент я не позиционирую себя как Fullstack разработчик, я решил реализовать данные условия, используя возможности Django (ну и Bootstrap).

## Установка и запуск в dev-режиме

 1. Установите виртуальное окружение (команда: `python -m venv venv`).
 2. Активируйте виртуальное окружение (команда: `source venv/Scripts/activate`).
 3. Установите зависимости из файла requirements.txt (команда: `pip install -r requirements.txt`).
 4. Заполните базу данных (команда: `python manage.py loaddata fixtures.json`)
 5. Запустите dev-сервер (команда: `python manage.py runserver`).

## Автор

Андрей Плотников (Andy.Plo@yandex.ru)