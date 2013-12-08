from django.http import HttpResponse

def hello(request):
  return HttpResponse("Hey bitches...I mean world")