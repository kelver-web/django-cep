# -*- coding: utf-8 -*-
from django.http import HttpResponse
import urllib2
import re
from pycorreios import Correios


# Podem ser usados outros webservices como o http://ceplivre.pc2consultoria.com/index.php?module=cep&cep=%s&formato=xml
# Entretanto deve ser observado o encoding para que ele seja alterado na linha 14
# Outra referencia util http://allissonazevedo.com/2012/03/22/buscando-cep-diretamente-pelo-site-dos-correios-em-python/
def addressGet(request, zipcode):
    # Trata o zipcode removendo caracteres diferentes de numeros.
    # Assim não precisamos nos preocupar de como vai vir o cep.
    zipcode = re.sub('[^\d]+', '', zipcode)
    results = Correios().cep(zipcode)
    return HttpResponse('{"street":"%s","district":"%s","city":"%s","state":"%s"}' % (
        results['logradouro'], results['bairro'], results['cidade'], results['uf']))
