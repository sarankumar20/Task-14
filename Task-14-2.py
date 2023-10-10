import requests
import json
# visit https://www.openbrewerydb.org/ url and write python script which will do the following
# 1.list the names of all breweries present in the states of alaska, maine and NewYork
# 2.what is the count of breweries in each of states mentioned above
class Breweries:
    def __init__(self, url):
        self.state1 = url
        # Send a GET request to the API
        self.request = requests.get(self.state1)
        self.response = self.request.json()
    def brewery_details(self):
        # Check if the request was successful (status code 200)
        if self.request.status_code == 200:
            # to get all brewery names and counts
            count_breweries =0
            list1 =[]
            for breweries in (self.response):
                count_breweries += 1
                name_breweries = breweries['name']
                data = {
                    'name':name_breweries
                }
                list1.append(data)
            print(f'Name of Breweries are in {state} are: {list1}')
            print(f'total count breweries in {state} is: {count_breweries}')
        else:
            print("failed to retrive data from api")

    # count and list how many breweries have websites in state of alaska,maine,New-york
    def list_brewery_website(self):
            list_website_brewery_alaska = []
            count_web = 0
            for count_website in self.response:
                if count_website['website_url']:
                    list_website_brewery_alaska.append(count_website['name'])
                    count_web += 1
            print(f'total counts of breweries have website in {state} :{count_web}')
            print(f'list of city have website in {state} states are:{list_website_brewery_alaska}')


    # count number of types of breweries present in individual cities in states
    def count_individual_brewery(self):
            city_brewery_count = {}
            # Iterate through each brewery in Alaska
            for brewery in self.response:
                city = brewery.get('city')
                brewery_type = brewery.get('brewery_type')
                # Count the types of breweries in each city
                if city in city_brewery_count:
                    if brewery_type not in city_brewery_count[city]:
                        city_brewery_count[city].append(brewery_type)
                    else:
                        city_brewery_count[city] = [brewery_type]
                # Print the counts of brewery types in each city
                print(f"City:{city}")
                print(f"Number of Brewery Types: {len(brewery_type)}")




state = input("enter a state: ")
#  Define the URL for the Open Brewery DB API endpoint for states
Url = Breweries(f"https://api.openbrewerydb.org/v1/breweries?by_state={state}")
Url.brewery_details()
Url.list_brewery_website()
Url.count_individual_brewery()

