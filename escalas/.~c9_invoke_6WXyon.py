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
    rechazo = models.CharField(
        verbose_name='¿rechazo ingreso?',
        max_length=2,
        choices=(
            ('01', 'Riesgo autolítico'),
            ('02', 'Falta de soporte familiar'),
            ('03', 'Falta de voluntariedad'),
            ('04', 'Sin criterio de ingreso agudo'),
            ('99', 'Otros'),
            ),
        blank=True,
        null=True,
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
    dg_previo = models.ForeignKey(
        Diagosti)
    
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
        try:
            return (self.item_01 + self.item_03 + self.item_04 + 
                    self.item_05 + self.item_06 + self.item_08 + 
                    self.item_12 + self.item_14 + self.item_15)
        except:
            return ("incomplete")
    @property
    def autocert(self):
        try:
            return (self.item_02 + self.item_07 +
                    self.item_09 + self.item_10 + self.item_11 +
                    self.item_13)
        except:
            return ("incomplete")
    @property
    def comp(self):
        try:
            return (self.autocert - self.autoref)
        except:
            return ("incomplete")
            
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
        choices=LIKERT6,
        default=0,
        )
    item_02 = models.PositiveSmallIntegerField(
        choices=LIKERT6,
        default=0,
        )
    item_03 = models.PositiveSmallIntegerField(
        choices=LIKERT6,
        default=0,
        )
    item_04 = models.PositiveSmallIntegerField(
        choices=LIKERT6,
        default=0,
        )
    item_05 = models.PositiveSmallIntegerField(
        choices=LIKERT6,
        default=0,
        )
    item_06 = models.PositiveSmallIntegerField(
        choices=LIKERT6,
        default=0,
        )
    item_07 = models.PositiveSmallIntegerField(
        choices=LIKERT6,
        default=0,
        )
    item_08 = models.PositiveSmallIntegerField(
        choices=LIKERT6,
        default=0,
        )
    item_09 = models.PositiveSmallIntegerField(
        choices=LIKERT6,
        default=0,
        )
    item_10 = models.PositiveSmallIntegerField(
        choices=LIKERT6,
        default=0,
        )
    item_11 = models.PositiveSmallIntegerField(
        choices=LIKERT6,
        default=0,
        )
    item_12 = models.PositiveSmallIntegerField(
        choices=LIKERT6,
        default=0,
        )
    item_13 = models.PositiveSmallIntegerField(
        choices=LIKERT6,
        default=0,
        )
    item_14 = models.PositiveSmallIntegerField(
        choices=LIKERT6,
        default=0,
        )
    item_15 = models.PositiveSmallIntegerField(
        choices=LIKERT6,
        default=0,
        )
    item_16 = models.PositiveSmallIntegerField(
        choices=LIKERT6,
        default=0,
        )
    item_17 = models.PositiveSmallIntegerField(
        choices=LIKERT6,
        default=0,
        )
    item_18 = models.PositiveSmallIntegerField(
        choices=LIKERT6,
        default=0,
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
            (4, 'Excelente'),
            (3, 'Buen'),
            (2, 'Regula'),
            (1, 'Mala'),
            ),
        )
    item_02 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=(
            (4, 'No definitivamente'),
            (3, 'En muy pocos casos'),
            (2, 'Si en general'),
            (1, 'Si definitivamente'),
            ),
        )
    item_03 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=(
            (4, 'En casi todos'),
            (3, 'En la mayor parte'),
            (2, 'Solo en algunos'),
            (1, 'En ninguno'),
            ),
        )
    item_04 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=(
            (4, 'No definitivamente'),
            (3, 'No , creo que no'),
            (2, 'Si, creo que si'),
            (1, 'Si definitivamente'),
            ),
        )
    item_05 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=(
            (4, 'Nada satisfecho/a'),
            (3, 'Indiferente o moderadamente no satisfecho/a'),
            (2, 'Moderadamente satisfecho/a'),
            (1, 'Muy satisfecho/a'),
            ),
        )
    item_06 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=(
            (4, 'Si me ayudaron mucho'),
            (3, 'Si me ayudaron algo'),
            (2, 'No realmente no me ayudaron'),
            (1, 'No parecían poner las cosas peor'),
            ),
        )
    item_07 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=(
            (4, 'Muy satisfecho/a'),
            (3, 'Moderadamente satisfecho/a'),
            (2, 'Algo insatisfecho/a'),
            (1, 'Muy Insatisfecho/a'),
            ),
        )
    item_08 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=(
            (4, 'No definitivamente'),
            (3, 'No posiblemente'),
            (2, 'Si, creo que si'),
            (1, 'Si con seguridad'),
            ),
        )
    item_09 = models.TextField(
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
        try:
            return (self.item_01 + self.item_02 + self.item_03 + self.item_04 + 
                    self.item_05 + self.item_06 + self.item_07 + self.item_08 + 
                    self.item_09 + self.item_10 + self.item_11)
        except:
            return ("incomplete")
            
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
        default=0,
        choices=(
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
        default='PSQ',
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
        default=0,
        choices = (
            (0, '0.No evaluado'),
            (1, '1.Mucho mejor'),
            (2, '2.Moderadamente mejor'),
            (3, '3.Levemente mejor'),
            (4, '4.Sin cambios'),
            (5, '5.Levemente peor'),
            (6, '6.Moderadamente peor'),
            (7, '7.Mucho peor'),
            ),
        )
    quien_me = models.CharField(
        max_length=3,
        default='PSQ',
        choices = (
    		('PSQ', 'Psiquiatra'),
    		('PAC', 'Paciente'),
    		),
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
        default=0,
        choices = (
            (0, '0.Ausente'),
            (1, '1.Estas sensaciones se indican solamente al ser preguntado'),
            (2, '2.Estas sensaciones se relatan oral y espontáneamente'),
            (3, '3.Sensaciones no comunicadas verbalmente, es decir, por la expresión facial, la postura, la voz y la tendencia al llanto'),
            (4, '4.El paciente manifiesta estas sensaciones en su comunicación verbal y no verbal de forma espontánea'),
            ),
        )
    item_02 = models.PositiveSmallIntegerField(
        default=0,
        choices = (
            (0, '0.Ausente'),
            (1, '1.Se culpa a si mismos, cree haber decepcionado a la gente'),
            (2, '2.Ideas de culpabilidad, o meditación sobre errores pasados o malas acciones'),
            (3, '3.La enfermedad actual es un castigo. Ideas delirantes de culpabilidad'),
            (4, '4.Oye  voces  acusatorias  o  de  denuncia  y/o  experiemtna  alucinaciones  visuales amenazadoras'),
            ),
        )
    item_03 = models.PositiveSmallIntegerField(
        default=0,
        choices = (
            (0, '0.Ausente'),
            (1, '1.Le parece que la vida no merece la pena ser vivida'),
            (2, '2.Desearía estar muerto o tiene pensamientos sobre la posibilidad de morirse'),
            (3, '3.Ideas de suicidio o amenazas'),
            (4, '4.Intentos de suicidio (cualuqier intento serio se califica 4)'),
            ),
        )
    item_04 = models.PositiveSmallIntegerField(
        default=0,
        choices = (
            (0, '0.Ausente'),
            (1, '1.Dificultades ocasionales para dormirse, por ejemplo, más de media hora'),
            (2, '2.Dificultades para dormirse cada noche'),
            ),
        )
    item_05 = models.PositiveSmallIntegerField(
        default=0,
        choices = (
            (0, '0.Ausente'),
            (1, '1.El paciente s queja de estar inquieto durante la noche'),
            (2, '2.Está despierto durante la noche; medicación, etc.'),
            ),
        )
    item_06 = models.PositiveSmallIntegerField(
        default=0,
        choices = (
            (0, '0.Ausente'),
            (1, '1.Se despierta a primeras horas de la madrugada pero vuelve a dormirse'),
            (2, '2.No puede volver a dormirse si se levanta de la cama'),
            ),
        )
    item_07 = models.PositiveSmallIntegerField(
        default=0,
        choices = (
            (0, '0.Ausente'),
            (1, '1.Ideas  y  sentimientos  de  incapacidad.  Fatiga  o  debilidad  relcionadas  con  su actividad,trabajo o aficiones'),
            (2, '2.Pérdida de interés en su actividad, aficiones, o trabajo, ,anifestado directamete por el enfermo o indirectamente por desatención, indecisión y vacilación'),
            (3, '3.Disminución del tiempo dedicado a actividades o descenso en la productividad'),
            (4, '4.Dejó de trabajar por la presente enfermedad'),
            ),
        )
    item_08 = models.PositiveSmallIntegerField(
        default=0,
        choices = (
            (0, '0.Palabra y pensamiento normales'),
            (1, '1.Ligero retras en el diálogo'),
            (2, '2.Evidente retraso en el diálogo'),
            (3, '3.Diálogo difícil'),
            (4, '4.Torpeza absoluta'),
            ),
        )
    item_09 = models.PositiveSmallIntegerField(
        default=0,
        choices = (
            (0, '0.Ninguna'),
            (1, '1.“Juega” con sus manos, cabellos, etc.'),
            (2, '2.Se retuerce las manos, se muerde las uñas, los labios, se tira de los cabellos, etc.'),
            ),
        )
    item_10 = models.PositiveSmallIntegerField(
        default=0,
        choices = (
            (0, '0.No hay dificultad'),
            (1, '1.Tensión subjetiva e irritable'),
            (2, '2.Preocupación por pequeñas cosas'),
            (3, '3.Actitud aprensiva aparente en la expresión o en el habla'),
            (4, '4.Terrores expresados sin preguntarle'),
            ),
        )
    item_11 = models.PositiveSmallIntegerField(
        default=0,
        choices = (
            (0, '0.Ausente'),
            (1, '1.Ligera'),
            (2, '2.Moderada'),
            (3, '3.Grave'),
            (4, '4.Incapacitante'),
            ),
        )
    item_12 = models.PositiveSmallIntegerField(
        default=0,
        choices = (
            (0, '0.Ninguno'),
            (1, '1.Pérdida de apetito, pero come sin necesidad de que estimulen. Sensación de pesadez en el abdomen'),
            (2, '2.Dificultad en comer si no se le insiste. Solicita o necesita laxantes o medicación intestinal para sus síntomas gastrointestinales'),
            ),
        )
    item_13 = models.PositiveSmallIntegerField(
        default=0,
        choices = (
            (0, '0.Ninguno'),
            (1, '1.Pesadez en las extremidades, espalda o cabeza. Dorsalgias, cefalalgias, algias musculares. Pérdida de energía y fatigabilidad'),
            (2, '2.Cualquier síntoma bien definido'),
            ),
        )
    item_14 = models.PositiveSmallIntegerField(
        default=0,
        choices = (
            (0, '0.Ausente'),
            (1, '1.Débil'),
            (2, '2.Grave'),
            (3, '3.Incapacitante'),
            ),
        )
    item_15 = models.PositiveSmallIntegerField(
        default=0,
        choices = (
            (0, '0.No la hay'),
            (1, '1.Preocupado de sí mismo (corporalmente)'),
            (2, '2.Preocupado por su sald'),
            (3, '3.Se lamenta constantemente, solicita ayudas, etc.'),
            (4, '4.Ideas delirantes hipocondríacas'),
            ),
        )
    item_16 = models.PositiveSmallIntegerField(
        default=0,
        choices = (
            (0, '0.No hay pérdida de peso'),
            (1, '1.Probable pérdida de peso asociada con la enfermedad actual'),
            (2, '2.Pérdida de peso definida (según el enfermo)'),
            ),
        )
    item_17 = models.PositiveSmallIntegerField(
        default=0,
        choices = (
            (0, '0.Se da cuenta de que está deprimido y enfermo'),
            (1, '1.Se da cuenta de sy enfermedad pero atribuye la causa a la mala alimentación, clima, exceso de trabajo, virus, etc.'),
            (2, '2.Niega que esté enfermo'),
            ),
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
        default=0,
        choices = (
            (0, '0. Sin tristeza'),
            (1, '1.'),
            (2, '2. Parece decaído/a pero se anima sin dificultad'),
            (3, '3.'),
            (4, '4. Parece triste y desgraciado/a la mayor parte del tiempo'),
            (5, '5.'),
            (6, '6.Parece siempre desgraciado/a. Extremadamente abatido/a'),
            ),
        )
    item_02 = models.PositiveSmallIntegerField(
        default=0,
        choices = (
            (0, '0. Tristeza esporádica según las circunstancias'),
            (1, '1.'),
            (2, '2. Triste o decaído/a, pero se anima sin dificultad'),
            (3, '3.'),
            (4, '4. Sentimientos generalizados de tristeza o melancolía. El estado de ánimo todavía se ve influido por circunstancias externas'),
            (5, '5.'),
            (6, '6. Abatimiento, desdicha o tristeza continuada o invariable'),
            ),
        )
    item_03 = models.PositiveSmallIntegerField(
        default=0,
        choices = (
            (0, '0. Apacible. Sólo tensión interna pasajera'),
            (1, '1.'),
            (2, '2. Sentimientos ocacionales de nerviosismo y maletar indefinido'),
            (3, '3.'),
            (4, '4. Sentimientos continuados de tensión interna o pánico intermitente que el sujeto sólo puede dominar con alguna dificultad'),
            (5, '5.'),
            (6, '6. Terror o angustia tenaz. Pánico irresistible'),
            ),
        )
    item_04 = models.PositiveSmallIntegerField(
        default=0,
        choices = (
            (0, '0. Duerme como siempre'),
            (1, '1.'),
            (2, '2. Ligera dificultad para dormirse o sueño ligeramente reducido, sueño ligero o perturbado'),
            (3, '3.'),
            (4, '4. Sueño reducido o interrumpido durante al menos 2 h'),
            (5, '5.'),
            (6, '6. Menos de 2 o 3 h de sueño'),
            ),
        )
    item_05 = models.PositiveSmallIntegerField(
        default=0,
        choices = (
            (0, '0. Apetito normal o aumentado'),
            (1, '1.'),
            (2, '2. Apetito ligeramente reducido'),
            (3, '3.'),
            (4, '4. Sin apetito. La comida es insípida'),
            (5, '5.'),
            (6, '6. Necesita persuasión para comer algo'),
            ),
        )
    item_06 = models.PositiveSmallIntegerField(
        default=0,
        choices = (    
            (0, '0. Ninguna dificultad para concentrarse'),
            (1, '1.'),
            (2, '2. Dificultades ocasionales para centrar los pensamientos'),
            (3, '3.'),
            (4, '4. Dificultades para concentrarse y seguir una idea que reduce la capacidad de leer o mantener una conversación'),
            (5, '5.'),
            (6, '6. Incapaz de leer o mantener una conversación si no es con gran dificultad'),
            ),
        )
    item_07 = models.PositiveSmallIntegerField(
        default=0,
        choices = (    
            (0, '0. Casi sin dificultad para empezar algo. Sin apatía'),
            (1, '1.'),
            (2, '2. Dificultades para empezar actividades'),
            (3, '3.'),
            (4, '4. Dificultades para empezar actividades rutinarias sencillas que se llevan a cabo con esfuerzo'),
            (5, '5.'),
            (6, '6. Lasitud total. Incapaz de hacer nada sin ayuda'),
            ),
        )
    item_08 = models.PositiveSmallIntegerField(
        default=0,
        choices = (    
            (0, '0. Interés normal por el entorno y por otras personas'),
            (1, '1.'),
            (2, '2. Menor capacidad para disfrutar de las cosas que normalmen te le interesan'),
            (3, '3.'),
            (4, '4. Pérdida de interés por el entorno. Pérdida de sentimientos respecto a los amigos y conocidos'),
            (5, '5.'),
            (6, '6. La experiencia de estar emocionalmente paralizado, incapacidad para sentir enfado, pena o placer y una total o incluso dolorosa falta de sentimientos hacia los parientes próximos y amigos'),
            ),
        )
    item_09 = models.PositiveSmallIntegerField(
        default=0,
        choices = (
            (0, '0. Sin pensamientos pesimistas'),
            (1, '1.'),
            (2, '2. Ideas variables de fracaso, autorreproche o autodesprecio'),
            (3, '3.'),
            (4, '4. Autoacusaciones persistentes o ideas definidas, pero aún racionales, de culpabilidad o pecado. Cada vez más pesimista respecto al futuro'),
            (5, '5.'),
            (6, '6. Alucinaciones de ruina, remordimiento o pecado irredimible. Autoacusaciones que son absurdas e inquebrantables'),
            ),
        )
    item_10 = models.PositiveSmallIntegerField(
        default=0,
        choices = (
            (0, '0. Disfruta de la vida o la acepta tal como viene'),
            (1, '1.'),
            (2, '2. Cansado de vivir. Sólo pensamientos suicidas pasajeros'),
            (3, '3.'),
            (4, '4. Probablemente  estaría  mejor  muerto/a. Los  pensamientos suicidas son habituales, y se considera el suicidio como una posible solución, pero sin ninguna intención o plan específico'),
            (5, '5.'),
            (6, '6. Planes explícitos de suicidio cuando se presente una oportunidad. Preparativos activos para el suicidio'),
            ),
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
    LIKERT_PANSS = (
    	(1, '1.Ausente'),
    	(2, '2.Mínimo'),
    	(3, '3.Ligero'),
    	(4, '4.Moderado'),
        (5, '5.Moderado severo'),
        (6, '6.Severo'),
        (7, '7.Extremo'),
        )
    class Meta:
        verbose_name = 'PANSS'
        verbose_name_plural = 'Escalas PANSS'
    item_p01 = models.PositiveSmallIntegerField(
        default=1,
        choices=LIKERT_PANSS,
        )
    item_p02 = models.PositiveSmallIntegerField(
        default=1,
        choices=LIKERT_PANSS,
        )
    item_p03 = models.PositiveSmallIntegerField(
        default=1,
        choices=LIKERT_PANSS,
        )
    item_p04 = models.PositiveSmallIntegerField(
        default=1,
        choices=LIKERT_PANSS,
        )
    item_p05 = models.PositiveSmallIntegerField(
        default=1,
        choices=LIKERT_PANSS,
        )
    item_p06 = models.PositiveSmallIntegerField(
        default=1,
        choices=LIKERT_PANSS,
        )
    item_p07 = models.PositiveSmallIntegerField(
        default=1,
        choices=LIKERT_PANSS,
        )
    @property
    def panss_sp(self):
        return (self.item_p01 + self.item_p02 + self.item_p03 + self.item_p04 + 
                self.item_p05 + self.item_p06 + self.item_p07)
    
    item_n01 = models.PositiveSmallIntegerField(
        default=1,
        choices=LIKERT_PANSS,
        )
    item_n02 = models.PositiveSmallIntegerField(
        default=1,
        choices=LIKERT_PANSS,
        )
    item_n03 = models.PositiveSmallIntegerField(
        default=1,
        choices=LIKERT_PANSS,
        )
    item_n04 = models.PositiveSmallIntegerField(
        default=1,
        choices=LIKERT_PANSS,
        )
    item_n05 = models.PositiveSmallIntegerField(
        default=1,
        choices=LIKERT_PANSS,
        )
    item_n06 = models.PositiveSmallIntegerField(
        default=1,
        choices=LIKERT_PANSS,
        )
    item_n07 = models.PositiveSmallIntegerField(
        default=1,
        choices=LIKERT_PANSS,
        )
    @property
    def panss_sn(self):
        return (self.item_n01 + self.item_n02 + self.item_n03 + self.item_n04 + 
                self.item_n05 + self.item_n06 + self.item_n07)

    item_g01 = models.PositiveSmallIntegerField(
        default=1,
        choices=LIKERT_PANSS,
        )
    item_g02 = models.PositiveSmallIntegerField(
        default=1,
        choices=LIKERT_PANSS,
        )
    item_g03 = models.PositiveSmallIntegerField(
        default=1,
        choices=LIKERT_PANSS,
        )
    item_g04 = models.PositiveSmallIntegerField(
        default=1,
        choices=LIKERT_PANSS,
        )
    item_g05 = models.PositiveSmallIntegerField(
        default=1,
        choices=LIKERT_PANSS,
        )
    item_g06 = models.PositiveSmallIntegerField(
        default=1,
        choices=LIKERT_PANSS,
        )
    item_g07 = models.PositiveSmallIntegerField(
        default=1,
        choices=LIKERT_PANSS,
        )
    item_g08 = models.PositiveSmallIntegerField(
        default=1,
        choices=LIKERT_PANSS,
        )
    item_g09 = models.PositiveSmallIntegerField(
        default=1,
        choices=LIKERT_PANSS,
        )
    item_g10 = models.PositiveSmallIntegerField(
        default=1,
        choices=LIKERT_PANSS,
        )
    item_g11 = models.PositiveSmallIntegerField(
        default=1,
        choices=LIKERT_PANSS,
        )
    item_g12 = models.PositiveSmallIntegerField(
        default=1,
        choices=LIKERT_PANSS,
        )
    item_g13 = models.PositiveSmallIntegerField(
        default=1,
        choices=LIKERT_PANSS,
        )
    item_g14 = models.PositiveSmallIntegerField(
        default=1,
        choices=LIKERT_PANSS,
        )
    item_g15 = models.PositiveSmallIntegerField(
        default=1,
        choices=LIKERT_PANSS,
        )
    item_g16 = models.PositiveSmallIntegerField(
        default=1,
        choices=LIKERT_PANSS,
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


#
#     ######     ###    ######## ####  ######
#    ##    ##   ## ##      ##     ##  ##    ##
#    ##        ##   ##     ##     ##  ##
#     ######  ##     ##    ##     ##   ######
#          ## #########    ##     ##        ##
#    ##    ## ##     ##    ##     ##  ##    ##
#     ######  ##     ##    ##    ####  ######
#

class Satis(models.Model):
    LIKERT_SATIS = (
    	(1, '1.Muy Poca'),
    	(2, '2.Poca'),
    	(3, '3.Normal'),
    	(4, '4.Bastante'),
        (5, '5.Mucha'),
        )
    class Meta:
        verbose_name = 'Satisfaccion'
        verbose_name_plural = 'Escalas Satisfaccion'
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
        choices=LIKERT_SATIS,
        )
    item_02 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=LIKERT_SATIS,
        )
    item_03 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=LIKERT_SATIS,
        )
    item_04 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=LIKERT_SATIS,
        )
    item_05 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=LIKERT_SATIS,
        )
    item_06 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=LIKERT_SATIS,
        )
    item_07 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=LIKERT_SATIS,
        )
    item_08 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=LIKERT_SATIS,
        )
    item_09 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=LIKERT_SATIS,
        )
    item_10 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices=(
    	    (1, '1.Siempre ingresaria en hosp'),
    	    (2, '2.Casi siempre hosp '),
    	    (3, '3.Me daría igual'),
    	    (4, '4.Casi siempre dom'),
            (5, '5.Siempre dom'),
            ),
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
        default=0,
        choices = (
            (0, '0.Ausente'),
            (1, '1.Posible o moderada, sólo cuando se le pregunta'),
            (2, '2.Clara aunque subjetiva y apropiada al contenido: optimista, seguro de sí mismo/a, alegre'),
            (3, '3.Elevada e inapropiada'),
            (4, '4.Claramente eufórico/a, risa inadecuada, canta durante la entrevista, etc.'),
            ),
        )
    item_02 = models.PositiveSmallIntegerField(
        default=0,
        choices = (
            (0, '0.Ausente'),
            (1, '1.Subjetivamente aumentada'),
            (2, '2.Vigoroso/a, hipergestual'),
            (3, '3.Energía excesiva, hiperactividad fluctuante, inquietud (puede ser calmado/a)'),
            (4, '4.Agitación o hiperactividad constante (no puede ser calmado/a)'),
            ),
        )
    item_03 = models.PositiveSmallIntegerField(
        default=0,
        choices = (
            (0, '0.Normal, no aumentado'),
            (1, '1.Posible o moderadamente aumentado'),
            (2, '2.Claro aumento al preguntar'),
            (3, '3.Referido como elevado de forma espontánea, contenido sexual del discurso, preocupación por temas sexuales'),
            (4, '4.Actos o incitaciones sexuales evidentes (hacia pacientes, personal o entrevistador)'),
            ),
        )
    item_04 = models.PositiveSmallIntegerField(
        default=0,
        choices = (
            (0, '0.No reducido'),
            (1, '1.Disminución en menos de 1 ,hora'),
            (2, '2.Disminución en más de 1 hora'),
            (3, '3.Refiere disminución de la necesidad de dormir'),
            (4, '4.Niega necesidad de dormir'),
            ),
        )
    item_05 = models.PositiveSmallIntegerField(
        default=0,
        choices = (
            (0, '0.Ausente'),
            (1, '1.'),
            (2, '2.Subjetivamente aumentada'),
            (3, '3.'),
            (4, '4.Irritabilidad fluctuante durante la entrevista, episodios recientes de rabia o enfado'),
            (5, '5.'),
            (6, '6.Predominantemente irritable durante la entrevista, brusco y cortante'),
            (7, '7.'),
            (8, '8.Hostil, no colaborador/a, entrevista imposible'),
            ),
        )
    item_06 = models.PositiveSmallIntegerField(
        default=0,
        choices = (
            (0, '0.No aumentada'),
            (1, '1.'),
            (2, '2.Sensación de locuacidad'),
            (3, '3.'),
            (4, '4.Aumentada de forma fluctuante, verborrea ocasional'),
            (5, '5.'),
            (6, '6.Claramente aumentada en ritmo y cantidad, difícil de interrumpir, intrusiva'),
            (7, '7.'),
            (8, '8.Verborrea ininterrumpible y continua'),
            ),
        )
    item_07 = models.PositiveSmallIntegerField(
        default=0,
        choices = (
            (0, '0.Ausentes'),
            (1, '1.Circunstancialidad, distraibilidad moderada, aceleración del pensamiento'),
            (2, '2.Distraibilidad clara, descarrilamiento, taquipsiquia'),
            (3, '3.Fuga de ideas, tangencialidad, discurso difícil de seguir, rimas, ecolalia'),
            (4, '4.Incoherencia, ininteligibilidad, comunicación imposible'),
            ),
        )
    item_08 = models.PositiveSmallIntegerField(
        default=0,
        choices = (
            (0, '0.Ausentes'),
            (1, '1.'),
            (2, '2.Planes discutibles, nuevos intereses'),
            (3, '3.'),
            (4, '4.Proyectos especiales, misticismo'),
            (5, '5.'),
            (6, '6.Ideas grandiosas o paranoides, ideas de referencia'),
            (7, '7.'),
            (8, '8.Delirios, alucinaciones'),
            ),
        )
    item_09 = models.PositiveSmallIntegerField(
        default=0,
        choices = (
            (0, '0.Ausente, colaborador/a'),
            (1, '1.'),
            (2, '2.Sarcástico/a, enfático/a, lacónico/a'),
            (3, '3.'),
            (4, '4.Querulante, pone en guardia'),
            (5, '5.'),
            (6, '6.Amenaza al entrevistador, habla a gritos, entrevista difícil'),
            (7, '7.'),
            (8, '8.Claramente agresivo/a, destructivo/a, entrevista imposible'),
            ),
        )
    item_10 = models.PositiveSmallIntegerField(
        default=0,
        choices = (
            (0, '0.Higiene e indumentaria apropiada '),
            (1, '1.Ligeramente descuidada'),
            (2, '2.Mal arreglado/a, moderadamente despeinado/a, indumentaria sobrecargada'),
            (3, '3.Despeinado/a, semidesnudo/a, maquillaje llamativo'),
            (4, '4.Completamente desaseado/a, adornado/a, indumentaria extravagante'),
            ),
        )
    item_11 = models.PositiveSmallIntegerField(
        default=0,
        choices = (
            (0, '0.Presente, admite la enfermedad, acepta tratamiento'),
            (1, '1.Según él/ella, posiblemente enfermo/a'),
            (2, '2.Admite cambio de conducta, pero niega enfermedad'),
            (3, '3.Admite posible cambio de conducta, niega enfermedad'),
            (4, '4.Niega cualquier cambio de conduct'),
            ),
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
    LIKERT_ZARIT= (
        (0, '0. Nunca'),
        (1, '1. Casi nunca'),
        (2, '2. A veces'),
        (3, '3. Bastantes veces'),
        (4, '4. Siempre'),
        )
    class Meta:
        verbose_name = 'ZARIT'
        verbose_name_plural = 'Escalas ZARIT'
    item_01 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices = LIKERT_ZARIT,
        )
    item_02 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices = LIKERT_ZARIT,
        )
    item_03 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices = LIKERT_ZARIT,
        )
    item_04 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices = LIKERT_ZARIT,
        )
    item_05 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices = LIKERT_ZARIT,
        )
    item_06 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices = LIKERT_ZARIT,
        )
    item_07 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices = LIKERT_ZARIT,
        )
    item_08 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices = LIKERT_ZARIT,
        )
    item_09 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices = LIKERT_ZARIT,
        )
    item_10 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices = LIKERT_ZARIT,
        )
    item_11 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices = LIKERT_ZARIT,
        )
    item_12 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices = LIKERT_ZARIT,
        )
    item_13 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices = LIKERT_ZARIT,
        )
    item_14 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices = LIKERT_ZARIT,
        )
    item_15 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices = LIKERT_ZARIT,
        )
    item_16 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices = LIKERT_ZARIT,
        )
    item_17 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices = LIKERT_ZARIT,
        )
    item_18 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices = LIKERT_ZARIT,
        )
    item_19 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices = LIKERT_ZARIT,
        )
    item_20 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices = LIKERT_ZARIT,
        )
    item_21 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices = LIKERT_ZARIT,
        )
    item_22 = models.PositiveSmallIntegerField(
        null = True,
        blank = True,
        choices = LIKERT_ZARIT,
        )
    @property
    def total(self):
        try:
            return (self.item_01 + self.item_02 + self.item_03 + self.item_04 + 
                    self.item_05 + self.item_06 + self.item_07 + self.item_08 + 
                    self.item_09 + self.item_10 + self.item_11 + self.item_12 + 
                    self.item_13 + self.item_14 + self.item_15 + self.item_16 + 
                    self.item_17 + self.item_18 + self.item_19 + self.item_20 +
                    self.item_21 + self.item_22)
        except:
            return ("incomplete")
            
    def __str__(self):
        return "%s: ZARIT=%s" % (self.fecha, str(self.total))

