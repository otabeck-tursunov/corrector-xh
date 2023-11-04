from django.shortcuts import render

from .models import Togri, Notogri


def home(request):
    s = request.GET.get('searched')
    t = Togri.objects.filter(soz=s)
    if len(t) > 0:
        n = Notogri.objects.filter(t_soz=t[0])
        t = t[0]
    else:
        n = Notogri.objects.filter(n_soz=s)
        if len(n) > 0:
            t = n[0].t_soz
            n = Notogri.objects.filter(t_soz=t)
    # if t==False:
    #     t = ''
    data = {
        'togri': t,
        'notogri': n
    }
    return render(request, 'result.html', data)
