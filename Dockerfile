FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install Flask pymongo
EXPOSE 5000
CMD ["python", "app_simple.py"]

