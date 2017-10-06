#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import date
from django.utils.translation import ugettext_lazy as _
from django.db.models import Q
from django.contrib import admin
from escalas.models import *
from escalas.forms import *
from django.forms import TextInput, RadioSelect

class MyModelOptions(admin.ModelAdmin):
    change_list_filter_template = "admin/filter_listing.html"


class Diagnostico_pacInLine(admin.StackedInline):
    model = Diagnostico_pac
    form = Diagnostico_pacForm
    extra = 0
    fields = (('dg_previo', 'diagnostico', 'dg_principal'),
             )

    raw_id_fields = ('dg_previo', 'diagnostico',)
    autocomplete_lookup_fields = {
        'fk': ['dg_previo', 'diagnostico',],
    }

class TratamientoInLine(admin.StackedInline):
    model=Tratamiento
    form = TratamientoForm
    extra=0
    fields=(('farmaco', 'mg_dia_inicio', 'mg_dia'),
            ('depot', 'motivo'),
            )
    raw_id_fields = ('farmaco',)
    autocomplete_lookup_fields = {
        'fk': ['farmaco'],
    }

class BcisInLine(admin.StackedInline):
    model = Bcis
    form = BcisAdminForm
    extra = 0
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-closed',)

class BprsInLine(admin.StackedInline):
    model = Bprs
    form = BprsAdminForm
    extra = 0
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-closed',)

class EeagInLine(admin.StackedInline):
    model = Eeag
    extra = 0
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-closed',)

class Icg_geInLine(admin.StackedInline):
    model = Icg_ge
    form = Icg_geAdminForm
    extra = 0
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-closed',)

class Icg_meInLine(admin.StackedInline):
    model = Icg_me
    form = Icg_meAdminForm
    extra = 0
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-closed',)
    
class DukeInLine(admin.StackedInline):
    model = Duke
    form = DukeAdminForm
    extra = 0
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-closed',)

class HdrsInLine(admin.StackedInline):
    model = Hdrs
    form = HdrsAdminForm
    extra = 0
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-closed',)
    
class MadrsInLine(admin.StackedInline):
    model = Madrs
    form = MadrsAdminForm
    extra = 0
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-closed',)

class PanssInLine(admin.StackedInline):
    model = Panss
    form = PanssAdminForm
    extra = 0
    classes = ('grp-collapse grp-open',)
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

class YmrsInLine(admin.StackedInline):
    model =Ymrs
    form = YmrsAdminForm
    extra = 0
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-closed',)
    fields = ('fecha',
        'item_01', 'item_02',
        'item_03', 'item_04',
        'item_05', 'item_06',
        'item_07', 'item_08',
        'item_09', 'item_10',
        'item_11',
        )

class Who_dasInline(admin.StackedInline):
    model = Who_das
    form = Who_dasAdminForm
    extra = 0
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-closed',)
    fieldsets = (
        (None, {
            'fields': ('fecha',)
            }),
        (None, {
            'fields': ('d1_1', 'd1_2', 'd1_3', 'd1_4', 'd1_5', 'd1_6',)
            }),
        (None, {
            'fields': ('d2_1', 'd2_2', 'd2_3', 'd2_4', 'd2_5',)
            }),
        (None, {
            'fields': ('d3_1', 'd3_2', 'd3_3', 'd3_4',)
            }),
        (None, {
            'fields': ('d4_1', 'd4_2', 'd4_3', 'd4_4', 'd4_5',)
            }),
        (None, {
            'fields': ('d5_1', 'd5_2', 'd5_3', 'd5_4', 'd5_5', 'd5_6', 'd5_7', 'd5_8',)
            }),
        (None, {
            'fields': ('d6_1', 'd6_2', 'd6_3', 'd6_4', 'd6_5', 'd6_6', 'd6_7', 'd6_8',)
            }),
        (None, {
            'fields': ('h1', 'h2', 'h3',)
            }),
        )
    

class ZaritInline(admin.StackedInline):
    model = Zarit
    form = ZaritAdminForm
    extra = 0
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-closed',)
    
@admin.register(Diagnostico)
class DiagnosticoAdmin(admin.ModelAdmin):
    list_display = ('diagnostico', 'dsm',)

@admin.register(Farmaco)
class FarmacoAdmin(admin.ModelAdmin):
    pass

@admin.register(Tratamiento)
class TratamientoAdmin(admin.ModelAdmin):
    pass

@admin.register(Csq8)
class Csq8Admin(admin.ModelAdmin):
    form = Csq8AdminForm
    
@admin.register(Satis)
class Csq8Satis(admin.ModelAdmin):
    form = SatisAdminForm




# Filtro para ver los que rechazan ingreso y los que no
class IngresoListFilter(admin.SimpleListFilter):
    title = _('Ingresa')
    parameter_name = 'ingresa'
    def lookups(self, request, model_admin):
        return (
            ('si', _('Si')),
            ('no', _('No')),
        )
    def queryset(self, request, queryset):
        if self.value() == 'no':
            return queryset.filter(rechazo__isnull=False).exclude(rechazo='')
        if self.value() == 'si':
            return queryset.filter(Q(rechazo__isnull=True) | Q(rechazo__exact=''))

@admin.register(Identificador)
class IdentificadorAdmin(admin.ModelAdmin):
    form = IdentificadorForm
    def _edad_(self,obj):
        today = date.today()
        try:
            return today.year - obj.fnac.year - (
                (today.month, today.day) < (obj.fnac.month, obj.fnac.day))
        except:
            return
            
    def _dg_(self, obj):
        try:
            return join(obj.diagnostico_pac_set.filter(dg_principal=True)
        except:
            return
        
    _dg_.allow_tags = True
    
    _dg_.short_description = 'Diagnósticos'
    _dg_.admin_order_field = '_dg_'
    
    _edad_.short_description = 'Edad'
    _edad_.admin_order_field = '_edad_'
    
    date_hierarchy = 'fecha_ingreso'
    list_filter = ['psiquiatra', IngresoListFilter,]
    
    list_display = ('fecha_ingreso', 'rechazo',  'codigo', 'sexo', '_edad_', 'sector', 'falta', 'dispalta', '_dg_', 'psiquiatra' )
    ordering = ('-fecha_ingreso',)

    fieldsets = (
        (None, {
            'fields': (
                ('codigo', 'sector', 'rechazo'),
                )
            }),
        ('Demográficos', {
          'fields': (
              ('fnac', 'sexo', 'estudios'),
              ('e_civil', 'n_hijos', 'laboral'),
              )
            }),
        ('Ingreso', {
          'fields': (
            ('fecha_ingreso', 'procedencia', 'psiquiatra'),
            ('falta', 'dispalta', 'estado_alta')
            )
          }),
        ('Cuidador', {
            'fields': (
                ('cuidador', 'horas_cuidador'),
                ('calidad_cuidador', 'claudica_cuidador')
                )
        })
        )

    inlines = [
               Diagnostico_pacInLine,
               TratamientoInLine,
               BcisInLine,
               BprsInLine,
               EeagInLine,
               Icg_geInLine,
               Icg_meInLine,
               DukeInLine,
               HdrsInLine,
               MadrsInLine,
               PanssInLine,
               YmrsInLine,
               Who_dasInline,
               ZaritInline
               ]
