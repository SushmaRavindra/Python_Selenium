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
**Moving all the test methods into class definition**
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
**Multiple ways of executing test's**
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
**pytest fixtures**
* Pytest fixture is a callable (normally a function or a generator) decorated with inbuilt pytest decorator @fixture
* Fixtures are used for dependency injection or to pass the data to the test functions
* Fixtures are accessed by test functions through arguments.
* Fixtures are used to run a piece of code repeatedly before and/or after every test method/class/module/session based on the defined scope.

**Advantages of fixtures**
* Each test can be run independently irrespective of previous test method is failed or passed
* Setup and teardown methods run irrespective of test's fail or pass
* Many tests can share the same setup/teardown
* Setup/Teardown in same function
* Pass data to test with return or yield

**Simple fixture that returns a string "hello world"**
```python
from pytest import fixture
@fixture
def greet():
    return "hello world"
 
def test_greet(greet):
    assert "hello world" == greet
```

**Sample pytest fixture for launching browser and closing browser**
```python
from pytest import fixture
@fixture
def init():
    print('Launching Browser and Navigating to a URL')
    yield
    print('Closing Browser')
``` 
* The code before yield statement run's once before every test method and the code after yield statement run's once after the completion of every test method. 

**Passing fixture to each test method in a class**
```python
class TestArithmetic:
    def test_valid_int(self, init):
        assert int_add(1, 2) == 3

    def test_invalid_data(self, init):
        with raises(TypeError):
            int_add(1, 1.2)
```
**Scoping of test fixtures**
* "function" Called once per test function (default)
* "module" Called once per module
* "class" Called once per class
* "session" Called once per-run
```python
@fixture(scope="session")
def fix_session():
    print('\n running setup SESSION scope')
    yield 
    print('\n running teardown SESSION scope')

@fixture(scope="module")
def fix_mod(fix_session):
    print('\n running setup MODULE scope')
    yield
    print('\n running teardown MODULE scope')

@fixture(scope="class")
def fix_class(fix_mod):
    print('\n running setup CLASS scope')
    yield 
    print('\n running teardown CLASS scope')

@fixture()
def fix_func(fix_class):
    print('\n running setup FUNCTION scope')
    yield 
    print('\n running teardown FUNCTOIN scope')

class TestArithmetic:
    def test_valid_int(self, fix_func):
        assert int_add(1, 2) == 3

    def test_invalid_data(self, fix_fun):
        with raises(TypeError):
            int_add(1, 1.2)
```
**Grouping test's**

```python
class TestArithmetic:
    @mark.smoke
    def test_valid_int(self, init):
        assert int_add(1, 2) == 3
    
    @mark.regression
    def test_invalid_data(self, init):
        with raises(TypeError):
            int_add(1, 1.2)
```
* Executing only those test's which are marked as smoke. **pytest test_utility.py -vs -m smoke**
* Executing only those test's which are marked as regression. **pytest test_utility.py -vs -m regression**

**Managing Test Dependency**
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

**Running only failed tests**
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
**Sharing fixtures: conftest.py**

* During implementing your tests you realize that you want to use a fixture function from multiple test files you can move it to a conftest.py file.
* You don’t need to import the fixture you want to use in a test, it automatically gets discovered by pytest. (Both contest.py and the test module should be in the same package! If contest.py is in other package than the test module, then contest.py module will not be automatically discovered)
* Pytest checks if the conftest file is present in the current package. If it is not present, if checks at the Project level. If there is a conftest file at project level, the fixture is automatically discovered. 
* Pytest discovers the conftest automatically if the test module and conftest are inside same package or if the conftest is at project level. 
* The discovery of fixture functions starts at test classes, then test modules, then conftest.py files.

**conftest.py**
```python
from pytest import fixture
from selenium import webdriver

@fixture
def init():
    driver = webdriver.Chrome('./chromedriver')
    driver.get("http://www.google.com")
    yield
    driver.quit()
```

**Passing driver instance to test method from contest.py**
* Fixture functions can accept the _**request**_ object.
* _**request**_ object holds the information of the test method/class/module calling the fixture.

```python
@pytest.fixture
def init(request):
    driver = webdriver.Chrome('../test_library/chromedriver')
    driver.get("http://www.google.com")
    yield driver
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

**Parallel execution using xdist.**
* Install 3rd party plugin "xdist" through pip command. (pip install xdist)
* Open terminal or command prompt, navigate to Project folder path and execute the command py.test -n 2
* The above command will execute the two different pytest scripts in parallel.

**Please refer the below links for official documentation**
* [pytest documentation](https://docs.pytest.org/en/stable/contents.html)
* [pytest-dependency](https://pytest-dependency.readthedocs.io/en/stable/usage.html)
* [pytest-html](https://github.com/pytest-dev/pytest-html)
