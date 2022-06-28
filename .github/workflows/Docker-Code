FROM ubuntu:20.04

WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app
# Time Zone
ENV TZ=Asia/Kolkata
RUN ln -snf "/usr/share/zoneinfo/$TZ" /etc/localtime
RUN echo "$TZ" > /etc/timezone

RUN apt-get update
RUN apt-get install -y tzdata
RUN apt-get -qq update
RUN apt install unzip -y
RUN apt-get -qq install -y git python3 python3-pip \
    locales python3-lxml aria2 \
    curl pv jq nginx npm

# gclone v1.58.1-mango
RUN aria2c https://github.com/l3v11/gclone/releases/download/v1.58.1-mango/gclone-v1.58.1-mango-linux-amd64.zip && \
    unzip gclone-v1.58.1-mango-linux-amd64.zip && mv gclone-v1.58.1-mango-linux-amd64/gclone /usr/bin/ && \
    chmod +x /usr/bin/gclone && rm -r gclone-v1.58.1-mango-linux-amd64

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt && \
    apt-get -qq purge git

COPY . .

RUN chmod +x run.sh

CMD ["bash","run.sh"]
