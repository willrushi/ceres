FROM ubuntu:20.04

# Connect to kali repository
RUN apt-get update && apt-get install -y wget gpg
RUN wget -q -O - https://archive.kali.org/archive-key.asc | apt-key add
RUN echo "deb http://http.kali.org/kali kali-rolling main non-free contrib" >> /etc/apt/sources.list
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y kali-linux-core --no-install-recommends

# Install dependencies
RUN apt-get update && apt-get install -y \
    openssh-server

RUN service ssh start
RUN echo "root:toor" | chpasswd
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config

WORKDIR /root

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]