from django.shortcuts import render
import datetime

def page(request, system):
    return render(request, "/home/isvperf/mi300x_h100_usage_tool/usage_webpage/usage_webpage/views/plotly_"+system + ".html")

def mlperf(request):
    return render(request, "mlperf.html")

def main(request):
    return render(request, "main.html")
