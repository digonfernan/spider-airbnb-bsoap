from spider_airbnb_soup import WebScraping
import csv

url = "https://www.airbnb.com.br/s/Doha--Qatar/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&query=Doha%2C%20Qatar&place_id=ChIJf-jc_zTFRT4RsdTPeJ8x2UQ&date_picker_type=calendar&checkin=2022-11-20&checkout=2022-12-18&source=structured_search_input_header&search_type=autocomplete_click&price_filter_num_nights=28&federated_search_session_id=0d551af5-28cb-4df8-b5a3-dcf3de14deaa&pagination_search=true"
web_scraping = WebScraping(url)
print(web_scraping.pick_all_rooms())

to_csv = (web_scraping.pick_all_rooms())
keys = to_csv[0].keys()

with open('AirbnbDohaWorldCupData.csv', 'w', encoding='utf8', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(to_csv)