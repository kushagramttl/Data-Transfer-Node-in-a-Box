FROM alpine:latest

RUN apk update

RUN apk upgrade

RUN apk add curl

RUN apk add bash

RUN apk add --no-cache unzip

RUN curl https://rclone.org/install.sh | bash

RUN rclone config create dummy s3 env_auth true access_key_id key secret_access_key secret region us-east-1 endpoint localhost

RUN mkdir root/data

EXPOSE 5572

COPY startup.sh startup.sh

CMD ["./startup.sh"]