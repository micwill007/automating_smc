from selenium import webdriver
from bs4 import BeautifulSoup

###############################################
#
#    SearchSpring V3 Field Settings Scraper
#
###############################################

## scrapes field settings from one account to another. DONT RUN UNLESS THEY'RE THE EXACT SAME.

def runFieldSettings(scrapeName, siteName, path, user, passw):

  print('Opening browser...')
  #since smc has bugs with firefox, have to use chromdriver with a direct path or add it to your PATH
  browser = webdriver.Chrome(path)

  #browser.maximize_window()
  browser.get('https://smc.searchspring.net/management/field-settings/display-fields')

  print('Logging in....')

  u = browser.find_element_by_id('username')
  u.send_keys(user)
  p = browser.find_element_by_id('password')
  p.send_keys(passw)
  s = browser.find_element_by_id('input_submit')
  s.submit()



  #navigate to scrapesite. 
  try:
    inputBox = browser.find_element_by_css_selector('.chosen-container-single')
    inputBox.click()
    siteSearchBox = browser.find_element_by_css_selector('.chosen-search input')
    siteSearchBox.click()
    siteSearchBox.send_keys(scrapeName)
    # selection = browser.find_element_by_css_selector('.chosen-results .active-result')
    selection = browser.find_element_by_xpath("//ul[@class='chosen-results']/li[not(contains(text(), 'dev'))]/em[text()= '" + scrapeName + "']")
    selection.click()
  except:
    sys.exit('Could not find elements')

  print('Grabbing Source...')
  page = browser.page_source

  #edit this for field settings. scrape the table.
  # then navigate to other site.
  # paste in table
  # click save

  print('parsing..')
  bs = BeautifulSoup(page, "html.parser")
  table = str(bs.find("table", { "class" : "dataSheet" }))
  print(table)
  print('Extraction complete. Next phase.')

  #switch the new site
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

  #navigate to settings, just in case we aren't there already (we should be)
  browser.get('https://smc.searchspring.net/management/field-settings/display-fields')

  js1 = "var aa=document.getElementsByClassName('dataSheet')[0];aa.parentNode.removeChild(aa)"
  browser.execute_script(js1)

  browser.execute_script("""
  var table = arguments[0];
  $('.divTableWithFloatingHeader').append(table);
  """, table)

  # now, submit it
  save = browser.find_element_by_css_selector('.page-action #btnSubmit')
  save.click()



  print('done')

  #comment this out if u wanna stay on the page
  #browser.quit()
