import requests as r
from bs4 import BeautifulSoup as bs

NUM_PER_PAGE = 50

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


def check_limit():
    p = r.get(f'https://fitgirl-repacks.site/all-my-repacks-a-z/?lcp_page0=1#lcp_instance_0').text
    d = bs(p, 'html.parser')
    f = d.find('article').find('div').find('ul', {'class': 'lcp_paginator'}).findAll('li')[-2]
    r_ = bs(str(f), 'html.parser')
    # print(a)
    m = []
    for a in r_.findAll('a', title=True):
        m.append(a['title'])
    return int(m[0])