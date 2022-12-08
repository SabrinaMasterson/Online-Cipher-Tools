#Sabrina Masterson
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from cleantext import clean

def makeDef(input_send):
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get("https://www.onelook.com/thesaurus")
    time.sleep(2)
    #driver opened to URL

    input_search = driver.find_element(By.ID, "thesinput")
    input_search.send_keys(input_send)
    input_search.send_keys(Keys.RETURN)
    time.sleep(2)
    #input added to web page

    soup = BeautifulSoup(driver.page_source, "html.parser")
    time.sleep(2)
    #BeautifulSoup collects html source

    definitions = soup.find("div", class_="def-box-defs")
    if definitions is None:
        #the word or phrase is not known to  TheOneLookThesaurus
        def_err = "No definition could be found for your word."
        return def_err
    else:
        def_text = definitions.get_text()
        def_print = ""
    #check if there is definition content, if no content, send the error text

    for text in def_text:
        if (text == u"\U0001F506"):
            text += "\r\n"
            def_print += text
        elif ';' in text:
            text += "\r\n"
            def_print += text
        else:
            def_print += text
    #the emoji actually denotes the end of line, so I can split the text on that

    def_print = clean(def_print, no_emoji=True)
    def_clean_print = def_print + "\r\n"
    #Definitions printed

    driver.quit()
    return def_clean_print

def makeDict(input_send):
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get("https://www.onelook.com/thesaurus")
    time.sleep(2)
    #driver opened to URL

    input_search = driver.find_element(By.ID, "thesinput")
    input_search.send_keys(input_send)
    input_search.send_keys(Keys.RETURN)
    time.sleep(2)
    #input added to web page

    soup = BeautifulSoup(driver.page_source, "html.parser")
    time.sleep(2)
    #BeautifulSoup collects html source


    tabs = soup.find("ul", {"id" : "tabs"})
    tabs_len = len(tabs)
    if (tabs_len == 0):
        dict_err = "No results could be found."
        return dict_err
    tabs_list = tabs.get_text(separator=' ').split()
    #tabs for each section of the collected words
    total_dict = ""
    for i in range(0, tabs_len):
        z = "zone"
        z = z + str(i+1)
        zone = soup.find("div", {"id" : z})

        if (tabs_list[i] == "All"):
            total_dict += "First page of associated words:"
        else:
            total_dict += "First page of associated " + tabs_list[i] + ": "
        if zone is None:
            total_dict += "No words were found for this section"
        else:
            zone_span =  zone.find_all("span")
            no_def = "Definitions"
            word = []
            for items in zone_span:
                items_list = items.get_text(separator=' ')

                if (items_list[0].isalpha() == False):
                    pass
                elif no_def in items_list:
                    index = items_list.index("Definitions")
                    for i in range(index):
                        key = items_list[i].strip()
                        word.append(key)
                    total_dict += ''.join(word)
                    total_dict += "\r\n"
                    word.clear()
                    #it's messy, but it gets only the words I'm looking for
                else:
                    pass
        total_dict += "\r\n"

    #printing of each set of words/phrases, no spaces for password cracking

    driver.quit()
    return total_dict
