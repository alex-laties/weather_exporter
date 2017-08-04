#!/usr/bin/env python

import os

cities = [
  {"name": "high camp", "latitude":"46.24106","longitude":"-121.52402"},
  {"name": "night 2", "latitude":"46.25634","longitude":"-121.47889"},
  {"name": "night 3", "latitude":"46.24971","longitude":"-121.52238"},
  {"name": "summit", "latitude":"46.2024","longitude":"-121.4910"},
  {"name": "portland", "latitude":"45.5231","longitude":"-122.6765"},
  {"name": "brooklyn", "latitude":"40.6782","longitude":"-73.9442"},
  {"name": "san francisco", "latitude":"37.7749","longitude":"-122.4194"},
]

def get():
  dark_sky_api_uri = os.getenv('DARK_SKY_API_URI', 'https://api.darksky.net/forecast')
  dark_sky_api_key = os.getenv('DARK_SKY_API_KEY')
  if not dark_sky_api_key:
    print "Unable to start; make sure to export your api key. See readme"
    exit(1)

  return {
    'dark_sky_api_url': "{0}/{1}".format(dark_sky_api_uri,dark_sky_api_key),
    'scrape_interval': int(os.getenv('SCRAPE_INTERVAL', 600)),
    'endpoint_port': int(os.getenv('ENDPOINT_PORT', 9265)),
    'geocode_timeout': int(os.getenv('GEOCODE_TIMEOUT', 10)),
    'cities': cities
  }