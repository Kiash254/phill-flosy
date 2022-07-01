from django.db import models

Places_lands=(
('thika' ,'thika'),
('kiambu' ,'kiambu'),
('mombasa' ,'mombasa'),
('nairobi' ,'nairobi'),
('nakuru' ,'nakuru'),
('makadimu', 'makadimu'),
('mombasa' ,'mombasa'),
('nairobi' ,'nairobi'),
('makuyu' ,'makuyu'),
('muranga' ,'muranga'),
('Nyeri' ,'Nyeri'),
)
class  Products(models.Model):
    name=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    description=models.TextField(max_length=100)
    image=models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url

class Laundry(models.Model):
    name=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    description=models.TextField(max_length=100)
    image=models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.name
    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url

class Land(models.Model):
    size=models.CharField(max_length=100)
    image=models.ImageField(null=True,blank=True)
    price=models.CharField(max_length=100)
    place=models.CharField(max_length=100,null=True,blank=True,choices=Places_lands)
    def __str__(self):
        return self.size
    @property
    def imageURL(self):
      try:
        url=self.image.url
      except:
        url=''
      return url


