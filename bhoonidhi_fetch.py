from pystac_client import Client
from config import API_URL

print("Connecting to Bhoonidhi STAC API...")

catalog = Client.open(API_URL)

print("Connection successful!")
print("API:", API_URL)