import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "analyzer",
    version = "0.1.0",
    author = "Khushiyant",
    author_email = "khushiyant2002@gmail.com",
    description = ("A Content analyzer which can find gramitical errors, and spelling misakes"),
    license = "",
    keywords = "opencv ml",
    long_description=read('README.md')    
)