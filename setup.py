import setuptools

def readme():
    with open("README.md") as readme:
        return readme.read()

setuptools.setup(
    name="ceres",
    description="A wrapper for the Ceres docker image, used as a penetration testing environment.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: Linux"
    ],
    url="https://github.com/willrushi/ceres",
    author="William Roberts",
    author_email="willprobertss@gmail.com",
    keywords="python docker ctf pentest",
    license="MIT",
    packages=setuptools.find_packages(),
    install_requires=[],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'ceres = ceres.__main__:main'
        ]
    }
)