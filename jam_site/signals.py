from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from models import Band, Userbands


@receiver(user_signed_up)
def update_userbands_on_signup(request, user):
    bands = Band.objects.all()
    for band in bands:
        userband = Userbands(user_id=user.id,
                             band_id=band.id,
                            band_name=band.name,
                            band_selected=true)
        userband.save()
