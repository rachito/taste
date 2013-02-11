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
    description = models.CharField(max_length=150)
    business = models.ForeignKey(Business)

    def __unicode__(self):
        return self.description


class MenuSection(models.Model):
    """Modelo que define la seccion de un menú"""
    description = models.CharField(max_length=150)
    menu = models.ForeignKey(Menu)

    def __unicode__(self):
        return self.description


class MenuItem(models.Model):
    """Modelo que define el item de un menú"""
    description = models.CharField(max_length=150)
    section = models.ForeignKey(MenuSection)
    business = models.ForeignKey(Business)

    def __unicode__(self):
        return self.description


class Branch(models.Model):
    """Modelo que define una sucursal de un negocio"""
    name = models.CharField(max_length=200)
    items = models.ManyToManyField(MenuItem)
    business = models.ForeignKey(Business)

    def __unicode__(self):
        return self.name
