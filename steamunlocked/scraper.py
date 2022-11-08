import requests as r
from bs4 import BeautifulSoup as bs
from models import steamun_db
import time

#COMPLETE
def check_limit(): 
    a = r.get('https://steamunlocked.net/?s=').text
    b = bs(a, 'html.parser').find('nav', {'class':"navigation pagination"}).find('div', {'class':'nav-links'}).findAll('a', {"class":"page-numbers"}) # type: ignore
    c = bs(str(b[-1]), 'html.parser').text
    return int(str(c).replace(',', ''))

d_link = 'https://steamunlocked.net/?s='
def s_link(s):
    return f'https://steamunlocked.net/page/{s}/?s='

def capture(l):
    r_ = r.get(l)
    if r_.status_code != 200:
        return False
    b = bs(r_.text, "html.parser").findAll('div', {"class": "cover-item-title"})
    m = []
    for t in b:
        t = bs(str(t), "html.parser")
        for a in t.findAll('a', href=True):
            m.append(a['href'])
    return list(m)

def capturef_t(f_num, t_num):
    counter =  f_num
    t_list = []
    while counter <= t_num:
        s = capture(s_link(counter))
        if s == False:
            return False
        for i in s: #type: ignore
            t_list.append(i)
        counter += 1
    print(len(t_list))
    # with open('a.txt', 'w') as f:
    #     f.write(str(t_list))
    return t_list

def capturea_f_p():
    s = capturef_t(1, check_limit)
    if s == False:
        return False
    return s

def scrape_content(link):
    r_ = r.get(link)
    if r_.status_code != 200:
        return False
    a = bs(r_.text, 'html.parser').find('div', {'class': 'col-lg-8 main-content no-padding'})
    return a
    with open("a.txt", "w", encoding='utf-8') as f:
        f.write(str(a))

def scrape_upload(link):
    cont = scrape_content(link)
    am_dict = {}
    if cont == False:
        return False
    name = cont.find('h2').text
    num_d = name.find("Free Download")
    if num_d == -1:
        name = name
    else:
        num_d -= 1
        name = name[0:num_d]
    print(name)
    am_dict.update({"name": str(name).lower()})
    link = link
    am_dict.update({"link": str(link)})
    about = cont.find("div", {"id": "game_area_description"})
    if about == None:
        about = None
    else:
        about = about.text
    am_dict.update({"about_game": str(about)})
    m_pic = cont.findAll("img", {"class": "attachment-post-large size-post-large"})
    l_pic = []
    for i in m_pic:
        im = bs(str(i), 'html.parser').find("img")["src"]
        l_pic.append(im)
    am_dict.update({"pictures": l_pic})
    size = cont.find('a', {"class": "btn-download"}).find('em')
    if size == None:
        size = None
        download_link = None
    else:
        size = size.text
        size_ = size.find("size: ")+7
        size = size[size_:]
        download_link = cont.find('a', {"class": "btn-download"})["href"]
    am_dict.update({"size": size})
    am_dict.update({"download_link": download_link})
    t_list = (cont.find('ul').findAll('li'))
    requirements = []
    for i in t_list:
        p = bs(str(i), 'html.parser').text
        requirements.append(p)
    am_dict.update({"Requirements": requirements})
    return am_dict

def upload_to_db(f_num, t_num, all=False):
    list_ = capturef_t(f_num, t_num)
    if all == True:
        list_ = capturea_f_p()
    if list_ == False:
        return False
    n_list = []
    counter = 1
    start = time.time()
    for i in list_:
        print(f"doing {counter}")
        c = scrape_upload(i)
        if c == False:
            return False
        n_list.append(c)
        counter += 1
    end = time.time()
    print(f"finishing processing in {end-start} seconds")
    print("started inserting to database")
    di = steamun_db(n_list)
    if di == False:
        print("failed to insert")
        return False
    print("done inserting to database")
    return True

print(upload_to_db(1,20))