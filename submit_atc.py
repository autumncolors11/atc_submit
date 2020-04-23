# -*- coding: utf-8 -*-

import json
import time
import re
from bs4 import BeautifulSoup
import requests
import codecs
import os

getsubmit=requests.get("https://kenkoooo.com/atcoder/atcoder-api/results?user=autumncolors").text

with open("results.txt", mode='w',newline='') as f:
    f.write(getsubmit)
f.close()

submituser_name='autumncolors'
submiturl = open("results.txt")
submitjson = json.load(submiturl)

al=open("already_problems.txt")
already=al.readlines()
al.close()

for i in range(len(already)):
    already[i]=already[i].rstrip("\n")

already_list = []

cnt=0
for kk in range(len(submitjson)):
    sid,sepo,sproid,sconid,suserid,slan,spoi,slen,sres,sexe = map(str,(list(submitjson[kk].values())))
    if sid not in already:
        if sres=="AC":
            html=requests.get("https://atcoder.jp/contests/"+sconid+"/submissions/"+sid).text
            soup=BeautifulSoup(html,"html.parser")
            pre = str(soup.find("pre",id="submission-code")).splitlines()
            pre[0]=pre[0].replace('<pre class="prettyprint linenums" id="submission-code">','')
            pre[-1]=pre[-1].replace("</pre>","")
            subtime = str(soup.find("time",class_='fixtime fixtime-second')).replace('<time class="fixtime fixtime-second">',"").replace('</time>',"").replace("-","").replace(":","").replace(" ","")[:-5]
            os.makedirs(sconid+"/"+sproid,exist_ok=True)

            f = open(sconid+"/"+sproid+"/"+subtime+".py","w",encoding="utf-8")
            for x in pre:
                f.write(str(x) + "\n")
            f.close()
            already_list.append(sid)
            cnt+=1
            print(cnt,sid)
            time.sleep(1)


if len(already_list)>0:
    alwrite = open("already_problems.txt","a",encoding="utf-8")
    for x in already_list:
        alwrite.write(str(x)+"\n")
    alwrite.close()
else:
    print("no write")
        

