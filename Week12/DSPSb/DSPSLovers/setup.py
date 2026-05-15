from setuptools import setup, find_packages
setup(name = "DSPSLovers",
      version = "1.0",
      description= "Our very first package :)",
      author= "Anthony",
      licence= "MIT",
      packages= find_packages(include=["mypackage"]),
      install_requires= ["requests", "playsound"]
) 
#if you dont need to install anything, leave the list blank