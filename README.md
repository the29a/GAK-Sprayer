# Google API Key Sprayer

Simple Google APIs token checker.

Used to determine whether or not a leaked/found Google API key is vulnerable to unauthorized access by other applications.

## Note
Most of Bug-bounty platforms mark this type of vulnerability as informational/low impact. If you're passing this off as a bug, double-check the find and impact.

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
#### Build and run:
```
docker build -t gak-sprayer .
docker run --rm -v $(pwd):/home/gak/ -i docker.io/library/gak-sprayer
```
## Current APIs support:
- [x] [Safe Browsing API](https://developers.google.com/safe-browsing/v4)
- [x] [FCM API](https://firebase.google.com/docs/reference/fcm/rest)
- [x] [Books API](https://developers.google.com/books) [Using the API](https://developers.google.com/books/docs/v1/using)
- [x] [Custom Search API](https://developers.google.com/custom-search/v1/overview)
- [x] [Directions API](https://developers.google.com/maps/documentation/directions/overview)
- [x] [Elevation API](https://developers.google.com/maps/documentation/elevation/start)
- [x] [Find Place From Text API](https://developers.google.com/maps/documentation/places/web-service/search-find-place)
- [x] [Distance Matrix API](https://developers.google.com/maps/documentation/distance-matrix/overview)
- [x] [Geocoding API](https://developers.google.com/maps/documentation/geocoding/overview)
- [x] [Geolocation API](https://developers.google.com/maps/documentation/geolocation/overview)
- [x] [Maps Embed API](https://developers.google.com/maps/documentation/embed/get-started)
- [x] [Nearby Search API](https://developers.google.com/maps/documentation/places/web-service/search-nearby)
- [x] [Nearest Roads API](https://developers.google.com/maps/documentation/roads/nearest)
- [x] [Place Autocomplete API](https://developers.google.com/maps/documentation/javascript/place-autocomplete)
- [x] [Place Details API](https://developers.google.com/maps/documentation/places/web-service/details)
- [x] [Place Photo API](https://developers.google.com/maps/documentation/places/web-service/photos)
- [x] [Directions API](https://developers.google.com/maps/documentation/directions/overview)
- [x] [Snap to Roads API](https://developers.google.com/maps/documentation/roads/snap)
- [x] [Speed Limits API](https://developers.google.com/maps/documentation/roads/speed-limits)
- [x] [Street View Static API](https://developers.google.com/maps/documentation/streetview/overview)
- [x] [Text Search Places API](https://developers.google.com/maps/documentation/places/web-service/search-text)
- [x] [Timezone API](https://developers.google.com/maps/documentation/timezone/overview)

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