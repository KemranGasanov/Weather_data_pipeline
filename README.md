# Weather Data Pipeline

## Описание проекта
**Weather Data Pipeline** – это ETL-пайплайн для сбора, обработки и хранения погодных данных по городам. Он предназначен для автоматизированного получения текущей и исторической информации о погоде из API и загрузки её в базу данных для дальнейшего анализа.

## Функциональность
- Извлечение погодных данных из **OpenWeather API**.
- Обработка и очистка данных.
- Загрузка данных в **PostgreSQL**.
- Поддержка текущих и исторических погодных данных.
- Обновление локального списка городов и погодных условий.


![picture.jpg](docs/picture.jpg)

## Структура проекта
```
Weather_data_pipeline/
├── config/                    # Конфигурационные файлы
│   ├── sqlalchemy_config.py    # Настройки подключения к БД
├── data/                       # Данные
│   ├── city_id.csv             # Локальный список городов
│   ├── weather_list.py         # Справочник погодных условий
│   ├── countries.py            # Список стран и городов с координатами
├── etl/                        # ETL процессы
│   ├── extract_data_request.py # Извлечение данных из API
│   ├── update_tables.py        # Обновление таблиц в БД
├── scripts/                    # Служебные скрипты
│   ├── init_db.py              # Инициализация базы данных (если нужно)
├── docs/                       # Документация
│   ├── Weather_gathering_pipeline.html # Диаграмма архитектуры
├── main.py                     # Точка входа для запуска ETL
├── requirements.txt             # Зависимости
├── README.md                    # Описание проекта
```

## Используемые технологии
- **Python 3**
- **SQLAlchemy** – ORM для работы с БД.
- **PostgreSQL** – хранилище данных.
- **Requests** – для работы с API.
- **pandas** – для обработки данных.
- **Dotenv** – загрузка переменных окружения.

## Установка
1. Клонировать репозиторий:
   ```bash
   git clone https://github.com/your-repo/weather_data_pipeline.git
   ```
2. Перейти в директорию проекта:
   ```bash
   cd weather_data_pipeline
   ```
3. Установить зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Создать `.env` файл с параметрами подключения к БД и API:
   ```
   DB_URL=postgresql://user:password@localhost:5432/weather_db
   OPEN_WEATHER_KEY=your_api_key
   ```

## Запуск
Для запуска ETL процесса выполните:
```bash
python main.py
```

## Дополнительные команды
- **Обновление списка городов:** `update_local_city_data()` (в `etl/update_tables.py`)
- **Загрузка новых погодных условий:** `load_new_weather(weather_list)` (в `etl/update_tables.py`)

## Авторы
**Ваше имя** – разработчик проекта.

## Лицензия
Этот проект распространяется под MIT License.

