from django.shortcuts import render
from Auth.models import DistrictCouncil, Member, DistrictRole
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from .models import DistReport, Task, Response
import json
from django.db import transaction
import datetime

year = datetime.datetime.now().year

def admin_getMonth(request):
    council = dict()
    councilList = DistrictCouncil.objects.all()
    for councilMember in councilList :
        memberProfile = Member.objects.filter(login=councilMember.accountId).first()
        council[councilMember.districtRole] = memberProfile
    return render(request, 'DistReport/getMonth.html',{'title':'Tasks','Tab':'Tasks','DRole':'0','Council':council})

def admin_getTasks(request, month, distRoleId):
    districtRole = DistrictRole.objects.filter(distRoleId=distRoleId).first()
    report = DistReport.objects.filter(reportingMonth=month).filter(districtRole=districtRole).first()
    response = Response.objects.filter(dReport=report).all().values_list('responseId','task__taskId','task__taskText','driveLink','completionStatus','response','modifiedOn','allottedBy')
    return render(request, 'DistReport/getTasks.html',{'title':'Tasks','Tab':'Tasks','DRole':'0','Response':response,'DistrictRole':distRoleId,'ReportId':report.dReportId,'Month':month,'Year':report.reportingYear})

def admin_addTask(request):
    print("Adding")
    try :
        data = json.loads(request.POST.get('data'))
        
        with transaction.atomic() :
            newTask = Task(taskText=data['taskText'])
            newTask.save()
        
            districtRole = DistrictRole.objects.filter(distRoleId=data['DistrictRole']).first()
            report = DistReport.objects.filter(dReportId=data['ReportId']).first()
        
            newResponse = Response(dReport = report, task = newTask)
            newResponse.save()

        jsonResponse = {}
        response = Response.objects.filter(dReport=report).values('responseId','task__taskId','task__taskText','completionStatus','response','driveLink','modifiedOn','allottedBy')
        for item in response :
            jsonResponse[item['responseId']] = item

        data = {
            'success': True,
            'tasks':jsonResponse
        }

    except Exception as Error :
        print(Error)
        data = {
            'error' : "An error has occurred, Contact the website coordinators",
            'success': False
        }
        
    return JsonResponse(data)

def admin_deleteTask(request):
    try :
        data = json.loads(request.POST.get('data'))
        
        with transaction.atomic() :
            districtRole = DistrictRole.objects.filter(distRoleId=data['DistrictRole']).first()
            report = DistReport.objects.filter(dReportId=data['ReportId']).first()
            Response.objects.filter(responseId=data['ResponseId']).delete()

        jsonResponse = {}
        response = Response.objects.filter(dReport=report).values('responseId','task__taskId','task__taskText','completionStatus','response','driveLink','modifiedOn','allottedBy')
        for item in response :
            jsonResponse[item['responseId']] = item

        data = {
            'success': True,
            'tasks':jsonResponse
        }

    except Exception as Error :
        data = {
            'error' : "An error has occurred, Contact the website coordinators",
            'success': False
        }
        
    return JsonResponse(data)

def admin_editTask(request):
    
    try :
        data = json.loads(request.POST.get('data'))
        
        with transaction.atomic() :
            districtRole = DistrictRole.objects.filter(distRoleId=data['DistrictRole']).first()
            report = DistReport.objects.filter(dReportId=data['ReportId']).first()
            Task.objects.filter(taskId=data['taskId']).update(taskText=data['taskText'])

        jsonResponse = {}
        response = Response.objects.filter(dReport=report).values('responseId','task__taskId','task__taskText','completionStatus','response','driveLink','modifiedOn','allottedBy')
        for item in response :
            jsonResponse[item['responseId']] = item

        data = {
            'success': True,
            'tasks':jsonResponse
        }

    except Exception as Error :
        data = {
            'error' : "An error has occurred, Contact the website coordinators",
            'success': False
        }
        
    return JsonResponse(data)

def council_index(request):
    Council = DistrictCouncil.objects.filter(accountId = request.user).first()
    return render(request, 'DistReport/index.html',{'title':'Tasks','Tab':'Tasks','DRole':'1','DistRole':Council.districtRole.distRoleName})

def council_getTasks(request):
    
    Council = DistrictCouncil.objects.filter(accountId = request.user).first()
    
    report = DistReport.objects.filter(districtRole = Council.districtRole)
    
    months = ['01','02','03','04','05','06','07','08','09','10','11','12']
    try :
        jsonResponse = {}
        
        for month in months :
            jsonResponse[month] = {}
            report1 = report.filter(reportingMonth=month).first()
            
            response1 = Response.objects.filter(dReport=report1).values('responseId','task__taskId','task__taskText','completionStatus','response','driveLink','modifiedOn','allottedBy')
            
            for item in response1 :
                jsonResponse[month][item['responseId']] = item

        data = {
            'success': True,
            'tasks':jsonResponse
        }

        print(jsonResponse)

    except Exception as Error :
        print(Error)
        data = {
            'success': False,
            'error' : "An error has occurred, Contact the website coordinators"
        }
        
    return JsonResponse(data)

def council_saveTask(request):

    data = json.loads(request.POST.get('data'))
    
    task = data['data']

    try :
        
        response = Response.objects.filter(responseId = data['responseId'])
        print(response)
        response.update(modifiedOn=datetime.datetime.now(), **task)
    
    except Exception as e :
        print(e)
        data = {
            'success': False,
            'error' : "An error has occurred, Contact the website coordinators"
        }
        return JsonResponse(data)

    Council = DistrictCouncil.objects.filter(accountId = request.user).first()

    report = DistReport.objects.filter(districtRole = Council.districtRole)
    
    months = ['01','02','03','04','05','06','07','08','09','10','11','12']
    try :
        jsonResponse = {}
        
        for month in months :
            jsonResponse[month] = {}
            report1 = report.filter(reportingMonth=month).first()
            
            response1 = Response.objects.filter(dReport=report1).values('responseId','task__taskId','task__taskText','completionStatus','response','driveLink','modifiedOn','allottedBy')
            
            for item in response1 :
                jsonResponse[month][item['responseId']] = item

        data = {
            'success': True,
            'tasks':jsonResponse
        }

        print(jsonResponse)

    except Exception as Error :
        print(Error)
        data = {
            'success': False,
            'error' : "An error has occurred, Contact the website coordinators"
        }
        
    return JsonResponse(data)

def council_addTask(request):

    try :
    
        data = json.loads(request.POST.get('data'))
        Council = DistrictCouncil.objects.filter(accountId = request.user).first()
        reportId = str(data['month'])+"-"+str(year)+"-"+str(Council.districtRole.distRoleId)
        print(reportId)
        with transaction.atomic() :
            
            newTask = Task(taskText=data['taskText'])
            newTask.save()

            Council = DistrictCouncil.objects.filter(accountId = request.user).first()
            report = DistReport.objects.filter(districtRole = Council.districtRole).filter(reportingMonth=data['month'])
            
            if report.exists() :
                newResponse = Response(dReport = report.first(), task = newTask, allottedBy = '1')
                newResponse.save()

            else :
                report = DistReport(districtRole=Council.districtRole, reportingMonth=data['month'], reportingYear = year, dReportId=reportId) 
                report.save()
                newResponse = Response(dReport = report, task = newTask, allottedBy = '1')
                newResponse.save()

        jsonResponse = {}
        
        months = ['01','02','03','04','05','06','07','08','09','10','11','12']
    
        for month in months :
            jsonResponse[month] = {}
            report1 = DistReport.objects.filter(districtRole = Council.districtRole).filter(reportingMonth=month).first()
            print(report1)
            response1 = Response.objects.filter(dReport=report1).values('responseId','task__taskId','task__taskText','completionStatus','response','driveLink','modifiedOn','allottedBy')
            print(response1)
            for item in response1 :
                jsonResponse[month][item['responseId']] = item
        print(jsonResponse)
        data = {
            'success': True,
            'tasks':jsonResponse
        }

    except Exception as Error :
    
        print(Error)
        data = {
            'error' : "An error has occurred, Contact the website coordinators",
            'success': False
        }
        
    return JsonResponse(data)
