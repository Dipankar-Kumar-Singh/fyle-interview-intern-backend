FROM python:3.8
EXPOSE 7755
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD [ "bash" , "run.sh" ]