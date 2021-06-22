from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def analyze(request):
    dtext = request.POST.get('text', 'off')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in dtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        dtext = analyzed


    if fullcaps=="on":
        analyzed = ""
        for char in dtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
        dtext = analyzed


    if newlineremover=="on":
        analyzed =""
        for char in dtext:
            if char == "\n":
                analyzed = analyzed+char
        params = {'purpose': 'Remove New Line ', 'analyzed_text': analyzed}
        dtext = analyzed


    if spaceremover == "on":
        analyzed = ""
        for index,char in enumerate(dtext):
            if not(dtext[index] == " " and dtext[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Remove New Line ', 'analyzed_text': analyzed}
        dtext = analyzed


    if charcount == "on":
        analyzed = len(dtext)

        params = {'purpose': 'Character Counter ', 'analyzed_text': analyzed}

    if (removepunc != "on" and fullcaps !="on" and newlineremover !="on" and spaceremover != "on" and charcount != "on"):
        return  render(request,'error.html')




    return render(request, 'analyze.html', params)

    params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
    return render(request, 'analyze.html',params)



