# coding=utf-8
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """Perfil del usuario"""
    user = models.OneToOneField(User)
    sex = models.CharField(max_length=1, null=True, blank=True)
    accepted_eula = models.BooleanField()

    def __unicode__(self):
        return ''.join(['Profile of ', self.user.first_name])


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
    """Modelo que define un menu para el negocio"""
    business = models.ForeignKey(Business)
    description = models.CharField(max_length=150)

    def __unicode__(self):
        return self.description


class SortCommon(models.Model):
    """Clase base de ordenado para cualquier objeto"""
    def __cmp__(self, other):
        if self.sort < other.sort:
            return -1
        elif self.sort > other.sort:
            return 1
        else:
            return 0

    sort = models.IntegerField()

    class Meta:
        abstract = True


class MenuItem(SortCommon):
    """Modelo que define el item de un menu"""
    business = models.ForeignKey(Business)
    menu = models.ForeignKey(Menu)
    description = models.CharField(max_length=150)

    def __unicode__(self):
        return self.description


class MenuSection(SortCommon):
    """Modelo que define la seccion de un menu"""
    menu = models.ForeignKey(Menu)
    items = models.ManyToManyField(MenuItem)
    description = models.CharField(max_length=150)

    def __unicode__(self):
        return self.description


class Branch(models.Model):
    """Modelo que define una sucursal de un negocio"""
    business = models.ForeignKey(Business)
    name = models.CharField(max_length=200)
    items = models.ManyToManyField(MenuItem)
    exclude_items = models.ManyToManyField(MenuItem, related_name="exclude_items")

    def __unicode__(self):
        return self.name