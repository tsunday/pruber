FROM python:3.8-alpine
RUN pip install --upgrade pip
RUN pip install pipenv

WORKDIR /code
COPY Pipfile.lock .
COPY Pipfile .
RUN pipenv install --system --deploy --dev --ignore-pipfile
COPY . .

CMD ./run.sh