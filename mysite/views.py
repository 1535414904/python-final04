from django.shortcuts import render   # 渲染網頁
from django.http import HttpResponse   # Django用來回應給瀏覽器特定資料的函式
import requests   # 匯入擷取網頁所需要的模組
import json       # 匯入操作JSON格式所需要的模組
from mysite import models  # 從 mysite 的資料夾中的 models.py 匯入所有的類別（資料表）
import random     # 匯入隨機模組
from datetime import datetime
from itertools import chain
import re 

def index(request):
    mynames = ["第四組"]
    myname = random.choice(mynames)
    return render(request, "index.html", locals())

def nkustnews(request):
    data = models.NKUSTnews.objects.all()
    return render(request, "nkustnews.html", locals())

def all_data(request):
    car_data=list()
    urls = ["https://api.kcg.gov.tw/api/service/get/0ba09913-7e69-469f-b7eb-1140e493d0a0",
            "https://api.kcg.gov.tw/api/service/get/1a31f2d8-7b7e-4802-a06e-b262a9f68983",
            "https://api.kcg.gov.tw/api/service/get/d480fcaf-a9d1-42cd-a36b-6f248c30fe7d",
            "https://api.kcg.gov.tw/api/service/get/a61991be-6ebe-471c-a62f-ad293f23d12a",
            "https://api.kcg.gov.tw/api/service/get/fc77ea43-d424-4618-b509-3b089b620470",
            "https://api.kcg.gov.tw/api/service/get/ea43f985-546e-4347-9329-abebf464e9fb",
            "https://api.kcg.gov.tw/api/service/get/2a803f78-3272-4bd4-a0a9-1d918fc6276c",
            "https://api.kcg.gov.tw/api/service/get/f72b68ab-ad33-4c22-9e09-c520c40f3f2e",
            "https://api.kcg.gov.tw/api/service/get/a548c991-54c0-41c7-8784-92d7fb157d00",
            "https://api.kcg.gov.tw/api/service/get/df9d1d5a-a70a-4664-96b1-4af55ddf2d70",
            "https://api.kcg.gov.tw/api/service/get/06d2f74e-0602-445f-b0de-6755a8696bb3",
            "https://api.kcg.gov.tw/api/service/get/671f3133-fae1-41f4-afc4-4bae95c1889d"]
    
    def remove_question_marks(data):
        for sublist in data:
            for item in sublist:
                for key in item:
                    if isinstance(item[key], str):
                        item[key] = re.sub(r'\s*\?.*', '', item[key])
        return data
    
    for url in urls:
        r = requests.get(url)
        data1 = json.loads(r.text)
        car_data.append(data1['data'])
        car_data = remove_question_marks(car_data)
    # Flatten the list of car_data
    car_data = [item for sublist in car_data for item in sublist]

    # Define a custom key function for sorting
    def custom_sort_key(item):
        date_str = item['發生日期']
        date_obj = parse_chinese_datetime(date_str)
        formatted_date_str = datetime.strftime(date_obj, "%Y/%m/%d %H:%M:%S")
        return formatted_date_str

    # Sort car_data by custom key function
    sorted_data = sorted(car_data, key=custom_sort_key)

    msg = "<h2>車禍資訊</h2><hr>"
    msg += "<table><tr bgcolor=#aaaaaa><td>編號</td><td>發生日期</td><td>原因</td><td>事故類別</td><td>速限</td><td>路面狀態說明</td><td>天候說明</td></tr>"

    for item in sorted_data:
        if item['事故類型及型態說明'] and item['發生日期'] and item['事故類型及型態說明'] != "":
            msg += "<tr bgcolor=#ffee33><td bgcolor=#aaaaaa>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(
                item['seq'],
                item['發生日期'],
                item['事故類型及型態說明'],
                item['事故類別'],
                item['速限'],
                item['路面狀態說明'],
                item['天候說明']
            )

    return HttpResponse(msg)

def parse_chinese_datetime(datetime_str):
    year = datetime_str.split('/')[0]
    month = datetime_str.split('/')[1]
    day = datetime_str.split('/')[2].split()[0]
    time_str = extract_time(datetime_str)

    if datetime_str.endswith('下午'):
        hour = int(time_str.split(':')[0]) + 12
        time_str = f"{hour}:{time_str.split(':')[1]}:{time_str.split(':')[2]}"

    datetime_obj = datetime.strptime(f"{year}/{month}/{day} {time_str}", "%Y/%m/%d %H:%M:%S")
    return datetime_obj

def extract_time(datetime_str):
    pattern = r'(\d+:\d+:\d+)'
    match = re.search(pattern, datetime_str)
    if match:
        return match.group(1)
        time_str = re.sub(r'\s*\?.*', '', time_str)
    else:
        return "12:00:00"

def filtered_data(request):
    
    os.makedirs(settings.STATIC_ROOT, exist_ok=True)
    car_data = []
    urls = [
            "https://api.kcg.gov.tw/api/service/get/0ba09913-7e69-469f-b7eb-1140e493d0a0",
            "https://api.kcg.gov.tw/api/service/get/1a31f2d8-7b7e-4802-a06e-b262a9f68983",
            "https://api.kcg.gov.tw/api/service/get/d480fcaf-a9d1-42cd-a36b-6f248c30fe7d",
            "https://api.kcg.gov.tw/api/service/get/a61991be-6ebe-471c-a62f-ad293f23d12a",
            "https://api.kcg.gov.tw/api/service/get/fc77ea43-d424-4618-b509-3b089b620470",
            "https://api.kcg.gov.tw/api/service/get/ea43f985-546e-4347-9329-abebf464e9fb",
            "https://api.kcg.gov.tw/api/service/get/2a803f78-3272-4bd4-a0a9-1d918fc6276c",
            "https://api.kcg.gov.tw/api/service/get/f72b68ab-ad33-4c22-9e09-c520c40f3f2e",
            "https://api.kcg.gov.tw/api/service/get/a548c991-54c0-41c7-8784-92d7fb157d00",
            "https://api.kcg.gov.tw/api/service/get/df9d1d5a-a70a-4664-96b1-4af55ddf2d70",
            "https://api.kcg.gov.tw/api/service/get/06d2f74e-0602-445f-b0de-6755a8696bb3",
            "https://api.kcg.gov.tw/api/service/get/671f3133-fae1-41f4-afc4-4bae95c1889d"
            ]
    
    def remove_question_marks(data):
        for sublist in data:
            for item in sublist:
                for key in item:
                    if isinstance(item[key], str):
                        item[key] = re.sub(r'\s*\?.*', '', item[key])
        return data
    
    for url in urls:
        r = requests.get(url)
        data1 = json.loads(r.text)
        car_data.append(data1['data'])
    car_data = remove_question_marks(car_data)
    car_data = [item for sublist in car_data for item in sublist]

    def custom_sort_key(item):
        date_str = item['發生日期']
        date_obj = parse_chinese_datetime(date_str)
        formatted_date_str = datetime.strftime(date_obj, "%Y/%m/%d %H:%M:%S")
        return formatted_date_str
    sorted_data = sorted(car_data, key=custom_sort_key)
    a1 = 0
    a2 = 0
    a3 = 0

    for item in sorted_data:
        if item['事故類別'] != "":
            if item['事故類別'] == "A1":
                a1 += 1
            elif item['事故類別'] == "A2":
                a2 += 1
            else:
                a3 += 1

    labels = ['A1', 'A2', 'A3']
    sizes = [a1, a2, a3]
    colors = ['#ff9999', '#66b3ff', '#99ff99']
    explode = (0.1, 0, 0)  # Highlight the first sector
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')  # Make the pie chart circular
    plt.title('車禍類別', fontproperties=font)

    
    chart_image_path = "C:/pythonfinal04/1.png"
    plt.savefig(chart_image_path)
    with open(chart_image_path, 'rb') as f:
        chart_image_data = f.read()
    chart_image_base64 = base64.b64encode(chart_image_data).decode('utf-8')
    chart_image_src = f"data:image/png;base64,{chart_image_base64}"
    return render(request, 'filter.html', {'chart_image_src': chart_image_src})


def kcg_data(request):

    return render(request, "kcg_data.html", locals())


def all(request):

    return render(request, "all.html", locals())
