Переда запуском внесите переменные, указанные в файле .env.sample.
Для запуска проекта выполните команду docker-compose up --build.

По умолчанию создается суперюзер с логином "admin@sky.pro" и паролем "qwerty123". При желании
можно данные можно изменить на любые другие, для этого откройте файл csu, который находится
в папке users/management/commands/ и внесите изменения. Далее для демонстрации работы
приложения используется коллекция запросов postman, файл с запросами находится в корневой
папке проекта под названием "Kitten_show.postman_collection.json".

Документация реализована при помощи drf-yasg по адресу http://localhost:8000/swagger/ или 
http://localhost:8000/redoc/.

ПУНКТ С ФИЛЬТРАЦИЕЙ КОТЯТ ПО ПОРОДЕ РЕАЛИЗОВАН ПО URL http://localhost:8000/kitten_show/kittens/,
НУЖНО ПРОСТО ДОБАВИТЬ СООТВЕТСТВУЮЩИЕ GET ПАРАМЕТРЫ В ЗАПРОС, НАПРИМЕР:
http://localhost:8000/kitten_show/kittens/?breed=test. В ЛЮБОМ СЛУЧАЕ ДЕМОНСТРАЦИЯ РЕШЕНИЯ
ДАННОЙ ЗАДАЧИ ЕСТЬ В ОСНОВНОЙ КОЛЛЕКЦИИ ЗАПРОСОВ.

ДАЛЕЕ БУДЕТ ОПИСАНИЕ РАБОТЫ С "POSTMAN", ЕСЛИ У ВАС УЖЕ ЕСТЬ ОПЫТ РАБОТЫ С НИМ ТО МОЖЕТЕ
ПРИСТУПАТЬ К ПРОВЕРКЕ. ТАКЖЕ В КОРНЕВОЙ ВКЛАДКЕ ПРОЕКТА БУДЕТ ВИДЕО С ДЕМОНСТРАЦИЕЙ РАБОТЫ
ПРИЛОЖЕНИЯ.

Для просмотра работоспособности приложения нужно зарегистрироваться
на сайте https://www.postman.com/. Далее открываем вкладку "workspaces"
в верхнем левом углу и нажимаем на "my workspace", на открывшейся странице в верхнем левом
углу нажимаем "import". Во вкладке "import" переносим наш файл с коллекцией запросов в
область экрана с надписью "Drop anywhere to import", после чего откроется коллекция
"Kitten_show".

Далее поочередно открываем запросы, первый на регистрацию пользователя, второй на формирование
jwt токена, остальные можно открывать в произвольном порядке. После получения jwt токена
копируем данные из ключа "access". В последующих запросах открываем вкладку headers, нажимаем
на пустую строку в столбце "Key" и вводим "Authorization", далее в той же строке, в столбце
"Value" вводим "Bearer " и после пробела вставляем наш токен. Далее, при помощи
аналогичных действием с каждым запросом, либо при помощи копирования адресной строки из
другой вкладки запроса во вкладку с введенным токеном можно проверять работоспособность
приложения.
