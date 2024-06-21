# urls.py가 의미하는 바

from django.urls import path
from .views import *

# 내 현재 동일한 앱 안에 있는 views 파일에서 함수를 다 불러온다는 의미 

app_name = "testapp"
urlpatterns = [
    path('test/', test, name="test"),
]

# mypage/ => 내가 임의로 정하는 것, 보통 식별이 가능하게 여기서는 [past] 기본 url 
# 두번째: 함수 이름을 써주면 됨, past
# past라는 함수를 불러올 거다, 뒤에 name은 식별자 보통은 함수 이름과 동일하게 설정