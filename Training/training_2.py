from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

# driver = webdriver.Chrome("./chromedriver")
# driver.get("file:///Users/sandeep/Documents/Python_Selenium/HTML_Pages/Standard_listbox.html")
# time.sleep(3)

# lst_box = driver.find_element_by_xpath("//select[@id='multiple_cars']")

# curr = driver.find_element_by_name("currency")
# s = Select(curr)
# s.select_by_value("INR")
# s.select_by_index(1)
# s.select_by_visible_text("Indian Rupees")

# s = Select(lst_box)
# print(s.is_multiple)
# all_opts = s.options
#
# items = [opt.text for opt in all_opts]
#
# for item in items:
#     s.select_by_visible_text(item)
#     time.sleep(0.3)
#
# s.deselect_all()



# cars = ['Audi', 'Ford', 'Mercedes']
# for car in cars:
#     s.select_by_visible_text(car)
#     time.sleep(1)

# s.deselect_all()
# s.deselect_by_visible_text("Audi")
# s.deselect_by_index(0)
# s.deselect_by_value("0")

# all_opts = s.all_selected_options

# for opt in all_opts:
#     print(opt.text)


# s.select_by_visible_text("Mercedes")
#
# time.sleep(1)
#
# print(s.first_selected_option.text)
#
# time.sleep(1)
#
# s.select_by_visible_text("Audi")
#
# print(s.first_selected_option.text)

# opts = s.options

# cars = [opt.text for opt in opts]  # List Comprehension

# search_car = 'Maruti'

# s.select_by_visible_text("Maruti")

# for index, car in enumerate(cars):
#     if car == search_car:
#         s.select_by_visible_text(car)
#         print(index)



# for index, item in enumerate(items):
#     s.select_by_index(index)
#     time.sleep(0.5)





