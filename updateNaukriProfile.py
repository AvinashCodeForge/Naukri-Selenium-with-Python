import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

#  url
driver.get("https://www.naukri.com/")

wait = WebDriverWait(driver, 10)

loginLayer = wait.until(EC.element_to_be_clickable((By.ID, "login_Layer")))

loginLayer.click()

# input field for username and password
username = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter your active Email ID / "
                                                                  "Username']")))
username.send_keys('avinashtester8@gmail.com')

password = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter your password']")))
password.send_keys('Avinashcak@8')

# login button locator
driver.find_element(By.XPATH, "//button[text()='Login']").click()

# Locator for hamburger
humbarger = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='nI-gNb-drawer__icon']")))
humbarger.click()

updateProfile = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "View & Update Profile")))
updateProfile.click()

# Edit button locator profile
editButton = wait.until(EC.element_to_be_clickable((By.XPATH, "//em[text()='editOneTheme']")))
editButton.click()
time.sleep(5)

actions = ActionChains(driver)

# locator for save button
saveButton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='saveBasicDetailsBtn']")))
driver.execute_script("arguments[0].scrollIntoView();", saveButton)
saveButton.click()

time.sleep(5)
driver.execute_script("window.scrollBy(0, 250);")
time.sleep(5)

# locator for resume upload
resumeUpload = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='attachCV']")))
resumeUpload.send_keys('E:\\Downloads\\Avinash_Immediate_Joinee.pdf')
time.sleep(5)

driver.execute_script("window.scrollBy(0, 250);")
time.sleep(5)

# locators for resume headline edit button
resumeHeadline = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Resume "
                                                                  "headline']//following-sibling::span[text("
                                                                  ")='editOneTheme']")))
resumeHeadline.click()
time.sleep(5)

resumeHeadlineSaveButton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Save']")))
driver.execute_script("arguments[0].scrollIntoView();", resumeHeadlineSaveButton)
resumeHeadlineSaveButton.click()
time.sleep(5)

driver.execute_script("window.scrollBy(0, 100);")
time.sleep(5)

# locators for key skills edit button
keySkills = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Key "
                                                             "skills']//following-sibling::span[text("
                                                             ")='editOneTheme']")))

keySkills.click()
time.sleep(5)

keySkillsSaveButton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Save']")))
driver.execute_script("arguments[0].scrollIntoView();", keySkillsSaveButton)
keySkillsSaveButton.click()
time.sleep(5)

driver.execute_script("window.scrollBy(0, 650);")
time.sleep(5)

# locators for key skills edit button
profileSummary = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Profile "
                                                                  "summary']//following-sibling::span[text("
                                                                  ")='editOneTheme']")))

profileSummary.click()
time.sleep(5)

profileSummarySaveButton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Save']")))
driver.execute_script("arguments[0].scrollIntoView();", profileSummarySaveButton)
profileSummarySaveButton.click()
time.sleep(5)

driver.execute_script("window.scrollBy(0, 350);")
time.sleep(5)

# locators for key skills edit button
careerProfile = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Career "
                                                                 "profile']//following-sibling::span[text("
                                                                 ")='editOneTheme']")))

careerProfile.click()
time.sleep(5)

careerProfileSaveButton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Save']")))
driver.execute_script("arguments[0].scrollIntoView();", careerProfileSaveButton)
careerProfileSaveButton.click()

time.sleep(20)

driver.quit()
