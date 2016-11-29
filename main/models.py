from __future__ import unicode_literals

from django.db import models
from django.dispatch import receiver
from django.utils.encoding import python_2_unicode_compatible
from django.core.files.uploadedfile import InMemoryUploadedFile
import qrcode
import StringIO
import binascii

class Pokemon(models.Model):
    pid = models.IntegerField(default=0)
    name = models.CharField(max_length=100, default="")
    link = models.CharField(max_length=100, default="")
    qr_code = models.TextField(default="")
    qr_code_image = models.ImageField(upload_to='qr', blank=True, null=True)

    def __str__(self):
        return str(self.pid) + " - " + self.name

@receiver(models.signals.post_save, sender=Pokemon)
def execute_after_save(sender, instance, created, *args, **kwargs):
    if created:
        
        print "calling post create..."

        qr = qrcode.QRCode(
            version = 1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size = 6,
            border = 0,
        )

        code = instance.qr_code

        hexa = binascii.unhexlify(code)

        print hexa

        qr.add_data(hexa)
        qr.make(fit=True)

        img = qr.make_image()

        buffer = StringIO.StringIO()
        img.save(buffer)
        filename = 'pokemon-%s.png' % (instance.pid)
        filebuffer = InMemoryUploadedFile(buffer, None, filename, 'image/png', buffer.len, None)
        instance.qr_code_image.save(filename, filebuffer)

