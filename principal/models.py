# coding=utf-8
from django.db import models
from django.contrib.auth.models import User

#Constantes
ITEMS_TYPES = (('SE', 'Section'), ('IT', 'Item'))


class Business(models.Model):
    """Modelo que define a un negocio"""
    name = models.CharField(max_length=150)
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.name


class Branch(models.Model):
    """Modelo que define una sucursal de un negocio"""
    business = models.ForeignKey(Business)
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Post(models.Model):
    """Modelo que define un post de un negocio"""
    business = models.ForeignKey(Business)


class Section(models.Model):
    """Modelo que define la seccion de un menu"""
    business = models.ForeignKey(Business)
    description = models.CharField(max_length=150)
    item_type = models.CharField(max_length=2, choices=ITEMS_TYPES)

    def __unicode__(self):
        return self.description


class Item(models.Model):
    """Modelo que define el item de un menu"""
    business = models.ForeignKey(Business)
    description = models.CharField(max_length=150)
    item_type = models.CharField(max_length=2, choices=ITEMS_TYPES)

    def __unicode__(self):
        return self.description


class Menu(models.Model):
    """Modelo que define un menu para el negocio"""
    business = models.ForeignKey(Business)
    description = models.CharField(max_length=150)
    sections = models.ManyToManyField(Section, through='MenuSection')
    items = models.ManyToManyField(Item, through='MenuItem')

    def __unicode__(self):
        return self.description

    def get_body(self):
        """Obtiene una lista de elementos que contiene el menu, en el orden correspondiente
        """
        menuSections = MenuSection.objects.filter(menu=self.pk).order_by('sort')
        menuItems = MenuItem.objects.filter(menu=self.pk).order_by('sort')
        body = []
        body.extend(menuSections)
        body.extend(menuItems)
        body.sort(key=lambda item: item.sort)
        return body


class MenuSection(models.Model):
    """Tabla muchos a muchos personalizada de las secciones de un menu"""
    menu = models.ForeignKey(Menu)
    section = models.ForeignKey(Section)
    sort = models.IntegerField()

    def __unicode__(self):
        return self.section.description


class MenuItem(models.Model):
    """Tabla muchos a muchos perzonalizada de los items de un menu"""
    menu = models.ForeignKey(Menu)
    item = models.ForeignKey(Item)
    sort = models.IntegerField()

    def __unicode__(self):
        return self.item.description