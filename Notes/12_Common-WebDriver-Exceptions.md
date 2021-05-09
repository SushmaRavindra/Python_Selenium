Below are the common exceptions that you may encounter while working with WebDriver.

* NoSuchElementException
* StaleElementReferenceException
* NoSuchAttributeException
* NoAlertPresentException
* ElementNotVisibleException
* ElementNotInteractableException
* TimeoutException
* NoSuchFrameException

**NoSuchElementException**
* This exception is raised when the element is not found in DOM.
* The exception is raised by find_element method.
* You may need to check the selector that you are using in find_element method to rectify the issue. 

**StaleElementReferenceException**
* Thrown when a reference to an element is now "stale" or Lost.
* The possible cause for this exception is that you are no longer on the same page, or the page may have refreshed since the element was located.
* The element may have been removed and re-added to the web page, since it was located.
* Element may have been inside an iframe or another context which was refreshed.

**NoSuchAttributeException**
* Thrown when the attribute of element could not be found.
* An attribute could be anything that you are trying to access after dot operator. It can be a method, property, variable etc.

**NoAlertPresentException**
* Thrown when switching to no presented alert.
* This can be caused by calling an operation on the Alert() class when an alert is not yet on the screen.

**ElementNotVisibleException**
* Thrown when an element is present on the DOM, but it is not visible.
* Most commonly encountered when trying to click or edit or read text of an element that is hidden from view.

**ElementNotInteractableException**
* Thrown when an element is present on the DOM but can not interaction with the element.
* Possible cause may be the element is disabled. 

**TimeoutException**
* Usually thrown by until method of WebDriverWait class.
* Possible cause would be when the command does not complete with in specified timeout period.

**NoSuchFrameException**
* Thrown when frame target to be switched doesn't exist.
