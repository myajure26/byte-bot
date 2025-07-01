""" https://nekosia.cat/ ## All documentation """

import requests

class NekosAPI:
  BASE_URL = "https://api.nekosia.cat/api/v1"

  def __init__(self):
    self.session = requests.Session()

  def get_random_catgirl(self, categories=None):
    url = f"{self.BASE_URL}/images/catgirl"
    params = {"categories": categories} if categories else {}
    try:
      response = self.session.get(url, params=params, timeout=10)
      response.raise_for_status()
      return response.json()
    except requests.exceptions.RequestException as e:
      print(f"Error fetching catgirl image: {e}")
      return None
