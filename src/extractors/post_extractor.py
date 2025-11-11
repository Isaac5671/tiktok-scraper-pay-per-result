thonimport requests

class PostExtractor:
    def __init__(self, base_url="https://api.tiktok.com"):
        self.base_url = base_url
        self.session = requests.Session()

    def get_post_data(self, post_id):
        url = f"{self.base_url}/post/{post_id}"
        response = self.session.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch post {post_id}: {response.status_code}")