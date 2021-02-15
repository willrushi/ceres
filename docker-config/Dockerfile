FROM ubuntu:20.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    openssh-server

RUN service ssh start
RUN echo "root:toor" | chpasswd
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config

COPY shared/ /root/shared/
WORKDIR /root/

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
