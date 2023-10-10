# Generate json structure dynamically Retrieve information from complex json structure
# using https://restcountries.com/v3.1/all url to finish the task
# 1.using OOPS concept for following task
# 2.create class constructor for taking input the mentioned above url for the task

import requests
import json
class Countries:
    def __init__(self, rest_api):
        self.all_details = rest_api

    # create a method that will fetch all the json data from url mentioned above
    def fetch_all_details(self):
        # to get contents from end point we using requests.get() method attribute
        request_get = requests.get(self.all_details)
        # we want content in json format using json() attribute
        response = request_get.json()
        # we can check end point is working are not if we get 200 status code its sucess
        # lets check using status_code attribute
        status_code = request_get.status_code
        modify_api = json.dumps(response, indent=2)
        print(f' signal_status: {status_code}')
        print(f'total countries are in a Restcountry api are:{len(response)}')
        #print("we will get all the contents in endpoint in json format:")
        #print(response)

    # create method a that will display name of countries, currency and currency symbols
    def get_name_currencies(self, name_currency):
        request_name = requests.get(name_currency)
        response_name = request_name.json()
        name_list = []
        for api_name in response_name:
            name = api_name["name"]
            currency = api_name['currencies']
            detail = {
                'name': name,
                'curr_name':currency
            }
            name_list.append(detail)
        print("we will get all names,currency,and currency symbol in below list:")
        return name_list
    # create a method that will display all those countries which have Dollar as its currency
    def Dollar_currency(self, url_dollar):
        request_currency = requests.get(url_dollar)
        response_currency = request_currency.json()
        print("These countries are using Dollar as its currency:")
        print(response_currency)
        print(f' total number of countries using Dollar as its currency are:{len(response_currency)}')
    # create a method that will display all those countries which have Euro as its currency
    def Euro_currency(self, url_Euro):
        request_Euro = requests.get(url_Euro)
        response_euro = request_Euro.json()
        list_euro = []
        for list in response_euro:
            name = list['name']['common']
            currency = list['currencies']
            data={
                'name':name,
                'currencies':currency
            }
            list_euro.append(data)
        print("in below list of countries are using Euro as its currency:")
        print(list_euro)
        print(f'total number of countries using Euro as its currency: {len(list_euro)}')

Url = Countries("https://restcountries.com/v3.1/all")

Url.fetch_all_details()
print(Url.get_name_currencies("https://restcountries.com/v3.1/all?fields=name,currencies"))
Url.Dollar_currency("https://restcountries.com/v3.1/currency/USD")
Url.Euro_currency("https://restcountries.com/v3.1/currency/EUR")
