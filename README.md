Развертывание 
В качестве брокера использован Redis
1)Выполните команду:

git clone ‘https://github.com/OlegYhay/Mailganer_test.git’

2)Перейти в каталог Mailganer и выполните команду:

pip install -r requirements.txt

3)Находясь в Mailganer, запустите работника celery командой:

celery -A Mailganer worker -l INFO --without-gossip

4)Запустите сервер командой:

Python manage.py runserver

Docker не был использован(в заданий не было требований), поэтому Redis и работников, запускаем сами.
