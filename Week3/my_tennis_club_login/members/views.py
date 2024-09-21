
from django.http import HttpResponse
from django.template import loader

def members(request):
    template = loader.get_template('login_reg_h.htm')
    return HttpResponse(template.render())
