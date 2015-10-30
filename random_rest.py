__author__ = 'Jorge'
import requests
import bs4

def get_rest():
    url="http://www.tripadvisor.es/RestaurantSearch-g187529-oa1980-a_Action.PAGE-a_ajax.1-a_availSearchEnabled.true-a_date.2015__2D__09__2D__24-a_itags.10591-a_people.2-a_time.20%%3A00%%3A00-jpopularity-Valencia_Valencia_Province_Valencian_Country.html#EATERY_LIST_CONTENTS"
    response=requests.get(url)
    soup = bs4.BeautifulSoup(response.text)


get_rest()
