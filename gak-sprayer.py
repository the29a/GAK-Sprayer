import requests
import sys
import os
import urllib3
import re


urllib3.disable_warnings()
'''
https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
'''

def api_spraying(apikey):
	# Staticmaps API https://developers.google.com/maps/documentation/maps-static/overview
	url = "https://maps.googleapis.com/maps/api/staticmap?center=45%2C10&zoom=7&size=400x400&key=" + apikey 
	response = requests.get(url, verify=False)
	if response.status_code == 200:
		print("- [+] Staticmap API - API key is valid. PoC link to use directly in browser:")
		print("- [+]", url, "\n")
	else:
		print("- [-] Staticmap API - API key is not valid.")
		print("- [-] Reason: " + str(response.text) + "\n")

	# Book API https://developers.google.com/books
	url = "https://www.googleapis.com/books/v1/volumes?q=flowers+inauthor:keyes&key="+apikey
	response = requests.get(url, verify=False)
	if response.status_code == 200:
		print("- [+] Book API - API key is valid. PoC link to use directly in browser:")
		print("- [+]", url, "\n")
	elif response.status_code == 403:
		print("- [-] Books API has not been used in project before or it is disabled")
		print("- [-] Reason: " + str(response.json()["error"]["message"]) + "\n")
	else:
		print("- [-] Book API - API key is not valid.")
		print("- [-] Reason: " + str(response.json()["error"]["message"]) + "\n")


	# Custom Search JSON API https://developers.google.com/custom-search/v1/overview
	url = "https://www.googleapis.com/customsearch/v1?cx=017576662512468239146:omuauf_lfve&q=lectures&key=" + apikey
	response = requests.get(url, verify=False)
	if response.status_code == 200:
		print("- [+] Custom Search API - API key is valid. PoC link to use directly in browser:")
		print("- [+]", url, "\n")
	elif response.status_code == 403:
		print("- [-] Custom Search API has not been used in project before or it is disabled" + "\n")
		print("- [-] Reason: " + str(response.json()["error"]["message"]) + "\n")
	else:
		print("- [-] Custom Search API - API key is not valid.")
		print("- [-] Reason: " + str(response.json()["error"]["message"]) + "\n")

	# Directions API https://developers.google.com/maps/documentation/directions/overview
	url = "https://maps.googleapis.com/maps/api/directions/json?origin=Toronto&destination=Montreal&key=" + apikey
	response = requests.get(url, verify=False)
	if response.text.find("error_message") < 0:
		print("- [+] Directions API - API key is valid. PoC link to use directly in browser:")
		print("- [+]", url, "\n")
	elif response.status_code == 403:
		print("- [-] Directions API has not been used in project before or it is disabled")
	else:
		print("- [-] Directions API - API key is not valid or disabled.")
		print("- [-] Reason: " + str(response.json()["error_message"]) + "\n")

	# Elevation API https://developers.google.com/maps/documentation/elevation/start
	url = "https://maps.googleapis.com/maps/api/elevation/json?locations=39.7391536%2C-104.9847034&key=" + apikey
	if response.text.find("error_message") < 0:
		print("- [+] Elevation API - API key is valid. PoC link to use directly in browser:")
		print("- [+]", url, "\n")
	elif response.status_code == 403:
		print("- [-] Elevation API has not been used in project before or it is disabled")
	else:
		print("- [-] Elevation API - API key is not valid or disabled.")
		print("- [-] Reason: " + str(response.json()["error_message"]) + "\n")

	# FCM API https://firebase.google.com/docs/reference/fcm/rest
	'''
	https://firebase.google.com/docs/cloud-messaging/http-server-ref
	HTTP legacy APIs was deprecated on June 20, 2023, and will be removed in June 2024.
	'''
	url = "https://fcm.googleapis.com/fcm/send"
	postdata = "{'registration_ids':['XYZ']}"
	response = requests.post(url, data=postdata, verify=False, headers={'Content-Type':'application/json','Authorization':'key='+apikey})
	if response.status_code == 200:
		print("- [+] FCM API - API key is valid. PoC link to use directly in browser:")
		# https://gist.github.com/uzeyirdestan/cbe20b7d95be4f962a8f17737c77267c#file-checkapikey-sh
		print("curl --header \"Authorization:key="+apikey+"\" --header Content-Type:\"application/json\" -s -d '{\"registration_ids\":[\"XYZ\"]}' https://fcm.googleapis.com/fcm/send")
	else:
		print("- [-] FCM API - API key is not valid or disabled.")
		if response.text.find("INVALID_KEY_TYPE"):
			print("- [-] Reason: Invalid Key Type." + "\n")
		else:
			print("- [-] Reason: Unexpected error." + "\n")

	#Find Place From Text API https://developers.google.com/maps/documentation/places/web-service/search-find-place
	url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Museum%20of%20Contemporary%20Art%20Australia&inputtype=textquery&fields=formatted_address%2Cname%2Crating%2Copening_hours%2Cgeometry&key=" + apikey
	response = requests.get(url, verify=False)
	if response.text.find("error_message") < 0:
		print("- [+] Find Place From Text API - API key is valid. PoC link to use directly in browser:")
		print("- [+]", url, "\n")
	elif response.status_code == 403:
		print("- [-] Find Place From Text API has not been used in project before or it is disabled")
		print("- [-] Reason: " + str(response.json()["error_message"]) + "\n")
	else:
		print("- [-] Find Place From Text API - API key is not valid or disabled.")
		print("- [-] Reason: " + str(response.json()["error_message"]) + "\n")

	# Distance Matrix API https://developers.google.com/maps/documentation/distance-matrix/overview
	url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=Seattle&destinations=San+Francisco&key=" + apikey
	response = requests.get(url, verify=False)
	if response.text.find("error_message") < 0:
		print("- [+] Distance Matrix API - API key is valid. PoC link to use directly in browser:")
		print("- [+]", url, "\n")
	elif response.status_code == 403:
		print("- [-] Distance Matrix API has not been used in project before or it is disabled")
		print("- [-] Reason: " + str(response.json()["error_message"]) + "\n")
	else:
		print("- [-] Distance Matrix API - API key is not valid or disabled.")
		print("- [-] Reason: " + str(response.json()["error_message"]) + "\n")

	# Geocoding API https://developers.google.com/maps/documentation/geocoding/overview
	url = "https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=" + apikey
	response = requests.get(url, verify=False)
	if response.text.find("error_message") < 0:
		print("- [+] Geocoding API - API key is valid. PoC link to use directly in browser:")
		print("- [+]", url, "\n")
	elif response.status_code == 403:
		print("- [-] Geocoding API has not been used in project before or it is disabled")
		print("- [-] Reason: " + str(response.json()["error_message"]) + "\n")
	else:
		print("- [-] Geocoding API - API key is not valid or disabled.")
		print("- [-] Reason: " + str(response.json()["error_message"]) + "\n")

	# Geolocation API https://developers.google.com/maps/documentation/geolocation/overview
	url =  "https://www.googleapis.com/geolocation/v1/geolocate?key="
	postdata = '{"homeMobileCountryCode":310, "homeMobileNetworkCode":410, "radioType":"gsm",   "carrier":"Vodafone",   "considerIp":true}'
	response = requests.post(url+apikey, data=postdata, verify=False, headers={'Content-Type':'application/json'})
	if response.status_code == 200:
		print("- [+] Geolocation API - API key is valid. PoC link to use directly in browser:")
		print("- [+]", url, "\n")
	elif response.status_code == 403:
		print("- [-] Geolocation API has not been used in project before or it is disabled")
		print("- [-] Reason: " + str(response.json()["error"]["message"]) + "\n")
	else:
		print("- [-] Geolocation API - API key is not valid or disabled.")
		print("- [-] Reason: " + str(response.json()["error"]["message"]) + "\n")

	# Maps Embed API https://developers.google.com/maps/documentation/embed/get-started
	url = "https://www.google.com/maps/embed/v1/place?q=place_id:ChIJzVO_VEcfLIgRkB4jxyh7AwU&key=" + apikey
	response = requests.get(url, verify=False)
	if response.status_code == 200:
		print("- [+] Maps Embed API - API key is valid. PoC link to use directly in browser:")
		print("- [+]", url, "\n")
	else:
		print("- [-] Maps Embed API has not been used in project before or it is disabled")
		print("- [-] Reason:", "Status code", response.status_code, "\n")


	# Nearby Search API https://developers.google.com/maps/documentation/places/web-service/search-nearby
	url = "https://places.googleapis.com/v1/places/ChIJj61dQgK6j4AR4GeTYWZsKWw?fields=id,displayName&key=" + apikey
	response = requests.get(url, verify=False)
	if response.status_code == 200:
		print("- [+] Nearby Search API - API key is valid. PoC link to use directly in browser:")
		print("- [+]", url, "\n")
	elif response.status_code == 403:
		print("- [-] Nearby Search API has not been used in project before or it is disabled")
		print("- [-] Reason: " + str(response.json()["error"]["message"]) + "\n")
	else:
		print("- [-] Nearby Search API - API key is not valid.")
		print("- [-] Reason: " + str(response.json()["error"]["message"]) + "\n")

	# Nearest Roads API https://developers.google.com/maps/documentation/roads/nearest
	url = "https://roads.googleapis.com/v1/nearestRoads?points=60.170880%2C24.942795%7C60.170879%2C24.942796%7C60.170877%2C24.942796&key=" + apikey
	response = requests.get(url, verify=False)
	if response.status_code == 200:
		print("- [+] Nearest Roads API - API key is valid. PoC link to use directly in browser:")
		print("- [+]", url, "\n")
	elif response.status_code == 403:
		print("- [-] Nearest Roads API has not been used in project before or it is disabled")
		print("- [-] Reason: " + str(response.json()["error"]["message"]) + "\n")
	else:
		print("- [-] Nearest Roads API - API key is not valid.")
		print("- [-] Reason: " + str(response.json()["error"]["message"]) + "\n")

	# Place Autocomplete API https://developers.google.com/maps/documentation/javascript/place-autocomplete (?)

	# Place Details API https://developers.google.com/maps/documentation/places/web-service/details
	url = "https://maps.googleapis.com/maps/api/place/details/json?fields=name%2Crating%2Cformatted_phone_number&place_id=ChIJN1t_tDeuEmsRUsoyG83frY4&key=" + apikey
	response = requests.get(url, verify=False)
	if response.text.find("error_message") < 0:
		print("- [+] Place Details From Text API - API key is valid. PoC link to use directly in browser:")
		print("- [+]", url, "\n")
	elif response.status_code == 403:
		print("- [-] Place Details From Text API has not been used in project before or it is disabled")
		print("- [-] Reason: " + str(response.json()["error_message"]) + "\n")
	else:
		print("- [-] Place Details From Text API - API key is not valid or disabled.")
		print("- [-] Reason: " + str(response.json()["error_message"]) + "\n")

	# Place Photo API https://developers.google.com/maps/documentation/places/web-service/photos
	url = "https://maps.googleapis.com/maps/api/place/details/json?placeid=ChIJcUElzOzMQQwRLuV30nMUEUM&key=" + apikey
	response = requests.get(url, verify=False)
	if response.text.find("error_message") < 0:
		print("- [+] Place Photo From Text API - API key is valid. PoC link to use directly in browser:")
		print("- [+]", url, "\n")
	elif response.status_code == 403:
		print("- [-] Place Photo From Text API has not been used in project before or it is disabled")
		print("- [-] Reason: " + str(response.json()["error_message"]) + "\n")
	else:
		print("- [-] Place Photo From Text API - API key is not valid or disabled.")
		print("- [-] Reason: " + str(response.json()["error_message"]) + "\n")

	# Directions API https://developers.google.com/maps/documentation/directions/overview
	url = "https://maps.googleapis.com/maps/api/directions/json?destination=Montreal&origin=Toronto&key=" + apikey
	response = requests.get(url, verify=False)
	if response.text.find("error_message") < 0:
		print("- [+] Directions API - API key is valid. PoC link to use directly in browser:")
		print("- [+]", url, "\n")
	elif response.status_code == 403:
		print("- [-] Directions API has not been used in project before or it is disabled")
		print("- [-] Reason: " + str(response.json()["error_message"]) + "\n")
	else:
		print("- [-] Directions API - API key is not valid or disabled.")
		print("- [-] Reason: " + str(response.json()["error_message"]) + "\n")

	# Safe Browsing API https://developers.google.com/safe-browsing/v4
	url = "https://safebrowsing.googleapis.com/v4/threatMatches:find?key=" + apikey
	response = requests.post(url+apikey, verify=False, headers={'Content-Type':'application/json'})
	if response.status_code == 200:
		print("- [+] Safe Browsing API - API key is valid. PoC link to use directly in browser:")
		print("- [+]", url, "\n")
	elif response.status_code == 403:
		print("- [-] Safe Browsing API has not been used in project before or it is disabled")
		print("- [-] Reason: " + str(response.json()["error"]["message"]) + "\n")
	else:
		print("- [-] Safe Browsing API - API key is not valid.")
		print("- [-] Reason: " + str(response.json()["error"]["message"]) + "\n")

	# Speed Limits API https://developers.google.com/maps/documentation/roads/speed-limits
	url = "https://roads.googleapis.com/v1/speedLimits?path=38.75807927603043,-9.03741754643809|38.6896537,-9.1770515|41.1399289,-8.6094075&key=" + apikey
	response = requests.get(url, verify=False)
	if response.status_code == 200:
		print("- [+] Speed Limits API - API key is valid. PoC link to use directly in browser:")
		print("- [+]", url, "\n")
	elif response.status_code == 403:
		print("- [-] Speed Limits API has not been used in project before or it is disabled")
		print("- [-] Reason: " + str(response.json()["error"]["message"]) + "\n")
	else:
		print("- [-] Speed Limits API - API key is not valid.")
		print("- [-] Reason: " + str(response.json()["error"]["message"]) + "\n")

	# Street View Static API https://developers.google.com/maps/documentation/streetview/overview
	url = "https://maps.googleapis.com/maps/api/streetview?size=400x400&location=47.5763831,-122.4211769&fov=80&heading=70&pitch=0&signature=321&key=" + apikey
	response = requests.get(url, verify=False)
	if response.status_code == 200:
		print("- [+] treet View Static API - API key is valid. PoC link to use directly in browser:")
		print("- [+]", url, "\n")
	elif response.text.find("Google Maps Platform rejected your request") != -1 :
		print("- [-] Street View Static API has not been used in project before or it is disabled")
		print("- [-] Reason:", response.text, "\n")
	else:
		print("- [-] Street View Static API has not been used in project before or it is disabled")
		print("- [-] Reason:", response.text, "\n")

	# Text Search Places API https://developers.google.com/maps/documentation/places/web-service/search-text
	url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants%20in%20Sydney&key=" + apikey
	response = requests.get(url, verify=False)
	if response.text.find("error_message") < 0:
		print("- [+] Text Search Places API - API key is valid. PoC link to use directly in browser:")
		print("- [+]", url, "\n")
	elif response.status_code == 403:
		print("- [-] Text Search Places API has not been used in project before or it is disabled")
	else:
		print("- [-] Text Search Places API - API key is not valid or disabled.")
		print("- [-] Reason: " + str(response.json()["error_message"]) + "\n")

	# Timezone API https://developers.google.com/maps/documentation/timezone/overview
	url = "https://maps.googleapis.com/maps/api/timezone/json?location=39.6034810,-119.6822510&timestamp=1331161200&key=" + apikey
	response = requests.get(url, verify=False)
	if response.text.find("errorMessage") < 0:
		print("- [+] Timezone API - API key is valid. PoC link to use directly in browser:")
		print("- [+]", url, "\n")
	elif response.status_code == 403:
		print("- [-] Timezone API has not been used in project before or it is disabled")
		print("- [-] Reason: " + str(response.json()["errorMessage"]) + "\n")
	else:
		print("- [-] Timezone API - API key is not valid or disabled.")
		print("- [-] Reason: " + str(response.json()["errorMessage"]) + "\n")

	#  Place Autocomplete API https://developers.google.com/maps/documentation/javascript/place-autocomplete
	url = "https://maps.googleapis.com/maps/api/place/autocomplete/json?input=Bingh&types=%28cities%29&key=" + apikey 
	response = requests.get(url, verify=False)
	if response.text.find("error_Message") != -1:
		print("- [+] Place Autocomplete API - API key is valid. PoC link to use directly in browser:")
		print("- [+]", url, "\n")
	else:
		print("- [-] Place Autocomplete API - API key is not valid or disabled.")
		print("- [-] Reason: " + str(response.json()["error_message"]) + "\n")

	# Snap to Roads API https://developers.google.com/maps/documentation/roads/snap
	url = "https://roads.googleapis.com/v1/snapToRoads?path=-35.27801,149.12958|-35.28032,149.12907&interpolate=true&key=" + apikey 
	response = requests.get(url, verify=False)
	if response.text.find("error") < 0:
		print("- [+] Snap to Roads API - API key is valid. PoC link to use directly in browser:")
		print("- [+]", url, "\n")
	else:
		print("- [-] Snap to Roads API - API key is not valid or disabled.")
		print("- [-] Reason: "+ response.json()["error"]["message"])

def api_spraying_help():
	print("Usage: gak-sprayer.py [OPTION] [APIKEY]")
	print("You can use -a or --api-key as argument.\n")
	print("Example: python3 gak-sprayer.py --api-key AIzaSyCxr...Rb-PzMOV8U4n2q...6e4")

def api_key_check(apikey):
	pattern = re.compile(r'^AIza[0-9A-Za-z_-]{35}$')
	if pattern.match(apikey):
		return True
	else:
	    return False

if len(sys.argv) == 1 or sys.argv[1] in ["--help", "-h"]:
    api_spraying_help()
elif sys.argv[1] in ["-a", "--api-key"]:
	if len(sys.argv) < 3:
		print("Missing API Key.")
		print("You can use -a or --api-key as argument.")
	else:
		api_key = sys.argv[2]
		if api_key_check(api_key):
			api_spraying(api_key)
		else:
			print("Invalid Google API Key.")
else:
	print("Invalid arguments, aborting.")

