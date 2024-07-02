from django.urls import path
from .views import ItemCreateView,ItemDeleteView,ItemRetrieveView,ItemUpdateView,ItemListView,TruncateData,UserSignupView,UserSigninView



# urlpatterns = [
    
#     path ("mainwork/create/", ItemCreateView.as_view()),
#     path ("mainwork/retrieve/<int:pk>/", ItemRetrieveView.as_view()),
#     path ("mainwork/update/<int:pk>/", ItemUpdateView.as_view()),
#     path ("mainwork/delete/<int:pk>/", ItemDeleteView.as_view()),
#     path ("mainwork/listView/", ItemListView.as_view()),    
#     path ("mainwork/TruncateData/", TruncateData.as_view()),    
#     path ("mainwork/UserSignupView/", UserSignupView.as_view()),    
#     path ("mainwork/UserSigninView/", UserSigninView.as_view()),    

# ]
urlpatterns = [
    
    path ("mainwork/create/", ItemCreateView.as_view()),
    path ("mainwork/retrieve/<int:pk>/", ItemRetrieveView.as_view()),
    path ("mainwork/update/<int:pk>/", ItemUpdateView.as_view()),
    path ("mainwork/delete/<int:pk>/", ItemDeleteView.as_view()),
    path ("mainwork/listView/", ItemListView.as_view()),    
    path ("mainwork/TruncateData/", TruncateData.as_view()),    
    path ("mainwork/UserSignupView/", UserSignupView.as_view()),    
    path ("mainwork/UserSigninView/", UserSigninView.as_view()),    

]