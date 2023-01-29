import argparse

from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary
import re
import copy
from datetime import datetime
import time
import telegram_send
import requests

hour_reg = re.compile("(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]")

url = "https://www.olx.pl/d/nieruchomosci/stancje-pokoje/krakow/q-pok%C3%B3j/?search%5Border%5D=created_at:desc"
telegram_group_id = '-627491859'
authentication_token = '5798349801:AAFSas7UHkLtgrkeb2-JN6J0KvYt1yHIlV4'
refresh_rate = 60


cookie_handler = driver.find_element(By.ID, "onetrust-accept-btn-handler")
cookie_handler.click()


def get_driver(path, url):
    driver = webdriver.Chrome(executable_path=path).
    driver.get(url)
    return driver


def prepare(args):
    offers = driver.find_elements(By.CLASS_NAME, "css-19ucd76")
    dates = []
    for o in offers:
        try:
            date_details = o.find_element(By.CSS_SELECTOR, "p.css-p6wsjo-Text.eu5v0x0")
            dates.append(date_details.text)
        except Exception:
            pass

    buffer = copy.copy(offers)
    buffer_text = [b.text for b in buffer]


def scrap_refresh(driver, refresh_rate, auth_token, group_id):
    while True:
        print("searching...")
        offers = driver.find_elements(By.CLASS_NAME, "css-19ucd76")
        for o in offers:
            try:
                if (o.text not in buffer_text) and (re.search(r"Dzisiaj", o.text)) and (not re.search(r'Odświeżono', o.text)):
                    buffer.insert(0, o)
                    buffer_text.insert(0, o.text)
                    found = hour_reg.search(o.text)
                    print(found.group())
                    print(o.text, "CURRENT_TIME:", datetime.now())
                    found_url = o.find_element(By.CSS_SELECTOR, "a.css-1bbgabe").get_attribute('href')
                    message = f'{found.group()}, {found_url}'
                    url_telegram = f'https://api.telegram.org/bot{auth_token}/sendMessage?chat_id={group_id}&text={message}'
                    out = requests.get(url_telegram)
            except Exception:
                pass
        time.sleep(refresh_rate)
        driver.refresh()


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type=str)
    parser.add_argument('--group_id', type=str, help=("telegram group"))
    parser.add_argument('--auth_token', type=str)
    parser.add_argument('--refresh_rate', type=int, default=60)
    parser.add_argument('--driver_path', type=str, default="./chromedriver/chromedriver.exe")
    args = parser.parse_known_args()[0]
    return args


def scrap(args):
    driver = get_driver(args.driver_path, args.url)
    prepare(args)
    scrap_refresh(driver, args.refresh_rate, args.auth_token, args.group_id)


if __name__ == "__main__":
    args = get_args()
    scrap(args)
