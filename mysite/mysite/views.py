from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def about(request):
    return HttpResponse("about")

def analyzer(request):


    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    newlineremover = request.POST.get('newlineremover','off')
    fullCaps = request.POST.get('fullCaps', 'off')

    if removepunc == 'on':
        analyzed_text = ''
        punctuations = '''!()*&^%$#@{}[];:'"<>?/,.'''

        for char in djtext:
            if char not in punctuations:
                analyzed_text = analyzed_text + char

        params = {'analyzed_text' : analyzed_text ,}
        djtext = analyzed_text
        
    if fullCaps == 'on':
        analyzed_text = ''
        for char in djtext:
            analyzed_text = analyzed_text + char.upper()
       
        params = {'analyzed_text' : analyzed_text }
        djtext = analyzed_text
        
    
    if newlineremover == 'on':
        analyzed_text = ''
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed_text = analyzed_text + char
        params = {'analyzed_text' : analyzed_text }
        djtext = analyzed_text

    return render(request, 'analyze.html', params)




