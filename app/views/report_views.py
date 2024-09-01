from django.http import HttpResponse
from django.shortcuts import redirect, render

from app.forms.member_form import Member_add_form, Member_edit_form
from app.models.category_models import Category
from app.models.member_models import Member
from app.views.menus import menus
from django.contrib import messages
from datetime import date, datetime, timedelta

def report(request):
    categories = Category.objects.all()
    get_items={key: value for key, value in request.GET.items()  }
    loop_dates =[]
    th_dates =[]
    members=None
    try:
        if get_items['category'].isdigit():
            get_items['category']= int(get_items['category'])
        
        from_date = datetime.strptime(get_items['from_date'], '%Y-%m-%d')
        to_date = datetime.strptime(get_items['to_date'], '%Y-%m-%d')
        
        current_date = from_date
        while current_date <= to_date:
            loop_dates.append(current_date.strftime('%d-%m-%Y'))
            th_dates.append([current_date.strftime('%b'),current_date.strftime('%d')])
            current_date += timedelta(days=1)
            
        if get_items['category'] == 0:
            members = Member.objects.filter(category=None).order_by('name')
        elif get_items['category'] =='all':
            members = Member.objects.all().order_by('name')
        else:
            members = Member.objects.filter(category=get_items['category']).order_by('name')
    except:
        pass
    
    

    data = {
        'menus': menus,
        'categories' : categories,
        'get_items':get_items,
        'loop_dates':loop_dates,
        'th_dates':th_dates,
        'members':members,
        'today_date' : date.today().strftime('%Y-%m-%d')
    }
    return render(request, 'report/report.html', data)