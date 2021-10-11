import time
import requests
import os
import threading
from bs4 import BeautifulSoup
from datetime import date



def process():
    requests.get("http://ipinfo.io")
    URL = "https://covid19ilfov.ro/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")



    results = soup.find_all("section", class_="corona-count-section home-4 bg-corona padding-tb pt-0")

    for result in results:
        x = result.find("tr", id="row_glina").text
        #print(x)
we
    today = date.today()

    dat = today.strftime("%d.%m.%Y")

    with open(dat + ".txt", "w") as handler:
        handler.write(x.strip())
        handler.close()
        os.startfile(dat + ".txt")


'''''''''
threads experiment
for i in range(30):
    x = threading.Thread(target = )
    x.start()

print('Active threads ', threading.activeCount())
'''''''''
process()
