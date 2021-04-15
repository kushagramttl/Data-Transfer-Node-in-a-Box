FROM python:3

WORKDIR /usr/src/code

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN curl https://rclone.org/install.sh | bash

COPY . .


CMD [ "bash", "-c", "python ./main.py && rclone rcd --rc-no-auth" ]