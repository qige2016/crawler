# coding:utf8
import requests
import re

def get_content(page):
    # url = 'https://xiaoyuan.zhaopin.com/full/538/0_0_160000_1_0_0_0_1_0'
    url ='http://sou.zhaopin.com/jobs/searchresult.ashx?jl=全国&kw=python&p='+ str(page)+'&kt=3'
    a = requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0'
    }).content
    html = a.decode('utf8')
    return html
def parse_html(html):
    reg = re.compile(r'<td class="zwmc.*?<a.*?>(.*?)</a>.*?<td class="gsmc.*?_blank">(.*?)</a>.*?<td class="zwyx">(.*?)</td.*?<td class="gzdd">(.*?)</td.*?<td class="gxsj"><span>(.*?)</span>',re.S)  # 匹配换行符
    results = re.findall(reg, html)
    rs_data = []
    for rs in results:
        remove_b = re.compile(r'<.*?>', re.S)
        name = re.sub(remove_b, '', rs[0])
        rs_tp = (name, rs[1], rs[2], rs[3], rs[4])
        rs_data.append(rs_tp)
    return rs_data
def main():
    for i in range(1, 80):
        html = get_content(1)
        items = parse_html(html)
        for item in items:
            print("工作地点:%s  职位名称:%s  公司名称:%s  发布日期:%s"% (item[3], item[0], item[1],  item[4]))
if __name__ == '__main__':
    main()