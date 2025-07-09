""" https://nekosia.cat/ ## All documentation """

import requests
import os
from dotenv import load_dotenv

load_dotenv()

class GiphyAPI:
  BASE_URL = "https://api.giphy.com/v1/gifs"
  API_KEY = os.getenv("API_KEY_GIPHY")

  def __init__(self):
    self.session = requests.Session()

  def esposo_de(self):
    print(self.API_KEY)
    url = f"{self.BASE_URL}/search"
    params = {
      "api_key": self.API_KEY,
      "q": "cristiano ronaldo",
    }
    try:
      response = self.session.get(url, params=params, timeout=10)
      response.raise_for_status()
      return response.json()
    except requests.exceptions.RequestException as e:
      print(f"Error fetching gif: {e}")
      return None

  def search_gif(self, gif_name):
    print(self.API_KEY)
    url = f"{self.BASE_URL}/search"
    params = {
      "api_key": self.API_KEY,
      "q": gif_name,
    }
    try:
      response = self.session.get(url, params=params, timeout=10)
      response.raise_for_status()
      return response.json()
    except requests.exceptions.RequestException as e:
      print(f"Error fetching gif: {e}")
      return None
  
  def trending_gif(self):
    print(self.API_KEY)
    url = f"{self.BASE_URL}/trending"
    params = {
      "api_key": self.API_KEY,
    }
    try:
      response = self.session.get(url, params=params, timeout=10)
      response.raise_for_status()
      return response.json()
    except requests.exceptions.RequestException as e:
      print(f"Error fetching gif: {e}")
      return None
    