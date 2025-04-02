from setuptools import setup, find_packages

setup(
    name="vezor",
    version="1.0.2",
    packages=find_packages(),
    install_requires=[],  
    author="Izzar Suly Nashrudin",
    author_email="Izzarsuly@proton.me",
    description="A collection of algorithm designs for easy application to assist mathematical problems.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/avezoor/vezor",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Unix",
        "Framework :: Jupyter"
    ],
    python_requires='>=3.6',
)
