#!/usr/bin/python3
# -*- coding:UTF-8 -*-

from moduleCollection import *
url = 'https://www.coinzest.co.kr/app/cxweb/cs/CS1501.jsp'
req = requests.get(url)
bsObj = bs(req.content,'html.parser')
find = bsObj.find('span',{'class':'badge'})
print(find)