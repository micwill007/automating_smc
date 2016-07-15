from selenium import webdriver
from bs4 import BeautifulSoup


###############################################
#
#       SearchSpring V3 Synonym Scraper
#
###############################################

## scrapes synonyms from one account to another

def runSynonym(scrapeName, siteName, path, user, passw):

  print('Opening browser...')
  #since smc has bugs with firefox, have to use chromdriver with a direct path or add it to your PATH
  browser = webdriver.Chrome(path)

  #browser.maximize_window()
  browser.get('https://smc.searchspring.net/management/synonyms/index/subtype/synonyms')

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
    selection = browser.find_element_by_xpath("//ul[@class='chosen-results']/li[not(contains(text()= 'dev'))]/em[text()= '" + scrapeName + "'")
    selection.click()
  except:
    sys.exit('Could not find elements')

  print('Grabbing Source...')
  page = browser.page_source

  print('parsing..')
  bs = BeautifulSoup(page, "html.parser")
  table = bs.find("table", { "class" : "tbl-synonyms" })
  lhs = table.findAll(attrs={"data-field" : "lhs"})
  rhs = table.findAll(attrs={"data-field" : "rhs"})
  print('parsing done')

  #keyword list
  keywords = []

  #synonyms list
  synonyms = []

  #if u wanna put it in a file..?
  #File = open('File.txt', 'w')

  for keyword in lhs:
    keywords.append(keyword.get_text(strip=True))
     # File.write(str(keyword.get_text(strip=True)) + '|')
    print('keywords done')
    for synonym in rhs:
      synonyms.append(synonym.get_text(strip=True))
      #File.write(str(synonym.get_text(strip=True)) + ',')
      
      print('synonyms done')


  #File.close()

  #If lists are huge, comment these out
  print(keywords)
  print(synonyms)

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

  #navigate to sorting, just in case we aren't there already (we should be)
  browser.get('https://smc.searchspring.net/management/synonyms/index/subtype/synonyms')


  # counter due to the second list, prob a better way but im lazy
  idx = 0

  for word in keywords:
      #we have to reinstate these variables on each ajax call or else they stale and it throws an error
      add = browser.find_element_by_css_selector('.smc_block .button')
      synonym = browser.find_element_by_css_selector('#synonym-lhs')
      values = browser.find_element_by_css_selector('#synonym-rhs')
      submit = browser.find_element_by_css_selector('.modal-footer a')
      
      add.click()
      synonym.send_keys(word)
      values.send_keys(synonyms[idx])
      submit.click()
      idx += 1


  print('Complete')