from selenium import webdriver
#from selenium.webdriver.common.by import by
import time
import random
#from selenium.webdriver.support.select import Select
#from selenium.webdriver.common.keys import Keys

class wbot:
  def __init__(self):
    options = webdriver.ChromeOptions()
    options.add_argument('lang=pt-br')
    self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
    #self.site = input('Qual site irmão?')
    self.site = 'https://cursomestresdaautomacao.club.hotmart.com/login'
    self.textao = 'Antes de iniciar esta aula, gostaria de parabenizar o Jhonatan pelo curso, e pela página que ele criou ali no netlify, com todos os desafios e componentes, para que seja possível testarmos os elementos na prática. Mto bom! Aliás, esse texto aqui foi feito por automação.'

  def Iniciar(self):

    self.driver.get(self.site)
    time.sleep(2)
    self.DigitarComoHumano('email', self.driver.find_element_by_name("login"))
    time.sleep(2)
    self.DigitarComoHumano('senha', self.driver.find_element_by_name("password"))
    time.sleep(2)
    self.driver.find_element_by_xpath('//button').click()
    self.driver.get('https://cursomestresdaautomacao.club.hotmart.com/lesson/ROxEVbVx4D/como-tirar-printsfotoscreenshots-da-tela')
    time.sleep(10)
    self.DigitarComoHumano(self.textao, self.driver.find_element_by_xpath('//textarea'))



    # titulo = self.driver.find_element_by_xpath("//input[@name='q']")
    # titulo = self.driver.find_element_by_css_selector("")
    # titulo = self.driver.find_element_by_id("oi")
    # titulo = self.driver.find_element_by_class_name("oi") #espaco > .
    # titulo = self.driver.find_element_by_link_text("oi")
    # titulo = self.driver.find_element_by_tag_name("button")
    # titulo = self.driver.find_element_by_partial_link_text("oi")
    #//thead[@class="thead-dark"]//th[3]
    

    # time.sleep(1)
    # titulo.click()
    # titulo.send_keys('amds rodrigo')
    # if titulo is not None:
    # if var.is_selected() == false
    #.text
    #.get_attribute("href")

  def DigitarComoHumano (self, textao, elemento):
    for letter in textao:
      elemento.send_keys(letter)
      time.sleep(random.randint(1,5) / 30)



bot = wbot()
bot.Iniciar()