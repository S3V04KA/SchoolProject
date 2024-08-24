  
FROM python:3.12.5

RUN mkdir /template
WORKDIR /template

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .