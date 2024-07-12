#use python official image
FROM python:3.9-slim
#set the working directory
WORKDIR /app
#copy the cureent directory
COPY  . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python","src/main.py"]