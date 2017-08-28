FROM python:3.6.1
#FROM continuumio/miniconda3
# Create the working directory
RUN mkdir -p /usr/src/app/web
WORKDIR /usr/src/app/web

# Install the package dependencies (this step is separated
# from copying all the source code to avoid having to
# re-install all python packages defined in requirements.txt
# whenever any source code change is made)
#RUN conda install pip
#RUN conda install numba
#RUN conda install -c conda-forge flask=0.12
#RUN conda install -c conda-forge elasticsearch=5.4.0
#RUN conda install -c conda-forge elasticsearch-dsl=5.3.0

COPY requirements.txt /usr/src/app/web
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code into the container
COPY . /usr/src/app/web
CMD ["python", "/usr/src/app/web/restapi/refresh_data.py"]

