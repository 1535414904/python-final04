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
    url = "https://api.kcg.gov.tw/api/service/get/671f3133-fae1-41f4-afc4-4bae95c1889d"
    r = requests.get(url)         # 實際擷取網頁的內容
    data1 = json.loads(r.text)     # 把網頁的文字轉換成JSON格式，放到data變數裡面
    car_data = data1['data'] # bicycle_data現在是串列格式，目前共有70筆項目
    msg = ""
    msg = "<h2>車禍資訊"  + "</h2><hr>"   
    msg = msg + "<table><tr bgcolor=#aaaaaa><td>編號</td><td>發生日期</td><td>原因</td><td>事故類別</td><td>速限</td><td>路面狀態說明</td><td>天候說明</td></tr>"
    for item in car_data:
        if item['事故類型及型態說明']and item['發生日期']and item['事故類型及型態說明']!="":
            msg = msg + "<tr bgcolor=#33ff33><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(  item['seq'], 
                item['發生日期'], 
                item['事故類型及型態說明'],item['事故類別'],item['速限'],item['路面狀態說明'],item['天候說明'])
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
