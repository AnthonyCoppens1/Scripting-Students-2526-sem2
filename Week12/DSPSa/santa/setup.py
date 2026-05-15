from setuptools import setup, find_packages

setup (name="santa",
       version="6.7",
       description="Joseph picked it because he loves or hates Christmas.",
       author="Santa's little helper - Anthony",
       license= "MIT",
       packages= find_packages(include=['MissSanta']),
       install_requires= ['requests', 'beautifulsoup4', 'playsound']
)