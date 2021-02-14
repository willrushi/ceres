from setuptools import setup

def readme():
    with open("README.md") as readme:
        return readme.read()

setup(
    name="ceres",
    description="A wrapper for the Ceres docker image, used as a penetration testing environment.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: Linux"
    ]
)