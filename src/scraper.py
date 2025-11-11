thonimport requests
import json
import time
from datetime import datetime

class TikTokScraper:
    def __init__(self, output_format='json', speed=600, base_url="https://api.tiktok.com"):
        self.output_format = output_format
        self.speed = speed
        self.base_url = base_url
        self.session = requests.Session()

    def scrape_post(self, post_id):
        url = f"{self.base_url}/post/{post_id}"
        response = self.session.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch post {post_id}: {response.status_code}")

    def scrape_profile(self, username):
        url = f"{self.base_url}/profile/{username}"
        response = self.session.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch profile {username}: {response.status_code}")

    def extract_data(self, post_ids, usernames):
        data = []
        for post_id in post_ids:
            post_data = self.scrape_post(post_id)
            data.append(post_data)
            time.sleep(1/self.speed)  # respect the scraping speed limit
        for username in usernames:
            profile_data = self.scrape_profile(username)
            data.append(profile_data)
            time.sleep(1/self.speed)
        return data

    def export_data(self, data):
        if self.output_format == 'json':
            with open('output.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)
        elif self.output_format == 'csv':
            import csv
            with open('output.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(data[0].keys())  # writing header
                for row in data:
                    writer.writerow(row.values())
        else:
            raise ValueError("Unsupported output format")

if __name__ == "__main__":
    scraper = TikTokScraper()
    post_ids = ["7353781970163272993"]
    usernames = ["jacksonstips"]
    data = scraper.extract_data(post_ids, usernames)
    scraper.export_data(data)