from django.shortcuts import render

# Create your views here.

def platform(request):
    text = 'купить'
    context ={
        'text': text,
    }

    return render(request,'platform.html',context)

def games(request):
    text = 'купить'
    text1 = 'Attomic Heart '
    text2 = 'Cyberpunc 2077 '
    text3 = 'PayDay2 '
    context ={
        'text': text,
        'text1':text1,
        'text2':text2,
        'text3': text3
    }

    return render(request,'games.html',context)

def cart(request):
    text = 'купить'
    context ={
        'text': text,
    }

    return render(request,'cart.html',context)