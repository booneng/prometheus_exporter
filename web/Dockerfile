FROM python:3.6.1
RUN mkdir -p /usr/src/app/web
WORKDIR /usr/src/app/web

COPY requirements.txt /usr/src/app/web
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code into the container
COPY . /usr/src/app/web
CMD ["python", "restapi/refresh_data.py"]

