# Streamlabs Water Monitor Python Library

This is an unofficial Python library for the [Streamlabs Water Monitor](https://www.streamlabswater.com/).

This library can be used to retrieve water usage and manage the away mode of your location.

## Installation

The easiest way to istall the library is via pip:

    $ pip install streamlabswater

## Getting Started

Usage is pretty simple but you can check out some sample usage via the examples directory.

### Getting an API Key

The first thing you will need to do is request an API key for your account. Follow the instructions on the [Streamlabs Getting Started](https://developer.streamlabswater.com/docs/getting-started.html) page to request your API key. The library supports the API key mode of authentication, so make sure you follow the steps to request that (OAUTH2 is not currently supported).

### Write Your Application

Once you have your API key you are ready to start using the library. The first step is to import the module and pass your API key to the client:

    from streamlabswater import streamlabswater
    
    api_key = "YOUR_API_KEY"
    client = streamlabswater.StreamlabsClient(api_key)

To retrieve water usage or change the away mode of your location you'll first need to determine its locationId.  The `get_locations` method is great for determining your available locations and their locationId.  The following retrieves the locationId for the first available location:

    location_id = client.get_locations()['locations'][0]['locationId']

With this we can now query the current water usage summary:

    water_usage = client.get_water_usage_summary(location_id)
    
    gallons_today = water_usage['today']
    gallons_this_month = water_usage['thisMonth']
    gallons_this_year = water_usage['thisYear']

Or retrieve the current away mode for the location:

    location = client.get_location(location_id)
    home_or_away = location['homeAway']
    if home_or_away == 'home':
        print("away mode not activated")
    else if home_or_away == 'away':
        print("away mode is activated")

Finally we can use the locationId to change the away mode for the location:

    client.update_location(location_id, "away")
