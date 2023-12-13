import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def scrape_data_from_page(driver, path, csv_writer):
    try:
        driver.get(path)

        items = driver.find_elements(By.CSS_SELECTOR, "span.sc-1x0vz2r-0.jZyObG")
        items2 = driver.find_elements(By.CSS_SELECTOR, "span.sc-1x0vz2r-0.gSLYtF")
        prix = driver.find_element(
            By.CSS_SELECTOR, "p.sc-1x0vz2r-0.lnEFFR.sc-1g3sn3w-13.czygWQ"
        )

        data_row = []

        for item, item2 in zip(items, items2):
            data_row.extend([item.text, item2.text])

        data_row.append(prix.text)

        csv_writer.writerow(data_row)

    except Exception as e:
        print(f"Erreur lors de la récupération des données de la page {path}: {e}")


# Chemin du pilote
path = "C:\\Program Files (x86)\\chromedriver.exe"

# Options du navigateur
chrome_options = Options()
chrome_options.add_argument(f"executable_path={path}")

# Ouvrir le fichier CSV en mode écriture
with open("donnees_scrappes.csv", mode="w", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)

    # En-tête du CSV
    csv_writer.writerow(["Item1", "Item2", "Prix"])

    with webdriver.Chrome(options=chrome_options) as driver:
        driver.get("https://www.avito.ma/fr/maroc/appartements")
        liens = driver.find_elements(By.CSS_SELECTOR, "a.sc-1jge648-0.eTbzNs")

        for lien in liens:
            scrape_data_from_page(driver, lien.get_attribute("href"), csv_writer)
