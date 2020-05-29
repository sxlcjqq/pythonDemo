# -*- coding:utf-8 -*-
import urllib2
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def main(cid):
  url = host + '/api/v1/lms/product/get_course_detail/?cid='+cid
  user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
  h = { 'User-Agent' : user_agent ,
  'x-client': 'web',
  'x-csrftoken': 'DZd4k210iltJ8vYxcPQ1dkTBQQT2D6JM',
  'cookie': '_ga=GA1.2.2041386423.1588757485; UM_distinctid=171f1f7a5fa460-0d09bf9212e91c-30667701-1fa400-171f1f7a5fb5a9; _log_user_id=256a92d2e8fdaea7ffa3624063fddfdc; frontendUserTrackPrev=51424; django_language=zh-cn; sharesessionid=ba38555ff8ac3407a21271a735a62119; frontendUserTrack=51427; frontendUserReferrer=http://www.xuetangx.com/event/snatc; _gid=GA1.2.953496377.1590563775; login_type=P; csrftoken=DZd4k210iltJ8vYxcPQ1dkTBQQT2D6JM; sessionid=xipzxm39tkukv7h5a69ar7cyigg3xugi; k=21454808; _gat_gtag_UA_164784773_1=1',
  'django-language':'zh',
  'xtbz': 'xt'}

  req = urllib2.Request(url,headers=h)
  response = urllib2.urlopen(req)
  responseData = json.loads(response.read())
  print '>>>>  name：'+responseData['data']['basic_data']['name']
  responseData = responseData['data']['content_data']['chapter_list']
  print '>>>>  章节：'
  print ''
  for chapter in responseData:
    print chapter['name']
    for section in chapter['section_list']:
      print '  '+section['name']



host = 'https://next.xuetangx.com'
# cids = ['1515450']
print "请输入班级id数组，形如：['1515450','1515450']"
cids = input("");
print "你输入的内容是: ", cids
for cid in cids:
  print '-----------------------------------------------'
  print '-----------------------------------------------'
  print '>>>>  班级id：'+cid
  main(cid)

