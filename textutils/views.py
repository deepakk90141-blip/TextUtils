from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("home")

def analyze(request):

    # et the text from request
    djtext = request.POST.get('text', 'default')

    # check checkbox value of removepunc
    removepunc = request.POST.get('removepunc', 'off')

    # check checkbox value of newline removal
    newlineremover = request.POST.get('newlineremover', 'off')

    # check checkbox value of Extra space remover
    Extraspaceremover = request.POST.get('Extraspaceremover', 'off')

    # check checkbox value of UPPER CASE
    fullcaps = request.POST.get('fullcaps', 'off')

    # check checkbox value of charcount
    charcount = request.POST.get('charcount', 'off')

    # check which checkbox is on
    if removepunc == "on":

        # Check which punctuation and remove this
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

        # Analsyze the text of punctuation removal
        # return render(request, 'analyze.html', params)
    
    # this condition is for uppercase
    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper() 
            params = {'purpose': 'Change to uppercase', 'analyzed_text': analyzed}
            djtext = analyzed
        # Analsyze the text of uppercase
        # return render(request, 'analyze.html', params)
    
    # this condition is for newlineremover
    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed = analyzed + char
                params = {'purpose': 'Newline Remover', 'analyzed_text': analyzed}
                djtext = analyzed
        # Analsyze the text of newlineremover
        # return render(request, 'analyze.html', params)
    
    # this condition is for Extraspaceremover
    if(Extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):           # use of enumerate function to get index
            if not(djtext[index] ==" " and djtext[index + 1]==" "):

                analyzed = analyzed + char
                params = {'purpose': 'Space Remover', 'analyzed_text': analyzed}
                # djtext = analyzed
        # Analsyze the text of space remover
        return render(request, 'analyze.html', params)

    # this condition is for charcount
    if(charcount=="on"):
        analyzed = 0
        for  char in djtext:
            analyzed = analyzed + 1
            params = {'purpose': 'Charactor Count', 'analyzed_text': analyzed}
            djtext = analyzed
        # Analsyze the text of charcount

    if(removepunc!="on" and newlineremover!="on" and Extraspaceremover!="on" and fullcaps!="on" and charcount!="on"):
        return HttpResponse("Please select any operation and try again")
        
        
    return render(request, 'analyze.html', params)

    # else:
    #     return HttpResponse("Error")
    