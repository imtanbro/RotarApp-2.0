from django.shortcuts import render
from django.http import HttpResponse
from Auth.models import DistrictCouncil

# Create your views here.

def home(request):
    dRole = None
    if request.user.is_authenticated :
        dRole = DistrictCouncil.objects.filter(accountId = request.user).first()
        dRole = dRole.districtRole.distRoleId if dRole!=None else None
    return render(request, 'Main/home.html',{'Tab':'home','DRole':dRole})

def home1(request):
    dRole = None
    if request.user.is_authenticated :
        dRole = DistrictCouncil.objects.filter(accountId = request.user).first()
        dRole = dRole.districtRole.distRoleId if dRole!=None else None
    return render(request, 'Main/m_home.html',{'Tab':'home','DRole':dRole})

def aboutUs(request):
    dRole = None
    if request.user.is_authenticated :
        dRole = DistrictCouncil.objects.filter(accountId = request.user).first()
        dRole = dRole.districtRole.distRoleId if dRole!=None else None
    return render(request, 'Main/m_aboutUs.html',{'Tab':'aboutUs','DRole':dRole})

def eRyla(request):
    dRole = None
    if request.user.is_authenticated :
        dRole = DistrictCouncil.objects.filter(accountId = request.user).first()
        dRole = dRole.districtRole.distRoleId if dRole!=None else None
    return render(request, 'Main/m_eRyla.html',{'Tab':'aboutUs','DRole':dRole})

def council(request):
    dRole = None
    if request.user.is_authenticated :
        dRole = DistrictCouncil.objects.filter(accountId = request.user).first()
        dRole = dRole.districtRole.distRoleId if dRole!=None else None
    return render(request, 'Main/m_council.html',{'Tab':'council','DRole':dRole})

def whatWeDo(request):
    dRole = None
    if request.user.is_authenticated :
        dRole = DistrictCouncil.objects.filter(accountId = request.user).first()
        dRole = dRole.districtRole.distRoleId if dRole!=None else None
    return render(request, 'Main/m_whatWeDo.html',{'Tab':'whatWeDo','DRole':dRole})

def resources(request):
    dRole = None
    if request.user.is_authenticated :
        dRole = DistrictCouncil.objects.filter(accountId = request.user).first()
        dRole = dRole.districtRole.distRoleId if dRole!=None else None
    return render(request, 'Main/m_resources.html',{'Tab':'resources','DRole':dRole,'document':document})

def document(request,document):
    dRole = None
    if request.user.is_authenticated :
        dRole = DistrictCouncil.objects.filter(accountId = request.user).first()
        dRole = dRole.districtRole.distRoleId if dRole!=None else None
    return render(request, 'Main/m_document.html',{'DRole':dRole,'document':document})
