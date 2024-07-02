from django.shortcuts import render,redirect
from .models import ItemBook
from .serializers import ItemBookSerializer,UserSignUp,UserSignIn
from rest_framework.response import Response
from rest_framework import status , permissions
from rest_framework.generics import CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,ListAPIView, GenericAPIView
from django.http import HttpResponse
from django.contrib.auth.models import User, Permission
from django.contrib.auth.forms import UserCreationForm
from rest_framework_simplejwt.views import TokenObtainPairView,TokenViewBase
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth import authenticate
import jwt



# Create your views here.
class ItemCreateView(CreateAPIView):
    queryset = ItemBook.objects.all()
    serializer_class = ItemBookSerializer

class ItemUpdateView(UpdateAPIView):
    queryset = ItemBook.objects.all()
    serializer_class = ItemBookSerializer

class ItemDeleteView(DestroyAPIView):
    queryset = ItemBook.objects.all()
    serializer_class = ItemBookSerializer

class ItemListView(ListAPIView):
    # queryset = ItemBook.objects.all()
    serializer_class = ItemBookSerializer
    def get_queryset(self):
        userId = self.request.query_params.get('userId')
        queryset = ItemBook.objects.filter(userId=userId)
        return queryset
    
    # def get(self,req):
    #     queryset = ItemBook.objects.all()
    #     print(req.data)
    #     return queryset
    
    
    

class ItemRetrieveView(RetrieveAPIView):
    queryset = ItemBook.objects.all()
    serializer_class = ItemBookSerializer

class TruncateData(GenericAPIView):
    def delete(self, request):
        # userId = self.request.query_params.get('userId',1)  1 default value aese dete hain
        userId = self.request.query_params.get('userId')
        ItemBook.objects.filter(userId=userId).delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

class UserSignupView(CreateAPIView):
    serializer_class = UserSignUp
    def post(self, request):
        # print(request.data) if we want to check api usersignup from api then we use the request.data
        print(request.data)
        uname = request.data.get('username', '') # request.data['username']
        mail = request.data.get('email', '')
        pwd = request.data.get('password', '')
        # pwd1 = request.POST['password1']
        user = User.objects.create_user(username=uname, password=pwd, email=mail)
        user.save()
        return Response(status=status.HTTP_201_CREATED, data={'success': True, 'message': 'User created'}) 
    
 #user signin api    
class UserSigninView(CreateAPIView):
    # permission_classes=[permissions.AllowAny]

    # serializer_class = UserSignIn
    # _serializer_class = UserSignIn
    # serializer_class = api_settings.TOKEN_OBTAIN_SERIALIZER
    # token_obtain_pair = TokenObtainPairView.as_view()
    serializer_class = UserSignIn
    def post(self, request):
        # print(request.data) 
        print(request.data)
        uname = request.data.get('username', '') # request.data['username']
        pwd = request.data.get('password', '')
        # encoded_jwt = jwt.encode({"username":uname,"password":pwd}, "secret", algorithm='HS256')
        # print(encoded_jwt)
        # decoded_jwt=jwt.decode(encoded_jwt, "secret", algorithms=['HS256'] )
        # print(decoded_jwt)
        user = authenticate(username=uname, password=pwd)
        userPk=user.pk
        if userPk:
            return Response(status=status.HTTP_200_OK, data={'success': True, 'message': 'User SignIN',"userPk":userPk})
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data={'success': False, 'message': 'User SignIN Failed'})
    


# new user creation using form and model
# class NewUser(CreateAPIView):
#     template_name='register.html'
 
#     # model= User
#     # form_class  = SignUpForm
#     form_class = UserCreationForm
#     model = User
#     fields = '_all_'
   
    # fields = ['username','password1', 'password2']
    # success_url= reverse_lazy('signin')

# class NewUserForm(CreateView):
#     template_name='registerform.html'
#     model=User
#     form= UserCreationForm
#     fields = ['username','password']
#     success_url= reverse_lazy('signin')



