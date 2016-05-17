|Travis|_ |Python27|_ |Python35|_ |PyPi|_

.. |Travis| image:: https://api.travis-ci.org/staticdev/django-cep.svg?branch=master
.. _Travis: https://travis-ci.org/staticdev/django-cep

.. |Python27| image:: https://img.shields.io/badge/python-2.7-blue.svg
.. _Python27: https://badge.fury.io/py/django-pagination-bootstrap

.. |Python35| image:: https://img.shields.io/badge/python-3.5-blue.svg
.. _Python35: https://badge.fury.io/py/django-pagination-bootstrap

.. |PyPi| image:: https://badge.fury.io/py/django-cep.svg
.. _PyPi: https://badge.fury.io/py/django-cep


django-cep
===============

This application enables Django_ powered websites to have autofilled address fields in forms based on brazilian CEP field.

Installation
------------
To install ``django-cep`` simply run::

    pip install django-cep

Configuration
-------------

We need to hook ``django-cep`` into our project.

Put ``cep`` into your ``INSTALLED_APPS`` at settings module::

      INSTALLED_APPS = (
         ...
         'cep',
      )

Bind the ``cep urls.py`` into your ``main urls.py`` with something like::

      url(r'^cep/', include('cep.urls')),

Usage
-----
Currently the only syntax supported is setting the IDs of the address fields in the widget of the CEP field. For other ways to set this up, see the NEXT-STEPS file.

I. Import the django-cep widget CEPInput in your forms.py::

    from cep.widgets import CEPInput

II. Set your CEP field for using the CEPInput, with the correct address fields ID, for example::

      my_cep_field = ChangeToMyCEPFieldModelName(label=u"CEP",
                              help_text="Format: XXXXX-XXX",
                              widget=CEPInput(address={
                                                       'street': 'id_street_field',
                                                       'district': 'id_district_field', 
                                                       'city': 'id_city_field',
                                                       'state': 'id_state_field'
                                                       }))

 That stands for a street field ID equals id_street_field, district field ID equals id_district_field, city field ID equals id_city_field and a state field ID equals id_state_field. 

Also note that the JavaScript used in this app requires JQuery_ to run properly.

It is highly recommended that you use `Django Localflavor`_'s BRStateChoiceField for the State field, to make it render the correct brazilian state from the list.

.. _Django: https://www.djangoproject.com/
.. _JQuery: http://jquery.com/
.. _Django Localflavor: https://github.com/django/django-localflavor-br
