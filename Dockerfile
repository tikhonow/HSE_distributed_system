FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/
RUN apt-get update && apt-get install -y netcat-openbsd && apt-get install -y nano && apt-get clean


RUN pip install --no-cache-dir -r requirements.txt

COPY 2_task /app/

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

CMD ["python", "-c", "import os; os.system('python number_processor/manage.py migrate'); os.system('python number_processor/manage.py runserver 0.0.0.0:8000')"]
