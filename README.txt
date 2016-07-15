Name: SearchSpring Modules
Author: Mike Williams
Version: 0.0.1
Dependencies: Python 3, selenium, beautifulsoup4, chromedriver
Tested on: Windows 7, Mac.

Notes: Windows and Mac require different chrome drivers.. both included in the 'dependencies' folder.


setup:


create a config.json in root folder 'Automating-WIP'.. enter smc account, pw, and full path to chromedriver. keys must be exact.
ex:

{
"driverlocation": "/Users/yourusername/Desktop/Automating-WIP/dependencies/chromedriver",
"password": “mysecretsmcpw”,
"username": “mysmcaccount@searchspring.com”
}

operation:

there are booleans that control which module is going to run based on the checkmarks. check the one u want to run. do not have any typos in the account names or you might make some funky shit happen.
scrape is used for scraping from an "original" smc account to a new account, sitename.


TODO:

copy data feed?
copy core fields?
copy sorting?
copy field faceting?


py2exe/dmg?