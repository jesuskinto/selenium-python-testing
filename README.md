# Python Testing with Selenium + Framework Design
This documentation is based on the course by Rahul Shetty (https://parso.udemy.com/course/learn-selenium-automation-in-easy-python-language)


why Python for Automation testing?
* It is easy to learn and understand, simpler to code.
* World is moving towards Artificial Intelligence with Machine Learning, and Python plays.
* More Jobs, Less competition

## Glance on Selenium Features
**Selenium Features**

* Selenium is open Source Automation Testing tool
* It is exclusively for Web Based applications.
* Selenium supports multiple browsers - Chrome, Firefox, Internet Explorer, Safari
* Selenium works with Multiple Platforms Windows, Apple OS X, Linux
* Selenium can be coded in multiple languages - Java, C#, Python, Javascript, Python, php,Ruby

## Installation steps

1. Install Python3

        https://www.python.org/downloads/

2. After installation run
        
        $ python3

    You should get an output similar to

        Python 3.x.x (default, Jan 26 2021, 15:33:00) 
        [GCC 8.4.0] on linux
        Type "help", "copyright", "credits" or "license" for more information.

    Run

        $ pip3

    You should get an output similar to

        Usage:
        pip <command> [options]
        ...


3. Install Selenium by Python with pip

    > **What is PIP:** PIP is the standard package manager for Python, It allows you install and manage additional packages that are not part of the Python standard library.


        $ pip3 install selenium

    > The optional –U flag will upgrade the existing version of the installed package `pip install -U selenium`

    You should get an output similar to **..Successfully installed**

4. Install PyTest with pip

        $ pip3 install pytest


    You should get an output similar to **..Successfully installed**


5. Install Pytest html with pip

        $ pip3 install pytest-html


    You should get an output similar to **..Successfully installed**


6. Install ChromeDriver

    Go: https://chromedriver.chromium.org/downloads and download the version of Chrome driver compatible with your Chrome version.

    Extract the downloaded file and save in `drivers/` folder


## Run Test
    
    You can run the demo tests for Selenium Easy (https://www.seleniumeasy.com/test/) with:
    
        $ py.test -v -s --html=report.html