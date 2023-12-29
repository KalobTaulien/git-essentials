FROM ubuntu:18.04

RUN apt update
RUN apt install vim nano git -y
ENV TERM=xterm-256color
CMD ["bash", "-l"]
