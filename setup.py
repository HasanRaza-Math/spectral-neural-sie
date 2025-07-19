from setuptools import setup, find_packages

setup(
    name="spectral-neural-sie",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "torch==2.2.1",
        "numpy==1.26.4",
    ],
    python_requires=">=3.10",
)
