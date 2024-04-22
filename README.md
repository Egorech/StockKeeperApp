<h1>Backend приложение для управления запасом кофе и печенья в офисе</h1>
<h2>Тестовое задание в Numedy</h2>

Структуру хранения информации следует выбрать с учетом того что: 
* есть несколько мест для хранения запасов, различающиеся по максимальному весу товара; 
* несколько сотрудников пополняющих и забирающих с полки товар; 
* ассортимент может произвольно пополняться.

Данные следует хранить в реляционной базе данных. 
Взаимодействие с порталом осуществляется по REST API. Для проверки работоспособности требуется API UI.

(*)Для оптимизации работы приложения было принято решение о вынесении расчета суммарного веса товара на полках в отдельный процесс. Требуется реализовать CELERY воркер расчета веса товара и взаимодействие с воркером.
При выполнении проекта следует использовать DjangoRestFramework для реализации API, ORM DJANGO для подключения к базе данных. Готовый проект подготовить к запуску в docker контейнере с обработкой запросов через wsgi веб сервер и подключению к бд.



Используемые технологии:
1) DjangoRestFramework
2) Redis
3) Celery
4) PostgreSQL
5) Docker Compose

Схема БД:
![image](https://github.com/Egorech/StockKeeperApp/assets/90097022/f79e0fd0-23c6-4d03-b72c-04816cc39aa0)

Админ панель:
![image](https://github.com/Egorech/StockKeeperApp/assets/90097022/2e6b2d3e-c5eb-4e5a-94cb-b54f1275e961)

Скрины приложения:
![image](https://github.com/Egorech/StockKeeperApp/assets/90097022/08fb0ff7-5549-4155-8ce0-8185768d0d27)
![image](https://github.com/Egorech/StockKeeperApp/assets/90097022/16a86446-9bed-45fc-8932-1110347ee3c3)
![image](https://github.com/Egorech/StockKeeperApp/assets/90097022/257ca8bb-873e-4b58-936e-c014e775c18f)
![image](https://github.com/Egorech/StockKeeperApp/assets/90097022/a0a0fc7c-cbca-4cfc-83b8-6fd2b3aebed4)



1) Таблица User хранит информацию о никнейме, пароле, имени, фамилии, почте.
2) Таблица StorageLocation хранит информацию о имени и максимальном весе хранилища
3) Таблица Product хранит информацию о название продукта.
4) Таблица Shelf хранит информацию о текущем количество товара на полке и использует два внешних ключа с связью один ко многим: StorageLocation и Product.
5) Таблица InventoryManagementTask хранит информацию о статусе задачи и результате, и также использует связь один ко многим с User, так как один пользователь может иметь много задач.

Для запуска проекта нужно будет сделать следующие действия:
1) git clone https://github.com/Egorech/StockKeeperApp.git
2) docker compose build
3) docker compose up
4) python manage.py migrate
5) http://localhost:8000/

<strong>(Важно отметить, что для корректной работы с Docker нужен запущенный docker engine, в качестве решения можете скачать Docker Desktop по ссылке: https://www.docker.com/products/docker-desktop/)</strong>
