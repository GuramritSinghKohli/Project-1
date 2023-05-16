from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a web driver instance (e.g., Chrome)
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://www.indiatoday.in/")

# Wait for the articles to load
wait = WebDriverWait(driver, 500)  # Increased timeout value to 50 seconds
articles = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="view-content"]/div[@class="catagory-listing"]/div[@class="catagory-listing-right"]/h3/a')))

# Loop through the first three articles
for article in articles[:3]:
    # Extract the headline text
    headline = article.text
    
    # Click on the article
    article.click()
    
    # Do something with the headline (print it here)
    print("Headline:", headline)
    
    # Go back to the previous page
    driver.back()

# Close the browser
driver.quit()
