# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 11:35:04 2017

@author: amartinezcotto
"""
from os import listdir
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
#%%
current_path= !cd
chrome_path = r"C:\Users\amartinezcotto\Desktop\chromedriver_win32\chromedriver.exe"
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : current_path[0]}
chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(executable_path=chrome_path, chrome_options=chromeOptions)

#%%
for idnumber in [1,2,3]:
    driver.get('http://www.tabc.state.tx.us/PublicInquiry/Roster.aspx')
    driver.find_element_by_xpath("""//*[@id="MainContent_btnLocation"]""").click()
    driver.find_element_by_xpath("""//*[@id="MainContent_btnSubmit"]""").click()
    driver.find_element_by_xpath("""//*[@id="MainContent_btnExit"]""").click()
    driver.find_element_by_xpath("""//*[@id="MainContent_btnLicense"]""").click()
    driver.find_element_by_id('MainContent_rblBoard_'+str(idnumber)).click()
    driver.find_element_by_xpath("""//*[@id="MainContent_chkSelectAll"]""").click()
    driver.find_element_by_xpath("""//*[@id="MainContent_btnSubmit"]""").click()
    driver.find_element_by_xpath("""//*[@id="MainContent_btnExit"]""").click()
    driver.find_element_by_xpath("""//*[@id="MainContent_btnSubmit"]""").click()
    select = Select(driver.find_element_by_xpath("""//*[@id="MainContent_ucSelectOutput_ddlOutputType"]"""))
    select.options[2].click()
    driver.find_element_by_xpath("""//*[@id="MainContent_btnSubmit"]""").click()

#%%
Texas_Files = []
for file in listdir(current_path[0]):
    if file.endswith(".txt"):
        Texas_Files.append(file)

#%%
df_list = list(map(lambda f: pd.read_csv(f), Texas_Files))
Texas_Licenses = pd.concat(df_list).reset_index(drop=True)


#%%








