### History
* Selenium was originally developed by Jason Huggins in 2004 as an internal tool at ThoughtWorks.
* Its a free (open-source) automated testing framework used to validate web applications across different browsers and platforms.
* You can use multiple programming languages like Java, C#, Python etc to create Selenium Test Scripts.

### Flavours of Selenium
* Selenium IDE
* Selenium RC
* Selenium WebDriver
* Selenium Grid

### Selenium IDE (Integrated Development Environment):
* Record and playback test automation plugin for the web application. It is implemented as Firefox Add-On and as Chrome Extension.
* It allows for recording, editing and debugging of functional tests.
* It was previously known as Selenium Recorder. Selenium-IDE was originally created by Shinya Kasatani in 2006.
* Getting started with Selenium IDE requires no additional setup other than installing the extension/Plugin on your browser.

**Drawbacks of Selenium IDE**
* Plug-in only available for Firefox & Chrome; not for other browsers.
* only simple tests can be recorded. Cannot automate a complex scenario as no programming logic could be scripted.
* Could not run the tests with multiple set of test data

### Selenium Remote Control (RC): (Selenium 1)
* Selenium Remote Control (RC) is a server, written in Java, that accepts commands for the browser via HTTP.
* RC makes it possible to write automated tests for a web application in any programming language, which allows for better integration of Selenium in existing unit test frameworks.
* Selenium 1 is not supported anymore

**Architecture of Selenium RC**
![RC Architecture](https://github.com/sandeepsuryaprasad/Python_Selenium/blob/master/Images/_RC_Architecture.png)

**Selenium Server**
* Selenium Server receives Selenium commands from your test program in the form of HTTP Request and forwards the same request to Selenium-Core which will be running on Browser.
* Selenium-Core is a JavaScript program, actually a set of JavaScript functions which interprets and executes Selenese commands using the browser’s built-in JavaScript interpreter.
* The RC server bundles Selenium Core and automatically injects it into the browser. This occurs when your test program opens the browser (using a client library API function). Once the Selenium Core program is injected, it starts receiving instructions from the RC server based on test scripts.Selenium Core executes all these instructions as JavaScript commands.
* The Server receives the Selenese commands from your test program using simple HTTP GET/POST requests.
* This means you can use any programming language that can send HTTP requests to automate Selenium tests on the browser.

**Client Libraries**
* The client libraries provide the programming support that allows you to run Selenium commands from a program of your own design.
* A Selenium client library provides a programming interface (API), i.e., a set of functions, which run Selenium commands from your own program.
* The client library takes a Selenese command and passes it to the Selenium Server for processing a specific action or test against the application under test (AUT).
* The client library also receives the result of that command and passes it back to your program. Your program can receive the result and store it into a program variable and report it as a success or failure, or possibly take corrective action if it was an unexpected error.

### Selenium WebDriver (Selenium 2)
* Selenium WebDriver is the successor to Selenium RC.
* In 2008, the whole Selenium Team decided to merge WebDriver and Selenium RC to form a more powerful tool called Selenium 2.
* Selenium WebDriver accepts commands (via a Client API or Client Library) and sends them to a browser.
* This is implemented through a browser-specific browser driver, which sends commands to a browser and retrieves results.

### Selenium Grid
* Selenium Grid allows the execution of WebDriver scripts on remote machines (virtual or real) by routing commands sent by the client to remote browser instances.
* It aims to provide an easy way to run tests in parallel on multiple machines.
* Selenium Grid allows us to run tests in parallel on multiple machines, and to manage different browser versions and browser configurations centrally (instead of in each individual test).
