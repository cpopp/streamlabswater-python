import requests


class StreamlabsClient(object):
    __STREAMLABS_API_URL = "https://api.streamlabswater.com/v1"

    __api_key = None

    def __init__(self, api_key: str):
        """StreamLabs Water Client

        :param api_key: API key granting access to the API
        """
        self.__api_key = api_key

        if self.__api_key is None:
            raise ValueError("API key is required")

    def get_locations(self) -> dict:
        """Retrieves information for all locations

        :return: dictionary containing information for all locations
        """
        url = self.__STREAMLABS_API_URL + "/locations"
        headers = self.__get_base_headers()

        r = requests.get(url, headers=headers)
        return r.json()

    def get_location(self, location_id: str) -> dict:
        """Retrieves information for a specific location

        :param location_id: id of location to retrieve
        :return: dictionary containing information for the specified location
        """
        url = self.__STREAMLABS_API_URL + "/locations/" + location_id
        headers = self.__get_base_headers()

        r = requests.get(url, headers=headers)
        return r.json()

    def update_location(self, location_id: str, home_or_away: str) -> dict:
        """Updates home/away state of location

        :param location_id: id of location to update
        :param home_or_away: home to indicate location is occupied, away to indicate it is vacant
        :return: dictionary containing updated information for the specified location
        """
        if home_or_away not in ['home', 'away']:
            raise ValueError("home_or_away must be either home or away")

        url = self.__STREAMLABS_API_URL + "/locations/" + location_id
        headers = self.__get_base_headers()

        r=requests.put(url, json={"homeAway": home_or_away}, headers=headers)
        return r.json()

    def get_water_usage_summary(self, location_id: str) -> dict:
        """Retrieves water usage summary for the location

        :param location_id: id of location to retrieve usage for
        :return: dictionary containing usage in gallons for the current day, month, and year
        """
        url = self.__STREAMLABS_API_URL + "/locations/" + location_id + "/readings/water-usage/summary"
        headers = self.__get_base_headers()

        r=requests.get(url, headers=headers)
        return r.json()


    def __get_base_headers(self):
        """Create headers common to all requests"""
        headers = {
            "Authorization": "Bearer {}".format(self.__api_key)
        }

        return headers
