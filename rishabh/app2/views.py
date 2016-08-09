from django.shortcuts import render

import textwrap

from django.http import HttpResponse
from django.views.generic.base import View


from app1.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

#class HomePageView(View):

    #def dispatch(request, *args, **kwargs):
      #   response_text = textwrap.dedent('''\
       #     <html>
        #    <head>
         #       <title>Greetings to the world</title>
          #  </head>
           # <body>
            #    <h1>Greetings to the world</h1>
             #   <p>Hello, world!</p>
              #   </body>
               #   </html>
                #     ''')
                 # return HttpResponse(response_text)

@login_required
def home(request):
        return render_to_response(
            'home2.html',
            {'user': request.user}
        )

