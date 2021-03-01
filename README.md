![logo](logo-wide.png)

Ceres is a package containing a Docker image with a Python-based wrapper. The image itself is intended to be used as a penetration testing or CTF environment, similar to a Kali Linux VM - as such, it includes relevant tools from the Kali repository, as well as functionality for connecting to VPNs. The wrapper gives an easy interface for interacting with the container (such as stopping, starting, and checking statistics), as well as providing some extra functionality like taking snapshots of the shared folder.

# Installation
These installation instructions assume that you are running Ubuntu, or a similar Debian-based Linux distro.


## Docker
Docker must be installed to use the image. Instructions can be found [here](https://docs.docker.com/engine/install/ubuntu/), or follow the steps below.

First, install the following packages with apt:
```bash
sudo apt-get update

sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
```

Next, add the Docker GPG key:
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

Add the Docker repository to apt:
```bash
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```

Finally, install Docker through apt:
```bash
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

## Docker Compose
Docker Compose must also be installed if using the Python wrapper. Instructions found [here](https://docs.docker.com/compose/install/), or follow below.

Get the most recent version of Docker Compose with curl:
```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.28.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

Apply executable permissions:
```bash
sudo chmod +x /usr/local/bin/docker-compose
```

If `/usr/local/bin` is not in your path, create a symlink:
```bash
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```

## Ceres
First clone this repo locally:
```bash
git clone https://github.com/willrushi/ceres.git
```

Change directories in to the Python library dir and install the required libraries using pip:
```bash
cd ceres
pip3 install -r requirements.txt
```

Install the library:
```bash
sudo python3 setup.py install
```
Ceres should now be installed on your machine and can be accessed using `ceres [command]`.

# Feedback
You can leave your feedback using the google form found [here](https://forms.gle/2Z3q7KE86EuCLVDq8).