from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By


###############################################
#
#   SearchSpring V3 Field Settings 'to text'
#
###############################################

## sets all field in field settings to 'text' type.

def runFieldSettingText(siteName, path, user, passw):

  browser = webdriver.Chrome(path)

  #browser.maximize_window()
  browser.get('https://smc.searchspring.net/management/field-settings/display-fields')
  browser.maximize_window()
  print('Logging in....')

  u = browser.find_element_by_id('username')
  u.send_keys(user)
  p = browser.find_element_by_id('password')
  p.send_keys(passw)
  s = browser.find_element_by_id('input_submit')
  s.submit()



  #navigate to site.
  print('navigating to sitename') 
  try:
    inputBox = browser.find_element_by_css_selector('.chosen-container-single')
    inputBox.click()
    siteSearchBox = browser.find_element_by_css_selector('.chosen-search input')
    siteSearchBox.click()
    siteSearchBox.send_keys(siteName)
    selection = browser.find_element_by_css_selector('.chosen-results')
    selection.click()
  except:
    sys.exit('Could not find elements')

  table = browser.find_element_by_css_selector('.smc_block .divTableWithFloatingHeader tbody')
  rows = table.find_elements(By.TAG_NAME, "tr") # get all of the rows in the table


  scroll = 0
  for row in rows:
    col = row.find_element(By.CLASS_NAME, "left-align")
    col.click()
    tex = col.find_elements_by_css_selector('.chosen-results li')
    tex[1].click()
    browser.execute_script("""
    var scroll = arguments[0];
    window.scrollTo(0, scroll);
    """, scroll)
    scroll += 35

  print('complete')
  #end this module