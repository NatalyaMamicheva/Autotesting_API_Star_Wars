Проект по автотестированию API + Python на примере API Star Wars (https://swapi.dev/). 


Сохраняет всех персонажей (имена), которые снимались в фильмах с Дарт Вейдером, в текстовый файл person.txt без дублирования.


В данном проекте представлены 2 главные директории:

1. utils – хранит в себе базовые методы для всех тестов (файлы checking.py, http_methods.py) и методы для тестирования Star Wars Api (файл api.py) ;

2. tests – хранит в себе запускаемые тесты (файл test_star_wars_api.py).


В конце тестирования происходит логирование результатов в директорию logs (с помощью файла logger.py)  и создаются отчеты с помощью Allure в директорию test_results/tests.

Инструкция по работе тестирования с Allure:

Ввести команду для запуска тестирования и сохранения отчета python -m pytest --alluredir=test_results/tests (в случае ошибки ввести команду pip install allure-pytest и повторить прошлую команду)

Ввести команду для просмотра отчета allure serve test_results/tests 

(Для корректной работы Allure убедитесь, что предварительно на Ваш компьютер установлен Scoop и Java версии 8 или выше).

Также данный проект содержит в себе файл «requirements.txt». В нем представлены модули и пакеты, необходимые для корректной работы данного проекта. Их можно загрузить с помощью команды «pip install -r "ваш путь до этого файла"»
