from django.db import models

class Services(models.Model):
    name = models.CharField(max_length=455, blank=False)
    desc = models.TextField()
    images = models.ManyToManyField('Images', related_name='Services')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Servis: {self.id} | {self.name}"
    class Meta:
        verbose_name = "Hizmet"
        verbose_name_plural = "Hizmetler"

class Projects(models.Model):
    name = models.CharField(max_length=444, blank=False)
    desc = models.TextField()
    partner = models.ManyToManyField("Partners", related_name="Projects")
    images = models.ManyToManyField("Images", related_name="Projects")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Proje: {self.id} | {self.name}"
    
    class Meta:
        verbose_name = "Proje"
        verbose_name_plural = "Projeler"


class Partners(models.Model): 
    name = models.CharField(max_length=444, blank=False)
    desc = models.TextField()
    partner_logo = models.ImageField()

    def __str__(self):
        return f"Partner: {self.id} | {self.name}"
    class Meta:
        verbose_name = "Partner"
        verbose_name_plural = "Partnerler"



class Images(models.Model):
    image = models.ImageField(upload_to='uploaded_images/')

    def __str__(self):
        return f"Image {self.id}"
    class Meta:
        verbose_name = "Görsel"
        verbose_name_plural = "Görseller"
