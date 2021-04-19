FROM python:3.7.9
COPY ./main.py /deploy/
COPY ./requirements.txt /deploy/
COPY ./MedCostModel.pkl /deploy/
WORKDIR /deploy/
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["python", "main.py"]