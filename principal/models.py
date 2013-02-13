# coding=utf-8
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """Perfil del usuario"""
    user = models.OneToOneField(User)


class Business(models.Model):
    """Modelo que define a un negocio"""
    name = models.CharField(max_length=150)
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.name


class Post(models.Model):
    """Modelo que define un post de un negocio"""
    business = models.ForeignKey(Business)


class Menu(models.Model):
    """Modelo que define un menú para el negocio"""
    business = models.ForeignKey(Business)
    description = models.CharField(max_length=150)

    def __unicode__(self):
        return self.description


class MenuSection(models.Model):
    """Modelo que define la seccion de un menú"""
    menu = models.ForeignKey(Menu)
    items = models.ManyToManyField(MenuItem)
    description = models.CharField(max_length=150)

    def __unicode__(self):
        return self.description


class MenuItem(models.Model):
    """Modelo que define el item de un menú"""
    business = models.ForeignKey(Business)
    section = models.ForeignKey(MenuSection)
    description = models.CharField(max_length=150)

    def __unicode__(self):
        return self.description


class Branch(models.Model):
    """Modelo que define una sucursal de un negocio"""
    business = models.ForeignKey(Business)
    items = models.ManyToManyField(MenuItem)
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name