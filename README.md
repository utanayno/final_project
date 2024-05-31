# final_project

## Шаблон для автоматизации тестирования на python

### Шаги:
1. Склонировать проект `git clone https://github.com/utanayno/final_project.git`
2. Установить все зависимости
3. Запустить тесты `pytest`
4. Сгенерировать отчет `allure generate allure-files -o allure-report`
5. Открыть отчет `allure open allure-report`

### Стек:
- pytest
- selenium
- requests
- allure
- config

### Структура:
- ./test - тесты
- ./page - описание страниц
- ./api - хелперы для работы с API
- ./db - хелперы для работы с БД
- ./configuration - провайдер настроек
    test_config.ini - настройки для тестов
- ./testdata - провайдер тестовых данных
    test_data.json


### Полезные ссылки:
- [Подсказка по markdown](https://www.markdownguide.org/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore/)

### Библиотеки:
- pip install pytest
- pip install Selenium
- pip install webdriver-manager
- pip install allure-pytest
- pip install requests