import requests
import os
from bs4 import BeautifulSoup
from datetime import date


class Main():
    def process(self):
        loc = input("Localitate: ").lower()
        requests.get("http://ipinfo.io")
        URL = "https://covid19ilfov.ro/"
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")



        results = soup.find_all("section", class_="corona-count-section home-4 bg-corona padding-tb pt-0")

        for result in results:
            x = result.find("tr", id=f"row_{loc}").text
            #print(x)
        #declaring filename related values
        today = date.today()
        name = loc.title()
        dat = today.strftime("%d.%m.%Y")

        with open(name + "_" + dat + ".txt", "w") as handler:
            handler.write(x.strip())
            handler.close()
            os.startfile(loc + "_" +dat + ".txt")




m = Main()
m.process()