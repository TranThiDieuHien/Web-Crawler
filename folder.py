# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 15:20:13 2021

@author: DUC-PC
"""
import os 

#Hàm này để kiểm tra và tạo thư mục 
def kiem_tra_folder(path):
    os.chdir(path)  #Di chuển đến thư mục trong đường dẫn path
    check = os.listdir(path)    #List các thư mục hiện có ở ổ C:\
    if 'CRAWLER' not in check:      #Nếu chưa có thư mục CRAWLER thì tạo thư mục CRAWLER
        os.mkdir('CRAWLER')

    #Tạo file History.txt
    path = 'C:\\CRAWLER\\'
    os.chdir(path)  # Di chuển đến thư mục trong đường dẫn path
    check = os.listdir(path)  # List các thư mục hiện có ở ổ C:\CRAWLER

    # Nếu chưa có file History.txt thì tạo thư mục trong CRAWLER
    if 'History.txt' not in check:
        line_1 = "\t+------------------------------------------------------+\n"
        line_2 = "\t|  Đây là file ghi lại lịch sử các url đã cào dữ liệu  |\n"
        line_3 = "\t+------------------------------------------------------+\n\n"
        line_4 = "Số thứ tự của đường link chính là số thứ tự của thư mục chứa nội dung đường dẫn đã cào\n"
        line_5 = "<Ví dụ đường dẫn có số thứ tự 1 thì thư mục chứ nội dung là Các trang web được cào>\n\n"
        content = [line_1, line_2, line_3, line_4, line_5]
        file = open("History.txt", "w", encoding="utf-8")
        for item in content:
            file.write(item)
        file.close()

        
def tao_ten_folder():
    path = "C:\\CRAWLER\\"
    os.chdir(path)
    folder = "Trang_web_được_cào"
    count = len(os.listdir(path)) - 1
    name_folder = folder + str(count)
    os.mkdir(name_folder)
    return name_folder
    
    

#Hàm này để lưu lại các đường dẫn đã lấy vào thư mục vừa tạo
def luu_file(data, name_folder):      
    #data là list chứa nội dung file html
    path = "C:\\CRAWLER\\"
    os.chdir(path + str(name_folder))
    

    

