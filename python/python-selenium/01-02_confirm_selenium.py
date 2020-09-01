from selenium import webdriver
browser = webdriver.Chrome()
ret = browser.get("http://calpoly.edu")
print(ret)
