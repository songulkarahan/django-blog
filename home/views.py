from django.shortcuts import render,HttpResponse

# Create your views here.

def home_view(request):
    if request.user.is_authenticated:
        context = {
            'isim' : 'Songül',
            'soyisim': 'Karahan',
        }
    else:
        context = {
            'isim' : 'Misafir',
            'soyisim': 'Kullanıcı',
        }

    return render(request, 'home.html', context)
