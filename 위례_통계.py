from bs4 import BeautifulSoup
from selenium import webdriver
import csv

url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
keywords = ['위례국어학원',
'위례국어',
'위례수학학원',
'위례수학']

browser = webdriver.Chrome()
browser.get(url)

file = open("위례키워드.csv", encoding="utf-8-sig", newline="", mode="w")
writer = csv.writer(file)
writer.writerow(["검색어", "순위", "글제목"])


for keyword in keywords:
    a = []
    elem = browser.find_element_by_id("nx_query")
    elem.clear()
    elem.send_keys(keyword)
    elem = browser.find_element_by_class_name("bt_search")
    elem.click()
    soup = BeautifulSoup(browser.page_source, "lxml")

    blog = soup.find("a", {"href": "https://blog.naver.com/wredusky"})
    if blog:
        li = blog.find_parent("li")
        rank = blog.find_parent("li")["data-cr-rank"]
        title = li.find("a", {"class" : "api_txt_lines total_tit _cross_trigger"}).text
        dic1 = {"keyword" : keyword, "rank" : rank, "title" : title}
        a.append(dic1)
        for b in a:
            writer.writerow(b.values())

    else:
        dic2 = {"keyword" : keyword, "rank" : "순위없음", "title" : "게시물없음"}
        a.append(dic2)
        for c in a:
            writer.writerow(c.values())

