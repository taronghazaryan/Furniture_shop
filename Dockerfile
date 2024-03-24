FROM python

ENV PYTHONUNBUFFERED 1

COPY . /app/

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

#RUN test -f /app/furniture_shop_project/db.sqlite3 && chmod 777 /app/furniture_shop_project/db.sqlite3 || true

RUN python /app/newsite/manage.py migrate
#RUN python /app/newsite/manage.py collectstatic --noinput

EXPOSE 8002

CMD ["python", "/app/newsite/manage.py", "runserver"]