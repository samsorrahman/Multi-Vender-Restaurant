from django.shortcuts import render, get_object_or_404
from accounts.forms import UserProfileForm
from .forms import VendorForm
# Create your views here.
from accounts.models import UserProfile
from .models import Vendor

def myprofile(request):
    # auto filled data
    profile= get_object_or_404(UserProfile, user=request.user)
    vendor= get_object_or_404(Vendor, user=request.user)
    profile_form = UserProfileForm(instance=profile)
    vendor_form = VendorForm(instance=vendor)
    
    context ={
        'profile_form': profile_form,
        'vendor_form': vendor_form,
        'profile': profile,
        'vendor': vendor,
    }
    return render(request, 'vendor/myprofile.html', context)
