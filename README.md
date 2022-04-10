Здравствуйте. Попробую описать выполненное тестовое задание сразу на двух языках.

#### Hello. I will try to describe the completed test task in two languages at once.

Данное задание было взято с адреса: [Bidnamic test](https://github.com/bidnamic/bidnamic-fullstack-challenge/blob/master/challenge.md)

#### This assignment was taken from: [Bidnamic test](https://github.com/bidnamic/bidnamic-fullstack-challenge/blob/master/challenge.md)

### Для запуска задания вам необходимо проделать несколько манипуляций.
## There are a few things you need to do to start the job.

Описание процесса разворачивание проекта я исхожу из умолчаний, что Вы, как и я работаете под линуксом. 

#### Description of the process project deployment I proceed from the defaults that you, like me, work under Linux.

0. Я использую PyEnv для установки и настройки виртуального окружения, описывать этот процесс здесь не считаю целесообразным. Извините. Я считаю, что это общедоступные данные.

   I'm using PyEnv for installing and tune-up a virtual environment, so I don't feel like describing the process here. Sorry. I believe this is public information.

1. Развернуть проект Вы можете склонировав его с моего репозитория запустив команду с параметрами:
   
   You can deploy the project by cloning it from my repository by running the command with parameters:
   
   'git clone https://github.com/SergKrasnikov/bidmatic.git'
   
2. В корневой папке проекта лежит файл requirements.txt с записями зависимостей пакетов необходимых для старта проекта.

   Установить зависимости можно с помощью команды:

   In the root folder of the project, there is a requirements.txt file with records of package dependencies necessary to start the project.

   You can install dependencies using:

   'pip install -r requirements.txt'
3. После этого нужно произвести создание и миграцию базы данных, а после создать суперпользователя для входа в интерфейс создания "пользователей":

   After that, you need to create and migrate the database, and then create a superuser to enter the interface for creating "users":

   'cd bidnamic && mkdir db'

   'python ./manage.py migrate'

   'python ./manage.py createsuperuser'

   'python ./manage.py collectstatic'

4. Запуск проекта осуществляется как всех других:

   После чего главная страница проекта должна быть доступна по адресу: http://127.0.0.1:8000/ в вашем броузере.

   The project is launched like all others:

   'python ./manage.py runserver'

   After that, the main page of the project should be available at: http://127.0.0.1:8000/ in your browser.

Как ответная часть мною была выбрана методика ClassBased Views. Это не было в описании к заданию. Если потребуется я могу переписать на функции.

Кроме того мною была выбрана методика минифицирования кода по причине очень упрощенного описания задания.

#### As a response, I chose the ClassBased Views technique. It wasn't in the quest description. If necessary, I can rewrite to functions.

#### In addition, I chose the method of minifying the code because of the very simplified description of the task.

В коде мало комментариев т.к. мало кода и имена переменных на мой взгляд красноречиво говорят сами за себя.

#### There are few comments in the code. little code and variable names in my opinion eloquently speak for themselves.

В коде использовано анотация функции только один раз.... Не нашёл другого места для применения....

#### The function annotation was used only once in the code.... I did not find another place to use it....

Проект писал в PyCharm поэтому PEP8 мне помогал соблюдать он. Но это не значит, что без PyCharm мой код станет совершенно ужасным.

#### The project was written in PyCharm, so PEP8 helped me to comply with it. But that doesn't mean that without PyCharm, my code will be downright awful.

В репозиторий не включены производные файлы от style.scss, а также в описание этапов разворачивания проекта. Я считаю, что такие простые задачи не подлежат пояснениям.

#### The repository does not include derived files from style.scss, as well as the description of the project deployment steps. I believe that such simple tasks are beyond explanation.




###Желаю хорошего дня....

## I wish you a good day....