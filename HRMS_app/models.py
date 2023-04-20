from django.db import models
from django.core.validators import RegexValidator


RELATION_CHOICES = (
    ('1', 'Father'),
    ('2', 'Mother'),
    ('3', 'Brother'),
    ('4', 'Sister'),
    ('5', 'wife'),
    ('6', 'husband'),
)

# g1wTxgQveAqU7PIvNL+dNtSklGSxCamFn0ST0S5T


class FamilyInfoManager(models.Manager):
    def send_msg(self, msg):


        account_sid = 'AC34ee859c1832745012adc68428d840a6'
        auth_token = '153888f2fca0da540e9deb290f692fda'
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=msg,
            from_='[+][120][28167190]',
            to=self.phone_number
        )

    def delete_family_info(self):
        self.is_deleted = True

        return 'Info deleted'

    def get_name(self):
        return self.first_name+' '+self.last_name

    def get_family_info(self):
        return 'Name : {}, DoB: {}, Relation: {} Phone NO: {}'.format(self.get_name(), self.dob,
                                                                      self.ralation, self.phone_number)


class FamilyInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    relation = models.CharField(max_length=1, choices=RELATION_CHOICES)
    dob = models.DateField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,13}$',
                                 message="Phone number must be entered in the format: '+999999999'."
                                         " Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=13, blank=True)
    is_deleted = models.BooleanField(default=False, verbose_name="Is Deleted", editable=False)
    objects = FamilyInfoManager()








