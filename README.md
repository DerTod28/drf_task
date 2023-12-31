# drf_task
API для представления структуры компании

## Инструция по запуску

### 1. Generate .env

```shell
cat deploy/docker/.env.example > deploy/docker/.env
```

Makefile

```shell
make env-gen
```

### 2. Build and run docker-compose.yml

```shell
docker-compose -f docker-compose.yml --env-file deploy/docker/.env build
```

Makefile
```shell
make build
```

### 3. Collectstatic

```shell
docker exec drf_task-django-1 python manage.py collectstatic --noinput
```

Makefile
```shell
make collectstatic
```


### 4. Migrate

```shell
docker exec drf_task-django-1 python manage.py migrate
```

Makefile
```shell
make migrate
```

### 5. Createsuperuser

```shell
docker exec drf_task-django-1 python manage.py createsuperuser --no-input
```

Makefile
```shell
make createsuperuser
```

### Полезные команды

Stop docker-compose.yml

```shell
make down
```

run tests

```shell
make tests
```

После загрузки статики доступна страница swagger:
http://localhost/api/schema/swagger-ui/


## Работа с админкой
Cозданы 2 таблицы: Employee - для сотрудников и  Department - для отделов

После создания superuser можно зайти в панель администратора и добавить данные 
1. Добавить отдел без указания директора
2. Добавить работника/директора отдела
3. Выбрать в отделе директора (список отфильтрован - показываются только директора)


Что достигнуто?
- обеспечена уникальности связки “сотрудник-департамент”.
- оптимизирован запрос поиска по фамилии сотрудника (ФИО)
- API методы для работы с данными по сотрудникам и департаментам
- для получения списка департаментов (включает искусственное поле с числом сотрудников + поле с суммарным окладам по всем сотрудникам
- swagger документация по API методам
- админка по модели данных
- тесты
- пагинация для списка сотрудников
- доступ к списку сотрудников для авторизованных пользователей

Что можно было бы улучшить?
- Вынести отдельно ФИО и разделить на фамилию/имя/отчество с улучшением поисковых фильтров
- Вынести отдельно директоров, что не было было связки OneToOne - FK (текущая реализацию сделана для упрощения)
- Продумать тщательнее тесты 
- Обработка ошибок