import requests as r
import time
import re
import json
from bs4 import BeautifulSoup as bs
from models import fitgirl_db

fitgirl = "https://fitgirl-repacks.site/"


def get_name(body):
    div = body.find('div', {'class': 'entry-content'}
                    ).find('h3').find('strong')
    version = div.find('span').extract(
    ).getText() if div.find('span') else None
    name = div.getText()
    id = body.find('span', {'class': 'entry-date'}
                   ).find('a').get('href')[29:-1]
    date = body.find('time', attrs={'datetime': True})['datetime']
    return (name, version, id, date)


def get_data(body):
    try:
        div = body.find('div', {'class': 'entry-content'}).find('p')
    except Exception as e:
        print(e)
        return None
    entries = div.findAll('strong')
    index = 0
    genres = None
    if len(entries) == 5:
        index = 1
        genres = entries[0].getText().split(', ')
    companies = (re.split("[,/-]+", entries[index].getText()))
    companies = [x.strip(' ') for x in companies]
    languages = entries[index+1].getText().split('/')
    originalSize = entries[index+2].getText()
    try:
        repackSize = entries[index+3].getText() if entries[index +
                                                           3].getText().find('from') else entries[index+3].getText()[5:]
    except IndexError:
        repackSize = entries[index +
                             3].getText()[:entries[index+3].getText().find('~')-1]
    selective = ('Selective' in str(div))
    return (originalSize, repackSize, selective, genres, companies, languages)


def get_links(body):
    div = body.find('div', {'class': 'entry-content'})
    links = {}
    try:
        table = div.find('ul').findAll('li')
        for li in table:
            for a in li.findAll('a'):
                if ('JDownloader' in a.getText()):
                    continue
                key = a.getText()
                if links.get(key):
                    key = a.getText()+'_1'
                links[key] = a.get('href')
    except AttributeError:
        p = div.findAll('p')[1].findAll('a')
        for a in p:
            if ('JDownloader' in a.getText()):
                continue
            key = a.getText()
            if links.get(key):
                key = a.getText()+'_1'
            links[key] = a.get('href')
    return links


def get_screenshots(body):
    div = body.find('div', {'class': 'entry-content'})
    screenshots = []
    img = div.findAll('img')
    for screenshot in img:
        if ('riotpixel' in screenshot.get('src')):
            screenshots.append(screenshot.get('src'))
    return screenshots


def game_data_(body):
    #body = get_body(gameID)
    data = get_data(body)
    if data is None:
        return None
    names = get_name(body)
    links = get_links(body)
    screenshots = get_screenshots(body)
    game = {'id': names[2], 'name': str(names[0]).lower(), 'version': names[1], 'date': names[3], 'originalSize': data[0], 'repackSize': data[1],
            'selective': data[2], 'mirrors': links, 'genres': data[3], 'companies': data[4], 'languages': data[5], 'screenshots': screenshots}
    return game


def get_game_with_name(game:str):
    #TODO?: make sure you handle signs and special characters
    game = game.replace(' ', '-')
    re_ = r.get(fitgirl+game).text
    soup = bs(re_, 'html.parser')
    return game_data_(soup)

def get_game_with_url(game:str):
    re_ = r.get(game).text
    soup = bs(re_, 'html.parser')
    return game_data_(soup)

def check_limit():
    p = r.get(f'https://fitgirl-repacks.site/all-my-repacks-a-z/?lcp_page0=1#lcp_instance_0').text
    d = bs(p, 'html.parser')
    f = d.find('article').find('div').find('ul', {'class': 'lcp_paginator'}).findAll('li')[-2] #type:ignore
    r_ = bs(str(f), 'html.parser')
    # print(a)
    m = []
    for a in r_.findAll('a', title=True):
        m.append(a['title'])
    return int(m[0])

def scrape_from_site(f_num:int, t_num:int):
    start = time.time()
    print(f"starting process at {str(start)}")
    if f_num <= t_num:
        l = []
        while f_num <= t_num:
            p = r.get(f'https://fitgirl-repacks.site/all-my-repacks-a-z/?lcp_page0={f_num}#lcp_instance_0').text
            d = bs(p, 'html.parser')           
            f = d.find('article').find('div').find('ul').findAll('li')  # type: ignore
            # print(type(l))
            for i in f:
                l.append(i)
            f_num += 1
        m = []
        
        for i in l:
            y = bs(str(i), 'html.parser').find('li')
            for a in y.findAll('a', href=True): # type: ignore
                m.append(a['href'])
        end = time.time()
        print(f"Took {end-start} seconds to complete")
        print(f"completed scraping from fitgirl...\n{len(m)} links scraped\nstarting data extraction...")
        chunk_data = []
        start_ = time.time()
        count = 1
        links = [] 
        for i in m:
            start = time.time()
            game = get_game_with_url(i)
            links.append(i)
            end = time.time()
            print(f"processes item {count} at {end-start} seconds")
            count += 1
            game.update({"links": i}) #type: ignore
            # print(f"each {game}")
            chunk_data.append(game)
        # game = chunk_data
        # print(f"chunk_Data>>: {chunk_data}")
        end_ = time.time()
        print(f"Took {end_-start_} to process total chunk")
        return chunk_data

    else:
        return False        

def scrape_all_from_site():
    f_num = 1
    t_num = check_limit()
    return scrape_from_site(f_num, t_num)

def upload_t_db(a, b):
    cont = scrape_from_site(a, b)
    fitgirl_db(cont)

upload_t_db(1,4)
# scrape_all_from_site()