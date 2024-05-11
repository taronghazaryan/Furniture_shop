FROM python

ENV PYTHONUNBUFFERED 1

COPY . /app/

WORKDIR /app

RUN apt-get update && apt-get install -y gettext

RUN pip install -r requirements.txt

#RUN pip install --no-cache-dir -r requirements.txt

#RUN test -f /app/furniture_shop_project/db.sqlite3 && chmod 777 /app/furniture_shop_project/db.sqlite3 || true


#RUN python /app/newsite/manage.py collectstatic --noinput
