FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /workspace

RUN cp /etc/apt/sources.list /etc/apt/sources.list.bak
RUN echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster main contrib non-free" > /etc/apt/sources.list
RUN echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-updates main contrib non-free" >> /etc/apt/sources.list
RUN echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-backports main contrib non-free" >> /etc/apt/sources.list
RUN echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian-security buster/updates main contrib non-free" >> /etc/apt/sources.list

RUN apt-get update
RUN apt install -y gcc gettext python-dev
RUN apt-get -y install vim
# RUN rm -rf /var/lib/apt/lists/*

RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo Asia/Shanghai > /etc/timezone

COPY requirements.txt /workspace/requirements.txt
# RUN pip install -r requirements.txt
RUN pip install -r requirements.txt -i https://pypi.doubanio.com/simple
#RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . /workspace

EXPOSE 8080
#VOLUME /workspace/static
#VOLUME /workspace/data

CMD python easyapp.py

