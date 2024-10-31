import pytest
import requests_mock
from api_manager import PostFetcher, UserFetcher

@pytest.fixture
def mock_response():
    with requests_mock.Mocker() as m:
        m.get("https://jsonplaceholder.typicode.com/posts", json=[{"id": 1, "title": "Test1"}])
        m.get("https://jsonplaceholder.typicode.com/users", json=[{"id": 1, "name": "Name1"}])
        yield m

def test_fetch_posts(mock_response):
    post_fetcher = PostFetcher()
    assert post_fetcher.fetch_posts() == [{"id": 1, "title": "Test1"}]

def test_fetch_users(mock_response):
    user_fetcher = UserFetcher()
    assert user_fetcher.fetch_users() == [{"id": 1, "name": "Name1"}] 
