from django.conf.urls import include, url
from django.contrib import admin
from mysite.views import HomeView                 # 추가!!!

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view(), name='home'),  # 추가!!!
    url(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
]




# # 장고 내장 함수 url() 임포트
# from django.conf.urls import url, include   # include('bookmark.urls') 함수를 위하여
# from django.contrib import admin
#
# # URL 패턴에 따라 뷰를 호출할 예정(해당 뷰 코드를 작성하면 오류 해결됨)
# from bookmark.views import BookmarkLV, BookmarkDV
# # from bookmark.views import *  # 모든 뷰 항목을 일괄 임포트
#
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     # url(regex, view, kwargs=None, name=None, prefix='')
#     # 여기서 regex와 view는 필수 인자)
#     url(r'', include('bookmark.urls')),
#     # 아래 내용을 모두 bookmark/urls.py 파일로 옮기자.
#     # # 북마크 앱을 위한 클래스 기반 뷰
#     # # /bookmark/ 요청을 처리할 뷰 클래스를 BookmarkLV로 지정하고, URL 패턴 이름 지정
#     # url(r'^bookmark/$', BookmarkLV.as_view(), name='index'),
#     # # /bookmark/숫자/ 요청을 처리할 뷰 클래스를 BookmarkDV로 지정하고, URL 패턴 이름 지정
#     # url(r'^bookmark/(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail'),
#     # # tabular list
#     # url(r'^bookmark_t/$', bookmark.views.tabularBookmark, name='index_t'),
# ]
