import requests
from typing import Any, Dict, List

class JSONPlaceholderAPI:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def fetch_data(self, endpoint: str) -> List[Dict[str, Any]]:
        response = requests.get(f"{self.BASE_URL}/{endpoint}")
        response.raise_for_status()
        return response.json()

class PostFetcher(JSONPlaceholderAPI):
    def fetch_posts(self) -> List[Dict[str, Any]]:
        return self.fetch_data("posts")

class UserFetcher(JSONPlaceholderAPI):
    def fetch_users(self) -> List[Dict[str, Any]]:
        return self.fetch_data("users")

if __name__ == "__main__":
    post_fetcher = PostFetcher()
    user_fetcher = UserFetcher()
    
    try:
        posts = post_fetcher.fetch_posts()
        users = user_fetcher.fetch_users()
        print("Posts:", posts)
        print("Users:", users)
    except Exception as e:
        print(f"An error occurred: {e}")
  