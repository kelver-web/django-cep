import json
from django.forms.widgets import TextInput
from django.utils.safestring import mark_safe


class CEPInput(TextInput):
    def __init__(self, *args, **kwargs):
        self.address = kwargs.pop('address')
        super(CEPInput, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs):
        # define input class based on user definition of attrs
        try:
            self.attrs['class']
        except KeyError:
            self.attrs['class'] = "zip-field"
        else:
            self.attrs['class'] = "zip-field %s" % self.attrs['class']
        output = super(CEPInput, self).render(name, value, attrs)
        # insert address json in the rendering
        if self.address is not None:
            js_dict = json.dumps(self.address)
            output += u'<script type="text/javascript">var address = %s;</script>' % js_dict
        return mark_safe(output)

    class Media:
        js = ('js/cep.js',)
