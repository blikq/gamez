import requests as r
from bs4 import BeautifulSoup as bs

# def do(f_num:int, t_num:int):
#     if f_num <= t_num:
#         l = []
#         while f_num <= t_num:
#             p = r.get(f'https://fitgirl-repacks.site/all-my-repacks-a-z/?lcp_page0={f_num}#lcp_instance_0').text
#             d = bs(p, 'html.parser')
#             f = d.find('article').find('div').find('ul').find_all('li')
#             # print(type(l))
#             for i in f:
#                 l.append(i)
#             f_num += 1
#         m = []

#         for i in l:
#             y = bs(str(i), 'html.parser').find('li')
#             for a in y.findAll('a', href=True):
#                 m.append(a['href'])

#     print("completed")
#     print(len(m))
#     with open('a.txt', 'w') as obj:
#         obj.write(str(m))

# do(1,3)


# def check_limit():
#     p = r.get(f'https://fitgirl-repacks.site/all-my-repacks-a-z/?lcp_page0=1#lcp_instance_0').text
#     d = bs(p, 'html.parser')
#     f = d.find('article').find('div').find('ul', {'class': 'lcp_paginator'}).findAll('li')[-2]
#     r_ = bs(str(f), 'html.parser')
#     # print(a)
#     m = []
#     for a in r_.findAll('a', title=True):
#         m.append(a['title'])
#     return int(m[0])


# with open("a.txt", "w") as f:
#     f.write(str(c))

def scrape_content(link):
    r_ = r.get(link)
    if r_.status_code != 200:
        return False
    a = bs(r_.text, 'html.parser').find('div', {'class': 'col-lg-8 main-content no-padding'})
    with open("a.txt", "w", encoding='utf-8') as f:
        f.write(str(a))

scrape_content('https://steamunlocked.net/25-marvels-spider-man-remastered-free-download/')