import os

def write_dockerfile():
    dockerfile = """
        FROM kalilinux/kali-rolling

        RUN apt-get update -y
        RUN DEBIAN_FRONTEND=noninteractive apt-get install -y kali-linux-core --no-install-recommends

        # Install dependencies
        RUN apt-get update && apt-get install -y \
            openssh-server

        RUN service ssh start
        RUN echo "root:toor" | chpasswd
        RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config

        WORKDIR /root

        EXPOSE 22
        CMD ["/usr/sbin/sshd", "-D"]
    """

    if input("Use extended kali tools list?").lower() == "y":
        dockerfile = dockerfile.replace("kali-linux-core", "kali-linux-core kali-tools-top10")

    with open(os.path.expanduser("~/.ceres/Dockerfile"),"w") as f:
        f.write(dockerfile)
        print("Written Dockerfile")

if __name__ == "__main__":
    write_dockerfile()
