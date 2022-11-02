from audioop import reverse
from email.policy import default
from enum import unique
from locale import currency
from pickle import TRUE
from random import choices
from secrets import choice
from turtle import title
from django.db import models
from django.template.defaultfilters import slugify, timesince_filter
from django.utils import timezone
from uuid import uuid4
from django.contrib.auth.models import User
import base64

class Client(models.Model):

    PROVINCES = [
    ('Gauteng', 'Gauteng'),
    ('Free State', 'Free State'),
    ('Limpopo', 'Limpopo'),
    ]

    #Basic Fields
    clientName = models.CharField(null=True, blank=True, max_length=200)
    addressLine1 = models.CharField(null=True, blank=True, max_length=200)
    province = models.CharField(choices=PROVINCES, blank=True, max_length=100)
    postalCode = models.CharField(null=True, blank=True, max_length=10)
    phoneNumber = models.CharField(null=True, blank=True, max_length=100)
    emailAddress = models.CharField(null=True, blank=True, max_length=100)


    #Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return '{} {} {}'.format(self.clientName, self.province, self.uniqueId)


    def get_absolute_url(self):
        return reverse('client-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {} {}'.format(self.clientName, self.province, self.uniqueId))

        self.slug = slugify('{} {} {}'.format(self.clientName, self.province, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Client, self).save(*args, **kwargs)

class Product(models.Model):
    CURRENCY = [
    ('R', 'ZAR',),
    ('$', 'USD'),
    ]

    title=models.CharField(null=True, blank=True,max_length=100)
    description = models.TextField(null = True , blank = True)
    quantity= models.FloatField(null = True , blank = True)
    price= models.FloatField(null=True, blank = True)
    currency= models.CharField(choices= CURRENCY, default='R', max_length = 100 )

        #utility fields

    uniqueID = models.CharField(null=True, blank= True, max_length = 100)
    slug = models.SlugField(max_length = 500 , unique= True, blank = True, null=True)
    date_created = models.DateTimeField(blank = True, null = True)
    last_updated = models.DateField(blank= True , null= True)

    def __str__(self):
        return '{}', '{}'.format(self.title, self.uniqueID)

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"slug": self.slug})

    def save(self, *args , **kwargs ):
        if self.date_created is None: 
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.clientName, self.province, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.clientName, self.province, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Product, self).save(*args, **kwargs)

class Invoice(models.Model):
    TERMS = [
        ('14 days', '14 days'),
        ('30 days', '30 days'),
        ('60 days', '60 days'),

        ]
    STATUS = [
        ('CURRENT','CURRENT'),
        ('OVERDUE', 'OVERDUE'),
        ('PAID', 'PAID'),
        ]

    title= models.CharField(null= True, blank= True, max_length = 100)
    number = models.CharField(null= True, blank=True, max_length=100)
    dueDate= models.DateField(null = True, blank = True, max_length = 100)
    paymentTrems = models.CharField(choices = STATUS, default ='CURRENT', max_length= 100)
    status = models.CharField(choices=STATUS, default = 'CURRENT', max_length= 100)
    notes = models.TextField(null= True, blank = True)

    client = models.ForeignKey(Client, blank = True, null = True , on_delete = models.SET_NULL)
    product = models.ForeignKey(Product , blank = True , null = True , on_delete = models.SET_NULL)
    uniqueId = models.CharField(null = True , blank = True , max_length = 100)
    slug = models.SlugField(max_length = 500 , unique = True , blank = True , null = True)
    date_created = models.DateTimeField(blank = True , null = True)
    last_updated = models.DateTimeField(blank = True , null = True)

    
    def __str__(self):
        return '{}', '{}'.format(self.title, self.uniqueID)

    def get_absolute_url(self):
        return reverse("invoice-detail", kwargs={"slug": self.slug})

    def save(self, *args , **kwargs ):
        if self.date_created is None: 
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.clientName, self.province, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.clientName, self.province, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Product, self).save(*args, **kwargs)

class Settings(models.Model):

    PROVINCE = [
        ('Gauteng', 'Gauteng'),
        ('Free State', 'Free State'),
        ('Limpopo', 'Limpopo' ),

    ]

    clientName = models.CharField(null = True , blank = True , max_length= 200)
    clientLogo = models.ImageField(default= 'default_logo.jpg', upload_to = 'company_logos')
    addressLine1 = models.CharField(null = True , blank = True , max_length = 200 )
    province = models.CharField(null =PROVINCE  , blank = True , max_length = 100  )
    postalCode = models.CharField(null = True , blank = True , max_length = 100 )
    phoneNumber = models.CharField(null = True , blank = True , max_length = 100 )
    emailAddress = models.CharField(null = True , blank = True , max_length = 100 )
    textNumber = models.CharField(null = True , blank = True , max_length = 100 )


    uniqueId = models.CharField(null = True , blank = True , max_length =100)
    slug = models.SlugField(max_length = 100 , unique = True , blank = True , null = True )
    date_created = models.DateTimeField(blank = True , null =True)
    last_created = models.DateTimeField(blank = True , null = True )


    def __str__(self):
        return '{} {} {}'.format(self.clientName,self.province, self.uniqueId)

    
    def get_absolute_url(self):
        return reverse('settings-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {} {}'.format(self.clientName, self.province, self.uniqueId))

        self.slug = slugify('{} {} {}'.format(self.clientName, self.province, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Settings, self).save(*args, **kwargs)