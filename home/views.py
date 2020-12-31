from django.shortcuts import render,HttpResponse,redirect
from  home.models import EnglishToManipuri

def home(request):
    """

    :param request:
    :return:
    """
    return render(request,"home/Home.html")


def index(request):
    """

    :param request:
    :return:
    """
    return redirect('home')


def about(request):
    """

    :param request:
    :return:
    """
    return render(request,"home/About.html")


def convert(request):
    if request.method == "POST":
        word = request.POST.get('english')
        firstLetter = word[0:1].upper()
        restLetters = word[1:len(word)].lower()
        fullwords = str(firstLetter) + str(restLetters)
        words_store = EnglishToManipuri.objects.filter(English = fullwords)
        print(words_store)
        msg = ''
        if not words_store:
            msg ='Word not found!!!Try again with correct spelling'
        else:
            msg = ''
        return render(request,"home/Home.html",{'word':words_store,'msg':msg})
    else:
        return redirect('home')



