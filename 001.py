import requests
from dingtalkchatbot.chatbot import DingtalkChatbot, ActionCard, CardItem
import time

limit = 40#电费提醒限制

area = 6# 楼号

location  = 1#2为北楼，一为南楼

roomid = 203 #房间号

type1 = 2 #南区的同学1为照明，2为空调 

webhook = 'https://oapi.dingtalk.com/robot/send?access_token=XXXXXXX' #替换为自己的钉钉机器人的wehook
secret = 'XXXXXX'  # 替换为自己的钉钉机器人的SECREAT
room = "300"+str(area)+str(roomid)+str(location)+("1" if area <= 5 else str(type1))
flag  = False
timenow = time.localtime(time.time()).tm_hour
myheaders = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Mobile Safari/537.36"
             }
url = "http://172.31.248.26:8988/web/Common/Tsm.html"+"?jsondata=%7B+%22query_elec_roominfo%22%3A+%7B+%22aid%22%3A%220030000000007301%22%2C+%22account%22%3A+%2230629%22%2C%22room%22%3A+%7B+%22roomid%22%3A+%22"+room+"%22%2C+%22room%22%3A+%22300620322%22+%7D%2C++%22floor%22%3A+%7B+%22floorid%22%3A+%22%22%2C+%22floor%22%3A+%22%22+%7D%2C+%22area%22%3A+%7B+%22area%22%3A+%22%22%2C+%22areaname%22%3A+%22%22+%7D%2C+%22building%22%3A+%7B+%22buildingid%22%3A+%22%22%2C+%22building%22%3A+%22%22+%7D%2C%22extdata%22%3A%22info1%3D%22+%7D+%7D&funname=synjones.onecard.query.elec.roominfo&json=true"
# while not flag:
#     if timenow != 12:
#         time.sleep(3000)
#     else:
response = requests.get(url,headers = myheaders)
# flag = True
if eval(str(response.text)[70:79]) < limit:
    xiaoding = DingtalkChatbot(webhook, secret=secret)
    xiaoding.send_text(msg='电费余额小于设置下限，电费目前为'+str(response.text)[70:79], is_at_all=True)
