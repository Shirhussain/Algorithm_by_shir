import requests
import time


def download_site(url, session):
    with session.get(url) as response:
        print(f"read {len(response.content)} lines of {url}")


def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


if __name__ == "__main__":
    # my_sites = ["www.google.com", "www.facebook.com"]*100
    my_sites = [
        "https://www.google.com",
        "http://www.facebook.com"
    ] * 80
    start = time.perf_counter()
    download_all_sites(my_sites)
    end = time.perf_counter() - start
    print("this is end of time", end)
