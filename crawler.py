# coding:utf8
import requests
import json
import re
def main(url):
    for i in range(1, 100):
        data = {
            'page': str(i),
            'rec_way': '1',
        }
    # 使用requests发送post请求
        resp = requests.post(url, data=data).text
        info = json.loads(resp)
    # 工作地点正则匹配四川-成都或全国-所有省市
        pattern1 = re.compile(r'四川-成都|全国-所有省市')
    # 职位名称正则匹配Java或java或JAVA
    #     pattern2 = re.compile(r'Java|java|JAVA')
    # 发布时间正则匹配2017
        pattern3 = re.compile(r'2017')
        for item in info['data']:
            result1 = re.search(pattern1, item['rec_work_place'])
            # result2 = re.search(pattern2, item['rec_title'])
            result3 = re.match(pattern3, item['rec_publish_time'])
            if result1 and result3:
                print("序号:%s 工作地点:%s  职位名称:%s  公司名称:%s  发布日期:%s" % (item['rec_No'], item['rec_work_place'], item['rec_title'],  item['rec_enter_name'],  item['rec_publish_time']))


if __name__ == '__main__':
    url = 'http://www.jiuye.org/new/sys/fore.php?op=listRecruit'
    main(url)
