# Version 10 Dockerfile
FROM python:3.7.9
COPY ./templates /deploy/templates/
COPY ./static /deploy/static/
COPY ./main.py /deploy/
COPY ./requirements.txt /deploy/
COPY ./MedCostModel.pkl /deploy/
COPY ./MedCosts.csv /deploy/
WORKDIR /deploy/
RUN pip install -r requirements.txt
EXPOSE 80 
ENTRYPOINT ["python3", "main.py"]
