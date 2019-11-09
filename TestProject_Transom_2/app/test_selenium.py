from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time

driver = webdriver.Chrome("C:/Users/MarleneRuedaCastillo/Documents/NewDjangoCrud/testproject_transom_2/TestProject_Transom_2/app/chromedriver.exe")

driver.set_page_load_timeout("10")
driver.get('http://localhost:8000/app/crear_vehiculo')

modelo = driver.find_element_by_name('modelo')
color = driver.find_element_by_name('color')
marca = driver.find_element_by_name('marca')
km = driver.find_element_by_name('kilometraje')
nuevo = driver.find_element_by_name('nuevo')

modelo.send_keys('Yalis 2018')
color.send_keys('Negro')
marca.send_keys('Toyota')
km.send_keys(10000)
# nuevo.send_keys(True)

