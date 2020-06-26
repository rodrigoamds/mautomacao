from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

import time
import random

import sys

class wbot:
  def __init__(self):
    chrome_options = Options()
    chrome_options.add_argument('--lang=pt-BR')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--disable-popup-blocking')
    chrome_options.add_experimental_option("prefs", {
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": False,
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_setting_values.automatic_downloads": 1,
        "profile.default_content_settings.popups": 0,
    })
    self.driver = webdriver.Chrome(
        executable_path=r'./chromedriver.exe', options=chrome_options)
    
    self.site = 'https://cursoautomacao.netlify.app/'
    self.radios = ['windows 10', 'mac', 'linux']
    self.selects = ['brasil', 'estados unidos', 'canada']
    self.escolha_radio = '0'
    self.escolha_select = '0'
    self.repetir = 's'

  def Iniciar(self):

    self.driver.get(self.site)

    while self.repetir == 's':
      self.PerguntaOpcaoRadio()
      self.ChecaOpcaoRadio()
      self.PerguntaOpcaoSelect()
      self.SelecionaOpcaoSelect()
      self.ExtraiCidades()
      self.DownloadArquivos()
      self.PegaNivel()
      self.PerguntaRepetir()

    self.driver.close()
    sys.exit()



  def PerguntaOpcaoRadio(self):
    print(f'Opções de Radio: {self.radios}')
    while self.escolha_radio not in self.radios:
      self.escolha_radio = input('Radio escolhido: ').lower()

  def ChecaOpcaoRadio(self):
    if self.escolha_radio == 'windows 10':
      self.driver.find_element_by_id("WindowsRadioButton").click()
    elif self.escolha_radio == 'mac':
      self.driver.find_element_by_id("MacRadioButton").click()
    else:
      self.driver.find_element_by_id("LinuxRadioButton").click()
    
  def PerguntaOpcaoSelect(self):
    print(f'Opções de Select: {self.selects}')
    while self.escolha_select not in self.selects:
      self.escolha_select = input('Select escolhido: ').lower()

  def SelecionaOpcaoSelect(self):
    pais_drop = self.driver.find_element_by_id("paisselect")
    opcoes = Select(pais_drop)
    if self.escolha_select == 'brasil':
      opcoes.select_by_index(0)
    elif self.escolha_select == 'estados unidos':
      opcoes.select_by_index(1)
    else:
      opcoes.select_by_index(2)

  def ExtraiCidades(self):
    cidades = self.driver.find_elements_by_xpath("//tbody[tr]//td[1]")
    print('Cidades localizadas: ')
    for cidade in cidades:
      print(cidade.text)
      
  def DownloadArquivos(self):
    print('Iniciando Downloads...')
    downloads = self.driver.find_elements_by_xpath("//a[@class='download']")
    for download in downloads:
      self.driver.execute_script('arguments[0].click()', download)
      print('Downloading 5% > 25% > 50% > 100% > Download completed')
      time.sleep(1)

  def PegaNivel(self):
    print('Níveis de acesso liberados:')
    niveis = self.driver.find_elements_by_xpath('//input[starts-with(@id,"acessoNivel")]')
    label_niveis = self.driver.find_elements_by_xpath('//label[starts-with(@for,"acessoNivel")]')
    for indice, nivel in enumerate(niveis):
      if nivel.is_enabled():
        print(label_niveis[indice].text)

      
  def PerguntaRepetir(self):
    time.sleep(1)
    self.driver.execute_script('window.scrollTo(0,document.body.scrollTop);')
    time.sleep(1)
    self.repetir = input('Bora mais uma vez? (s/n): ').lower()
    while self.repetir not in ['s','n']:
      self.repetir = input('Bora mais uma vez? (s/n): ').lower()
    if self.repetir == 's':
      print('Reiniciando...')
      self.escolha_radio = '0'
      self.escolha_select = '0'
    else:
      print('Encerrando...')

      

#Favor não deixar essa informação vazia

bot = wbot()
bot.Iniciar()


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

    # self.DigitarComoHumano('email', self.driver.find_element_by_name("login"))
    # time.sleep(2)
    # self.DigitarComoHumano('senha', self.driver.find_element_by_name("password"))
    # time.sleep(2)
    # self.driver.find_element_by_xpath('//button').click()
    # self.driver.get('https://cursomestresdaautomacao.club.hotmart.com/lesson/ROxEVbVx4D/como-tirar-printsfotoscreenshots-da-tela')
    # time.sleep(10)
    # self.DigitarComoHumano(self.textao, self.driver.find_element_by_xpath('//textarea'))


