from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.forms import UserProfileForm, UserInfoForm
# Create your views here.



@login_required(login_url='login')
def cprofile(request):
    user_profile= UserProfileForm()
    user_info= UserInfoForm()
    
    context={
        'user_profile': user_profile,
        'user_info': user_info,
        
    }
    return render(request, 'customers/cprofile.html', context)