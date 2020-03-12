from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mypackage", # Replace with your own username
    version="0.0.1",
    author="Lucia Ronchi Darre",
    author_email="lronchi@uchicago.edu",
    description="MSCA Class",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LUCIA-RONCHI/Python_Assignment3",
    packages=find_packages(exclude=["*test*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

# Without __init__.py the folder is just a folder
# run from terminal python3 setup.py install
