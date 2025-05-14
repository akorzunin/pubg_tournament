# pubg_tournament
Этот репозиторий содержит инструменты для организации и проведения турниров по PlayerUnknown's Battlegrounds (PUBG).
Так же возможны учет и управление участников клана.

## 📌 О проекте
Проект предоставляет удобный способ управления турнирами, включая:

-Регистрацию участников

-Формирование лобби и расписания матчей

-Подсчёт очков и ведение статистики

-Генерацию отчётов и таблиц результатов

## 🛠 Установка и настройка
Рекомендуется использовать виртуальное окружение для изоляции зависимостей

Клонируйте репозиторий:

```git clone https://github.com/warmMySoul/pubg_tournament.git```

```cd pubg_tournament```

Создайте виртуальное окружение:

```python -m venv venv```

Активируйте его:

*Windows:*

```.\venv\Scripts\activate```

*Linux/MacOS:*

```source venv/bin/activate```


Установите зависимости:

```pip install -r requirements.txt```

Создайте файл secrets.env и добавьте значения:

>ADMIN_MAIL - логин суперюзера
>
>ADMIN_PASS - пароль суперюзера
>
>FERNET_KEY - ключ шифрования
>
>MAIL_LOGIN - логин от почты mail.ru для рассылок
>
>MAIL_PASS - пароль от почты mail.ru для рассылок
>
>PASSWORD - пароль от учетки сервера, на котором запускаете проект
>
>PUBG_API_KEY - ключ к [API](https://documentation.pubg.com/en/api-keys.html)
>
>REMOTE_SERVER_IP -ip сервера, на котором запускаете проект
>
>SECRET_KEY - ключ для запуска проекта 
>
>USERNAME - логин от учетки сервера, на котором запускаете проект

## 🚀 Запуск
Запустите основной скрипт:

```python app.py```

## 🤝 Участие в разработке
Приветствуются пул-реквесты и предложения!

Скопируйте репозиторий (git clone)

Создайте ветку (git checkout -b feature/your-feature)

Внесите изменения (git add .)

Зафиксируйте изменения (git commit -m 'Add some feature')

Запушьте ветку (git push origin feature/your-feature)

Откройте Pull Request

## 📜 Лицензия
MIT License.

Автор: warmMySoul
Версия: 0.1.0
