import requests
import json

class DataReceiver:
    page = 0

    def __init__(self, url):
        self.url = url
    
    def get_remote_data(self):
        # method get_remote_data should receive the data from wikipedia URL
        response = requests.get(self.url)
        return response.text

    def clean_data(self):
        # method clean_data should remove all none unicode symbols from text and return the cleaned text
        text = self.get_remote_data()
        text_encode = text.encode("ascii", "ignore")
        text_decoded = text_encode.decode()
        return text_decoded

    def return_json_text(self):
        # method return_json_text should return the json object with params: "URL" - input user url, "message" - the cleaned text
        message = self.clean_data()
        json_text = {"URL" : self.url,
                     "message": message}
        return json.dumps(json_text)

    def save_to_file(self):
        # method save_to_file should save the json object to the json file
        json_text = self.return_json_text()
        page = self.distinct_page()
        with open(f"wikipage_data_{page}", "w") as file:
            file.write(json_text)

    @classmethod
    def distinct_page(cls):
        cls.page += 1
        return cls.page        


# print(DataReceiver("https://www.wikipedia.org/").get_remote_data())
# print(DataReceiver("https://www.wikipedia.org/").clean_data())
# print(DataReceiver("https://www.wikipedia.org/").return_json_text())
# print(DataReceiver("https://www.wikipedia.org/").save_to_file())