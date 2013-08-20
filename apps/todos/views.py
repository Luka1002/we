from django.shortcuts import render_to_response
from django.template import RequestContext

#from forms import PracticeForm

def todo_list(request):
    context = RequestContext(request)
    #form = PracticeForm()

    #context.update({'form': form})
    return render_to_response('todo/index.html',context)

