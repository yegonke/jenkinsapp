from django.db import models
from django.core.validators import RegexValidator

#Custom
from totp.abstractbaseuser import AbstractBaseUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from totp.usermanager import UserManager, PermissionsMixin
# Create your models here.

# this model Stores the data of the Phones Verified
class PhoneModel(AbstractBaseUser, PermissionsMixin):
    # refer  https://stackoverflow.com/questions/2113908/what-regular-expression-will-match-valid-international-phone-numbers
    phone_regex = RegexValidator(regex=r'\+(9[976]\d|8[987530]\d|6[987]\d|5[90]\d|42\d|3[875]\d|2[98654321]\d|9[8543210]|8[6421]|6[6543210]|5[87654321]|4[987654310]|3[9643210]|2[70]|7|1)\d{1,14}$', message="Phone number must be entered in the format: '+2547XXXXXXXX'. Up to 15 digits allowed.")
    mobile = models.CharField(validators=[phone_regex], verbose_name="Phone number", max_length=15, unique=True)
    
    isVerified = models.BooleanField(blank=False, default=False)
    counter = models.IntegerField(default=0, blank=False)   # For HOTP Verification

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)


    objects = UserManager()

    USERNAME_FIELD = 'mobile'
    def __str__(self):
        return str(self.mobile)

    class Meta:
        verbose_name = "Phone No."
        verbose_name_plural = "Phone No.s"