import sys

from streamlabswater import streamlabswater

if len(sys.argv) != 2:
    raise ValueError("Expected API key as argument")

api_key = sys.argv[1]
client = streamlabswater.StreamlabsClient(api_key)


def print_location(location):
    location_id = location['locationId']
    name = location['name']
    home_or_away = location['homeAway']
    alerts = location['alerts']
    subscriptions = location['subscriptionIds']

    print("Location (id={} name={} home_or_away={} alerts={} subscriptions={})".format(location_id, name, home_or_away, alerts, subscriptions))

    for device in location['devices']:
        device_id = device['deviceId']
        device_type = device['type']
        calibrated = device['calibrated']
        connected = device['connected']

        print("\t Device (id={} type={} calibrated={} connected={})".format(device_id, device_type, calibrated, connected))


print("*** 1.) Retrieving Locations")
locations = client.get_locations()

for location in locations['locations']:
    print_location(location)

print()
print("*** 2.) Retrieving Specific Location")
location = client.get_location(locations['locations'][0]['locationId'])

print_location(location)

print()
print("*** 3.) Updating Location Home/Away State")
location_id = location['locationId']
home_or_away = location['homeAway']
location = client.update_location(location_id, "home" if home_or_away == "away" else "away")

print_location(location)

print()
print("*** 4.) Retrieving Water Usage Summary")
location_id = location['locationId']
water_usage = client.get_water_usage_summary(location_id)

gallons_this_year = water_usage['thisYear']
gallons_this_month = water_usage['thisMonth']
gallons_today = water_usage['today']
print("Water Usage in Gallons today={} thisMonth={} thisYear={}".format(gallons_today, gallons_this_month, gallons_this_year))
