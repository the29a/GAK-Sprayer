# GAK-Sprayer

Simple Google APIs token checker.

Used to determine whether or not a leaked/found Google API key is vulnerable to unauthorized access by other applications.

## Note
Most of Bug-bounty platformplatforms mark this type of vulnerability as informational/low impact. If you're passing this off as a bug, double-check the find and impact.

## Usage
### Local
Clone repo:
```
git clone https://github.com/the29a/GAK-Sprayer
```
Or
```
gh repo clone the29a/GAK-Sprayer
```
Run:
```
python3 gak-sprayer.py
```
### Docker
To-do.

## Current APIs support:
- [+] [Safe Browsing API](https://developers.google.com/safe-browsing/v4)
- [+] [FCM API](https://firebase.google.com/docs/reference/fcm/rest)
- [+] [Books API](https://developers.google.com/books) [Using the API](https://developers.google.com/books/docs/v1/using)
- [+] [Custom Search API](https://developers.google.com/custom-search/v1/overview)
- [+] [Directions API](https://developers.google.com/maps/documentation/directions/overview)
- [+] [Elevation API](https://developers.google.com/maps/documentation/elevation/start)
- [+] [Find Place From Text API](https://developers.google.com/maps/documentation/places/web-service/search-find-place)
- [+] [Distance Matrix API](https://developers.google.com/maps/documentation/distance-matrix/overview)
- [+] [Geocoding API](https://developers.google.com/maps/documentation/geocoding/overview)
- [+] [Geolocation API](https://developers.google.com/maps/documentation/geolocation/overview)
- [+] [Maps Embed API](https://developers.google.com/maps/documentation/embed/get-started)
- [+] [Nearby Search API](https://developers.google.com/maps/documentation/places/web-service/search-nearby)
- [+] [Nearest Roads API](https://developers.google.com/maps/documentation/roads/nearest)
- [+] [Place Autocomplete API](https://developers.google.com/maps/documentation/javascript/place-autocomplete)
- [+] [Place Details API](https://developers.google.com/maps/documentation/places/web-service/details)
- [+] [Place Photo API](https://developers.google.com/maps/documentation/places/web-service/photos)
- [+] [Directions API](https://developers.google.com/maps/documentation/directions/overview)
- [+] [Snap to Roads API](https://developers.google.com/maps/documentation/roads/snap)
- [+] [Speed Limits API](https://developers.google.com/maps/documentation/roads/speed-limits)
- [+] [Street View Static API](https://developers.google.com/maps/documentation/streetview/overview)
- [+] [Text Search Places API](https://developers.google.com/maps/documentation/places/web-service/search-text)
- [+] [Timezone API](https://developers.google.com/maps/documentation/timezone/overview)

Non-actual:  
- [?] [Maps Embed Advanced API](https://developers.google.com/maps/documentation/embed/get-started)
- [?] [Maps Static API](https://developers.google.com/maps/documentation/maps-static/overview) (embed static maps)
- [?] [Playable Locations API](https://developers.google.com/maps/documentation/gaming/overview_locations) deprecated as of October 18, 2021

---
Google API:  
[Google Cloud APIs](https://cloud.google.com/apis?hl=en)  
[Google APIs Explorer](https://developers.google.com/apis-explorer)  

---
Similar and related projects:  
[gmapsapiscanner](https://github.com/ozguralp/gmapsapiscanner/)  
[fcm-takeover](https://github.com/MazX0p/fcm-takeover/)  