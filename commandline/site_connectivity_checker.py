import time
import requests
import validators
import asyncio


def get_url():
    while True:
        site_url = input("Enter the Site URL: ")
        if validators.url(site_url) == True:
                break
        else:
            print("Error: Enter proper url")
    return site_url
        
async def check_url_status(site_url):
    while True:
        response = requests.get(site_url)
        if response.status_code != 200:
            print(f"{site_url} : DOWN")
        else:
            print(f"{site_url} : UP")
        await asyncio.sleep(5)


if __name__ == "__main__":
    site_url = get_url()
    try:
        asyncio.run(check_url_status(site_url))
    except KeyboardInterrupt as err:
            print("Exiting the URL checker...")