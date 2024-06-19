# urls.py가 의미하는 바

from django.urls import path
from .views import *

# 내 현재 동일한 앱 안에 있는 views 파일에서 함수를 다 불러온다는 의미 

app_name = "testapp"
urlpatterns = [
    path('past/', past, name="past"),
    path('page2/', page2, name="page2"),
    path('page5/', page5, name="page5"),
    path('page6/', page6, name="page6"),
     path('page7/', page7, name="page7"),
]

# 1. 이것을 직접 입력해야 링크로 연결된다는 의미
# 2. views.py에 있는 함수의 이름
# 3. 보통은 모두 같은 이름으로 통일... ㅎㅎ 어디에 쓰이는지는 잘 모름 ><

# mypage/ => 내가 임의로 정하는 것, 보통 식별이 가능하게 여기서는 [past] 기본 url 
# 두번째: 함수 이름을 써주면 됨, past
# past라는 함수를 불러올 거다, 뒤에 name은 식별자 보통은 함수 이름과 동일하게 설정