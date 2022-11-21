# Shop_Stripe
Shop with a connected payment system Stripe

## Описание:

Магазин с одной html страничкой, которая обращается к Stripe (платежная система).

## Технологии:
Python 3.7, 
Django 2.2.19, 
Docker, 
Stripe

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/E-bean/Shop_Stripe
```

```
cd Shop_Stripe
```

Создать .env файл.
```
touch shop/shop/.env
```

Шаблон наполнения env-файла:
```
SECRET_KEY=django-insecure-=yqcdw*vahv=5e5s)8qn-)-!#3p)qfz!l(_f4kast6mh@e45!+ # ключ для Django

STRIPE_SECRET_KEY=sk_test_51M5x8gEb2OYMXtYbAas1Mc4Zuf5t0q3F8wOzpfWmkQ0Pyt6yByosUDBn6eAf5vqb9jusfrmXUEjpjvRa4A6CC3Cd00pAJodbE6 # ключ Stripe API (https://stripe.com/docs/keys)

STRIPE_PUBLISHABLE_KEY=pk_test_51M5x9gEb2OYMXtYboXsx2JJey3TLw4lTPKoCYaHlGVJpg4GW2ovViSOFLA5wealqrapM3HZ4JTJb5S1NRcG0TAy0001r2HqAVp # ключ Stripe API (https://stripe.com/docs/keys)

```
Запустить сборку образа:

```
docker build -t shop . 
```

Запустить контейнер:

```
docker run --name local_shop -it -p 8000:8000 shop
```

Выполните миграции:

```
docker exec web python manage.py migrate
```
Для создания суперпользователя введите:

```
docker exec web python manage.py createsuperuser
```

В админ панели добавьте товар. http://localhost:8000/admin/
По адресу http://localhost:8000/item/1/ можно протестировать оплату товара.
Карты для тестовой оплаты https://stripe.com/docs/testing#cards.
