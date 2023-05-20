from django.shortcuts import render   # 渲染網頁
from django.http import HttpResponse   # Django用來回應給瀏覽器特定資料的函式
import requests   # 匯入擷取網頁所需要的模組
import json       # 匯入操作JSON格式所需要的模組
from mysite import models  # 從 mysite 的資料夾中的 models.py 匯入所有的類別（資料表）
import random     # 匯入隨機模組

def index(request):    
    return render(request, "index.html", locals())

def nkustnews(request):
    data = models.NKUSTnews.objects.all()
    return render(request, "nkustnews.html", locals())

def all_data(request):
    url = "https://opendata.hccg.gov.tw/OpenDataFileHit.ashx?ID=48DEDBDAC3A31FC6&u=77DFE16E459DFCE3F5CEA2F931E333F7E23D5729EF83D5F20744125E844FB27044F9892E6F09372518441B3BB84260426ADE242A57DFB9E8C9A50C50134F4F47"

    r = requests.get(url)         
    data = json.loads(r.text)     
    msg = ""
    msg = "<h2>新竹市自行車可用資訊" + data['updated_at'] + "</h2><hr>"   
    bicycle_data = data['retVal'] 
    msg = msg + "<table><tr bgcolor=#aaaaaa><td>站名</td><td>可用數量</td></tr>"
    for item in bicycle_data:
        msg = msg + "<tr bgcolor=#33ff33><td>{}</td><td>{}/{}</td></tr>".format(item['sna'].split("_")[1], item['sbi'], item['tot'])
    msg = msg + "</table>"
    return HttpResponse(msg)

def filtered_data(request):
    models.cardata.objects.all().delete()
    url = "https://api.kcg.gov.tw/api/service/get/ad197194-6db9-4f14-ad38-2adceea831c3"
    r = requests.get(url)
    data1 = json.loads(r.text)
    car_data = data1["data"]

    for item in car_data:
        # print("{}:{}/{}".format)(
        #     item['seq'],
        #     item['事故年月'],
        #     item['事故類型及型態說明']
        # )
        new_record = models.cardata(
            編號 = int(item['seq']),
            發生日期 = item['事故年月'],
            原因 = item['事故類型及型態說明']
            )
        new_record.save()
        


    # 過濾 HBicycleData 裡面的所有記錄，找出其中sbi>=10的站台放到data中
    # data = models.cardata.filter()
    return render(request, "filter.html", locals())

     

def kcg_data(request):

    return render(request, "kcg_data.html", locals())
