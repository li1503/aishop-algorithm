### 1. Get Linux
FROM alpine:3.7

### 2. Get Java via the package manager
RUN apk update \
&& apk upgrade \
&& apk add --no-cache bash \
&& apk add --no-cache --virtual=build-dependencies unzip \
&& apk add --no-cache curl \
&& apk add --no-cache openjdk8-jre

### 3. Get Python, PIP

RUN apk add --no-cache python3 \
&& python3 -m ensurepip \
&& pip3 install --upgrade pip setuptools \
&& rm -r /usr/lib/python*/ensurepip && \
if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
rm -r /root/.cache

####
#### OPTIONAL : 4. SET JAVA_HOME environment variable, uncomment the line below if you need it

ENV JAVA_HOME="/usr/lib/jvm/java-1.8-openjdk"

# copy the content of the local src directory to the working directory
COPY . /code

# set the working directory in the container
WORKDIR /code

# install dependencies
RUN pip install -r requirements.txt

# run virtual env
CMD ["source", "/code/venv/Scripts/activate"]

# command to run on container start
CMD ["python", "__init__.py"]

