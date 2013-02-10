# coding=utf-8
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """Perfil del usuario"""
    user = models.OneToOneField(User)


class Business(models.Model):
    """Modelo que define a un negocio"""
    user = models.OneToOneField(User)


class Post(models.Model):
    """Modelo que define un post de un negocio"""
    business = models.ForeignKey(Business)


class MenuItem(models.Model):
    """Modelo que define el item de un menú"""
    description = models.CharField(max_length=200)
    business = models.ForeignKey(Business)


class MenuSection(models.Model):
    """Modelo que define la seccion de un menú"""
    description = models.CharField(max_length=200)
    business = models.ForeignKey(Business)
    items = models.ManyToManyField(MenuItem)


class Menu(models.Model):
    """Modelo que define un menú para el negocio"""
    business = models.ForeignKey(Business)
    sections = models.ManyToManyField(MenuSection)


class Branch(models.Model):
    """Modelo que define una sucursal de un negocio"""
    name = models.CharField(max_length=200)
    business = models.ForeignKey(Business)
    menus = models.ManyToManyField(Menu)
