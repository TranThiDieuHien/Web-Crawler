# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 11:32:12 2021

@author: DUC-PC
"""

#import thư viện cần dùng
import requests
from bs4 import BeautifulSoup
import re
import os

#Hàm này dùng để đọc nội dung đường dẫn
#Kết quả trả về là nội dung trong đường dẫn 
def doc_noi_dung(url):
    page = requests.get(url).text    #Gửi yêu cầu truy cập url
    content = BeautifulSoup(page, 'html.parser')
    return content

#Hàm này để lấy đường dẫn
#Kết quả trả về là một DS chứa các đường dẫn 
def lay_duong_dan(content):
    
    url_list = []
    result = []
    raw = content.find_all("a")     #Lọc các thẻ <a>
    for item in raw:
        link = item.get("href")     #Lấy ra các đường dẫn trong href
        url_list.append(link)
    for item in url_list:                                           ###
        item = str(item)                                              ###
        if (item.find("http", 0, 4)):                                   ###    Lọc các đường dẫn trong url_list
            if (item.find("java", 0, 4)):                                 ##     Giữ lại các đường dẫn
                if (item.find("#", 0, 4)):                            ##    như https://... và /vn/..
                    if (item.find("None", 0, 4)):                   ###      Rồi thêm vào list Result
                        if len(item) > 2:
                            result.append(item)
        
        if not(item.find("http", 0, 4)):
            result.append(item)
    return result

#Hàm này để kiểm tra đường dẫn: 
    #Hợp lệ: True
    #ko hợp lệ: False
#url: đường dẫn
def kiem_tra_duong_dan(url):
    check = re.search("^http", url)
    try:
        if url == check.string:
            return True
    except:
        return False        
        
#Hàm này để chỉnh sửa đường dẫn chưa hợp lệ
def chinh_sua_duong_dan(url, item): 
    item = str(url) + item    #Thêm https://... vào
    return item


def kiem_tra_url_da_duyet(url):
    path = "C:\\CRAWLER\\"
    os.chdir(path)
    file = open("History.txt", 'r+', encoding='utf-8')
    ds_da_duyet = file.readlines()
    for i in ds_da_duyet:
        if url in i:
            return True
    file.close()
    return False