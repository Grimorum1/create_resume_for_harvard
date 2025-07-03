# create_resume_for_harward
Помогает создать pdf файл с резюме в стиле Harward
для заполнения данными зайдите в `src/main.py` и начните редактировать информацию о себе начиная со строки `81`
как только заполните можно запустить проект через Docker.

```bash
docker compose up --build
```

готовый pdf файл будет находиться в папку `volumes`

Если слишком часто создавали pdf стоит почистить docker system

```bash
docker system prune
```