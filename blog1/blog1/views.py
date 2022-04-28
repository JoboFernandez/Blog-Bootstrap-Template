from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'index.html', context)


def blog(request):
    context = {}
    return render(request, 'post_list.html', context)


def post(request):
    context = {}
    return render(request, 'post_detail.html', context)