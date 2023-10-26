FROM python:3.11.6-alpine3.18
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
#ENTRYPOINT ["python",  "getgistflask.py"]
#CMD ["cmd", "start"]
ENTRYPOINT ["/bin/sh",  "/app/case.sh", "start"]