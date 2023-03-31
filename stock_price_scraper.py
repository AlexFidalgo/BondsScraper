from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
import time

# URL of the Google search results page
url = 'https://www.google.com/search?q=abcb4'

while 1:
    
    # Initialize a Chrome webdriver instance
    driver = webdriver.Chrome()
        
    # Navigate to the URL using the webdriver
    driver.get(url)
    # Find the element that contains the bond price
    # (from Copy -> Copy selector; look at the end of the string)
    price_elem = driver.find_element(By.CSS_SELECTOR, 'span.IsqQVc.NprOob.wT3VGc')
    
    # Extract the price from the element
    price = price_elem.text
    
    # Printing price
    print(price)
    
    # Check the bond price
    if float(price.replace(",", ".")) < 16.5:
        # Open and show the image if the price is less than 16.8
        img = Image.open('stock_dip.jpg')
        img.show()
    
    # Quit the webdriver instance
    driver.quit()
    
    time.sleep(5)
    


