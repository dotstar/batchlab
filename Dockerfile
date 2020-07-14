FROM python:latest
WORKDIR /app
COPY matrixmath.py /app
COPY requirements.txt ./
# See this for space optimization recommendations
# https://towardsdatascience.com/how-to-shrink-numpy-scipy-pandas-and-matplotlib-for-your-data-product-4ec8d7e86ee4
RUN pip install -r requirements.txt --no-cache-dir --compile 
CMD ["python","matrixmath.py"]