from django.http import HttpResponse
from django.template import loader
from Familiares.models import Familiar

# Create your views here.


def lista_familiares(request):
    template = loader.get_template('familias_index.html')

    familiares = Familiar.objects.all()
    familiares_list = []

    for pariente in familiares:
        par_str = f'''{pariente.name} {pariente.surname}. Nació el {pariente.birthday.date()}, tiene {pariente.age} 
                   años y es mi {pariente.relation}'''

        familiares_list.append(par_str)

    data = {'familiares': familiares_list}
    doc = template.render(data)

    return HttpResponse(doc)
