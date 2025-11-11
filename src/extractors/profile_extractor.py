thonimport requests

class ProfileExtractor:
    def __init__(self, base_url="https://api.tiktok.com"):
        self.base_url = base_url
        self.session = requests.Session()

    def get_profile_data(self, username):
        url = f"{self.base_url}/profile/{username}"
        response = self.session.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch profile {username}: {response.status_code}")