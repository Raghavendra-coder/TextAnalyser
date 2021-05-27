# i have  created this file - RK
from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request, 'index.html')
def analyse(request):

    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capitalise = request.POST.get('capitalise', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')
    charcounter = request.POST.get('charcounter', 'off')
    #print(removepunc)
    #print(djtext)
    if removepunc == 'on':
        analysed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analysed = analysed + char
        params = {'purpose': 'Removed Punctuations', 'analysed_text': analysed}

        djtext=analysed
    if capitalise == 'on':
        analysed = ""
        for char in djtext:
            analysed = analysed+char.upper()
        params = {'purpose': 'capitalise', 'analysed_text': analysed}

        djtext=analysed
    if newlineremove == 'on':
        analysed = ""
        for char in djtext:
            if char !="\n" and char != "\r":
                analysed = analysed+char.upper()
        params = {'purpose': 'Newline Removal', 'analysed_text': analysed}

        djtext = analysed
    if spaceremove == 'on':
        analysed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analysed = analysed + char
        params = {'purpose': 'Extra Space Removal', 'analysed_text': analysed}

        djtext = analysed
    if charcounter == "on":
        analysed = len(djtext)
        params = {'purpose': 'Character Counter', 'analysed_text': analysed}

        djtext = analysed
    if(removepunc != 'on' and capitalise != 'on' and newlineremove != 'on' and spaceremove != 'on' and charcounter != 'on'):
        return HttpResponse("Error")
    return render(request, 'analyse.html', params)