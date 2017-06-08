#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

class Identificador(models.Model):
    class Meta:
        verbose_name = 'Identificador'
        verbose_name_plural = 'Identificadores'

    codigo = models.CharField(
        max_length=100,
        )
    fecha_ingreso = models.DateField(
        )
    def __str__(self):
        return "%s: %s" % (self.fecha_ingreso, self.codigo)



#     ########     ###     ######  #### ######## ##    ## ######## ########
#     ##     ##   ## ##   ##    ##  ##  ##       ###   ##    ##    ##
#     ##     ##  ##   ##  ##        ##  ##       ####  ##    ##    ##
#     ########  ##     ## ##        ##  ######   ## ## ##    ##    ######
#     ##        ######### ##        ##  ##       ##  ####    ##    ##
#     ##        ##     ## ##    ##  ##  ##       ##   ###    ##    ##
#     ##        ##     ##  ######  #### ######## ##    ##    ##    ########


class Demo(models.Model):
    E_CIVIL = (
        ('1', 'Soltero'),
        ('2', 'Casado'),
        ('3', 'Pareja estable'),
        ('4', 'Separado'),
        ('5', 'Viudo'),
        ('6', 'Otro'),
        )
    ESTUDIOS = (
        ('1', 'Primarios'),
        ('2', 'Secundarios'),
        ('3', 'Superiores'),
        ('4', 'Sin estudios'),
        ('5', 'Desconocido'),
        )
    LABORAL = (
        ('1', 'Activo'),
        ('2', 'Baja temporal'),
        ('3', 'Sin trabajo actual'),
        ('4', 'Pensionista'),
        ('5', 'Nunca ha trabajado'),
        ('6', 'Desconocido'),
        )
    SEXO = (
        ('1', 'Masculino'),
        ('2', 'Femenino'),
        )
    SECTOR = (
        ('1', 'AIS Gracia'),
        ('2', 'AIS Dreta'),
        ('3', 'AIS Guinardó'),
        )

    identificador = models.OneToOneField(
        Identificador,
        on_delete=models.CASCADE,
        primary_key=True,
        )
    fnac = models.DateField(
        verbose_name='Fecha de Nac.',
        blank=True,
        )
    sexo = models.CharField(
        choices=SEXO,
        max_length=2,
        blank=True,
        )
    sector = models.CharField(
        verbose_name='Sector',
        max_length=1,
        choices=SECTOR,
        blank=True,
        )
    e_civil = models.CharField(
        verbose_name='Estado civil',
        max_length=1,
        choices=E_CIVIL,
        blank=True,
        )
    n_hijos = models.PositiveSmallIntegerField(
        verbose_name='Número de hijos',
        blank=True,
        null=True,
        )
    laboral = models.CharField(
        verbose_name='Situación laboral',
        max_length=1,
        choices=LABORAL,
        blank=True,
        )
    estudios = models.CharField(
        verbose_name='Nivel de estudios',
        max_length=1,
        choices=ESTUDIOS,
        blank=True,
        )

class Ingreso(models.Model):
    identificador = models.OneToOneField(
        Identificador,
        on_delete=models.CASCADE,
        primary_key=True,
        )
    fing = models.DateField(
        verbose_name='Fecha de Ingreso',
        blank=True,
        )
    falta = models.DateField(
        verbose_name='Fecha de Alta',
        blank=True,
        )
    dispalta = models.CharField(
        verbose_name='Dispositivo de alta',
        max_length=2,
        choices= (
            (0, 'Domicilio'),
            (1, 'CESMA'),
            (2, 'H de dia'),
            (3, 'Subagudos'),
            (4, 'Agudos'),
            (5, 'Otros'),
            ),
        blank=True,
        )

class Escala(models.Model):
    identificador = models.ForeignKey(
        Identificador,
        )
    fecha = models.DateField(
        )
    class Meta:
        abstract = True


#     ########   ######  ####  ######
#     ##     ## ##    ##  ##  ##    ##
#     ##     ## ##        ##  ##
#     ########  ##        ##   ######
#     ##     ## ##        ##        ##
#     ##     ## ##    ##  ##  ##    ##
#     ########   ######  ####  ######

class Bcis(Escala):
    class Meta:
        verbose_name = 'BCIS'
        verbose_name_plural = 'Escalas BCIS'

    item_01 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_02 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_03 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_04 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_05 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_06 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_07 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_08 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_09 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_10 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_11 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_12 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_13 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_14 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_15 = models.PositiveSmallIntegerField(
        null = True,
        )
    
    @property
    def autoref(self):
        return (self.item_01 + self.item_03 + self.item_04 + 
                self.item_05 + self.item_06 + self.item_08 + 
                self.item_12 + self.item_14 + self.item_15)
    
    @property
    def autocert(self):
        return (self.item_02 + self.item_07 +
                self.item_09 + self.item_10 + self.item_11 +
                self.item_13)
    @property
    def comp(self):
        return (self.autocert + self.autoref)

    def __str__(self):
        return "%s: A.ref=%s / A.cert=%s / Comp.=%s" % (self.fecha,
              str(self.autoref),
              str(self.autocert),
              str(self.comp))


#     ########  ########  ########   ######
#     ##     ## ##     ## ##     ## ##    ##
#     ##     ## ##     ## ##     ## ##
#     ########  ########  ########   ######
#     ##     ## ##        ##   ##         ##
#     ##     ## ##        ##    ##  ##    ##
#     ########  ##        ##     ##  ######


class Bprs(Escala):
    class Meta:
        verbose_name = 'BPRS'
        verbose_name_plural = 'Escalas BPRS'
    item_01 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_02 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_03 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_04 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_05 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_06 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_07 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_08 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_09 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_10 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_11 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_12 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_13 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_14 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_15 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_16 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_17 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_18 = models.PositiveSmallIntegerField(
        null = True,
        )
    @property
    def total(self):
        return (self.item_01 + self.item_02 + self.item_03 + self.item_04 + 
                self.item_05 + self.item_06 + self.item_07 + self.item_08 + 
                self.item_09 + self.item_10 + self.item_11 + self.item_12 + 
                self.item_13 + self.item_14 + self.item_15 + self.item_16 + 
                self.item_17 + self.item_18)
    def __str__(self):
        return "%s: BPRS=%s" % (self.fecha, str(self.total))

class Cgi(Escala):
    class Meta:
        verbose_name = 'escala CGI'
        verbose_name_plural = 'escalas CGI'
    cgi_a = models.PositiveSmallIntegerField(
        null = True,
        )
    cgi_b = models.PositiveSmallIntegerField(
        null = True,
        )
    def __str__(self):
        return "%s: CGI_s=%s / CGI_e=%s" % (self.fecha, self.cgi_a, self.cgi_b)

class Eeag(Escala):
    class Meta:
        verbose_name = 'escala EEAG'
        verbose_name_plural = 'escalas EEAG'
    eeag = models.PositiveSmallIntegerField()
    def __str__(self):
        return "%s: EEAG=%s" % (self.fecha, self.eeag)



#     DUKE

class Duke(Escala):
    class Meta:
        verbose_name = 'Duke'
        verbose_name_plural = 'Escalas Duke'

    item_01 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_02 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_03 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_04 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_05 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_06 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_07 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_08 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_09 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_10 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_11 = models.PositiveSmallIntegerField(
        null = True,
        )
    
    @property
    def total(self):
        return (self.item_01 + self.item_02 + self.item_03 + self.item_04 + 
                self.item_05 + self.item_06 + self.item_07 + self.item_08 + 
                self.item_09 + self.item_10 + self.item_11)
    def __str__(self):
        return "%s: DUKE=%s" % (self.fecha, str(self.total))



#     ##     ## ########  ########   ######
#     ##     ## ##     ## ##     ## ##    ##
#     ##     ## ##     ## ##     ## ##
#     ######### ##     ## ########   ######
#     ##     ## ##     ## ##   ##         ##
#     ##     ## ##     ## ##    ##  ##    ##
#     ##     ## ########  ##     ##  ######
#
class Hdrs(Escala):
    class Meta:
        verbose_name = 'escala Hamilton'
        verbose_name_plural = 'escalas Hamilton'
    item_01 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_02 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_03 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_04 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_05 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_06 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_07 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_08 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_09 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_10 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_11 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_12 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_13 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_14 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_15 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_16 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_17 = models.PositiveSmallIntegerField(
        null = True,
        )
    @property
    def total(self):
        return (self.item_01 + self.item_02 + self.item_03 + self.item_04 + 
                self.item_05 + self.item_06 + self.item_07 + self.item_08 + 
                self.item_09 + self.item_10 + self.item_11 + self.item_12 + 
                self.item_13 + self.item_14 + self.item_15 + self.item_16 + 
                self.item_17)
    def __str__(self):
        return "%s: HDRS=%s" % (self.fecha, str(self.total))
        
        
# MADRS
#     DUKE

class Madrs(Escala):
    class Meta:
        verbose_name = 'MADRS'
        verbose_name_plural = 'Escalas MADRS'

    item_01 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_02 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_03 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_04 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_05 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_06 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_07 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_08 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_09 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_10 = models.PositiveSmallIntegerField(
        null = True,
        )
    
    @property
    def total(self):
        return (self.item_01 + self.item_02 + self.item_03 + self.item_04 + 
                self.item_05 + self.item_06 + self.item_07 + self.item_08 + 
                self.item_09 + self.item_10)
    def __str__(self):
        return "%s: MADRS=%s" % (self.fecha, str(self.total))
        

#
#      ######     ##     ##   ##   #####    #####
#      ##   ##    ##     ###  ##  ##   ##  ##   ##
#      ##   ##   ####    ###  ##  ##       ##
#      ######    ## #    ## # ##   #####    #####
#      ##       ######   ## # ##       ##       ##
#      ##       ##   #   ##  ###  ##   ##  ##   ##
#      ##      ###   ##  ##   ##   #####    #####
#
class Panss(Escala):
    class Meta:
        verbose_name = 'PANSS'
        verbose_name_plural = 'Escalas PANSS'

    item_p01 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_p02 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_p03 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_p04 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_p05 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_p06 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_p07 = models.PositiveSmallIntegerField(
        null = True,
        )
    @property
    def panss_sp(self):
        return (self.item_p01 + self.item_p02 + self.item_p03 + self.item_p04 + 
                self.item_p05 + self.item_p06 + self.item_p07)
    
    item_n01 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_n02 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_n03 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_n04 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_n05 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_n06 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_n07 = models.PositiveSmallIntegerField(
        null = True,
        )
    @property
    def panss_sn(self):
        return (self.item_n01 + self.item_n02 + self.item_n03 + self.item_n04 + 
                self.item_n05 + self.item_n06 + self.item_n07)

    item_g01 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_g02 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_g03 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_g04 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_g05 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_g06 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_g07 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_g08 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_g09 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_g10 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_g11 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_g12 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_g13 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_g14 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_g15 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_g16 = models.PositiveSmallIntegerField(
        null = True,
        )
    @property
    def panss_sg(self):
        return (self.item_g01 + self.item_g02 + self.item_g03 + self.item_g04 + 
                self.item_g05 + self.item_g06 + self.item_g07 + self.item_g08 + 
                self.item_g09 + self.item_g10 + self.item_g11 + self.item_g12 + 
                self.item_g13 + self.item_g14 + self.item_g15 + self.item_g16)
    
    @property
    def total(self):
        return (self.panss_sp + self.panss_sn + self.panss_sg)
    
    def __str__(self):
        return "%s: SP=%s / SN=%s / SG=%s / Total=%s" % (self.fecha, str(self.panss_sp),
                                                         str(self.panss_sn), str(self.panss_sg),
                                                         str(self.total))
    

#     ########  ##       ##     ## ########  ######  ##     ## #### ##    ##
#     ##     ## ##       ##     ##    ##    ##    ## ##     ##  ##  ##   ##
#     ##     ## ##       ##     ##    ##    ##       ##     ##  ##  ##  ##
#     ########  ##       ##     ##    ##    ##       #########  ##  #####
#     ##        ##       ##     ##    ##    ##       ##     ##  ##  ##  ##
#     ##        ##       ##     ##    ##    ##    ## ##     ##  ##  ##   ##
#     ##        ########  #######     ##     ######  ##     ## #### ##    ##

class Plutchik_s(Escala):
    class Meta:
        verbose_name = "Escala de Riesgo Suicida de Plutchik"
    item_01 = models.BooleanField()
    item_02 = models.BooleanField()
    item_03 = models.BooleanField()
    item_04 = models.BooleanField()
    item_05 = models.BooleanField()
    item_06 = models.BooleanField()
    item_07 = models.BooleanField()
    item_08 = models.BooleanField()
    item_09 = models.BooleanField()
    item_10 = models.BooleanField()
    item_11 = models.BooleanField()
    item_12 = models.BooleanField()
    item_13 = models.BooleanField()
    item_14 = models.BooleanField()
    item_15 = models.BooleanField()

class Plutchik_v(Escala):
    class Meta:
        verbose_name = "Escala de Riesgo Violencia de Plutchik"
    item_01 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_02 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_03 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_04 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_05 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_06 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_07 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_08 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_09 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_10 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_11 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_12 = models.BooleanField()


class Satisfaccion(Escala):
    class Meta:
        verbose_name = "Escala Satisfacción"
        verbose_name_plural = "Escalas Satisfacción"
    item_1 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_2 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_3 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_4 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_5 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_6 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_7 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_8 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_9 = models.TextField(
        null = True,
        )
    item_10 = models.TextField(
        null = True,
        )

#     ##    ## ##     ## ########   ######
#      ##  ##  ###   ### ##     ## ##    ##
#       ####   #### #### ##     ## ##
#        ##    ## ### ## ########   ######
#        ##    ##     ## ##   ##         ##
#        ##    ##     ## ##    ##  ##    ##
#        ##    ##     ## ##     ##  ######
class Ymrs(Escala):
    class Meta:
        verbose_name = 'escala Young de manía'
        verbose_name_plural = 'escalas Young de manía'
    item_01 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_02 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_03 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_04 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_05 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_06 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_07 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_08 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_09 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_10 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_11 = models.PositiveSmallIntegerField(
        null = True,
        )
    
    @property
    def total(self):
        return (self.item_01 + self.item_02 + self.item_03 + self.item_04 + 
                self.item_05 + self.item_06 + self.item_07 + self.item_08 + 
                self.item_09 + self.item_10 + self.item_11)
    
    def __str__(self):
        return "%s: YMRS=%s" % (self.fecha, str(self.total))

class Who_das(Escala):
    class Meta:
        verbose_name = 'escala WHO-DAS'
        verbose_name_plural = 'escalas WHO-DAS'
    d1_1 = models.PositiveSmallIntegerField(
        null = True,
        )
    d1_2 = models.PositiveSmallIntegerField(
        null = True,
        )
    d1_3 = models.PositiveSmallIntegerField(
        null = True,
        )
    d1_4 = models.PositiveSmallIntegerField(
        null = True,
        )
    d1_5 = models.PositiveSmallIntegerField(
        null = True,
        )
    d1_6 = models.PositiveSmallIntegerField(
        null = True,
        )
    d2_1 = models.PositiveSmallIntegerField(
        null = True,
        )
    d2_2 = models.PositiveSmallIntegerField(
        null = True,
        )
    d2_3 = models.PositiveSmallIntegerField(
        null = True,
        )
    d2_4 = models.PositiveSmallIntegerField(
        null = True,
        )
    d2_5 = models.PositiveSmallIntegerField(
        null = True,
        )
    d3_1 = models.PositiveSmallIntegerField(
        null = True,
        )
    d3_2 = models.PositiveSmallIntegerField(
        null = True,
        )
    d3_3 = models.PositiveSmallIntegerField(
        null = True,
        )
    d3_4 = models.PositiveSmallIntegerField(
        null = True,
        )
    d4_1 = models.PositiveSmallIntegerField(
        null = True,
        )
    d4_2 = models.PositiveSmallIntegerField(
        null = True,
        )
    d4_3 = models.PositiveSmallIntegerField(
        null = True,
        )
    d4_4 = models.PositiveSmallIntegerField(
        null = True,
        )
    d4_5 = models.PositiveSmallIntegerField(
        null = True,
        )
    d5_1 = models.PositiveSmallIntegerField(
        null = True,
        )
    d5_2 = models.PositiveSmallIntegerField(
        null = True,
        )
    d5_3 = models.PositiveSmallIntegerField(
        null = True,
        )
    d5_4 = models.PositiveSmallIntegerField(
        null = True,
        )
    d5_5 = models.PositiveSmallIntegerField(
        null = True,
        )
    d5_6 = models.PositiveSmallIntegerField(
        null = True,
        ) 
    d5_7 = models.PositiveSmallIntegerField(
        null = True,
        )
    d5_8 = models.PositiveSmallIntegerField(
        null = True,
        )
    d6_1 = models.PositiveSmallIntegerField(
        null = True,
        )
    d6_2 = models.PositiveSmallIntegerField(
        null = True,
        )
    d6_3 = models.PositiveSmallIntegerField(
        null = True,
        )
    d6_4 = models.PositiveSmallIntegerField(
        null = True,
        )
    d6_5 = models.PositiveSmallIntegerField(
        null = True,
        )
    d6_6 = models.PositiveSmallIntegerField(
        null = True,
        )
    d6_7 = models.PositiveSmallIntegerField(
        null = True,
        )
    d6_8 = models.PositiveSmallIntegerField(
        null = True
        )   
    h1 = models.PositiveSmallIntegerField(
        null = True
        )
    h2 = models.PositiveSmallIntegerField(
        null = True
        )
    h3 = models.PositiveSmallIntegerField(
        null = True
        )


# ZARIT

class Zarit(Escala):
    class Meta:
        verbose_name = 'ZARIT'
        verbose_name_plural = 'Escalas ZARIT'
    item_01 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_02 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_03 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_04 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_05 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_06 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_07 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_08 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_09 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_10 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_11 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_12 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_13 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_14 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_15 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_16 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_17 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_18 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_19 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_20 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_21 = models.PositiveSmallIntegerField(
        null = True,
        )
    item_22 = models.PositiveSmallIntegerField(
        null = True,
        )
    @property
    def total(self):
        return (self.item_01 + self.item_02 + self.item_03 + self.item_04 + 
                self.item_05 + self.item_06 + self.item_07 + self.item_08 + 
                self.item_09 + self.item_10 + self.item_11 + self.item_12 + 
                self.item_13 + self.item_14 + self.item_15 + self.item_16 + 
                self.item_17 + self.item_18 + self.item_19 + self.item_20 +
                self.item_21 + self.item_22)
    def __str__(self):
        return "%s: ZARIT=%s" % (self.fecha, str(self.total))