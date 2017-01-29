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
            html += "<td style=\"border: 1px solid black; color: red\">"
        else :
            html += "<td style=\"border: 1px solid black; color: green\">"
        html += str(record.temprature) + "</td>"

        if prev_record != None :
            if record.temprature < prev_record.temprature :
                html += "<td style=\"border: 1px solid black;\">"
                html += "<img src=\"/home/Desktop/down_green.png\"/>" + "</td>"
            elif record.temprature > prev_record.temprature :
                html += "<td style=\"border: 1px solid black;\">"
                html += "<img src=\"/home/Desktop/up_red.png\"/>" + "</td>"
            else :
                html += "<td style=\"border: 1px solid black;\">" + "</td>"
        else :
            html += "<td style=\"border: 1px solid black;\">" + "</td>"

        if record.humidity > 55 :
            html += "<td style=\"border: 1px solid black; color: red\">"
        else :
            html += "<td style=\"border: 1px solid black; color: green\">"
        html += str(record.humidity) + "</td>"

        if prev_record != None :
            if record.humidity < prev_record.humidity :
                html += "<td style=\"border: 1px solid black;\">"
                html += "<img src=\"/home/Desktop/down_green.png\"/>" + "</td>"
            elif record.humidity > prev_record.humidity :
                html += "<td style=\"border: 1px solid black;\">"
                html += "<img src=\"/home/Desktop/up_red.png\"/>" + "</td>"
            else :
                html += "<td style=\"border: 1px solid black;\">" + "</td>"
        else :
            html += "<td style=\"border: 1px solid black;\">" + "</td>"

        html += "<td style=\"border: 1px solid black;\">"
        html += str(record.date) + "</td>"
        html += "</tr>"
        prev_record = record
    html += "</table>"
    return HttpResponse(html)

def summary(Request) :
    all_records = Weather.objects.all()
    sum_temprature = 0.0
    sum_humidity = 0.0
    average_temprature = []
    average_humidity = []
    time_begin = []
    time_end = []
    i = 0
    size = 0
    for record in all_records :
        sum_temprature += record.temprature
        sum_humidity += record.humidity
        i += 1
        if i == 1 :
            time_begin.append(record.date)
        if i == 10 :
            sum_temprature /= 10.0
            sum_humidity   /= 10.0
            average_temprature.append(sum_temprature)
            average_humidity.append(sum_humidity)
            time_end.append(record.date)
            sum_temprature = 0.0
            sum_humidity = 0.0
            i = 0
            size += 1

    html = "<table style=\"width:100%;border: 1px solid black;\">"
    for i in range(size) :
        html += "<tr>"
        if record.temprature > 25 :
            html += "<td style=\"border: 1px solid black; color: red\">"
        else :
            html += "<td style=\"border: 1px solid black; color: green\">"
        html += str(average_temprature[i]) + "</td>"

        if record.humidity > 55 :
            html += "<td style=\"border: 1px solid black; color: red\">"
        else :
            html += "<td style=\"border: 1px solid black; color: green\">"
        html += str(average_humidity[i]) + "</td>"

        html += "<td style=\"border: 1px solid black;\">"
        html += str(time_begin[i]) + "</td>"
        html += "<td style=\"border: 1px solid black;\">"
        html += str(time_end[i]) + "</td>"
        html += "</tr>"
    html += "</table>"
    return HttpResponse(html)
