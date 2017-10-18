# coding:utf8
import requests
import re
from multiprocessing import Pool
jobarea = '090200'
serch = ' '
def get_content(page):
    url ='http://search.51job.com/list/'+jobarea+',000000,0000,00,9,99,'+serch+',2,'+ str(page)+'.html'
    a = requests.get(url).content
    html = a.decode('gbk')
    return html
def parse_html(html):
    reg = re.compile(r'class="t1 ">.*? <a target="_blank" title="(.*?)".*?<span class="t2"><a target="_blank" title="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*? <span class="t5">(.*?)</span>',re.S)  # 匹配换行符
    items = re.findall(reg, html)
    return items
def main():
    for i in range(1, 80):
        html = get_content(i)
        for item in parse_html(html):
            print("工作地点:%s  职位名称:%s  公司名称:%s  发布日期:%s" % (item[2], item[0], item[1],  item[4]))
            # print(item)

if __name__ == '__main__':
    pool = Pool(processes=4)
    pool.map_async(main())
    pool.close()
    pool.join()
