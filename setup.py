from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="poetic_errors",
    version="0.1.3",
    author="Jugal Kothari",
    author_email="jugalprakashk19@gmail.com",
    description="Transform Python errors into delightful poems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JugalKothari/poetic-errors",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)