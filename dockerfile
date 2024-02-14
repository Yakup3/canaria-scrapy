FROM python:3.8-slim

WORKDIR /jobs_project

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY jobs_project /jobs_project

COPY wait-for-it.sh /usr/local/bin/wait-for-it
RUN chmod +x /usr/local/bin/wait-for-it

CMD ["wait-for-it", "postgres:54321", "--", "scrapy", "crawl", "job_spider"]
