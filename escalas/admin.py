#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from escalas.models import *
from escalas.forms import *
from django.forms import TextInput

class MyModelOptions(admin.ModelAdmin):
    change_list_filter_template = "admin/filter_listing.html"

class Diagnostico_pacInLine(admin.StackedInline):
    model = Diagnostico_pac
    extra = 0
    fieldsets = (
        (None, {
            'fields': (
                ('f_dg', 'diagnostico'),
                )
            }),
        )
    raw_id_fields = ('diagnostico',)
    related_lookup_fields = {
        'fk': ['identificador','diagnostico'],
    }

class TratamientoInLine(admin.StackedInline):
    model=Tratamiento
    extra=0
    fields=(('f_inicio', 'farmaco', 'mg_dia'),
            ('f_termino', 'motivo'),
            )

class BcisInLine(admin.StackedInline):
    model = Bcis
    form = BcisAdminForm
    extra = 0
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)

class BprsInLine(admin.StackedInline):
    model = Bprs
    form = BprsAdminForm
    extra = 0
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)

class CgiInLine(admin.StackedInline):
    model = Cgi
    form = CgiAdminForm
    extra = 0
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)
    
class DukeInLine(admin.StackedInline):
    model = Duke
    form = DukeAdminForm
    extra = 0
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)

class HdrsInLine(admin.StackedInline):
    model = Hdrs
    form = HdrsAdminForm
    extra = 0
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)
    
class MadrsInLine(admin.StackedInline):
    model = Madrs
    form = MadrsAdminForm
    extra = 0
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)
    
class YmrsInLine(admin.StackedInline):
    model =Ymrs
    form = YmrsAdminForm
    extra = 0
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)

class PanssInLine(admin.StackedInline):
    model = Panss
    form = PanssAdminForm
    extra = 0
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)
    fieldsets = (
        (None, {
            'fields': ('fecha',)
          }),
        ('Síntomas positivos', {
            'fields': ('item_p01', 'item_p02',
                       'item_p03', 'item_p04',
                       'item_p05', 'item_p06',
                       'item_p07',)
          }),
        ('Síntomas negativos', {
            'fields': ('item_n01', 'item_n02',
                       'item_n03', 'item_n04',
                       'item_n05', 'item_n06',
                       'item_n07',)
          }),
        ('Síntomas generales', {
            'fields': ('item_g01', 'item_g02',
                       'item_g03', 'item_g04',
                       'item_g05', 'item_g06',
                       'item_g07', 'item_g08',
                       'item_g09', 'item_g10',
                       'item_g11', 'item_g12',
                       'item_g13', 'item_g14',
                       'item_g15', 'item_g16')
          }),

      )

class Who_dasInline(admin.StackedInline):
    model = Who_das
    form = Who_dasAdminForm
    extra = 0
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)

class ZaritInline(admin.StackedInline):
    model = Zarit
    form = ZaritAdminForm
    extra = 0
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)

@admin.register(Identificador)
class IdentificadorAdmin(admin.ModelAdmin):
    date_hierarchy = 'fecha_ingreso'
    list_display = ('fecha_ingreso', 'codigo')
    ordering = ('fecha_ingreso',)


    fieldsets = (
        (None, {
            'fields': (
                ('codigo'),
                )
            }),
        ('Demográficos', {
          'fields': (
              ('fnac', 'sexo'),
              ('e_civil', 'n_hijos', 'laboral'),
              )
            }),
        ('Ingreso', {
          'fields': (
            ('fecha_ingreso', 'procedencia'),
            ('falta', 'dispalta')
            )
          }),
        )

    inlines = [
               Diagnostico_pacInLine,
               TratamientoInLine,
               BcisInLine,
               BprsInLine,
               CgiInLine,
               DukeInLine,
               HdrsInLine,
               MadrsInLine,
               PanssInLine,
               YmrsInLine,
               Who_dasInline,
               ZaritInline
               ]



admin.site.register(Diagnostico)
admin.site.register(Farmaco)
