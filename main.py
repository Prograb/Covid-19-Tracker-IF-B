import requests
import os
import threading
from bs4 import BeautifulSoup
from datetime import date
import threading
import PySimpleGUI as sg

version = "v1.0.1"



def process():
    requests.get("http://ipinfo.io")
    URL = "https://covid19ilfov.ro/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find_all("section", class_="corona-count-section home-4 bg-corona padding-tb pt-0")

    for result in results:
       global x
       x = result.find("tr", id="row_glina").text
        #print(x)

    today = date.today()

    dat = today.strftime("%d.%m.%Y")

    with open(dat + ".txt", "w+") as handler:
        handler.write(x.strip())
        global y
        y = handler.readline(6)
        handler.close()


        #os.startfile(dat + ".txt")


process()
def GUI():
    layout = [[sg.Text(f"{x}")]]

    window = sg.Window(f'Covid Tracker {version}', layout, resizable=True)

    event, values = window.read()
    window.maximize()

    window.close()

GUI()