FROM python:3.12
# NAME "phishshield-python-app"
WORKDIR /usr/src/app
ADD . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "main.py"]