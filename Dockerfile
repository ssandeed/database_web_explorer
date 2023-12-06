FROM python:3.8.2

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./src /app/src

COPY ./app/streamlit_app.py .

EXPOSE 8501

CMD ["streamlit", "run", "streamlit_app.py"]