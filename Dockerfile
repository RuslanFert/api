# Базовый образ
FROM python:3.10
LABEL author="Rinat"
# Задаем рабочую дерикторию
WORKDIR app
# Копируем файлы
COPY app .

EXPOSE 8844

# Команда выполняемая при запуске контейнера,
# выбрав ENTRYPOINT мы блокируем возможность замены выполняемой команды
ENTRYPOINT ["python", "main.py"]

