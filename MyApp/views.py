from django.shortcuts import render
from .models import Weather
from django.http import HttpResponse

# Create your views here.
def show(Request) :
    all_records = Weather.objects.all()
    html = "<table style=\"width:100%;border: 1px solid black;\">"
    prev_record = None
    for record in all_records :
        html += "<tr>"
        if record.temprature > 25 :
            html += "<td style=\"border: 1px solid black; color: red\">" + str(record.temprature) + "</td>"
        else :
            html += "<td style=\"border: 1px solid black; color: green\">" + str(record.temprature) + "</td>"

        if prev_record != None :
            if record.temprature < prev_record.temprature :
                html += "<td style=\"border: 1px solid black;\">" + "<img src=\"/home/Desktop/down_green.png\"/>" + "</td>"
            elif record.temprature > prev_record.temprature :
                html += "<td style=\"border: 1px solid black;\">" + "<img src=\"http://www.mediafire.com/file/10g30j1tbbkd9yj/03.jpg\"/>" + "</td>"
            else :
                html += "<td style=\"border: 1px solid black;\">" + "</td>"
        else :
            html += "<td style=\"border: 1px solid black;\">" + "</td>"

        if record.humidity > 55 :
            html += "<td style=\"border: 1px solid black; color: red\">" + str(record.humidity) + "</td>"
        else :
            html += "<td style=\"border: 1px solid black; color: green\">" + str(record.humidity) + "</td>"

        if prev_record != None :
            if record.humidity < prev_record.humidity :
                html += "<td style=\"border: 1px solid black;\">" + "<img src=\"/home/Desktop/down_green.png\"/>" + "</td>"
            elif record.humidity > prev_record.humidity :
                html += "<td style=\"border: 1px solid black;\">" + "<img src=\"http://www.mediafire.com/file/10g30j1tbbkd9yj/03.jpg\"/>" + "</td>"
            else :
                html += "<td style=\"border: 1px solid black;\">" + "</td>"
        else :
            html += "<td style=\"border: 1px solid black;\">" + "</td>"

        html += "<td style=\"border: 1px solid black;\">" + str(record.date) + "</td>"
        html += "</tr>"
        prev_record = record
    html += "</table>"
    return HttpResponse(html)

def summary(Request) :
    all_records = Weather.objects.all()
    html = "<table style=\"width:100%;border: 1px solid black;\">"
    prev_record = None
    average_record = None
    i = 0
    for record in all_records :
        html += "<tr>"
        if record.temprature > 25 :
            html += "<td style=\"border: 1px solid black; color: red\">" + str(record.temprature) + "</td>"
        else :
            html += "<td style=\"border: 1px solid black; color: green\">" + str(record.temprature) + "</td>"

        if prev_record != None :
            if record.temprature < prev_record.temprature :
                html += "<td style=\"border: 1px solid black;\">" + "<img src=\"/home/Desktop/down_green.png\"/>" + "</td>"
            elif record.temprature > prev_record.temprature :
                html += "<td style=\"border: 1px solid black;\">" + "<img src=\"http://www.mediafire.com/file/10g30j1tbbkd9yj/03.jpg\"/>" + "</td>"
            else :
                html += "<td style=\"border: 1px solid black;\">" + "</td>"
        else :
            html += "<td style=\"border: 1px solid black;\">" + "</td>"

        if record.humidity > 55 :
            html += "<td style=\"border: 1px solid black; color: red\">" + str(record.humidity) + "</td>"
        else :
            html += "<td style=\"border: 1px solid black; color: green\">" + str(record.humidity) + "</td>"

        if prev_record != None :
            if record.humidity < prev_record.humidity :
                html += "<td style=\"border: 1px solid black;\">" + "<img src=\"/home/Desktop/down_green.png\"/>" + "</td>"
            elif record.humidity > prev_record.humidity :
                html += "<td style=\"border: 1px solid black;\">" + "<img src=\"http://www.mediafire.com/file/10g30j1tbbkd9yj/03.jpg\"/>" + "</td>"
            else :
                html += "<td style=\"border: 1px solid black;\">" + "</td>"
        else :
            html += "<td style=\"border: 1px solid black;\">" + "</td>"

        html += "<td style=\"border: 1px solid black;\">" + str(record.date) + "</td>"
        html += "</tr>"
        prev_record = record
    html += "</table>"
    return HttpResponse(html)
