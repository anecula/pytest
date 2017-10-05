from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
         desired_capabilities=DesiredCapabilities.CHROME)
driver.get("http://www.eaudeweb.ro/")

image = driver.get_screenshot_as_base64()
from IPython.display import HTML
HTML("""<img src="data:image/png;base64,{0}">""".format(image))
driver.quit()
