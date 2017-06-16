#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from escalas.models import *

CHOICES = (
    (0, 'No'),
    (1, 'Si'),
    )


    
VARFORM = forms.Select


#     ########   ######  ####  ######
#     ##     ## ##    ##  ##  ##    ##
#     ##     ## ##        ##  ##
#     ########  ##        ##   ######
#     ##     ## ##        ##        ##
#     ##     ## ##    ##  ##  ##    ##
#     ########   ######  ####  ######

class BcisAdminForm(forms.ModelForm):
    L_BCIS = (
        (0, '0.Nada de acuerdo'),
        (1, '1.Un poco de acuerdo'),
        (2, '2.Bastante de acuerdo'),
        (3, '3.Totalmente de acuerdo'),
        )
    class Meta:
        model = Bcis
        fields = '__all__'
    item_01 = forms.ChoiceField(
        choices=L_BCIS, 
        label = '1. Algunas veces he malinterpretado las actitudes que los demás tienen hacia mí',
        widget = VARFORM,
        )
    item_02 = forms.ChoiceField(
        choices=L_BCIS, 
        label = '2. Las interpretaciones que hago de mis experiencias son sin duda correctas',
        widget = VARFORM,
        )
    item_03 = forms.ChoiceField(
        choices=L_BCIS, 
        label = '3. Otras personas pueden entender mejor que yo la causa de mis experiencias raras',
        widget = VARFORM,
        )
    item_04 = forms.ChoiceField(
        choices=L_BCIS, 
        label = '4. Llego a conclusiones demasiado rápido',
        widget = VARFORM,
        )
    item_05 = forms.ChoiceField(
        choices=L_BCIS, 
        label = '5. Algunas de mis experiencias que me han parecido muy reales pueden haberse debido a mi imaginación',
        widget = VARFORM,
        )
    item_06 = forms.ChoiceField(
        choices=L_BCIS, 
        label = '6. Algunas de las ideas que tenía como ciertas acabaron siendo falsas',
        widget = VARFORM,
        )
    item_07 = forms.ChoiceField(
        choices=L_BCIS, 
        label = '7. Si siento que algo es correcto significa que es correcto',
        widget = VARFORM,
        )
    item_08 = forms.ChoiceField(
        choices=L_BCIS, 
        label = '8. Aunque me siento muy seguro/a de estar en lo cierto, podría estar equivocado/a',
        widget = VARFORM,
        )
    item_09 = forms.ChoiceField(
        choices=L_BCIS, 
        label = '9. Conozco mejor que nadie cuáles son mis problemas',
        widget = VARFORM,
        )
    item_10 = forms.ChoiceField(
        choices=L_BCIS, 
        label = '10. Cuando los demás no está de acuerdo conmigo, normalmente están equivocados',
        widget = VARFORM,
        )
    item_11 = forms.ChoiceField(
        choices=L_BCIS, 
        label = '11. No puedo fiarme de lo que opinan los demás sobre mis experiencias',
        widget = VARFORM,
        )
    item_12 = forms.ChoiceField(
        choices=L_BCIS, 
        label = '12. Si alguien comenta que mis creencias son erróneas estoy dispuesto/a a considerar su opinión',
        widget = VARFORM,
        )
    item_13 = forms.ChoiceField(
        choices=L_BCIS, 
        label = '13. Puedo confiar en mi propio juicio siempre',
        widget = VARFORM,
        )
    item_14 = forms.ChoiceField(
        choices=L_BCIS, 
        label = '14. Suele haber más de una explicación posible sobre por qué la gente actúa de la manera en que lo hace',
        widget = VARFORM,
        )
    item_15 = forms.ChoiceField(
        choices=L_BCIS, 
        label = '15. Mis experiencias raras pueden deberse a que esté muy alterado/a o estresado/a',
        widget = VARFORM,
        )



#     ########  ########  ########   ######
#     ##     ## ##     ## ##     ## ##    ##
#     ##     ## ##     ## ##     ## ##
#     ########  ########  ########   ######
#     ##     ## ##        ##   ##         ##
#     ##     ## ##        ##    ##  ##    ##
#     ########  ##        ##     ##  ######
#
class BprsAdminForm(forms.ModelForm):
    LIKERT6 = (
        (6, '6.Muy Grave'),
        (5, '5.Grave'),
        (4, '4.Bastante acentuado'),
        (3, '3.Moderado'),
        (2, '2.Leve'),
        (1, '1.Muy leve'),
        (0, '0.Ausente'),
        )
    class Meta:
        model = Bprs
        fields = '__all__'
    item_01 = forms.ChoiceField(
        choices=LIKERT6,
        label='1.- Preocupación somática',
        widget = VARFORM,
        )
    item_02 = forms.ChoiceField(
        choices=LIKERT6,
        label='2.- Ansiedad psíquica',
        widget = VARFORM,
        )   
    item_03 = forms.ChoiceField(
        choices=LIKERT6,
        label='3.- Aislamiento emocional',
        widget = VARFORM,
        )
    item_04 = forms.ChoiceField(
        choices=LIKERT6,
        label='4.- Desorganización conceptual (incoherencia)',
        widget = VARFORM,
        )
    item_05 = forms.ChoiceField(
        choices=LIKERT6,
        label='5.- Autodesprecio y sentimientos de culpa',
        widget = VARFORM,
        )
    item_06 = forms.ChoiceField(
        choices=LIKERT6,
        label='6.- Tensión. Ansiedad somática',
        widget = VARFORM,
        )   
    item_07 = forms.ChoiceField(
        choices=LIKERT6,
        label='7.- Manierismo y postura extraña',
        widget = VARFORM,
        )
    item_08 = forms.ChoiceField(
        choices=LIKERT6,
        label='8.- Grandeza',
        widget = VARFORM,
        )
    item_09 = forms.ChoiceField(
        choices=LIKERT6,
        label='9.- Humor depresivo',
        widget = VARFORM,
        )
    item_10 = forms.ChoiceField(
        choices=LIKERT6,
        label='10.- Hostilidad',
        widget = VARFORM,
        )
    item_11 = forms.ChoiceField(
        choices=LIKERT6,
        label='11.- Suspicacia',
        widget = VARFORM,
        )
    item_12 = forms.ChoiceField(
        choices=LIKERT6,
        label='12.- Alucinaciones',
        widget = VARFORM,
        )   
    item_13 = forms.ChoiceField(
        choices=LIKERT6,
        label='13.- Enlentecimiento motor',
        widget = VARFORM,
        )
    item_14 = forms.ChoiceField(
        choices=LIKERT6,
        label='14.- Falta de cooperación',
        widget = VARFORM,
        )   
    item_15 = forms.ChoiceField(
        choices=LIKERT6,
        label='15.- Contenido insusual del pensamiento',
        widget = VARFORM,
        )
    item_16 = forms.ChoiceField(
        choices=LIKERT6,
        label='16.- Embotamiento, aplanamiento afectivo',
        widget = VARFORM,
        )   
    item_17 = forms.ChoiceField(
        choices=LIKERT6,
        label='17.- Exitación',
        widget = VARFORM,
        )
    item_18 = forms.ChoiceField(
        choices=LIKERT6,
        label='18.- Desorientación y confusión',
        widget = VARFORM,
        )


        
#     ########  ##     ## ##    ## ########
#     ##     ## ##     ## ##   ##  ##
#     ##     ## ##     ## ##  ##   ##
#     ##     ## ##     ## #####    ######
#     ##     ## ##     ## ##  ##   ##
#     ##     ## ##     ## ##   ##  ##
#     ########   #######  ##    ## ########


class DukeAdminForm(forms.ModelForm):
    LIKERT_DUKE = (
        (5, '5. Tanto como deseo'),
        (4, '4. Casi como deseo'),
        (3, '3. Ni mucho ni poco'),
        (2, '2. Menos de lo que deseo'),
        (1, '1. Mucho menos de lo que deseo'),
        )
    class Meta:
        model = Duke
        fields = '__all__'
    item_01 = forms.ChoiceField(
        choices=LIKERT_DUKE,
        label='1.- Recibo visitas de mis amigos y familiares',
        widget = VARFORM,
        )
    item_02 = forms.ChoiceField(
        choices=LIKERT_DUKE,
        label='2.- Recibo ayuda en asuntos relacionados con mi casa',
        widget = VARFORM,
        )   
    item_03 = forms.ChoiceField(
        choices=LIKERT_DUKE,
        label='3.- Recibo elogios y reconocimientos cuando hago bien mi trabajo',
        widget = VARFORM,
        )
    item_04 = forms.ChoiceField(
        choices=LIKERT_DUKE,
        label='4.- Cuento con personas que se preocupan de lo que me sucede',
        widget = VARFORM,
        )
    item_05 = forms.ChoiceField(
        choices=LIKERT_DUKE,
        label='5.- Recibo amor y afecto',
        widget = VARFORM,
        )
    item_06 = forms.ChoiceField(
        choices=LIKERT_DUKE,
        label='6.- Tengo posibilidad de hablar con alguien de mis problemas de trabajo o en la casa',
        widget = VARFORM,
        )   
    item_07 = forms.ChoiceField(
        choices=LIKERT_DUKE,
        label='7.- Tengo la posibilidad de hablar con alguien de mis problemas personales y familiares',
        widget = VARFORM,
        )
    item_08 = forms.ChoiceField(
        choices=LIKERT_DUKE,
        label='8.- Tengo la posibilidad de hablar con alguien de mis problemas económicos',
        widget = VARFORM,
        )
    item_09 = forms.ChoiceField(
        choices=LIKERT_DUKE,
        label='9.- Recibo invitaciones para distraerme y salir con otras personas',
        widget = VARFORM,
        )
    item_10 = forms.ChoiceField(
        choices=LIKERT_DUKE,
        label='10.- Recibo consejos útiles cuando me ocurre algún acontecimiento importante en mi vida',
        widget = VARFORM,
        )
    item_11 = forms.ChoiceField(
        choices=LIKERT_DUKE,
        label='11.- Recibo ayuda cuando estoy enfermo en la cama',
        widget = VARFORM,
        )



#
#        ####     ####   ######
#       ##  ##   ##  ##    ##
#      ##       ##         ##
#      ##       ##         ##
#      ##       ##  ###    ##
#       ##  ##   ##  ##    ##
#        ####     #####  ######
#
#
class CgiAdminForm(forms.ModelForm):
    class Meta:
        model = Cgi
        fields = '__all__'
    cgi_a = forms.ChoiceField(
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
        label = 'ICG Gravedad',
        widget = VARFORM,
    )
    cgi_b = forms.ChoiceField(
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
        label = 'ICG Mejoría Global',
        widget = VARFORM,
    )
    
    
    
# CSQ-8
class Csq8AdminForm(forms.ModelForm):
    class Meta:
        model = Csq8
        fields = '__all__'
        
    autor = forms.ChoiceField(
        widget=forms.RadioSelect,
        )
    item_01 = forms.ChoiceField(
        label='1.-¿Cómo evaluaría la calidad de los servicios que ha recibido',
        choices=(
            ('4', 'Excelent'),
            ('3', 'Buen'),
            ('2', 'Regula'),
            ('1', 'Mala'),
            ),
        widget=VARFORM,
        )
    item_02 = forms.ChoiceField(
        label='2.-¿Recibió la clase de servicio que usted requería?',
        choices=(
            ('4', 'No definitivamente'),
            ('3', 'En muy pocos casos'),
            ('2', 'Si en general'),
            ('1', 'Si definitivamente'),
            ),
        widget=VARFORM,
        )
    item_03 = forms.ChoiceField(
        label='3.-¿Hasta que punto ha ayudado nuestro programa a solucionar sus problemas?',
        choices=(
            ('4', 'En casi todos'),
            ('3', 'En la mayor parte'),
            ('2', 'Solo en algunos'),
            ('1', 'En ninguno'),
            ),
        widget=VARFORM,
        )
    item_04 = forms.ChoiceField(
        label='4.-¿Si un/a amigo/a estuviera en necesidad de ayuda similar, le recomendaría nuestro programa?',
        choices=(
            ('4', 'No definitivamente'),
            ('3', 'No , creo que no'),
            ('2', 'Si, creo que si'),
            ('1', 'Si definitivamente'),
            ),
        widget=VARFORM,
        )
    item_05 = forms.ChoiceField(
        label='5.-¿Cómo de satisfecho/a esta usted con la cantidad de ayuda que ha recibido?',
        choices=(
            ('4', 'Nada satisfecho/a'),
            ('3', 'Indiferente o moderadamente no satisfecho/a'),
            ('2', 'Moderadamente satisfecho/a'),
            ('1', 'Muy satisfecho/a'),
            ),
        widget=VARFORM,
        )
    item_06 = forms.ChoiceField(
        label='6.-¿Los servicios que ha recibido le han ayudado a enfrentarse mejor a sus problemas?',
        choices=(
            ('4', 'Si me ayudaron mucho'),
            ('3', 'Si me ayudaron algo'),
            ('2', 'No realmente no me ayudaron'),
            ('1', 'No parecían poner las cosas peor'),
            ),
        widget=VARFORM,
        )
    item_07 = forms.ChoiceField(
        label='7.- ¿En general, cómo de satisfecho/a está usted con los servicios que ha recibido?',
        choices=(
            ('4', 'Muy satisfecho/a'),
            ('3', 'Moderadamente satisfecho/a'),
            ('2', 'Algo insatisfecho/a'),
            ('1', 'Muy Insatisfecho/a'),
            ),
        widget=VARFORM,
        )
    item_08 = forms.ChoiceField(
        label='8.-¿Si necesitara ayuda otra vez volvería a nuestro programa?',
        choices=(
            ('4', 'No definitivamente'),
            ('3', 'No posiblemente'),
            ('2', 'Si, creo que si'),
            ('1', 'Si con seguridad'),
            ),
        widget=VARFORM,
        )
    item_09 = forms.CharField(
        label='9.-Lo que más me ha gustado de la atención que he recibido ha sido:',
        )
    item_10 = forms.CharField(
        label='10.-Creo que se tendría que mejorar:'
        )



#     ##     ## ########  ########   ######
#     ##     ## ##     ## ##     ## ##    ##
#     ##     ## ##     ## ##     ## ##
#     ######### ##     ## ########   ######
#     ##     ## ##     ## ##   ##         ##
#     ##     ## ##     ## ##    ##  ##    ##
#     ##     ## ########  ##     ##  ######
#
class HdrsAdminForm(forms.ModelForm):
    class Meta:
        model = Hdrs
        fields = '__all__'
    item_01 = forms.ChoiceField(
        label = '1.- Humor deprimido',
        choices = (
            (0, '0.Ausente'),
            (1, '1.Estas sensaciones se indican solamente al ser preguntado'),
            (2, '2.Estas sensaciones se relatan oral y espontáneamente'),
            (3, '3.Sensaciones no comunicadas verbalmente, es decir, por la expresión facial, la postura, la voz y la tendencia al llanto'),
            (4, '4.El paciente manifiesta estas sensaciones en su comunicación verbal y no verbal de forma espontánea'),
            ),
        widget = VARFORM,
        )
    item_02 = forms.ChoiceField(
        label = '2.- Sensación de culpabilidad',
        choices = (
            (0, '0.Ausente'),
            (1, '1.Se culpa a si mismos, cree haber decepcionado a la gente'),
            (2, '2.Ideas de culpabilidad, o meditación sobre errores pasados o malas acciones'),
            (3, '3.La enfermedad actual es un castigo. Ideas delirantes de culpabilidad'),
            (4, '4.Oye  voces  acusatorias  o  de  denuncia  y/o  experiemtna  alucinaciones  visuales amenazadoras'),
            ),
        widget = VARFORM,
        )
    item_03 = forms.ChoiceField(
        label = '3.- Suicidio',
        choices = (
            (0, '0.Ausente'),
            (1, '1.Le parece que la vida no merece la pena ser vivida'),
            (2, '2.Desearía estar muerto o tiene pensamientos sobre la posibilidad de morirse'),
            (3, '3.Ideas de suicidio o amenazas'),
            (4, '4.Intentos de suicidio (cualuqier intento serio se califica 4)'),
            ),
        widget = VARFORM,
        )
    item_04 = forms.ChoiceField(
        label = '4.- Insomnio precoz',
        choices = (
            (0, '0.Ausente'),
            (1, '1.Dificultades ocasionales para dormirse, por ejemplo, más de media hora'),
            (2, '2.Dificultades para dormirse cada noche'),
            ),
        widget = VARFORM,
        )
    item_05 = forms.ChoiceField(
        label = '5.- Insomnio medio',
        choices = (
            (0, '0.Ausente'),
            (1, '1.El paciente s queja de estar inquieto durante la noche'),
            (2, '2.Está despierto durante la noche; medicación, etc.'),
            ),
        widget = VARFORM,
        )
    item_06 = forms.ChoiceField(
        label = '6.- Insomnio tardío',
        choices = (
            (0, '0.Ausente'),
            (1, '1.Se despierta a primeras horas de la madrugada pero vuelve a dormirse'),
            (2, '2.No puede volver a dormirse si se levanta de la cama'),
            ),
        widget = VARFORM,
        )
    item_07 = forms.ChoiceField(
        label = '7.- Trabajo y actividades',
        choices = (
            (0, '0.Ausente'),
            (1, '1.Ideas  y  sentimientos  de  incapacidad.  Fatiga  o  debilidad  relcionadas  con  su actividad,trabajo o aficiones'),
            (2, '2.Pérdida de interés en su actividad, aficiones, o trabajo, ,anifestado directamete por el enfermo o indirectamente por desatención, indecisión y vacilación'),
            (3, '3.Disminución del tiempo dedicado a actividades o descenso en la productividad'),
            (4, '4.Dejó de trabajar por la presente enfermedad'),
            ),
        widget = VARFORM,
        )
    item_08 = forms.ChoiceField(
        label = '8.- Inhibición',
        choices = (
            (0, '0.Palabra y pensamiento normales'),
            (1, '1.Ligero retras en el diálogo'),
            (2, '2.Evidente retraso en el diálogo'),
            (3, '3.Diálogo difícil'),
            (4, '4.Torpeza absoluta'),
            ),
        widget = VARFORM,
        )
    item_09 = forms.ChoiceField(
        label = '9.- Agitación',
        choices = (
            (0, '0.Ninguna'),
            (1, '1.“Juega” con sus manos, cabellos, etc.'),
            (2, '2.Se retuerce las manos, se muerde las uñas, los labios, se tira de los cabellos, etc.'),
            ),
        widget = VARFORM,
        )
    item_10 = forms.ChoiceField(
        label = '10.- Ansiedad psíquica',
        choices = (
            (0, '0.No hay dificultad'),
            (1, '1.Tensión subjetiva e irritable'),
            (2, '2.Preocupación por pequeñas cosas'),
            (3, '3.Actitud aprensiva aparente en la expresión o en el habla'),
            (4, '4.Terrores expresados sin preguntarle'),
            ),
        widget = VARFORM,
        )
    item_11 = forms.ChoiceField(
        label = '11.- Ansiedad somática',
        choices = (
            (0, '0.Ausente'),
            (1, '1.Ligera'),
            (2, '2.Moderada'),
            (3, '3.Grave'),
            (4, '4.Incapacitante'),
            ),
        widget = VARFORM,
        )
    item_12 = forms.ChoiceField(
        label = '12.- Síntomas somáticos gastrointestinales',
        choices = (
            (0, '0.Ninguno'),
            (1, '1.Pérdida de apetito, pero come sin necesidad de que estimulen. Sensación de pesadez en el abdomen'),
            (2, '2.Difucultad en comer si no se le insiste. Solicita o necesita laxantes o medicación intestinal para sus síntomas gastrointestinales'),
            ),
        widget = VARFORM,
        )
    item_13 = forms.ChoiceField(
        label = '13.- Síntomas somáticos generales',
        choices = (
            (0, '0.Ninguno'),
            (1, '1.Pesadez en las extremidades, espalda o cabeza. Dorsalgias, cefalalgias, algias musculares. Pérdida de energía y fatigabilidad'),
            (2, '2.Cualquier síntoma bien definido'),
            ),
        widget = VARFORM,
        )
    item_14 = forms.ChoiceField(
        label = '14.- Síntomas genitales',
        choices = (
            (0, '0.Ausente'),
            (1, '1.Débil'),
            (2, '2.Grave'),
            (3, '3.Incapacitante'),
            ),
        widget = VARFORM,
        )
    item_15 = forms.ChoiceField(
        label = '15.- Hipocondría',
        choices = (
            (0, '0.No la hay'),
            (1, '1.Preocupado de sí mismo (corporalmente)'),
            (2, '2.Preocupado por su sald'),
            (3, '3.Se lamenta constantemente, solicita ayudas, etc.'),
            (4, '4.Ideas delirantes hipocondríacas'),
            ),
        widget = VARFORM,
        )

    item_16 = forms.ChoiceField(
        label = '16.- Pérdida de peso',
        choices = (
            (0, '0.No hay pérdida de peso'),
            (1, '1.Probable pérdida de peso asociada con la enfermedad actual'),
            (2, '2.Pérdida de peso definida (según el enfermo)'),
            ),
        widget = VARFORM,
        )

    item_17 = forms.ChoiceField(
        label = '17.- Insight (conciencia de enfermedad)',
        choices = (
            (0, '0.Se da cuenta de que está deprimido y enfermo'),
            (1, '1.Se da cuenta de sy enfermedad pero atribuye la causa a la mala alimentación, clima, exceso de trabajo, virus, etc.'),
            (2, '2.Niega que esté enfermo'),
            ),
        widget = VARFORM,
        )


#     ##     ##    ###    ########  ########   ######
#     ###   ###   ## ##   ##     ## ##     ## ##    ##
#     #### ####  ##   ##  ##     ## ##     ## ##
#     ## ### ## ##     ## ##     ## ########   ######
#     ##     ## ######### ##     ## ##   ##         ##
#     ##     ## ##     ## ##     ## ##    ##  ##    ##
#     ##     ## ##     ## ########  ##     ##  ######


class MadrsAdminForm(forms.ModelForm):
    class Meta:
        model = Madrs
        fields = '__all__'
    item_01 = forms.ChoiceField(
        label = '1.- Tristeza observada',
        choices = (
            (0, '0. Sin tristeza'),
            (1, '1.'),
            (2, '2. Parece decaído/a pero se anima sin dificultad'),
            (3, '3.'),
            (4, '4. Parece triste y desgraciado/a la mayor parte del tiempo'),
            (5, '5.'),
            (6, '6.Parece siempre desgraciado/a. Extremadamente abatido/a'),
            ),
        widget = VARFORM,
        )
    item_02 = forms.ChoiceField(
        label = '2.- Tristeza declarada por el paciente',
        choices = (
            (0, '0. Tristeza esporádica según las circunstancias'),
            (1, '1.'),
            (2, '2. Triste o decaído/a, pero se anima sin dificultad'),
            (3, '3.'),
            (4, '4. Sentimientos generalizados de tristeza o melancolía. El estado de ánimo todavía se ve influido por circunstancias externas'),
            (5, '5.'),
            (6, '6. Abatimiento, desdicha o tristeza continuada o invariable'),
            ),
        widget = VARFORM,
        )
    item_03 = forms.ChoiceField(
        label = '3.- Tensión interna',
        choices = (
            (0, '0. Apacible. Sólo tensión interna pasajera'),
            (1, '1.'),
            (2, '2. Sentimientos ocacionales de nerviosismo y maletar indefinido'),
            (3, '3.'),
            (4, '4. Sentimientos continuados de tensión interna o pánico intermitente que el sujeto sólo puede dominar con alguna dificultad'),
            (5, '5.'),
            (6, '6. Terror o angustia tenaz. Pánico irresistible'),
            ),
        widget = VARFORM,
        )
    item_04 = forms.ChoiceField(
        label = '4.- Sueño reducido',
        choices = (
            (0, '0. Duerme como siempre'),
            (1, '1.'),
            (2, '2. Ligera dificultad para dormirse o sueño ligeramente reducido, sueño ligero o perturbado'),
            (3, '3.'),
            (4, '4. Sueño reducido o interrumpido durante al menos 2 h'),
            (5, '5.'),
            (6, '6. Menos de 2 o 3 h de sueño'),
            ),
        widget = VARFORM,
        )
    item_05 = forms.ChoiceField(
        label = '5.- Apetito reducido',
        choices = (
            (0, '0. Apetito normal o aumentado'),
            (1, '1.'),
            (2, '2. Apetito ligeramente reducido'),
            (3, '3.'),
            (4, '4. Sin apetito. La comida es insípida'),
            (5, '5.'),
            (6, '6. Necesita persuasión para comer algo'),
            ),
        widget = VARFORM,
        )
    item_06 = forms.ChoiceField(
        label = '6. Dificultades para concentrarse',
        choices = (    
            (0, '0. Ninguna dificultad para concentrarse'),
            (1, '1.'),
            (2, '2. Dificultades ocasionales para centrar los pensamientos'),
            (3, '3.'),
            (4, '4. Dificultades para concentrarse y seguir una idea que reduce la capacidad de leer o mantener una conversación'),
            (5, '5.'),
            (6, '6. Incapaz de leer o mantener una conversación si no es con gran dificultad'),
            ),
        widget = VARFORM,
        )
    item_07 = forms.ChoiceField(
        label = '7. Lasitud',
        choices = (    
            (0, '0. Casi sin dificultad para empezar algo. Sin apatía'),
            (1, '1.'),
            (2, '2. Dificultades para empezar actividades'),
            (3, '3.'),
            (4, '4. Dificultades para empezar actividades rutinarias sencillas que se llevan a cabo con esfuerzo'),
            (5, '5.'),
            (6, '6. Lasitud total. Incapaz de hacer nada sin ayuda'),
            ),
        widget = VARFORM,
        )
    item_08 = forms.ChoiceField(
        label = '8. Incapacidad para sentir',
        choices = (    
            (0, '0. Interés normal por el entorno y por otras personas'),
            (1, '1.'),
            (2, '2. Menor capacidad para disfrutar de las cosas que normalmen te le interesan'),
            (3, '3.'),
            (4, '4. Pérdida de interés por el entorno. Pérdida de sentimientos respecto a los amigos y conocidos'),
            (5, '5.'),
            (6, '6. La experiencia de estar emocionalmente paralizado, incapacidad para sentir enfado, pena o placer y una total o incluso dolorosa falta de sentimientos hacia los parientes próximos y amigos'),
            ),
        widget = VARFORM,
        )
    item_09 = forms.ChoiceField(    
        label = '9. Pensamientos pesimistas',
        choices = (
            (0, '0. Sin pensamientos pesimistas'),
            (1, '1.'),
            (2, '2. Ideas variables de fracaso, autorreproche o autodesprecio'),
            (3, '3.'),
            (4, '4. Autoacusaciones persistentes o ideas definidas, pero aún racionales, de culpabilidad o pecado. Cada vez más pesimista respecto al futuro'),
            (5, '5.'),
            (6, '6. Alucinaciones de ruina, remordimiento o pecado irredimible. Autoacusaciones que son absurdas e inquebrantables'),
            ),
        widget = VARFORM,
        )
    item_10 = forms.ChoiceField(    
        label = '10. Pensamientos suicidas',
        choices = (
            (0, '0. Disfruta de la vida o la acepta tal como viene'),
            (1, '1.'),
            (2, '2. Cansado de vivir. Sólo pensamientos suicidas pasajeros'),
            (3, '3.'),
            (4, '4. Probablemente  estaría  mejor  muerto/a. Los  pensamientos suicidas son habituales, y se considera el suicidio como una posible solución, pero sin ninguna intención o plan específico'),
            (5, '5.'),
            (6, '6. Planes explícitos de suicidio cuando se presente una oportunidad. Preparativos activos para el suicidio'),
            ),
        widget = VARFORM,
        )


    
#     ########     ###    ##    ##  ######   ######
#     ##     ##   ## ##   ###   ## ##    ## ##    ##
#     ##     ##  ##   ##  ####  ## ##       ##
#     ########  ##     ## ## ## ##  ######   ######
#     ##        ######### ##  ####       ##       ##
#     ##        ##     ## ##   ### ##    ## ##    ##
#     ##        ##     ## ##    ##  ######   ######
#

class PanssAdminForm(forms.ModelForm):
    LIKERT_PANSS = (
        (7, '7.Extremo'),
        (6, '6.Severo'),
        (5, '5.Moderado severo'),
        (4, '4.Moderado'),
        (3, '3.Ligero'),
        (2, '2.Mínimo'),
        (1, '1.Ausente'),
        )
    class Meta:
        model = Panss
        fields = '__all__'
    item_p01 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='1.- Delirios.',
        widget = VARFORM,
        )
    item_p02 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='2.- Desorganización conceptual.',
        widget = VARFORM,
        )
    item_p03 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='3.- Conducta alucinatoria.',
        widget = VARFORM,
        )
    item_p04 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='4.- Exitación.',
        widget = VARFORM,
        )
    item_p05 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='5.- Grandiosidad.',
        widget = VARFORM,
        )
    item_p06 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='6.- Suspicacia / Perjuicio.',
        widget = VARFORM,
        )
    item_p07 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='7.- Hostilidad.',
        widget = VARFORM,
        )

    item_n01 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='1.- Embotamiento afectivo.',
        widget = VARFORM,
        )
    item_n02 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='2.- Retracción emocional.',
        widget = VARFORM,
        )
    item_n03 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='3.- Pobre relación.',
        widget = VARFORM,
        )
    item_n04 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='4.- Retracción social, apatía pasiva.',
        widget = VARFORM,
        )
    item_n05 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='5.- Dificultad de pensamiento abstracto.',
        widget = VARFORM,
        )
    item_n06 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='6.- Falta de espontaneidad y fluidez de la conversación.',
        widget = VARFORM,
        )
    item_n07 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='7.- Pensamiento estereotipado',
        widget = VARFORM,
        )

    item_g01 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='1.- Preocupaciones somáticas.',
        widget = VARFORM,
        )
    item_g02 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='2.- Ansiedad.',
        widget = VARFORM,
        )
    item_g03 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='3.- Sentimientos de culpa.',
        widget = VARFORM,
        )
    item_g04 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='4.- Tensión motora.',
        widget = VARFORM,
        )
    item_g05 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='5.- Manierismos y posturas.',
        widget = VARFORM,
        )
    item_g06 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='6.- Depresión.',
        widget = VARFORM,
        )
    item_g07 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='7.- Retardo motor',
        widget = VARFORM,
        )
    item_g08 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='8.- Falta de colaboración.',
        widget = VARFORM,
        )
    item_g09 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='9.- Inusuales contenidos del pensamiento.',
        widget = VARFORM,
        )
    item_g10 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='10.- Desorientación.',
        widget = VARFORM,
        )
    item_g11 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='11.- Atención deficiente.',
        widget = VARFORM,
        )
    item_g12 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='12.- Ausencia de juicio e introspección.',
        widget = VARFORM,
        )
    item_g13 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='13.- Trastorno de la volición.',
        widget = VARFORM,
        )
    item_g14 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='14.- Control deficiente de impulsos.',
        widget = VARFORM,
        )
    item_g15 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='15.- Preocupación.',
        widget = VARFORM,
        )
    item_g16 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='16.- Evitación social activa',
        widget = VARFORM,
        )


#     ##    ## ##     ## ########   ######
#      ##  ##  ###   ### ##     ## ##    ##
#       ####   #### #### ##     ## ##
#        ##    ## ### ## ########   ######
#        ##    ##     ## ##   ##         ##
#        ##    ##     ## ##    ##  ##    ##
#        ##    ##     ## ##     ##  ######
#
class YmrsAdminForm(forms.ModelForm):
    class Meta:
        model = Ymrs
        fields = '__all__'
    item_01 = forms.ChoiceField(
        label = '1.- Euforia',
        choices = (
            (0, '0.Ausente'),
            (1, '1.Posible o moderada, sólo cuando se le pregunta'),
            (2, '2.Clara aunque subjetiva y apropiada al contenido: optimista, seguro de sí mismo/a, alegre'),
            (3, '3.Elevada e inapropiada'),
            (4, '4.Claramente eufórico/a, risa inadecuada, canta durante la entrevista, etc.'),
            ),
        widget = VARFORM,
        )
    item_02 = forms.ChoiceField(
        label = '2.- Hiperactividad',
        choices = (
            (0, '0.Ausente'),
            (1, '1.Subjetivamente aumentada'),
            (2, '2.Vigoroso/a, hipergestual'),
            (3, '3.Energía excesiva, hiperactividad fluctuante, inquietud (puede ser calmado/a)'),
            (4, '4.Agitación o hiperactividad constante (no puede ser calmado/a)'),
            ),
        widget = VARFORM,
        )
    item_03 = forms.ChoiceField(
        label = '3.- Impulso sexual',
        choices = (
            (0, '0.Normal, no aumentado'),
            (1, '1.Posible o moderadamente aumentado'),
            (2, '2.Claro aumento al preguntar'),
            (3, '3.Referido como elevado de forma espontánea, contenido sexual del discurso, preocupación por temas sexuales'),
            (4, '4.Actos o incitaciones sexuales evidentes (hacia pacientes, personal o entrevistador)'),
            ),
        widget = VARFORM,
        )
    item_04 = forms.ChoiceField(
        label = '4.- Sueño',
        choices = (
            (0, '0.No reducido'),
            (1, '1.Disminución en menos de 1 ,hora'),
            (2, '2.Disminución en más de 1 hora'),
            (3, '3.Refiere disminución de la necesidad de dormir'),
            (4, '4.Niega necesidad de dormir'),
            ),
        widget = VARFORM,
        )
    item_05 = forms.ChoiceField(
        label = '5.- Irritabilidad',
        choices = (
            (0, '0.Ausente'),
            (2, '2.Subjetivamente aumentada'),
            (4, '4.Irritabilidad fluctuante durante la entrevista, episodios recientes de rabia o enfado'),
            (6, '6.Predominantemente irritable durante la entrevista, brusco y cortante'),
            (8, '8.Hostil, no colaborador/a, entrevista imposible'),
            ),
        widget = VARFORM,
        )

    item_06 = forms.ChoiceField(
        label = '6.- Expresión verbal',
        choices = (
            (0, '0.No aumentada'),
            (2, '2.Sensación de locuacidad'),
            (4, '4.Aumentada de forma fluctuante, verborrea ocasional'),
            (6, '6.Claramente aumentada en ritmo y cantidad, difícil de interrumpir, intrusiva'),
            (8, '8.Verborrea ininterrumpible y continua'),
            ),
        widget = VARFORM,
        )
    item_07 = forms.ChoiceField(
        label = '7.- Trastornos del curso del pensamiento y el lenguaje',
        choices = (
            (0, '0.Ausentes'),
            (1, '1.Circunstancialidad, distraibilidad moderada, aceleración del pensamiento'),
            (2, '2.Distraibilidad clara, descarrilamiento, taquipsiquia'),
            (3, '3.Fuga de ideas, tangencialidad, discurso difícil de seguir, rimas, ecolalia'),
            (4, '4.Incoherencia, ininteligibilidad, comunicación imposible'),
            ),
        widget = VARFORM,
        )
    item_08 = forms.ChoiceField(
        label = '8.- Trastornos del contenido del pensamiento',
        choices = (
            (0, '0.Ausentes'),
            (2, '2.Planes discutibles, nuevos intereses'),
            (4, '4.Proyectos especiales, misticismo'),
            (6, '6.Ideas grandiosas o paranoides, ideas de referencia'),
            (8, '8.Delirios, alucinaciones'),
            ),
        widget = VARFORM,
        )
    item_09 = forms.ChoiceField(
        label = '9.- Agresividad',
        choices = (
            (0, '0.Ausente, colaborador/a'),
            (2, '2.Sarcástico/a, enfático/a, lacónico/a'),
            (4, '4.Querulante, pone en guardia'),
            (6, '6.Amenaza al entrevistador, habla a gritos, entrevista difícil'),
            (8, '8.Claramente agresivo/a, destructivo/a, entrevista imposible'),
            ),
        widget = VARFORM,
        )
    item_10 = forms.ChoiceField(
        label = '10.- Apariencia',
        choices = (
            (0, '0.Higiene e indumentaria apropiada '),
            (1, '1.Ligeramente descuidada'),
            (2, '2.Mal arreglado/a, moderadamente despeinado/a, indumentaria sobrecargada'),
            (3, '3.Despeinado/a, semidesnudo/a, maquillaje llamativo'),
            (4, '4.Completamente desaseado/a, adornado/a, indumentaria extravagante'),
            ),
        widget = VARFORM,
        )
    item_11 = forms.ChoiceField(
        label = '11.- Conciencia de enfermedad',
        choices = (
            (0, '0.Presente, admite la enfermedad, acepta tratamiento'),
            (1, '1.Según él/ella, posiblemente enfermo/a'),
            (2, '2.Admite cambio de conducta, pero niega enfermedad'),
            (3, '3.Admite posible cambio de conducta, niega enfermedad'),
            (4, '4.Niega cualquier cambio de conduct'),
            ),
        widget = VARFORM,
        )

#
#      ##   ##  ##   ##    ###             #####      ##      #####
#      ##   ##  ##   ##   ## ##            ##  ##     ##     ##   ##
#      ## # ##  ##   ##  ##   ##           ##   ##   ####    ##
#      ## # ##  #######  ##   ##  #######  ##   ##   ## #     #####
#      ## # ##  ##   ##  ##   ##           ##   ##  ######        ##
#      ### ###  ##   ##   ## ##            ##  ##   ##   #   ##   ##
#      ##   ##  ##   ##    ###             #####   ###   ##   #####
#

   
# WHO-DAS 2.0 36 items
class Who_dasAdminForm(forms.ModelForm):
    LIKERT5 = (
        (5, '5.Extrema / no puede'),
        (4, '4.Severa'),
        (3, '3.Moderada'),
        (2, '2.Leve'),
        (1, '1.Ninguna'),
        )
    class Meta:
        model = Who_das
        fields = '__all__'
    d1_1 = forms.ChoiceField(
        label = 'D1.1 Concentrarse en hacer algo durante 10 minutos?',
        choices = LIKERT5,
        widget = VARFORM,
        )
    d1_2 = forms.ChoiceField(
        label = 'D1.2 Recordar las cosas importantes que tiene que hacer?',
        choices = LIKERT5,
        widget = VARFORM,
        )
    d1_3 = forms.ChoiceField(
        label = 'D1.3 Analizar y encontrar soluciones a los problemas de la vida diaria?',
        choices = LIKERT5,
        widget = VARFORM,
        )
    d1_4 = forms.ChoiceField(
        label = 'D1.4 Aprender una nueva tarea, como por ejemplo llegar a un lugar nuevo?',
        choices = LIKERT5,
        widget = VARFORM,
        )
    d1_5 = forms.ChoiceField(
        label = 'D1.5 Entender en general lo que dice la gente?',
        choices = LIKERT5,
        widget = VARFORM,
        )
    d1_6 = forms.ChoiceField(
        label = 'D1.6 Iniciar o mantener una conversación?',
        choices = LIKERT5,
        widget = VARFORM,
        )
    d2_1 = forms.ChoiceField(
        label = 'D2.1 Estar de pie durante largos periodos de tiempo, como por ejemplo 30 minutos?',
        choices = LIKERT5,
        widget = VARFORM,
        )
    d2_2 = forms.ChoiceField(
        label = 'D2.2 Ponerse de pie cuando estaba sentado(a)?',
        choices = LIKERT5,
        widget = VARFORM,
        )
    d2_3 = forms.ChoiceField(
        label = 'D2.3 Moverse dentro de su casa?',
        choices = LIKERT5,
        widget = VARFORM,
        )
    d2_4 = forms.ChoiceField(
        label = 'D2.4 Salir de su casa?',
        choices = LIKERT5,
        widget = VARFORM,
        )
    d2_5 = forms.ChoiceField(
        label = 'D2.5 Andar largas distancias, como un kilómetro?',
        choices = LIKERT5,
        widget = VARFORM,
        )
    d3_1 = forms.ChoiceField(
        label = 'D3.1 Lavarse todo el cuerpo (bañarse)?',
        choices = LIKERT5,
        widget = VARFORM,
        )
    d3_2 = forms.ChoiceField(
        label = 'D3.2 Vestirse?',
        choices = LIKERT5,
        widget = VARFORM,
        )
    d3_3 = forms.ChoiceField(
        label = 'D3.3 Comer?',
        choices = LIKERT5,
        widget = VARFORM,
        )
    d3_4 = forms.ChoiceField(
        label = 'D3.4 Estar sólo durante unos días?',
        choices = LIKERT5,
        widget = VARFORM,
        )
    d4_1 = forms.ChoiceField(
        label = 'D4.1 Relacionarse con personas que no conoce?',
        choices = LIKERT5,
        widget = VARFORM,
        )
    d4_2 = forms.ChoiceField(
        label = 'D4.2 Mantener una amistad?',
        choices = LIKERT5,
        widget = VARFORM,
        )
    d4_3 = forms.ChoiceField(
        label = 'D4.3 Llevarse bien con personas cercanas a usted?',
        choices = LIKERT5,
        widget = VARFORM,
        )
    d4_4 = forms.ChoiceField(
        label = 'D4.4 Hacer nuevos amigos?',
        choices = LIKERT5,
        widget = VARFORM,
        )
    d4_5 = forms.ChoiceField(
        label = 'D4.5 Tener relaciones sexuales?',
        choices = LIKERT5,
        widget = VARFORM,
        )
    d5_1 = forms.ChoiceField(
        label = 'D5.1 Cumplir con sus quehaceres de la casa?',
        choices = LIKERT5,
        widget = VARFORM,
        )
    d5_2 = forms.ChoiceField(
        label = 'D5.2 Realizar bien sus quehaceres de la casa mas importantes?',
        choices = LIKERT5,
        widget = VARFORM,
        )
    d5_3 = forms.ChoiceField(
        label = 'D5.3 Acabar todo el trabajo de la casa que tenía que hacer?',
        choices = LIKERT5,
        widget = VARFORM,
        )
    d5_4 = forms.ChoiceField(
        label = 'D5.4 Acabar sus quehaceres de la casa tan rapido com osea necesario?',
        choices = LIKERT5,
        widget = VARFORM,
        )
    d5_5 = forms.ChoiceField(
        label = 'D5.5 Llevar a cabo su trabajo diario o las actividades escolares?',
        choices = LIKERT5,
        widget = VARFORM,
        )
    d5_6 = forms.ChoiceField(
        label = 'D5.6 Realizar bien las tareas más importantes de su trabajo o de la escuela?',
        choices = LIKERT5,
        widget = VARFORM,
        )   
    d5_7 = forms.ChoiceField(
        label = 'D5.7 Acabar todo el trabajo que necesitaba hacer?',
        choices = LIKERT5,
        widget = VARFORM,
        )
    d5_8 = forms.ChoiceField(
        label = 'D5.8 Acabar su trabajo tan rápido como era necesario?',
        choices = LIKERT5,
        widget = VARFORM,
        )
    d6_1 = forms.ChoiceField(
        label = 'D6.1 Cuánta dificultad ha tenido para participar, al mismo nivel que el resto de las personas, en actividades de la comunidad (por ejemplo, fiestas, actividades religiosas u otras actividades)?',
        choices = LIKERT5,
        widget = VARFORM,
        )
    d6_2 = forms.ChoiceField(
        label = 'D6.2 Cuánta dificultad ha tenido debido a barreras u obstáculos existentes en su alrededor (entorno)?',
        choices = LIKERT5,
        widget = VARFORM,
        )
    d6_3 = forms.ChoiceField(
        label = 'D6.3 Cuánta dificultad ha tenido para vivir con dignidad (o respeto) debido a las actitudes y acciones de otras personas?',
        choices = LIKERT5,
        widget = VARFORM,
        )
    d6_4 = forms.ChoiceField(
        label = 'D6.4 Cuánto tiempo ha dedicado a su “condición de salud” o a las consecuencias de la misma?',
        choices = LIKERT5,
        widget = VARFORM,
        )
    d6_5 = forms.ChoiceField(
        label = 'D6.5 Cuánto le ha afectado emocionalmente su “condición de salud”?',
        choices = LIKERT5,
        widget = VARFORM,
        )
    d6_6 = forms.ChoiceField(
        label = 'D6.6 Qué impacto económico ha tenido para usted o para su familia su “condición de salud”?',
        choices = LIKERT5,
        widget = VARFORM,
        )
    d6_7 = forms.ChoiceField(
        label = 'D6.7 Cuánta dificultad ha tenido su familia debido a su condición de salud?',
        choices = LIKERT5,
        widget = VARFORM,
        )      
    d6_8 = forms.ChoiceField(
        label = 'D6.8 Cuánta dificultad ha tenido para realizar por sí mismo(a) cosas que le ayuden a relajarse o disfrutar?',
        choices = LIKERT5,
        widget = VARFORM,
        )   
    h1 = forms.ChoiceField(
        label = 'H1 En los últimos 30 días, durante cuántos días ha tenido esas dificultades?',
        choices = LIKERT5,
        widget = forms.NumberInput,
        )
    h2 = forms.ChoiceField(
        label = 'H2 En los últimos 30 días, cuántos días fue no pudo realizar nada de sus actividades habituales o en el trabajo debido a su condición de salud?',
        choices = LIKERT5,
        widget = forms.NumberInput,
        )
    h3 = forms.ChoiceField(
        label = 'H3 En los últimos 30 días, sin contar los días que no pudo realizar nada de sus actividades habituales cuántos días tuvo que recortar o reducir sus actividades habituales o en el trabajo, debido a su condición de salud?',
        choices = LIKERT5,
        widget = forms.NumberInput,
        )

# ZARIT

LIKERT_ZARIT= (
        (0, '0. Nunca'),
        (1, '1. Casi nunca'),
        (2, '2. A veces'),
        (3, '3. Bastantes veces'),
        (4, '4. Siempre'),
        )

class ZaritAdminForm(forms.ModelForm):
    class Meta:
        model = Zarit
        fields = '__all__'
    item_01 = forms.ChoiceField(
        label = '1.- ¿Siente que su familiar solicita más ayuda de la que realmente necesita?',
        choices = LIKERT_ZARIT,
        widget = VARFORM,
        )
    item_02 = forms.ChoiceField(
        label = '2.- ¿Siente que debido al tiempo que dedica a su familiar ya no dispone de tiempo suficiente para usted?',
        choices = LIKERT_ZARIT,
        widget = VARFORM,
        )
    item_03 = forms.ChoiceField(
        label = '3.- ¿Se siente tenso cuando tiene que cuidar a su familiar y atender además otras responsabilidades?',
        choices = LIKERT_ZARIT,
        widget = VARFORM,
        )
    item_04 = forms.ChoiceField(
        label = '4.- ¿Se siente avergonzado por la conducta de su familiar?',
        choices = LIKERT_ZARIT,
        widget = VARFORM,
        )
    item_05 = forms.ChoiceField(
        label = '5.- ¿Se siente enfadado cuando está cerca de su familiar?',
        choices = LIKERT_ZARIT,
        widget = VARFORM,
        )
    item_06 = forms.ChoiceField(
        label = '6.- ¿Cree que la situación actual afecta de manera negativa a su relación con amigos y otros miembros de su familia?',
        choices = LIKERT_ZARIT,
        widget = VARFORM,
        )
    item_07 = forms.ChoiceField(
        label = '7.- ¿Siente temor por el futuro que le espera a su familiar?',
        choices = LIKERT_ZARIT,
        widget = VARFORM,
        )
    item_08 = forms.ChoiceField(
        label = '8.- ¿Siente que su familiar depende de usted?',
        choices = LIKERT_ZARIT,
        widget = VARFORM,
        )
    item_09 = forms.ChoiceField(
        label = '9.- ¿Se siente agobiado cuando tiene que estar junto a su familiar?',
        choices = LIKERT_ZARIT,
        widget = VARFORM,
        )
    item_10 = forms.ChoiceField(
        label = '10.- ¿Siente que su salud se ha resentido por cuidar a su familiar?',
        choices = LIKERT_ZARIT,
        widget = VARFORM,
        )
    item_11 = forms.ChoiceField(
        label = '11.- ¿Siente que no tiene la vida privada que desearía debido a su familiar?',
        choices = LIKERT_ZARIT,
        widget = VARFORM,
        )
    item_12 = forms.ChoiceField(
        label = '12.- ¿Cree que su vida social se ha visto afectada por tener que cuidar de su familiar?',
        choices = LIKERT_ZARIT,
        widget = VARFORM,
        )
    item_13 = forms.ChoiceField(
        label = '13.- ¿Se siente incómodo para invitar amigos a casa, a causa de su familiar?',
        choices = LIKERT_ZARIT,
        widget = VARFORM,
        )
    item_14 = forms.ChoiceField(
        label = '14.- ¿Cree que su familiar espera que usted le cuide, como si fuera la única persona con la que puede contar?',
        choices = LIKERT_ZARIT,
        widget = VARFORM,
        )
    item_15 = forms.ChoiceField(
        label = '15.- ¿Cree que no dispone de dinero suficiente para cuidar a su familiar además de sus otros gastos?',
        choices = LIKERT_ZARIT,
        widget = VARFORM,
        )
    item_16 = forms.ChoiceField(
        label = '16.- ¿Siente que será incapaz de cuidar a su familiar por mucho más tiempo?',
        choices = LIKERT_ZARIT,
        widget = VARFORM,
        )
    item_17 = forms.ChoiceField(
        label = '17.- ¿Siente que ha perdido el control sobre su vida desde que la enfermedad de su familiar se manifestó?',
        choices = LIKERT_ZARIT,
        widget = VARFORM,
        )
    item_18 = forms.ChoiceField(
        label = '18.- ¿Desearía poder encargar el cuidado de su familiar a otras personas?',
        choices = LIKERT_ZARIT,
        widget = VARFORM,
        )
    item_19 = forms.ChoiceField(
        label = '19.- ¿Se siente inseguro acerca de lo que debe hacer con su familiar?',
        choices = LIKERT_ZARIT,
        widget = VARFORM,
        )
    item_20 = forms.ChoiceField(
        label = '20.- ¿Siente que debería hacer más de lo que hace por su familiar?',
        choices = LIKERT_ZARIT,
        widget = VARFORM,
        )
    item_21 = forms.ChoiceField(
        label = '21.- ¿Cree que podría cuidar de su familiar mejor de lo que lo hace?',
        choices = LIKERT_ZARIT,
        widget = VARFORM,
        )
    item_22 = forms.ChoiceField(
        label = '22.- En general: ¿Se siente muy sobrecargado por tener que cuidar de su familia',
        choices = LIKERT_ZARIT,
        widget = VARFORM,
        )