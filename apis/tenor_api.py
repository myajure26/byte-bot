import requests
import os
from dotenv import load_dotenv

load_dotenv()

class TenorAPI:
  BASE_URL = "https://tenor.googleapis.com/v2"
  API_KEY = os.getenv("API_KEY_TENOR")

  def __init__(self):
    self.session = requests.Session()

  def search_gif(self, gif_name):
    print(self.API_KEY)
    url = f"{self.BASE_URL}/search"
    params = {
      "key": self.API_KEY,
      "q": gif_name,
    }
    try:
      response = self.session.get(url, params=params, timeout=10)
      response.raise_for_status()
      return response.json()
    except requests.exceptions.RequestException as e:
      print(f"Error fetching gif: {e}")
      return None
  
  def featured_gif(self):
    print(self.API_KEY)
    url = f"{self.BASE_URL}/featured"
    params = {
      "key": self.API_KEY,
    }
    try:
      response = self.session.get(url, params=params, timeout=10)
      response.raise_for_status()
      return response.json()
    except requests.exceptions.RequestException as e:
      print(f"Error fetching gif: {e}")
      return None

  def esposo_de(self):
    print(self.API_KEY)
    url = f"{self.BASE_URL}/search"
    params = {
      "key": self.API_KEY,
      "q": "cristiano ronaldo",
    }
    try:
      response = self.session.get(url, params=params, timeout=10)
      response.raise_for_status()
      return response.json()
    except requests.exceptions.RequestException as e:
      print(f"Error fetching gif: {e}")
      return None
    