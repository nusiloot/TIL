# django imports style guide
# 1. standard library (내장 모듈 / ex. random)
# 2. thrid-part (ex.bs4, requests)
# 3. django (기본으로 써있는 애들)
# 4. local django

import random # 얘는 1번
from datetime import datetime # 얘도 1번
from django.shortcuts import render # 얘는 3번

# Create your views here.

def index(request): # 첫 번째 인자는 반드시 request
    return render(request, 'index.html') # render()의 첫 번째 인자도 반드시 request


# 함수 간 두 줄 띄어쓰는 것이 convention
def introduce(request, name, age):
    context = {'name': name, 'age': age,}
    return render(request, 'introduce.html', context)


def dinner(request):
    menu = ['냉국수', '치즈돈가스', '보쌈', '치킨']
    pick = random.choice(menu)
    # 앞의 pick : templates에서 가져갈 이름, 뒤의 pick : 바로 윗 줄의 pick 변수
    # 통상적으로 key랑 value는 같은 이름을 쓴다.
    context = {'pick': pick}
    return render(request, 'dinner.html', context)


def image(request):
    return render(request, 'image.html')


def hello(request, name): # name은 원하는 변수명으로 지정
    menu = ['냉국수', '치즈돈가스', '보쌈', '치킨']
    pick = random.choice(menu)
    context = {'name': name, 'pick': pick,} # 위의 name은 context 딕셔너리의 value와 같다.
    # value값 pick 뒤에 마지막 ,는 적어주는 습관 기르자
    # 이와 같이 context는 개수 제한 없이 넘길 수 있다.
    return render(request, 'hello.html', context)


def times(request, num1, num2):
    num3 = num1 * num2
    context = {'num1': num1, 'num2': num2, 'num3': num3,}
    return render(request, 'times.html', context)


def area(request, r):
    area = (r ** 2) * 3.14
    context = {'r': r, 'area': area,}
    return render(request, 'area.html', context)


def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '볶음밥', '양장피', '팔보채',]
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'bean',]
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'datetimenow': datetimenow,
        'empty_list': empty_list,
    }
    return render(request, 'template_language.html', context)


def isitgwangbok(request):
    today = datetime.now()
    if today.month == 8 and today.day == 15:
        result = True
    else:
        result = False
    context = {'result': result,}
    return render(request, 'isitgwangbok.html', context)