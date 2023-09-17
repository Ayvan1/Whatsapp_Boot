from selenium import webdriver
from selenium.webdriver.support import wait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchAttributeException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Boot:
    """
    The Class Boot allows to search , send messages and  stickers to contacts
    """
    def __init__(self):
        """
            Intialize a selenium Webdriver and open the whatsapp web page
        """
        self.__driver = webdriver.Chrome()
        self.__driver.get("https://web.whatsapp.com/")
        
    def wait_load_page(self):
        """
        the wait_load_page methode waits until the website is loaded
        Returns:
           None
        """
        try:
            wait.WebDriverWait(driver=self.__driver,timeout=10).until(lambda driver:driver.execute_script("return document.readyState") == "complete")
        except TimeoutException as e_msg:
            print(f"---> Error message: <{e_msg}>")
    def search_contact(self,name:str):
        """
        the search_contact method searches for the contact's name on the Whatsapp Web search screen.
        Args:
            name (str): the name  of the person
        """
        try:
            box_search_contact = wait.WebDriverWait(driver=self.__driver,timeout=10).until(EC.presence_of_element_located((By.XPATH,"//div[@role='textbox'][@contenteditable='true']")))
            if box_search_contact:
                box_search_contact.send_keys(name,Keys.ENTER)
                print(f"---> the person with the name : <{name}> was found")
        except (NoSuchAttributeException,ElementNotInteractableException,NoSuchElementException,TimeoutException) as e_msg:
            print(f"---> Error message: <{e_msg}>") 
    def send_sticker(self,times:int,index_sticker:int):
        """
        the sennd_sticker method sends stickers to the contact
        Args:
            times (int): the amount of sticker
            index_sticker (int): the  position of the sticker in the block of sticker
        """
        try:
            sticker_btn = wait.WebDriverWait(driver=self.__driver,timeout=10).until(EC.presence_of_element_located((By.XPATH,"//div[@data-state='closed']/button[@aria-label='Sticker-Auswahlbereich öffnen']")))
            if sticker_btn:
                sticker_btn.send_keys(Keys.ENTER)
                sticker =  wait.WebDriverWait(driver=self.__driver,timeout=10).until(EC.element_to_be_clickable((By.XPATH,f"//div[@tabindex='-1'][@class='_3kN2f']//div[@tabindex='-1'][@class='rpvcun8f p357zi0d lkhkxwyq fhf7t426 ln8gz9je']/div[{index_sticker}]")))
                if sticker:
                    for time in range(times):
                        sticker.click()
                    print(f"---> The Sticker with id: {index_sticker} was sent {times} time")
        except (NoSuchAttributeException,ElementNotInteractableException,NoSuchElementException,TimeoutException) as e_msg:
            print(f"---> Error message: <{e_msg}>")
    def send_message(self,msg:str):
        """
        The send_message methode send messages to the contact
        Args:
            msg (str): message
        """
        
        try:
            box_message = wait.WebDriverWait(driver=self.__driver,timeout=10).until(EC.presence_of_element_located((By.XPATH,"//div[@role='textbox'][@tabindex='10']")))
            if box_message:
                box_message.send_keys(msg,Keys.ENTER)
                print(f"---> the message {msg} was sent")
        except (NoSuchAttributeException,ElementNotInteractableException,NoSuchElementException,TimeoutException) as e_msg:
            print(f"---> Error message: <{e_msg}>")
    def boot_end(self):
        """
        the boot_end methode closes the webdriver
        """
        print(f"--- Thanks for the usage ---")
        self.__driver.quit()