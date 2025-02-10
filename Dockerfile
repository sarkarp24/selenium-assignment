FROM python:3.9-slim-buster


ARG srcDir=src
WORKDIR /app
COPY $srcDir/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY $srcDir/facebook-login.py .

CMD ["python", "fcebook-login.py"]