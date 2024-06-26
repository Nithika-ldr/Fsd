import pytz 
from datetime import datetime, timedelta 
from django.shortcuts import render 
def current_datetime(request): 
  utc = pytz.utc   
  ist = pytz.timezone('Asia/Kolkata') 
  datetime_utc = datetime.now(utc) 
  datetime_ist = datetime.now(ist) 
  formatted_utc = datetime_utc.strftime('%Y-%m-%d %H:%M:%S %Z %z') 
  formatted_ist = datetime_ist.strftime('%Y-%m-%d %H:%M:%S %Z %z') 
  context = { 
     'utc_time': formatted_utc, 
     'ist_time': formatted_ist 
  } 
  return render(request, 'myapp/current_datetime.html', context)

def date_time_offset(request): 

  current_datetime = datetime.now() 
  datetime_ahead = current_datetime + timedelta(hours=4) 
  datetime_before = current_datetime - timedelta(hours=4) 

  formatted_current_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S') 
  formatted_datetime_ahead = datetime_ahead.strftime('%Y-%m-%d %H:%M:%S') 
  formatted_datetime_before = datetime_before.strftime('%Y-%m-%d %H:%M:%S')

  context = { 
     'current_datetime': formatted_current_datetime, 
     'datetime_ahead': formatted_datetime_ahead, 
     'datetime_before': formatted_datetime_before  
  } 
  return render(request, 'myapp/date_time_offset.html', context)
