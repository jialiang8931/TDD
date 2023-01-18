FROM jialiang8931/python-common
COPY . /app
WORKDIR /app
CMD ["python", "py/test_money.py"]