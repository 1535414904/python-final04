from django.shortcuts import render   # 渲染網頁
from django.conf import settings
from django.http import HttpResponse   # Django用來回應給瀏覽器特定資料的函式
import requests   # 匯入擷取網頁所需要的模組
import json       # 匯入操作JSON格式所需要的模組
from mysite import models  # 從 mysite 的資料夾中的 models.py 匯入所有的類別（資料表）
import re 


def index(request):
    return render(request, "index.html")

# def nkustnews(request):
#     data = models.NKUSTnews.objects.all()
#     return render(request, "nkustnews.html", locals())

# def phonelist(request, id=-1):
#     if id == -1:
#         data = models.PhoneModel.objects.all()              #找出所有的手機
#     else:
#         maker = models.PhoneMaker.objects.get(id=id)        #找出一個(get)指定的廠牌
#         data = models.PhoneModel.objects.filter(maker=maker) #找出一堆(filter)符合的資料
#     return render(request, "phonelist.html", locals())

def create_data():
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

    for data in car_data:
        models.cardata.objects.create(
                serial_number = data['seq'],
                accident_year_month = extract_time(data['發生日期']),
                company_name = data['單位名稱'],
                township = data['鄉鎮市區'],
                death_toll = to_int(data['死亡人數']),
                Injured_umber = to_int(data['受傷人數']),
                weather_description = data['天候說明'],
                light_description = data['光線說明'],
                road_description = data['道路說明'],
                speed_limit = to_int(data['速限']),
                description_of_road_type = data['道路型態說明'],
                description_of_road_conditions = data['路面狀態說明'],
                description_of_pavement_defects = data['路面缺陷說明'],
                obstacle_description = data['障礙物說明'],
                accident_type_and_pattern = to_int(data['事故類型及型態']),
                accident_type_and_description = data['事故類型及型態說明'],
                surveillance_tape = data['監視影帶'],
                )


# def parse_chinese_datetime(datetime_str):
#     year = datetime_str.split('/')[0]
#     month = datetime_str.split('/')[1]
#     day = datetime_str.split('/')[2].split()[0]
#     time_str = extract_time(datetime_str)

#     if datetime_str.endswith('下午'):
#         hour = int(time_str.split(':')[0]) + 12
#         time_str = f"{hour}:{time_str.split(':')[1]}:{time_str.split(':')[2]}"

#     datetime_obj = datetime.strptime(f"{year}/{month}/{day} {time_str}", "%Y/%m/%d %H:%M:%S")
#     return datetime_obj

def extract_time(datetime_str):
    # extract date part and convert it to yyyy-mm-dd
    return datetime_str.split(' ')[0].replace('/', '-')

def to_int(string):
    try:
        return int(string)
    except:
        return 0

def filtered_data(request):
    
    return render(request, 'filter.html')


def kcg_data(request):

    return render(request, "kcg_data.html")


def all(request):

    return render(request, "all.html", context={'data': models.cardata.objects.all()})

def die(request):

    return render(request, "die.html")