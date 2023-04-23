from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="NotifyUI",
    version="0.0.2",
    packages=find_packages(),
    url="https://github.com/chetan0402/NotifyUI",
    license="CC BY 4.0",
    author="Chetan0402",
    description="Python Notification library integrated with PyQt6",
    long_description=long_description,
    long_description_content_type="text/markdown",
    requires=["PyQt6"],
    install_requires=["PyQt6"],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
