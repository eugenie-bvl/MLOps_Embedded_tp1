FROM python:3.12

COPY ./requirements.txt /requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /requirements.txt

COPY ./regression.joblib /regression.joblib
COPY ./create_api.py /create_api.py


CMD ["fastapi", "run", "create_api.py", "--port", "8023"]