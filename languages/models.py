from django.db import models
from heroku_connect.db import models as hc_model
class Language(models.Model):
    name = models.CharField(max_length=50)
    paradigm = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class LanguageSalesforce(hc_model.HerokuConnectModel):
    sf_object_name = 'language__c'
    name = hc_model.Text(sf_field_name='name__c',max_length=50)
