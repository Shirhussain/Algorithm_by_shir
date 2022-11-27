import concurrent.futures
import requests
import threading
import time


thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
        return thread_local.session


def download_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f"read {len(response.content)} lines of {url}")


def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)


if __name__ == "__main__":
    sites = [
        "https://www.google.com", "https://www.facebook.com"
    ]*100
    start = time.perf_counter()
    download_all_sites(sites)
    end = time.perf_counter()
    result = end - start
    print(f"it's take {result} seconds to download all {len(sites)} sites")
