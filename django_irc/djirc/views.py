from django.shortcuts import render_to_response, HttpResponseRedirect
from models import Comment
from forms import CommentForm
from django.core.context_processors import csrf
import time

# Create your views here.
def djirc(request):
    '''
    '''

    return render_to_response('djirc.html',
                              {'username': request.user.username})