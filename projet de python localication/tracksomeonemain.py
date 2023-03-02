

# ---------
# install phonenumbers
# --phonenumbers: une bibliothèque Python pour valider et formater
# les numéros de téléphone selon les normes internationales--
from phonenumbers import carrier

# Importation du module OpenCage pour obtenir des informations géographiques.
from opencage.geocoder import OpenCageGeocode
import opencage
import pycountry
import phonenumbers
from myphone import number
# --La fonction geocoder de la bibliothèque phonenumbers permet de déterminer
# le pays associé à un numéro de téléphone--
from phonenumbers import geocoder
pepnumber = phonenumbers.parse(number)  # --analyse du numéro de téléphone--
print(pepnumber)  # Country Code: 33 National Number: ********
# extraction du code de pays à partir du numéro de téléphone
country_code = phonenumbers.region_code_for_number(pepnumber)

# --install pycountry :
# on utilise la bibliothèque pycountry pour obtenir le nom du pays à partir du code de pays--
country_name = pycountry.countries.get(alpha_2=country_code).name
print(country_name)
# ----------

service_pro = phonenumbers.parse(number)
# Affichage du nom du fournisseur de service en anglais.
print(carrier.name_for_number(service_pro, "en"))

# opencage: une API de géocodage qui permet de convertir des adresses
# ou des noms de lieux en coordonnées géographiques (latitude et longitude).
# install  opeancage
# Clé d'API OpenCage pour accéder au service.
key = 'e**********************************'
# Initialisation du géocodeur avec la clé d'API.
geocoder = OpenCageGeocode(key)
# Conversion du nom du pays en chaîne de caractères pour la requête géographique.
query = str(country_name)
# Recherche des informations géographiques pour le pays spécifié.
results = geocoder.geocode(query)
# print(results)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)

import folium
# folium: une bibliothèque Python qui permet de créer des cartes interactives
# en utilisant les données de OpenStreetMap.
# Création d'une carte centrée sur les coordonnées géographiques avec un zoom de niveau 9.
myMap = folium.Map(location=[lat, lng], zoom_start=9)
# Ajout d'un marqueur à l'emplacement spécifié avec une info-bulle affichant le nom du pays.
folium.Marker([lat, lng], popup=country_name).add_to(myMap)
# Enregistrement de la carte sous forme de fichier HTML.
myMap.save("mylocation.html")
