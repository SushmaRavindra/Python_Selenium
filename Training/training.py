from Library.selenium_wrapper import Wrapper

w = Wrapper()
w.launch_url()
w.click_element(("link text", "Register"))
w.click_element(("id", "gender-male"))
w.enter_text(("name", "FirstName"), "Sandeep")
w.enter_text(("name", "LastName"), "Suryaprasad")
w.click_element(("id", "register-button"))
w.close_application()
