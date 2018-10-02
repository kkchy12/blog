"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# 장고 내장 함수 url() 임포트
from django.conf.urls import url, include   # include('bookmark.urls') 함수를 위하여
from django.contrib import admin

# URL 패턴에 따라 뷰를 호출할 예정(해당 뷰 코드를 작성하면 오류 해결됨)
from bookmark.views import BookmarkLV, BookmarkDV
# from bookmark.views import *  # 모든 뷰 항목을 일괄 임포트

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(regex, view, kwargs=None, name=None, prefix='')
    # 여기서 regex와 view는 필수 인자)
    url(r'', include('bookmark.urls')),
    # 아래 내용을 모두 bookmark/urls.py 파일로 옮기자.
    # # 북마크 앱을 위한 클래스 기반 뷰
    # # /bookmark/ 요청을 처리할 뷰 클래스를 BookmarkLV로 지정하고, URL 패턴 이름 지정
    # url(r'^bookmark/$', BookmarkLV.as_view(), name='index'),
    # # /bookmark/숫자/ 요청을 처리할 뷰 클래스를 BookmarkDV로 지정하고, URL 패턴 이름 지정
    # url(r'^bookmark/(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail'),
    # # tabular list
    # url(r'^bookmark_t/$', bookmark.views.tabularBookmark, name='index_t'),
]
