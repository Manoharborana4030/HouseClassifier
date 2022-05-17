from django.shortcuts import render

def home(request):

    return render(request,'index.html')
def find(request):

    return render(request,'find.html')
def predicate(request):
    if request.method=='POST':
        file_name=request.FILES['file']
        print('@@@',file_name)

    return render(request,'predicate.html')