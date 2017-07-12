#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.core.validators import RegexValidator

class Identificador(models.Model):
    class Meta:
        verbose_name = 'Identificador'
        verbose_name_plural = 'Identificadores'
    codigo = models.CharField(
        max_length=100,
        help_text = 'Siglas nombre + fecha ingreso: p.e. "ABC24122016',
        validators=[
            RegexValidator(
                regex=r'\b[A-Z]{3}\d{8}',
                message='Formato incorrecto (XYZddmmaaaa)',
                ),
            ]
        )
    fecha_ingreso = models.DateField(
        )    
    fnac = models.DateField(
        verbose_name='Fecha de Nac.',
        blank=True,
        null=True,
        )
    sexo = models.CharField(
        choices=(
            ('1', 'Masculino'),
            ('2', 'Femenino'),
            ),
        max_length=2,
        blank=True,
        )
    e_civil = models.CharField(
        verbose_name='Estado civil',
        max_length=1,
        choices=(
            ('1', 'Soltero'),
            ('2', 'Casado'),
            ('3', 'Pareja estable'),
            ('4', 'Separado'),
            ('5', 'Viudo'),
            ('9', 'Otro'),
            ),
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
        choices=(
            ('1', 'Activo'),
            ('2', 'Baja temporal'),
            ('3', 'Sin trabajo actual'),
            ('4', 'Pensionista'),
            ('5', 'Nunca ha trabajado'),
            ('6', 'Estudiante'),
            ('9', 'Desconocido'),
            ),
        blank=True,
        )
    estudios = models.CharField(
        verbose_name='Nivel de estudios',
        max_length=1,
        choices=(
            ('1', 'Primarios'),
            ('2', 'Secundarios'),
            ('3', 'Superiores'),
            ('4', 'Sin estudios'),
            ('5', 'Desconocido'),
            ),
        blank=True,
        )
    sector = models.CharField(
        verbose_name='Sector',
        max_length=1,
        choices=(
            ('1', 'AIS Gracia'),
            ('2', 'AIS Dreta'),
            ('3', 'AIS Guinardó'),
            ),
        blank=True,
        )
    procedencia = models.CharField(
        verbose_name='Procedencia',
        max_length=2,
        choices=(
            ('00', 'Urgencias'),
            ('01', 'Sala B2'),
            ('02', 'CSMA'),
            ('03', 'H de día'),
            ('04', 'CCEE'),
            ('05', 'Subagudos'),
            ('99', 'Otros'),
            ),
        blank=True,
        )
    falta = models.DateField(
        verbose_name='Fecha de Alta',
        blank=True,
        null=True,
        )
    dispalta = models.CharField(
        verbose_name='Dispositivo de alta',
        max_length=2,
        choices= (
            ('0', 'Domicilio'),
            ('1', 'CSMA'),
            ('2', 'H de dia'),
            ('3', 'Subagudos'),
            ('4', 'Agudos'),
            ('5', 'CCEE Sant Pau'),
            ('9', 'Otros'),
            ),
        blank=True,
        )
    psiquiatra = models.CharField(
        verbose_name='psiquiatra',
        max_length=3,
        choices=(
            ('AKG', 'A. Keymer'),
            ('AMB', 'A. Martin'),
            ('SVC', 'S. Vieira'),
            ),
        blank=True,
        )
    def __str__(self):
        return self.codigo



#     ######## ########     ###    ########    ###    ##     ## #### ######## ##    ## ########  #######
#        ##    ##     ##   ## ##      ##      ## ##   ###   ###  ##  ##       ###   ##    ##    ##     ##
#        ##    ##     ##  ##   ##     ##     ##   ##  #### ####  ##  ##       ####  ##    ##    ##     ##
#        ##    ########  ##     ##    ##    ##     ## ## ### ##  ##  ######   ## ## ##    ##    ##     ##
#        ##    ##   ##   #########    ##    ######### ##     ##  ##  ##       ##  ####    ##    ##     ##
#        ##    ##    ##  ##     ##    ##    ##     ## ##     ##  ##  ##       ##   ###    ##    ##     ##
#        ##    ##     ## ##     ##    ##    ##     ## ##     ## #### ######## ##    ##    ##     #######

class Farmaco(models.Model):
    farmaco=models.CharField(
        max_length=200,
        )
    def __str__(self):
        return self.farmaco
    
    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "farmaco__icontains",)
      
   
class Tratamiento(models.Model):
    identificador = models.ForeignKey(
        Identificador,
        )
    f_inicio = models.DateField(
        verbose_name='Fecha de incio',
        )
    farmaco = models.ForeignKey(
        Farmaco,
        )    
    mg_dia = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name='mg/dia',
        )
    depot = models.BooleanField(
        choices=(
            (False, 'No'),
            (True, 'Si'),
            )
        )
    f_termino = models.DateField(
        verbose_name='Fecha de término',
        blank=True,
        null=True,
        )
    motivo = models.CharField(
        max_length=2,
        blank=True,
        null=True,
        choices=(
            ('01', 'Abandono de tratamiento'),
            ('02', 'Falta de eficacia'),
            ('03', 'Efecto adverso EP'),
            ('04', 'Efecto adverso digestivo'),
            ('05', 'Efecto adverso hematologico'),
            ('06', 'Efecto adverso autonómico'),
            ('07', 'Otro efecto adverso'),
            ('99', 'NE'),
            )
        )

    def __str__(self):
        return "%s:%s %s mg/dia" % (self.f_inicio, self.farmaco, self.mg_dia)
        
        

#     ########  ####    ###     ######   ##    ##  #######   ######  ######## ####  ######   #######
#     ##     ##  ##    ## ##   ##    ##  ###   ## ##     ## ##    ##    ##     ##  ##    ## ##     ##
#     ##     ##  ##   ##   ##  ##        ####  ## ##     ## ##          ##     ##  ##       ##     ##
#     ##     ##  ##  ##     ## ##   #### ## ## ## ##     ##  ######     ##     ##  ##       ##     ##
#     ##     ##  ##  ######### ##    ##  ##  #### ##     ##       ##    ##     ##  ##       ##     ##
#     ##     ##  ##  ##     ## ##    ##  ##   ### ##     ## ##    ##    ##     ##  ##    ## ##     ##
#     ########  #### ##     ##  ######   ##    ##  #######   ######     ##    ####  ######   #######

class Diagnostico(models.Model):
    diagnostico=models.CharField(
        max_length=300,
        )
    def __str__(self):
        return self.diagnostico
        
    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "diagnostico__icontains",)

class Diagnostico_pac(models.Model):
    class Meta:
        verbose_name = 'Diagnóstico'
        verbose_name_plural = 'Diagnósticos'
    identificador = models.ForeignKey(
        Identificador,
        )
    f_dg = models.DateField(
        verbose_name = "Fecha diagnostico",
        )
    diagnostico = models.ForeignKey(
        Diagnostico,
        )
    def __str__(self):
        return "%s:%s" % (self.f_dg, self.diagnostico)



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
    L_BCIS = (
        (0, '0.Nada de acuerdo'),
        (1, '1.Un poco de acuerdo'),
        (2, '2.Bastante de acuerdo'),
        (3, '3.Totalmente de acuerdo'),
        )
    class Meta:
        verbose_name = 'BCIS'
        verbose_name_plural = 'Escalas BCIS'

    item_01 = models.PositiveSmallIntegerField(
        choices=L_BCIS,
        null = True,
        blank = True,
        )
    item_02 = models.PositiveSmallIntegerField(
        choices=L_BCIS,
        null = True,
        blank = True,
        )
    item_03 = models.PositiveSmallIntegerField(
        choices=L_BCIS,
        null = True,
        blank = True,
        )
    item_04 = models.PositiveSmallIntegerField(
        choices=L_BCIS,
        null = True,
        blank = True,
        )
    item_05 = models.PositiveSmallIntegerField(
        choices=L_BCIS,
        null = True,
        blank = True,
        )
    item_06 = models.PositiveSmallIntegerField(
        choices=L_BCIS,
        null = True,
        blank = True,
        )
    item_07 = models.PositiveSmallIntegerField(
        choices=L_BCIS,
        null = True,
        blank = True,
        )
    item_08 = models.PositiveSmallIntegerField(
        choices=L_BCIS,
        null = True,
        blank = True,
        )
    item_09 = models.PositiveSmallIntegerField(
        choices=L_BCIS,
        null = True,
        blank = True,
        )
    item_10 = models.PositiveSmallIntegerField(
        choices=L_BCIS,
        null = True,
        blank = True,
        )
    item_11 = models.PositiveSmallIntegerField(
        choices=L_BCIS,
        null = True,
        blank = True,
        )
    item_12 = models.PositiveSmallIntegerField(
        choices=L_BCIS,
        null = True,
        blank = True,
        )
    item_13 = models.PositiveSmallIntegerField(
        choices=L_BCIS,
        null = True,
        blank = True,
        )
    item_14 = models.PositiveSmallIntegerField(
        choices=L_BCIS,
        null = True,
        blank = True,
        )
    item_15 = models.PositiveSmallIntegerField(
        choices=L_BCIS,
        null = True,
        blank = True,
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
    LIKERT6 = (
    	(0, '0.Ausente'),
    	(1, '1.Muy leve'),
    	(2, '2.Leve'),
    	(3, '3.Moderado'),
    	(4, '4.Bastante acentuado'),
    	(5, '5.Grave'),
        (6, '6.Muy Grave'),
        )
    class Meta:
        verbose_name = 'BPRS'
        verbose_name_plural = 'Escalas BPRS'
    item_01 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=LIKERT6,
        )
    item_02 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=LIKERT6,
        )
    item_03 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=LIKERT6,
        )
    item_04 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=LIKERT6,
        )
    item_05 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=LIKERT6,
        )
    item_06 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=LIKERT6,
        )
    item_07 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=LIKERT6,
        )
    item_08 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=LIKERT6,
        )
    item_09 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=LIKERT6,
        )
    item_10 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=LIKERT6,
        )
    item_11 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=LIKERT6,
        )
    item_12 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=LIKERT6,
        )
    item_13 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=LIKERT6,
        )
    item_14 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=LIKERT6,
        )
    item_15 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=LIKERT6,
        )
    item_16 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=LIKERT6,
        )
    item_17 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=LIKERT6,
        )
    item_18 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=LIKERT6,
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


#      ######   ######   #######           #######
#     ##    ## ##    ## ##     ##         ##     ##
#     ##       ##       ##     ##         ##     ##
#     ##        ######  ##     ## #######  #######
#     ##             ## ##  ## ##         ##     ##
#     ##    ## ##    ## ##    ##          ##     ##
#      ######   ######   ##### ##          #######    
class Csq8(models.Model):
    class Meta:
        verbose_name = 'CSQ-8'
        verbose_name_plural = 'Escalas CSQ-8'
    autor = models.CharField(
        max_length=3,
        blank = True,
        choices=(
            ('PAC', 'Paciente'),
            ('FAM', 'Familia'),
            ),
        )
    item_01 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=(
            ('4', 'Excelente'),
            ('3', 'Buen'),
            ('2', 'Regula'),
            ('1', 'Mala'),
            ),
        )
    item_02 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=(
            ('4', 'No definitivamente'),
            ('3', 'En muy pocos casos'),
            ('2', 'Si en general'),
            ('1', 'Si definitivamente'),
            ),
        )
    item_03 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=(
            ('4', 'En casi todos'),
            ('3', 'En la mayor parte'),
            ('2', 'Solo en algunos'),
            ('1', 'En ninguno'),
            ),
        )
    item_04 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=(
            ('4', 'No definitivamente'),
            ('3', 'No , creo que no'),
            ('2', 'Si, creo que si'),
            ('1', 'Si definitivamente'),
            ),
        )
    item_05 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=(
            ('4', 'Nada satisfecho/a'),
            ('3', 'Indiferente o moderadamente no satisfecho/a'),
            ('2', 'Moderadamente satisfecho/a'),
            ('1', 'Muy satisfecho/a'),
            ),
        )
    item_06 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=(
            ('4', 'Si me ayudaron mucho'),
            ('3', 'Si me ayudaron algo'),
            ('2', 'No realmente no me ayudaron'),
            ('1', 'No parecían poner las cosas peor'),
            ),
        )
    item_07 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=(
            ('4', 'Muy satisfecho/a'),
            ('3', 'Moderadamente satisfecho/a'),
            ('2', 'Algo insatisfecho/a'),
            ('1', 'Muy Insatisfecho/a'),
            ),
        )
    item_08 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=(
            ('4', 'No definitivamente'),
            ('3', 'No posiblemente'),
            ('2', 'Si, creo que si'),
            ('1', 'Si con seguridad'),
            ),
        )
    item_09 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_10 = models.TextField(
        null = True,
        blank = True,
        )

#     ########  ##     ## ##    ## ########
#     ##     ## ##     ## ##   ##  ##
#     ##     ## ##     ## ##  ##   ##
#     ##     ## ##     ## #####    ######
#     ##     ## ##     ## ##  ##   ##
#     ##     ## ##     ## ##   ##  ##
#     ########   #######  ##    ## ########

class Duke(Escala):
    LIKERT_DUKE = (
        (1, '1. Mucho menos de lo que deseo'),
        (2, '2. Menos de lo que deseo'),
        (3, '3. Ni mucho ni poco'),
        (4, '4. Casi como deseo'),
        (5, '5. Tanto como deseo'),
        )
    class Meta:
        verbose_name = 'Duke'
        verbose_name_plural = 'Escalas Duke'
    item_01 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=LIKERT_DUKE,
        )
    item_02 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=LIKERT_DUKE,
        )
    item_03 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=LIKERT_DUKE,
        )
    item_04 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=LIKERT_DUKE,
        )
    item_05 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=LIKERT_DUKE,
        )
    item_06 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=LIKERT_DUKE,
        )
    item_07 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=LIKERT_DUKE,
        )
    item_08 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=LIKERT_DUKE,
        )
    item_09 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=LIKERT_DUKE,
        )
    item_10 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=LIKERT_DUKE,
        )
    item_11 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=LIKERT_DUKE,
        )
    @property
    def total(self):
        return (self.item_01 + self.item_02 + self.item_03 + self.item_04 + 
                self.item_05 + self.item_06 + self.item_07 + self.item_08 + 
                self.item_09 + self.item_10 + self.item_11)
    def __str__(self):
        return "%s: DUKE=%s" % (self.fecha, str(self.total))
        
        
#     ####  ######   ######
#      ##  ##    ## ##    ##
#      ##  ##       ##
#      ##  ##       ##   ####
#      ##  ##       ##    ##
#      ##  ##    ## ##    ##
#     ####  ######   ######
class Icg_ge(Escala):
    class Meta:
        verbose_name = 'escala ICG_Gravedad'
        verbose_name_plural = 'escalas ICG_Gravedad'
    icg_ge = models.PositiveSmallIntegerField(
        null = True,
        choices = (
            (0, '0.No evaluado'),
            (1, '1.Normal, no enfermo'),
            (2, '2.Dudosamente enfermo'),
            (3, '3.Levemente enfermo'),
            (4, '4.Moderadamente enfermo'),
            (5, '5.Marcadamente enfermo'),
            (6, '6.Gravemente enfermo'),
            (7, '7.Entre los pac. mas extremadamente enfermos'),
            ),
        )
    quien_ge = models.CharField(
        max_length=3,
        null = True,
        choices = (
    		('PSQ', 'Psiquiatra'),
    		('PAC', 'Paciente'),
    		),
        )
    def __str__(self):
        return "%s: ICG_GE=%s" % (self.fecha, self.icg_ge)

class Icg_me(Escala):
    class Meta:
        verbose_name = 'escala ICG_Mejoría'
        verbose_name_plural = 'escalas ICG_Mejoría'
    icg_me = models.PositiveSmallIntegerField(
        null = True,
        )
    quien_me = models.CharField(
        max_length=3,
        null = True,
        )
    def __str__(self):
        return "%s: ICG_ME=%s" % (self.fecha, self.icg_me)

class Eeag(Escala):
    class Meta:
        verbose_name = 'escala EEAG'
        verbose_name_plural = 'escalas EEAG'
    eeag = models.PositiveSmallIntegerField()
    def __str__(self):
        return "%s: EEAG=%s" % (self.fecha, self.eeag)







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
        blank = True,
        )
    item_02 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_03 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_04 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_05 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_06 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_07 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_08 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_09 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_10 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_11 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_12 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_13 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_14 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_15 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_16 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_17 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
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
        
        
#     ##     ##    ###    ########  ########   ######
#     ###   ###   ## ##   ##     ## ##     ## ##    ##
#     #### ####  ##   ##  ##     ## ##     ## ##
#     ## ### ## ##     ## ##     ## ########   ######
#     ##     ## ######### ##     ## ##   ##         ##
#     ##     ## ##     ## ##     ## ##    ##  ##    ##
#     ##     ## ##     ## ########  ##     ##  ######
class Madrs(Escala):
    class Meta:
        verbose_name = 'MADRS'
        verbose_name_plural = 'Escalas MADRS'

    item_01 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_02 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_03 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_04 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_05 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_06 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_07 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_08 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_09 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_10 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
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
        blank = True,
        )
    item_p02 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_p03 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_p04 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_p05 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_p06 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_p07 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    @property
    def panss_sp(self):
        return (self.item_p01 + self.item_p02 + self.item_p03 + self.item_p04 + 
                self.item_p05 + self.item_p06 + self.item_p07)
    
    item_n01 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_n02 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_n03 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_n04 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_n05 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_n06 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_n07 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    @property
    def panss_sn(self):
        return (self.item_n01 + self.item_n02 + self.item_n03 + self.item_n04 + 
                self.item_n05 + self.item_n06 + self.item_n07)

    item_g01 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_g02 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_g03 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_g04 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_g05 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_g06 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_g07 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_g08 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_g09 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_g10 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_g11 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_g12 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_g13 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_g14 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_g15 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_g16 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
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
        blank = True,
        )
    item_02 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_03 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_04 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_05 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_06 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_07 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_08 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_09 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_10 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_11 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
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
    LIKERT5 = (
        (1, '1.Ninguna'),
        (2, '2.Leve'),
        (3, '3.Moderada'),
        (4, '4.Severa'),
        (5, '5.Extrema / no puede'),
        )
    d1_1 = models.IntegerField(
        choices = LIKERT5,
        null = True,
        blank = True,
        )
    d1_2 = models.PositiveSmallIntegerField(
        choices = LIKERT5,
        null = True,
        blank = True,
        )
    d1_3 = models.PositiveSmallIntegerField(
        choices = LIKERT5,
        null = True,
        blank = True,
        )
    d1_4 = models.PositiveSmallIntegerField(
        choices = LIKERT5,
        null = True,
        blank = True,
        )
    d1_5 = models.PositiveSmallIntegerField(
        choices = LIKERT5,
        null = True,
        blank = True,
        )
    d1_6 = models.PositiveSmallIntegerField(
        choices = LIKERT5,
        null = True,
        blank = True,
        )
    d2_1 = models.PositiveSmallIntegerField(
        choices = LIKERT5,
        null = True,
        blank = True,
        )
    d2_2 = models.PositiveSmallIntegerField(
        choices = LIKERT5,
        null = True,
        blank = True,
        )
    d2_3 = models.PositiveSmallIntegerField(
        choices = LIKERT5,
        null = True,
        blank = True,
        )
    d2_4 = models.PositiveSmallIntegerField(
        choices = LIKERT5,
        null = True,
        blank = True,
        )
    d2_5 = models.PositiveSmallIntegerField(
        choices = LIKERT5,
        null = True,
        blank = True,
        )
    d3_1 = models.PositiveSmallIntegerField(
        choices = LIKERT5,
        null = True,
        blank = True,
        )
    d3_2 = models.PositiveSmallIntegerField(
        choices = LIKERT5,
        null = True,
        blank = True,
        )
    d3_3 = models.PositiveSmallIntegerField(
        choices = LIKERT5,
        null = True,
        blank = True,
        )
    d3_4 = models.PositiveSmallIntegerField(
        choices = LIKERT5,
        null = True,
        blank = True,
        )
    d4_1 = models.PositiveSmallIntegerField(
        choices = LIKERT5,
        null = True,
        blank = True,
        )
    d4_2 = models.PositiveSmallIntegerField(
        choices = LIKERT5,
        null = True,
        blank = True,
        )
    d4_3 = models.PositiveSmallIntegerField(
        choices = LIKERT5,
        null = True,
        blank = True,
        )
    d4_4 = models.PositiveSmallIntegerField(
        choices = LIKERT5,
        null = True,
        blank = True,
        )
    d4_5 = models.PositiveSmallIntegerField(
        choices = LIKERT5,
        null = True,
        blank = True,
        )
    d5_1 = models.PositiveSmallIntegerField(
        choices = LIKERT5,
        null = True,
        blank = True,
        )
    d5_2 = models.PositiveSmallIntegerField(
        choices = LIKERT5,
        null = True,
        blank = True,
        )
    d5_3 = models.PositiveSmallIntegerField(
        choices = LIKERT5,
        null = True,
        blank = True,
        )
    d5_4 = models.PositiveSmallIntegerField(
        choices = LIKERT5,
        null = True,
        blank = True,
        )
    d5_5 = models.PositiveSmallIntegerField(
        choices = LIKERT5,
        null = True,
        blank = True,
        )
    d5_6 = models.PositiveSmallIntegerField(
        choices = LIKERT5,
        null = True,
        blank = True,
        ) 
    d5_7 = models.PositiveSmallIntegerField(
        choices = LIKERT5,
        null = True,
        blank = True,
        )
    d5_8 = models.PositiveSmallIntegerField(
        choices = LIKERT5,
        null = True,
        blank = True,
        )
    d6_1 = models.PositiveSmallIntegerField(
        choices = LIKERT5,
        null = True,
        blank = True,
        )
    d6_2 = models.PositiveSmallIntegerField(
        choices = LIKERT5,
        null = True,
        blank = True,
        )
    d6_3 = models.PositiveSmallIntegerField(
        choices = LIKERT5,
        null = True,
        blank = True,
        )
    d6_4 = models.PositiveSmallIntegerField(
        choices = LIKERT5,
        null = True,
        blank = True,
        )
    d6_5 = models.PositiveSmallIntegerField(
        choices = LIKERT5,
        null = True,
        blank = True,
        )
    d6_6 = models.PositiveSmallIntegerField(
        choices = LIKERT5,
        null = True,
        blank = True,
        )
    d6_7 = models.PositiveSmallIntegerField(
        choices = LIKERT5,
        null = True,
        blank = True,
        )
    d6_8 = models.PositiveSmallIntegerField(
        choices = LIKERT5,
        null = True,
        blank = True,
        )   
    h1 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    h2 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    h3 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )


#     ########    ###    ########  #### ########
#          ##    ## ##   ##     ##  ##     ##
#         ##    ##   ##  ##     ##  ##     ##
#        ##    ##     ## ########   ##     ##
#       ##     ######### ##   ##    ##     ##
#      ##      ##     ## ##    ##   ##     ##
#     ######## ##     ## ##     ## ####    ##

class Zarit(Escala):
    class Meta:
        verbose_name = 'ZARIT'
        verbose_name_plural = 'Escalas ZARIT'
    item_01 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_02 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_03 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_04 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_05 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_06 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_07 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_08 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_09 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_10 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_11 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_12 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_13 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_14 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_15 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_16 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_17 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_18 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_19 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_20 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_21 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        )
    item_22 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
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

