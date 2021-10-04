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

and Voilà... 🚀


# Recipe
> For more documentation on selenium-python see: https://selenium-python.readthedocs.io/


## Common Browser Methods
* driver.get("https://...")
* driver.minimize_window()
* driver.maximize_window()
* driver.back()
* driver.refresh()
* driver.close()
* driver.get_screenshot_as_file("screen.png")


## Chrome Options

```python
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=800,600")
driver = webdriver.Chrome(executable_path="<PATH>", options=chrome_options)
```

> For more documentation on chrome options see: https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions

## Select
Example html file
```html
<select id="cars">
  <option value="volvo">Volvo</option>
  <option value="saab">Saab</option>
  <option value="mercedes">Mercedes</option>
  <option value="audi">Audi</option>
</select>
```
Example python file
```python
el = driver.find_element_by_id("cars")
dropdown = Select(el)

dropdown.select_by_visible_text("Volvo")
# or dropdown.select_by_index(0)
# or dropdown.select_by_value("volvo")
```

## Input

Example html file
```html
<form action="/action_page.php">
  <label for="name">First name:</label>
  <input type="text" id="name" name="name">
  <label for="password">Last name:</label>
  <input type="password" id="password" name="password">
  <input type="submit" value="Submit" id="submit">
</form>
```

Example python file
```python
driver.find_element_by_id("name").send_keys("pedro")
driver.find_element_by_id("password").send_keys("secret")
driver.find_element_by_id("submit").click()
```

## Radio
Example html file
```html
<form action="/action_page.php">
  <p>Please select your favorite Web language:</p>
  <input type="radio" id="ruby" name="fav_language" value="Ruby">
  <label for="ruby">Ruby</label>
  <input type="radio" id="javascript" name="fav_language" value="JavaScript">
  <label for="javascript">JavaScript</label>
</form>
```

Example python file
```python
radio_buttons = driver.find_elements_by_name("fav_language")
radio_buttons[1].click()
assert radio_buttons[1].is_selected()
```

## Checkbox
Example html file
```html
<form action="/action_page.php">
  <input type="checkbox" id="vehicle1" name="vehicle1" value="Bike">
  <label for="vehicle1"> I have a bike</label><br>
  <input type="checkbox" id="vehicle2" name="vehicle2" value="Car">
  <label for="vehicle2"> I have a car</label><br>
  <input type="checkbox" id="vehicle3" name="vehicle3" value="Boat">
  <label for="vehicle3"> I have a boat</label><br><br>
  <input type="submit" value="Submit">
</form>
```


Example python file
```python
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "Boat":
        checkbox.click()
        assert checkbox.is_selected()
```

## Hover / Double click /  Context
Example html file
```html
<button id="action-button">Action button</button>
```


Example python file
```python
...
from selenium.webdriver import ActionChains

action = ActionChains(driver)
action.move_to_element(driver.find_element_by_id("action-button")).perform()
action.context_click(driver.find_element_by_id("action-button")).perform()
action.double_click(driver.find_element_by_id("action-button")).perform()
```

## Implicitly wait

The Implicit Wait in Selenium is used to tell the web driver to wait for a certain amount of time before it throws a “No Such Element Exception”

```python
driver.implicitly_wait(5) # wait 5 seconds
```


## Explicit wait

By using the Explicit Wait command, the WebDriver is directed to wait until a certain condition occurs before proceeding with executing the code.
 
Setting Explicit Wait is important in cases where there are certain elements that naturally take more time to load. If one sets an implicit wait command, then the browser will wait for the same time frame before loading every web element. This causes an unnecessary delay in executing the test script.

Explicit wait is more intelligent, but can only be applied for specified elements. However, it is an improvement on implicit wait since it allows the program to pause for dynamically loaded Ajax elements.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

wait = WebDriverWait(driver, 8)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"promoInfo")))
driver.find_element_by_css_selector("promoInfo").text
```

## Switch Alert
```python
obj = driver.switch_to.alert
message=obj.text
```

## Switch tab
Allows you to go to the parent tab or the child tabs of a window.

```python
driver.switch_to.window(driver.window_handle([0])) # parent
driver.switch_to.window(driver.window_handle([1])) # first child
driver.switch_to.window(driver.window_handle([2])) # second child
driver.switch_to.window(driver.window_handle([3])) # Third child
```

## Switch to iframe
Allows you to go to the iframe.

```python
driver.switch_to.frame("id_iframe") #use id or name or index value
```   

Go back
```python
driver.switch_to.default_content()
```   

## Javascript
Js DOM can access any elements on web page just like how selenium does, selenium have a method to execute javascript code in it


```python
driver.execute_script('<JAVASCRIPT_CODE>')
#or
el = driver.find_element_by_id("cars")
driver.execute_script('<JAVASCRIPT_CODE>', el)
```

## Page Object Model and Page Factory in Selenium
Page Object Model, also known as POM, is a design pattern in Selenium that creates an object repository for storing all web elements. It is useful in reducing code duplication and improves test case maintenance.

More: 
https://www.browserstack.com/guide/page-object-model-in-selenium