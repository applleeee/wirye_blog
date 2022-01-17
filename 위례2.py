from bs4 import BeautifulSoup
from selenium import webdriver
import csv

url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
keywords = [
'위례고국어',
'위례고국어내신',
'한빛고국어',
'한빛고국어내신',
'덕수고국어',
'덕수고국어내신',
'위례덕수고 국어',
'위례중앙중 국어',
'위례중앙중학교 국어',
'위례중앙중 국어학원',
'한빛중 국어',
'위례한빛중 국어',
'한빛중 국어학원',
'위례중 국어',
'위례중학교 국어',
'위례중 국어학원',
'송례중 국어',
'위례송례중 국어',
'송례중 국어학원',
'위례국어',
'위례국어학원',
'위례고등국어',
'위례고등국어학원',
'위례중등국어',
'위례중등국어학원',
'위례수능국어',
'위례수능국어학원',
'위례독서논술',
'위례중앙타워 국어',
'위례중앙타워 국어학원',
'위례중앙타워 송현국어',
'위례동국어',
'위례동국어학원',
'성남국어',
'성남국어학원',
'수정구국어',
'수정구국어학원',
'창곡동국어',
'창곡동국어학원',
'장지동국어',
'장지동국어학원',
'위례고수학',
'위례고수학내신',
'한빛고수학',
'한빛고수학내신',
'덕수고수학',
'덕수고수학내신',
'위례덕수고 수학',
'위례중앙중 수학',
'위례중앙중학교 수학',
'위례중앙중 수학학원',
'한빛중 수학',
'위례한빛중 수학',
'한빛중 수학학원',
'위례중 수학',
'위례중학교 수학',
'위례중 수학학원',
'송례중 수학',
'위례송례중 수학',
'송례중 수학학원',
'위례수학',
'위례수학학원',
'위례고등수학',
'위례고등수학학원',
'위례중등수학',
'위례중등수학학원',
'위례초등수학',
'위례초등수학학원',
'위례경시',
'위례경시대회',
'위례영재교육',
'위례중앙타워 수학',
'위례중앙타워 수학학원',
'위례중앙타워 하늘교육',
'위례중앙타워 학원',
'위례동수학',
'위례동수학학원',
'성남수학',
'성남수학학원',
'수정구수학',
'수정구수학학원',
'창곡동수학',
'창곡동수학학원',
'장지동수학',
'장지동수학학원',
]

browser = webdriver.Chrome("C:/Users/user/Naver MYBOX/코딩/python/naver_blog/chromedriver.exe")
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
        print("검색중")
        li = blog.find_parent("li")
        rank = blog.find_parent("li")["data-cr-rank"]
        title = li.find("a", {"class" : "api_txt_lines total_tit _cross_trigger"}).text
        dic1 = {"keyword" : keyword, "rank" : rank, "title" : title}
        a.append(dic1)
        for b in a:
            writer.writerow(b.values())

    else:
        print("순위없음")
        dic2 = {"keyword" : keyword, "rank" : "순위없음", "title" : "게시물없음"}
        a.append(dic2)
        for c in a:
            writer.writerow(c.values())
