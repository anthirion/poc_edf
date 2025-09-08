import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

base_url = "https://api.countrylayer.com/v2"


def get_country_data(country: str) -> dict:
  url = f"{base_url}/name/{country}?access_key={api_key}&fullText=true"
  response = requests.get(url)
  if response.status_code == 200:
    data = response.json()
    if data:
      return data[0]
  return {}


def get_capital_city(data: dict) -> str:
  return data.get("capital", "N/A")


def get_region(data: dict) -> str:
  return data.get("region", "N/A")


if __name__ == "__main__":
  countries = ["France",
               "Canada",
               "Brazil",
               ]

  for country in countries:
    country_data = get_country_data(country)
    capital = get_capital_city(country_data)
    region = get_region(country_data)
    print(f"{capital} is the capital city of {country}")
    print(f"{country} is in {region}")
