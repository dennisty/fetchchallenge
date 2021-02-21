# Prerequisites
1. Install [Google Chrome](https://www.google.com/chrome/)
2. Download [Chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) and [add it to your PATH](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/#adding-executables-to-your-path)
3. Install [Python 3](https://www.python.org/downloads/)
4. Install [PIP](https://pip.pypa.io/en/stable/installing/#installing-with-get-pip-py)

# Project Setup
1. Open terminal, navigate to the desired project directory, and clone the repo with the following command:
```
git clone https://github.com/dennisty/fetchchallenge.git
```
2. Create a virtual environment
```
python3 -m venv fetchenv
```
3. Activate the virtual environment
```
source fetchenv/bin/activate
```
4. Install the required PIP modules
```
pip install -r requirements.txt
```

# Run Project

Run the fake gold bar algorithm
```
python -m unittest test_fetchchallenge.py
```
Example output:
```
Fake bar = 0
Weighed 2 times
Weigh list:
[0,1,2] < [3,4,5]
[0] < [1]
Alert message: Yay! You find it!
```

