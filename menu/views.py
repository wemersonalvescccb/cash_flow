from django.shortcuts import render

# Create your views here.
def menu(args):
    return render(args, 'menu.html')
    