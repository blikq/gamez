import requests as r
from bs4 import BeautifulSoup as bs

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
    with open('a.txt', 'w') as f:
        f.write(str(t_list))

def capturea_f_p():
    s = capturef_t(1, check_limit)
    if s == False:
        return False
    return True

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
    am_dict.update({"name": str(name)})
    link = link
    am_dict.update({"link": str(link)})
    about = cont.find("div", {"id": "game_area_description"}).text
    am_dict.update({"about_game": str(about)})
    # m_pic = cont.find("img", {"class": "attachment-post-large size-post-large"})
    m_pic = cont.findAll("img", {"class": "attachment-post-large size-post-large", "src": True})
    am_dict.update({"main_pic": m_pic[0]["src"]})
    print(am_dict)

scrape_upload('https://steamunlocked.net/car-dealership-simulator-free-download/')