# Imports
from bs4 import BeautifulSoup
import requests

# Class e funções
class WebScraping:
    def __init__(self, url):
        self.url = url
        self.soup = self.__get_html()
    
    def __get_html(self):
        req = requests.get(self.url)
        soup = BeautifulSoup(req.content, "html.parser")
        return soup
    
    def __get_rooms(self):
        return self.soup.find_all("div", class_ = "c4mnd7m dir dir-ltr")
    
    def __get_subtitle(self, room):
        return room.find("div", class_="t1jojoys dir dir-ltr").text
    
    def __get_title(self, room):
        return room.find("span", class_="tjbvqj3 dir dir-ltr").text

    def __get_rating(self, room):
        return room.find("span", class_="t5eq1io r4a59j5 dir dir-ltr").text

    #def __get_photo(self, room):
        return self.soup.find_all("div", class_ = "_6tbg2q")

    def __get_attrs(self, room):
        attr_room = {}
        details = room.find("div", class_="f15liw5s s1cjsi4j dir dir-ltr")
        attrs = details.find_all("span", class_=" dir dir-ltr") #A classe está dessa forma porém não funciona
        for attr in attrs:
            attr_info = attr.text.split()
            attr_room[f"{attr_info[1][:3]}"] = attr_info[0]
        return attr_room

    def __get_price(self, room_html):
        return room_html.find("div", class_ = "p11pu8yw dir dir-ltr").find("span", class_ = "_tyxjp1").text[2:]
    
    def pick_all_rooms(self):
        list_of_rooms = []
        for room in self.__get_rooms():
            room_info = {}

            room_info["Title"] = self.__get_title(room)
            room_info["Subtitle"] = self.__get_subtitle(room)
            room_info["Price During the World Cup (R$)"] = self.__get_price(room)
            room_info["Rating"] = self.__get_rating(room)
            #room_info["Photo"] = self.__get_photo(room)
            attrs = self.__get_attrs(room)
            room_info["Guests"] = attrs.get("hós", None) #Não há essa informação nos anúncios
            room_info["Bedrooms"] = attrs.get("qua", None) #Não há essa informação nos anúncios
            room_info["Beds"] = attrs.get("cam", None) #O anúncio não apresenta a classe correta
            room_info["Bathrooms"] = attrs.get("ban", None) #Não há essa informação nos anúncios

            list_of_rooms.append(room_info)
        
        return list_of_rooms