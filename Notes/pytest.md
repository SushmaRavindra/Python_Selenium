### What is Unit Testing
* A unit test is a way of testing a unit - the smallest piece of code that can be logically isolated in a system. In most programming languages, that is a function, a subroutine, a method or property.

### What Do Unit Tests Look Like?
* A unit can be almost anything you want it to be -- a line of code, a method, or a class. Generally though, smaller is better.
* Smaller tests give you a much more granular view of how your code is performing.
* There is also the practical aspect that when you test very small units, your tests can be run fast; like a thousand tests in a second fast.

### Who Should Create The Unit Tests?
* The programmer that wrote the code will likely know how to access the parts that can be tested easily and how to mock objects that can't be accessed otherwise.

### What is pytest
* The pytest framework makes it easy to write small tests using Python.

### Advantages of pytest
* Very easy to start with because of its simple and easy syntax.
* Can run tests in parallel.
* Can run a specific test or a subset of tests.
* Dependency test.
* Grouping of test methods.
* Generates report.

### Install pytest
```python
pip3 install pytest
```

### Check the version of pytest
```python
pytest --version
```

### Conventions for Python test discovery
**pytest implements the following standard test discovery:**

* The module name should either start with test_* or *_test.
* All the classes inside the module should start from Test* (without an __init__ method)
* All the test methods should start from test_*.

**If we don't follow the above naming conventions, then pytest will not pick up tests from the python file/module.**

### library/utility.py module
```python
def int_add(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('Only ints allowed')
    return a + b
```

**Writing unittests to test the above function**
```python
from pytest import raises

def test_valid_int():
    assert int_add(1, 2) == 3

def test_invalid_data(1, 1.2):
    with raises(TypeError):
        int_add(a, b)
```

**Parameterizing the tests**
```python
from pytest import mark
from pytest import raises

valid_data = [(1, 2, 3), (10, 20, 30)]
invalid_data = [(1.2, 1), (1, 1.2), ('1', '2')]

@mark.parametrize("a, b, expected", valid_data)
def test_valid_int(a, b, expected):
    assert int_add(a, b) == expected

@mark.parametrize("a, b, expected", invalid_data)
def test_invalid_data(a, b, expected):
    with raises(TypeError):
        int_add(a, b)
```
Moving all the test methods into class definition
```python
class TestArithmetic:
    @mark.parametrize("a, b, expected", valid_data)
    def test_valid_int(self, a, b, expected):
        assert int_add(a, b) == expected

    @mark.parametrize("a, b, expected", invalid_data)
    def test_invalid_data(self, a, b, expected):
        with raises(expected):
            int_add(a, b)
```
### Multiple ways of executing test's
* Discovers all the python modules that starts from test_* or *_test in the current working directory and executes all the test methods inside the module.
```python
pytest 
```
* Executes all the test methods inside module test_utility.py (which is inside package test_library).
```python
pytest test_library/test_utility.py 
```
* Executes all the test methods inside module test_spam.py (which is inside package test_spam).
```python
pytest test_spam/test_spam.py
```
* Discovers all the python modules which starts from test_ or _test inside package test_library and executes all the test methods inside each module
```python
pytest test_library
```

* Executes the test method test_even present inside the class TestUtility (Executing a particular test method inside the class)
```python
pytest test_library/test_utility.py::TestUtility::test_valid_int
```
* Executes the test method test_spam present inside the module test_spam.py (Which is inside package test_spam)
```python
pytest test_spam/test_spam.py::test_spam
```
### pytest fixtures
* Pytest fixture is a callable (normally a function or a generator) decorated with inbuilt pytest decorator @fixture
* Fixtures are used for dependency injection or to pass the data to the test functions
* Fixtures are accessed by test functions through arguments.
* Fixtures are used to run a piece of code repeatedly before and/or after every test method/class/module/session based on the defined scope.

### Simple fixture that returns a string "hello world".
```python
from pytest import fixture
@fixture
def greet():
    return "hello world"
 
def test_greet(greet):
    assert "hello world" == greet
```

### Sample pytest fixture for launching browser and closing browser.
```python
from pytest import fixture
@fixture
def init():
    print('Launching Browser and Navigating to a URL')
    yield
    print('Closing Browser')
``` 
* The code before yield statement run's once before every test method and the code after yield statement run's once after the completion of every test method. 

### Passing fixture to each test method.
```python
class TestUtility:
    def test_even(self, init):
        assert is_even(10) == True

    def test_odd(self, init):
        assert is_even(9) == False

    def test_invalid_number(self, init):
        with pytest.raises(TypeError):
            is_even('10')

    def test_float(self, init):
        with pytest.raises(TypeError):
            is_even(1.2)

    def test_palindrome(self, init):
        assert is_palindrome('racecar') == True

    def test_not_palindrome(self, init):
        assert is_palindrome('hello') == False
```
**Executing the above pytest would produce the below output**
```python
sandeep@Sandeeps-MacBook-Pro test_library % pytest -vs test_utility.py
=========================================================== test session starts ===========================================================
platform darwin -- Python 3.8.3, pytest-6.1.0, py-1.9.0, pluggy-0.13.1 -- /Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8
cachedir: .pytest_cache
metadata: {'Python': '3.8.3', 'Platform': 'macOS-10.15.6-x86_64-i386-64bit', 'Packages': {'pytest': '6.1.0', 'py': '1.9.0', 'pluggy': '0.13.1'}, 'Plugins': {'metadata': '1.10.0', 'html': '2.1.1', 'ordering': '0.6'}}
rootdir: /Users/sandeep/Documents/Pytesting/test_library
plugins: metadata-1.10.0, html-2.1.1, ordering-0.6
collected 6 items                                                                                                                         

test_utility.py::TestLibrary::test_even Launching Browser and Navigating to a URL
PASSEDClosing Browser

test_utility.py::TestLibrary::test_odd Launching Browser and Navigating to a URL
PASSEDClosing Browser

test_utility.py::TestLibrary::test_invalid_number Launching Browser and Navigating to a URL
PASSEDClosing Browser

test_utility.py::TestLibrary::test_float Launching Browser and Navigating to a URL
PASSEDClosing Browser

test_utility.py::TestLibrary::test_palindrome Launching Browser and Navigating to a URL
PASSEDClosing Browser

test_utility.py::TestLibrary::test_not_palindrome Launching Browser and Navigating to a URL
PASSEDClosing Browser
============================================================ 6 passed in 0.02s============================================================
```
### Passing fixture to all the test method's at once.
```python
@pytest.mark.usefixtures("init")
class TestUtility:
    def test_even(self):
        assert is_even(10) == True

    def test_odd(self):
        assert is_even(9) == False

    def test_invalid_number(self):
        with pytest.raises(TypeError):
            is_even('10')

    def test_float(self):
        with pytest.raises(TypeError):
            is_even(1.2)

    def test_palindrome(self):
        assert is_palindrome('racecar') == True

    def test_not_palindrome(self):
        assert is_palindrome('hello') == False
```
### Passing fixture to all the test method's with using pytest.mark.usefixtures().
* When keyword argument "autouse" is set to boolean True, the fixture is automatically applied to all the test methods and Test Classes
```python
@pytest.fixture(autouse=True)
def init():
    print('Launching Browser and Navigating to a URL')
    yield
    print('Closing Browser')
```
### Scoping of test fixtures.
**The statements before yield keyword runs once before every class and statements after yield keyword runs once after every class**
```python
@pytest.fixture(scope="class")
def init():
    print('Launching Browser and Navigating to a URL')
    yield
    print('Closing Browser')
``` 
**The statements before yield keyword runs once before every module and statements after yield keyword runs once after every module**
```python
@pytest.fixture(scope="module")
def init():
    print('Launching Browser and Navigating to a URL')
    yield
    print('Closing Browser')
``` 
**The statements before yield keyword runs once before every session and statements after yield keyword runs once after every session**
```python
@pytest.fixture(scope="session")
def init():
    print('Launching Browser and Navigating to a URL')
    yield
    print('Closing Browser')
``` 
**If no scope is mentioned in the fixture, the default scope is at method/function level. The statements before yield keyword runs once before every test method and statements after yield keyword runs once after test method**
```python
@pytest.fixture()
def init():
    print('Launching Browser and Navigating to a URL')
    yield
    print('Closing Browser')
``` 
### Grouping test's

```python
class TestUtility:
    @pytest.mark.smoke
    def test_even(self):
        assert is_even(10) == True
    
    @pytest.mark.smoke
    def test_odd(self):
        assert is_even(9) == False

    @pytest.mark.smoke
    def test_invalid_number(self):
        with pytest.raises(TypeError):
            is_even('10')
    
    @pytest.mark.smoke
    def test_float(self):
        with pytest.raises(TypeError):
            is_even(1.2)
    
    @pytest.mark.regression
    def test_palindrome(self):
        assert is_palindrome('racecar') == True

    @pytest.mark.regression
    def test_not_palindrome(self):
        assert is_palindrome('hello') == False
```
* Executing only those test's which are marked as smoke. **pytest test_utility.py -vs -m smoke**
```python
sandeep@Sandeeps-MacBook-Pro test_library % pytest test_utility.py -vs -m smoke
=========================================================== test session starts ===========================================================
platform darwin -- Python 3.8.3, pytest-6.1.0, py-1.9.0, pluggy-0.13.1 -- /Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8
cachedir: .pytest_cache
metadata: {'Python': '3.8.3', 'Platform': 'macOS-10.15.6-x86_64-i386-64bit', 'Packages': {'pytest': '6.1.0', 'py': '1.9.0', 'pluggy': '0.13.1'}, 'Plugins': {'metadata': '1.10.0', 'html': '2.1.1', 'ordering': '0.6'}}
rootdir: /Users/sandeep/Documents/Pytesting/test_library
plugins: metadata-1.10.0, html-2.1.1, ordering-0.6
collected 6 items / 3 deselected / 3 selected                                                                                             

test_utility.py::TestLibrary::test_even PASSED
test_utility.py::TestLibrary::test_odd PASSED
test_utility.py::TestLibrary::test_invalid_number PASSED
============================================================ warnings summary =============================================================
test_utility.py:24
  /Users/sandeep/Documents/Pytesting/test_library/test_utility.py:24: PytestUnknownMarkWarning: Unknown pytest.mark.smoke - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/mark.html
    @pytest.mark.smoke

test_utility.py:29
  /Users/sandeep/Documents/Pytesting/test_library/test_utility.py:29: PytestUnknownMarkWarning: Unknown pytest.mark.smoke - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/mark.html
    @pytest.mark.smoke

test_utility.py:34
  /Users/sandeep/Documents/Pytesting/test_library/test_utility.py:34: PytestUnknownMarkWarning: Unknown pytest.mark.smoke - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/mark.html
    @pytest.mark.smoke

-- Docs: https://docs.pytest.org/en/stable/warnings.html
=============================================== 3 passed, 3 deselected, 3 warnings in 0.02s ===============================================
```
* Executing only those test's which are marked as regression. **pytest test_utility.py -vs -m regression**
```python
sandeep@Sandeeps-MacBook-Pro test_library % pytest test_utility.py -vs -m regression
=========================================================== test session starts ===========================================================
platform darwin -- Python 3.8.3, pytest-6.1.0, py-1.9.0, pluggy-0.13.1 -- /Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8
cachedir: .pytest_cache
metadata: {'Python': '3.8.3', 'Platform': 'macOS-10.15.6-x86_64-i386-64bit', 'Packages': {'pytest': '6.1.0', 'py': '1.9.0', 'pluggy': '0.13.1'}, 'Plugins': {'metadata': '1.10.0', 'html': '2.1.1', 'ordering': '0.6'}}
rootdir: /Users/sandeep/Documents/Pytesting/test_library
plugins: metadata-1.10.0, html-2.1.1, ordering-0.6
collected 6 items / 4 deselected / 2 selected                                                                                             

test_utility.py::TestLibrary::test_palindrome PASSED
test_utility.py::TestLibrary::test_not_palindrome PASSED
============================================================ warnings summary =============================================================
test_utility.py:46
  /Users/sandeep/Documents/Pytesting/test_library/test_utility.py:46: PytestUnknownMarkWarning: Unknown pytest.mark.regression - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/mark.html
    @pytest.mark.regression

test_utility.py:51
  /Users/sandeep/Documents/Pytesting/test_library/test_utility.py:51: PytestUnknownMarkWarning: Unknown pytest.mark.regression - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/mark.html
    @pytest.mark.regression

-- Docs: https://docs.pytest.org/en/stable/warnings.html
=============================================== 2 passed, 4 deselected, 2 warnings in 0.02s ===============================================
```
### Ordering test's
* Normally all the test method's will run in the order in which the methods are defined inside a module/class. 
* But the order of test method execution can be changed.
* In-order to change the execution order, we need to install a plugin **pytest-ordering**
* The order number can be any positive value starting zero. But the number can not be negative.
```python
class TestLibrary:
    @pytest.mark.run(order=4)
    def test_even(self):
        print('Running test_even')
        assert is_even(10) == True

    @pytest.mark.run(order=3)
    def test_odd(self):
        print('Running test_odd')
        assert is_even(9) == False

    @pytest.mark.run(order=1)
    def test_invalid_number(self):
        print('Running test_invalid_number')
        with pytest.raises(TypeError):
            is_even('10')

    @pytest.mark.run(order=2)
    def test_float(self):
        print('Running test_float')
        with pytest.raises(TypeError):
            is_even(1.2)

    @pytest.mark.run(order=6)
    def test_palindrome(self):
        print('Running test_palindrome')
        assert is_palindrome('racecar') == True

    @pytest.mark.run(order=5)
    def test_not_palindrome(self):
        print('Running test_not_palindrome')
        assert is_palindrome('hello') == False
```
* Executing above test's would produce the below output.
```python
sandeep@Sandeeps-MacBook-Pro test_library % pytest test_utility.py -vs 
=========================================================== test session starts ===========================================================
platform darwin -- Python 3.8.3, pytest-6.1.0, py-1.9.0, pluggy-0.13.1 -- /Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8
cachedir: .pytest_cache
metadata: {'Python': '3.8.3', 'Platform': 'macOS-10.15.6-x86_64-i386-64bit', 'Packages': {'pytest': '6.1.0', 'py': '1.9.0', 'pluggy': '0.13.1'}, 'Plugins': {'metadata': '1.10.0', 'html': '2.1.1', 'ordering': '0.6'}}
rootdir: /Users/sandeep/Documents/Pytesting/test_library
plugins: metadata-1.10.0, html-2.1.1, ordering-0.6
collected 6 items                                                                                                                         

test_utility.py::TestLibrary::test_invalid_number Running test_invalid_number
PASSED

test_utility.py::TestLibrary::test_float Running test_float
PASSED

test_utility.py::TestLibrary::test_odd Running test_odd
PASSED

test_utility.py::TestLibrary::test_even Running test_even
PASSED

test_utility.py::TestLibrary::test_not_palindrome Running test_not_palindrome
PASSED

test_utility.py::TestLibrary::test_palindrome Running test_palindrome
PASSED
============================================================ 6 passed in 0.02s ===========================================================
```
### Managing Test Dependency
* In order make one test method to depend on the test result of another test method, we need to install a plugin **pytest-dependency**
* It allows to mark some tests as dependent from other tests. These tests will then be skipped if any of the dependencies did fail or has been skipped.
```python
class TestLogin:
    @pytest.mark.dependency()
    def test_login(self):
        print('Running test_login')
        assert False

    @pytest.mark.dependency(depends=["TestLogin::test_login"])
    def test_logout(self):
        print('Running test_logout')
```
* Both the tests are decorated with pytest.mark.dependency()
* This will cause the test results to be registered internally and thus other tests may depend on them.
* Running this test, we will get the following result:
```python
sandeep@Sandeeps-MacBook-Pro test_library % pytest -vs test_utility.py
============================= test session starts ==============================
platform darwin -- Python 3.8.3, pytest-6.1.0, py-1.9.0, pluggy-0.13.1 -- /Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8
cachedir: .pytest_cache
metadata: {'Python': '3.8.3', 'Platform': 'macOS-10.15.7-x86_64-i386-64bit', 'Packages': {'pytest': '6.1.0', 'py': '1.9.0', 'pluggy': '0.13.1'}, 'Plugins': {'metadata': '1.10.0', 'html': '2.1.1', 'ordering': '0.6', 'dependency': '0.5.1'}}
rootdir: /Users/sandeep/Documents/Pytesting/test_library
plugins: metadata-1.10.0, html-2.1.1, ordering-0.6, dependency-0.5.1
collected 2 items                                                              

test_utility.py::TestLogin::test_login Running test_login
FAILED
test_utility.py::TestLogin::test_logout SKIPPED
=================================== FAILURES ===================================
_____________________________ TestLogin.test_login _____________________________

self = <test_library.test_utility.TestLogin object at 0x7fd7ca241eb0>

    @pytest.mark.dependency()
    def test_login(self):
        print('Running test_login')
>       assert False
E       assert False

test_utility.py:10: AssertionError
=========================== short test summary info ============================
FAILED test_utility.py::TestLogin::test_login - assert False
========================= 1 failed, 1 skipped in 0.08s =========================
```
* In the above test, test_logout method has skipped because test_login method has failed.

### Running only failed tests
```python
pytest --last-failed --last-failed-no-failures none   # run no tests and exit
```
* If there are no failed test's in the previous run or if the lastfailed file is empty, then the above command does not run any of the test's.

### Generating HTML Report
* To Generate test results in html format, we need to install a plugin **pytest-html**
* While running the pytest from terminal, include the following in command line arguments.
```python
pytest --html="reports.html"
```
### Parametrizing test methods
* Every test method can be parameterised using parameterized fixture.
* Headers are passed as comma separated values and actual data is passed as list of tuples.

```python
@pytest.mark.usefixtures("init")
@pytest.mark.parametrize('username, password',[('u1', 'p1'), ('u2', 'p2')], scope="class")
class TestLogin:
    def test_admin(self, username, password):
        print('Entering ', username)
        print('Entering ', password)

    def test_user(self, username, password):
        print('Entering ', username)
        print('Entering ', password)
```
**Running above test will result in the following output.**

```python
sandeep@Sandeeps-MacBook-Pro test_library % pytest test_utility.py -vs
============================= test session starts ==============================
platform darwin -- Python 3.8.3, pytest-6.1.0, py-1.9.0, pluggy-0.13.1 -- /Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8
cachedir: .pytest_cache
metadata: {'Python': '3.8.3', 'Platform': 'macOS-10.15.6-x86_64-i386-64bit', 'Packages': {'pytest': '6.1.0', 'py': '1.9.0', 'pluggy': '0.13.1'}, 'Plugins': {'metadata': '1.10.0', 'html': '2.1.1', 'ordering': '0.6'}}
rootdir: /Users/sandeep/Documents/Pytesting/test_library
plugins: metadata-1.10.0, html-2.1.1, ordering-0.6
collected 4 items                                                              

test_utility.py::TestLibrary::test_admin[u1-p1] Launching Browser and Navigating to a URL
Entering  u1
Entering  p1
PASSEDClosing Browser

test_utility.py::TestLibrary::test_user[u1-p1] Launching Browser and Navigating to a URL
Entering  u1
Entering  p1
PASSEDClosing Browser

test_utility.py::TestLibrary::test_admin[u2-p2] Launching Browser and Navigating to a URL
Entering  u2
Entering  p2
PASSEDClosing Browser

test_utility.py::TestLibrary::test_user[u2-p2] Launching Browser and Navigating to a URL
Entering  u2
Entering  p2
PASSEDClosing Browser

============================== 4 passed in 0.02s ===============================
```
### Sharing fixtures: conftest.py

* During implementing your tests you realize that you want to use a fixture function from multiple test files you can move it to a conftest.py file.
* You don’t need to import the fixture you want to use in a test, it automatically gets discovered by pytest. (Both contest.py and the test module should be in the same package! If contest.py is in other package than the test module, then contest.py module will not be automatically discovered)
* Pytest checks if the conftest file is present in the current package. If it is not present, if checks at the Project level. If there is a conftest file at project level, the fixture is automatically discovered. 
* Pytest discovers the conftest automatically if the test module and conftest are inside same package or if the conftest is at project level. 
* The discovery of fixture functions starts at test classes, then test modules, then conftest.py files.

**conftest.py**
```python
import pytest
from selenium import webdriver

@pytest.fixture()
def init():
    driver = webdriver.Chrome('./chromedriver')
    driver.get("http://www.google.com")
    yield
    driver.quit()
```

### Passing driver instance to test method from contest.py
* Fixture functions can accept the _**request**_ object.
* _**request**_ object holds the information of the test method/class/module calling the fixture.

```python
@pytest.fixture()
def init(request):
    driver = webdriver.Chrome('../test_library/chromedriver')
    request.cls.driver = driver
    driver.get("http://www.google.com")
    yield
    driver.quit()
```
### Ignoring scripts in certain directories.
```python
tests/
|-- example
|   |-- test_example_01.py
|   |-- test_example_02.py
|   '-- test_example_03.py
|-- foobar
|   |-- test_foobar_01.py
|   |-- test_foobar_02.py
|   '-- test_foobar_03.py
'-- hello
    '-- world
        |-- test_world_01.py
        |-- test_world_02.py
        '-- test_world_03.py

pytest --ignore=tests/hello/ # Skips all the scripts inside folder "hello"
pytest --ignore=tests/foobar/ --ignore=tests/hello/   # Skips all the scripts inside folder "foobar" and "hello"
```

### Parallel execution using xdist.
* Install 3rd party plugin "xdist" through pip command. (pip install xdist)
* Open terminal or command prompt, navigate to Project folder path and execute the command py.test -n 2
* The above command will execute the two different pytest scripts in parallel.

### Please refer the below links for official documentation
* [request object](https://docs.pytest.org/en/stable/reference.html#pytest.fixtures.FixtureRequest)
* [pytest documentation](https://docs.pytest.org/en/stable/contents.html)
* [pytest-dependency](https://pytest-dependency.readthedocs.io/en/stable/usage.html)
* [pytest-html](https://github.com/pytest-dev/pytest-html)
