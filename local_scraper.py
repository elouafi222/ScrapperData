import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# sc-1x0vz2r-0 lnEFFR sc-1g3sn3w-13 gIuweS
# sc-1x0vz2r-0 lnEFFR sc-1g3sn3w-13 czygWQ
### premier cas ######
# Chemin du pilote
path = "C:\\Program Files (x86)\\chromedriver.exe"

# Options du navigateur
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument(f"executable_path={path}")


def creeAppartement(itemsType, itemsValue, icon, prix, nbrColome=10):
    typeDeValeurCherche = {
        "type": 0,
        "secteur": 1,
        "étage": 2,
        "surface habitable": 3,
        "surfacetotaletitleid": 4,
        "chambrestitleid": 5,
        "salledebaintitleid": 6,
        "salons": 7,
        "âge du bien": 8,
        "prix": 9,
    }
    AppartementList = ["None"] * nbrColome
    for item, item2 in zip(itemsType, itemsValue):
        try:
            val = typeDeValeurCherche.get(item.text.lower())
            AppartementList[val] = item2.text.lower()
        except Exception as e:
            print("l'element n'est pas interesser")

    for val, val2 in zip(icon.keys(), icon.values()):
        AppartementList[typeDeValeurCherche.get(val.lower())] = val2

    if prix != "None":
        AppartementList[9] = prix.text

    return AppartementList


def scrape_data_from_page(path, csv_writer):
    try:
        with webdriver.Chrome(options=chrome_options) as driver:
            driver.get(path)
            items = driver.find_elements(By.CSS_SELECTOR, "span.sc-1x0vz2r-0.jZyObG")
            items2 = driver.find_elements(By.CSS_SELECTOR, "span.sc-1x0vz2r-0.gSLYtF")
            prix = "None"
            icon = {}

            try:
                prix = driver.find_element(
                    By.CSS_SELECTOR, "p.sc-1x0vz2r-0.lnEFFR.sc-1g3sn3w-13.czygWQ"
                )
            except Exception as e:
                print(f"Erreur lors de la recherche des éléments : {e}")

            # sc-6p5md9-2 bxrxrn
            divValue1 = driver.find_elements(By.CSS_SELECTOR, "div.sc-6p5md9-2.bxrxrn")

            for div in divValue1:
                try:
                    divValue = div.find_element(
                        By.CSS_SELECTOR, "div.sc-wdregf-0.esVxwv"
                    )
                    svg_element = divValue.find_element(By.CSS_SELECTOR, "svg.av-icon")
                    # Obtenez la valeur de l'attribut aria-labelledby
                    aria_labelled_by_value = svg_element.get_attribute(
                        "aria-labelledby"
                    )
                    valeurIcon = div.find_element(
                        By.CSS_SELECTOR, "span.sc-1x0vz2r-0.kQHNss"
                    )
                    icon[aria_labelled_by_value] = valeurIcon.text
                except Exception as e:
                    print(
                        f"Erreur lors de la récupération des données de la page {path}: {e}"
                    )

            print(icon)
            data_row = creeAppartement(items, items2, icon, prix)

            csv_writer.writerow(data_row)

    except Exception as e:
        print(f"Erreur lors de la récupération des données de la page {path}: {e}")


# Ouvrir le fichier CSV en mode écriture
with open("meuble1.csv", mode="w", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)

    # En-tête du CSV
    csv_writer.writerow(
        [
            "type",
            "secteur",
            "etage",
            "surface habitable",
            "surface totale",
            "nbr chambre",
            "nbr salleBain",
            "salon",
            "age de bien",
            "prix",
        ]
    )

    with webdriver.Chrome(options=chrome_options) as driver:
        driver.get("https://www.avito.ma/fr/casablanca/appartements-%C3%A0_vendre?o=1")
        liens = driver.find_elements(By.CSS_SELECTOR, "a.sc-1jge648-0.eTbzNs")
        for lien in liens:
            # print(lien.get_attribute("href"))
            scrape_data_from_page(lien.get_attribute("href"), csv_writer)

    """
    path = "https://www.avito.ma/fr/sidi_bernoussi/appartements/Appartement_%C3%A0_vendre_81_m%C2%B2_%C3%A0_Casablanca_53843087.htm"
    path2 = "https://www.avito.ma/fr/ben_ejdia/appartements/Appartement_ensoleill%C3%A9_au_coeur_de_Casablanca__53441952.htm"
    path3 = "https://www.avito.ma/fr/maarif/appartements/STUDIO_38M_A_VENDRE_A_QUARTIER_MAARIF__54209364.htm"
    data_row = creeAppartement(
                items,
                items2,
                SalleDeBainId,
                SurfaceTotaleTitleID,
                ChambresTitleID,
                valeurIcon,
                prix,
            )

            csv_writer.writerow(data_row)
    """
