"""
Author: Basel Amr Barakat
Email: baselamr52@gmail.com
Date: 2024-12-19
Task Name : File Handling - Working with Threads and APIs
Task Number : 19
Part :  File Handling
Module : Python Programming Language for AI / ML
Submit_Number : 1

Description:
This task covers creating and managing threads to handle concurrent operations.
It also covers how to interact with web APIs using the requests module.

Requirement 1:
Description: 
Create a program that downloads multiple files concurrently using Python’s threading module.

Requirement 2:
Description: 
Use the requests module to interact with a public API (e.g., JSONPlaceholder).
Fetch a list of posts and display the title of each post.

Requirement 3:
Description: 
Create a program that fetches data from multiple APIs concurrently using threads and prints the results.
"""
import threading
import requests
import os
from typing import List

# Requirement 1: Download multiple files concurrently using threading
class FileDownloader:
    """
    A class to handle concurrent downloading of files using threading.
    """
    def __init__(self, file_urls: List[str], save_dir: str):
        self.file_urls = file_urls
        self.save_dir = save_dir

    def download_file(self, url: str):
        """Downloads a file from the given URL."""
        try:
            file_name = url.split("/")[-1]
            response = requests.get(url, stream=True)
            response.raise_for_status()

            with open(os.path.join(self.save_dir, file_name), 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)

            print(f"Downloaded: {file_name}")
        except Exception as e:
            print(f"Error downloading {url}: {e}")

    def download_all(self):
        """Downloads all files concurrently."""
        threads = []
        for url in self.file_urls:
            thread = threading.Thread(target=self.download_file, args=(url,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()


# Requirement 2: Fetch and display post titles from an API
class APIFetcher:
    """
    A class to interact with a public API and fetch data.
    """
    @staticmethod
    def fetch_posts(api_url: str):
        """Fetches posts from the API and prints their titles."""
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            posts = response.json()

            print("\nPost Titles:")
            for post in posts:
                print(f"- {post['title']}")
        except Exception as e:
            print(f"Error fetching posts: {e}")


# Requirement 3: Fetch data from multiple APIs concurrently
class ConcurrentAPIFetcher:
    """
    A class to fetch data from multiple APIs concurrently using threads.
    """
    def __init__(self, api_urls: List[str]):
        self.api_urls = api_urls

    def fetch_data(self, api_url: str):
        """Fetches data from a single API and prints the result."""
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()
            print(f"Data from {api_url}: {data[:3]}...\n")  # Displaying a snippet for brevity
        except Exception as e:
            print(f"Error fetching data from {api_url}: {e}")

    def fetch_all(self):
        """Fetches data from all APIs concurrently."""
        threads = []
        for url in self.api_urls:
            thread = threading.Thread(target=self.fetch_data, args=(url,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()


# Main Function for Interaction
def main():
    print("--- File Downloader ---")
    file_urls = [
    "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv", 
    "https://norvig.com/big.txt",  
    "https://www.gutenberg.org/files/1342/1342-0.txt" 
]
    save_dir = "downloads"

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    downloader = FileDownloader(file_urls, save_dir)
    downloader.download_all()

    print("\n--- API Fetcher ---")
    api_url = "https://jsonplaceholder.typicode.com/posts"
    APIFetcher.fetch_posts(api_url)

    print("\n--- Concurrent API Fetcher ---")
    api_urls = [
        "https://jsonplaceholder.typicode.com/posts",
        "https://jsonplaceholder.typicode.com/albums",
    ]
    concurrent_fetcher = ConcurrentAPIFetcher(api_urls)
    concurrent_fetcher.fetch_all()


if __name__ == "__main__":
    main()
