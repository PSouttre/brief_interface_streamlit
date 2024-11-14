from streamlit.testing.v1 import AppTest
import pandas as pd
import streamlit as st
import datetime

at = AppTest.from_file("app.py", default_timeout=10).run()
df = pd.read_csv("./car_prices_clean.csv", delimiter = ',', encoding='utf-8')

# Titre
def test_title():
    assert at.title[0].value == "Ventes de voiture aux Etats-Unis"

# selectbox
def test_colonnes_selectbox():
    assert at.selectbox[0].options[1] ==  'make' 

def test_asc_desc():
    at.selectbox[0].set_value("make").run()
    assert at.selectbox[1].options[1] == 'Décroissant'


# slider
def test_price_slider():
    assert at.slider[0].value[0] == 1
    assert at.slider[0].value[1] == 230000

def test_km_slider():
    assert at.slider[1].value[0] == 1
    assert at.slider[1].value[1] == 999999


# input_text
def test_make_text_input():
    at.text_input[0].set_value("chevrolet").run()
    assert at.text_input[0].value == "chevrolet"

# input_text
def test_model_text_input():
    at.text_input[1].set_value("pickup").run()
    assert at.text_input[1].value == "pickup"

# date_input
def test_date_input():
    at = AppTest.from_file("app.py", default_timeout=10).run()   # permet de réinitialiser et repartir de l'app d'origine
    assert at.date_input[0].value[0] == datetime.date(2014,1,1)
    assert at.date_input[0].value[1] == datetime.date(2015,7,21)


