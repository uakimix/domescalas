#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.utils.safestring import mark_safe
from django import forms
from escalas.models import *

CHOICES = (
    (0, 'No'),
    (1, 'Si'),
    )


class HorizRadioRenderer(forms.RadioSelect.renderer):
    """ this overrides widget method to put radio buttons horizontally
        instead of vertically.
    """
    def render(self):
            """Outputs radios"""
            return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


class TratamientoForm(forms.ModelForm):
	class Meta:
		model = Tratamiento
		fields = '__all__'
	depot=forms.ChoiceField(
		choices=(
            (False, 'No'),
            (True, 'Si'),
            ),
		label='¿Depot?',
		widget=forms.RadioSelect(renderer=HorizRadioRenderer),
		)

#     ########   ######  ####  ######
#     ##     ## ##    ##  ##  ##    ##
#     ##     ## ##        ##  ##
#     ########  ##        ##   ######
#     ##     ## ##        ##        ##
#     ##     ## ##    ##  ##  ##    ##
#     ########   ######  ####  ######

class BcisAdminForm(forms.ModelForm):
   
    class Meta:
        model = Bcis
        fields = '__all__'
        widgets = {
            'item_01': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_02': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_03': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_04': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_05': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_06': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_07': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_08': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_09': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_10': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_11': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_12': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_13': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_14': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_15': forms.RadioSelect(renderer=HorizRadioRenderer),
        }
        labels = {
            'item_01': ('1. Algunas veces he malinterpretado las actitudes que los demás tienen hacia mí'),
            'item_02': ('2. Las interpretaciones que hago de mis experiencias son sin duda correctas'),
            'item_03': ('3. Otras personas pueden entender mejor que yo la causa de mis experiencias raras'),
            'item_04': ('4. Llego a conclusiones demasiado rápido'),
            'item_05': ('5. Algunas de mis experiencias que me han parecido muy reales pueden haberse debido a mi imaginación'),
            'item_06': ('6. Algunas de las ideas que tenía como ciertas acabaron siendo falsas'),
            'item_07': ('7. Si siento que algo es correcto significa que es correcto'),
            'item_08': ('8. Aunque me siento muy seguro/a de estar en lo cierto, podría estar equivocado/a'),
            'item_09': ('9. Conozco mejor que nadie cuáles son mis problemas'),
            'item_10': ('10. Cuando los demás no está de acuerdo conmigo, normalmente están equivocados'),
            'item_11': ('11. No puedo fiarme de lo que opinan los demás sobre mis experiencias'),
            'item_12': ('12. Si alguien comenta que mis creencias son erróneas estoy dispuesto/a a considerar su opinión'),
            'item_13': ('13. Puedo confiar en mi propio juicio siempre'),
            'item_14': ('14. Suele haber más de una explicación posible sobre por qué la gente actúa de la manera en que lo hace'),
            'item_15': ('15. Mis experiencias raras pueden deberse a que esté muy alterado/a o estresado/a'),
        }
        
        
#     ########  ########  ########   ######
#     ##     ## ##     ## ##     ## ##    ##
#     ##     ## ##     ## ##     ## ##
#     ########  ########  ########   ######
#     ##     ## ##        ##   ##         ##
#     ##     ## ##        ##    ##  ##    ##
#     ########  ##        ##     ##  ######

class BprsAdminForm(forms.ModelForm):
    class Meta:
        model = Bprs
        fields = '__all__'
        widgets = {
            'item_01': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_02': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_03': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_04': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_05': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_06': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_07': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_08': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_09': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_10': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_11': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_12': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_13': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_14': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_15': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_16': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_17': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_18': forms.RadioSelect(renderer=HorizRadioRenderer),
        }
        labels = {
            'item_01': ('1.- Preocupación somática'),
            'item_02': ('2.- Ansiedad psíquica'),
            'item_03': ('3.- Aislamiento emocional'),
            'item_04': ('4.- Desorganización conceptual (incoherencia)'),
            'item_05': ('5.- Autodesprecio y sentimientos de culpa'),
            'item_06': ('6.- Tensión. Ansiedad somática'),
            'item_07': ('7.- Manierismo y postura extraña'),
            'item_08': ('8.- Grandeza'),
            'item_09': ('9.- Humor depresivo'),
            'item_10': ('10.- Hostilidad'),
            'item_11': ('11.- Suspicacia'),
            'item_12': ('12.- Alucinaciones'),
            'item_13': ('13.- Enlentecimiento motor'),
            'item_14': ('14.- Falta de cooperación'),
            'item_15': ('15.- Contenido insusual del pensamiento'),
            'item_16': ('16.- Embotamiento, aplanamiento afectivo'),
            'item_17': ('17.- Exitación'),
            'item_18': ('18.- Desorientación y confusión'),
        }
        
# 	 ######   ######   #######           #######
# 	##    ## ##    ## ##     ##         ##     ##
# 	##       ##       ##     ##         ##     ##
# 	##        ######  ##     ## #######  #######
# 	##             ## ##  ## ##         ##     ##
# 	##    ## ##    ## ##    ##          ##     ##
# 	 ######   ######   ##### ##          #######

class Csq8AdminForm(forms.ModelForm):
    class Meta:
        model = Csq8
        fields = '__all__'
        widgets = {
            'autor': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_01': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_02': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_03': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_04': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_05': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_06': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_07': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_08': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_09': forms.RadioSelect(renderer=HorizRadioRenderer),
            }
        labels = {
            'author' : ('Autor'),    
            'item_01': ('1.-¿Cómo evaluaría la calidad de los servicios que ha recibido'),
            'item_02': ('2.-¿Recibió la clase de servicio que usted requería?'),
            'item_03': ('3.-¿Hasta que punto ha ayudado nuestro programa a solucionar sus problemas?'),
            'item_04': ('4.-¿Si un/a amigo/a estuviera en necesidad de ayuda similar, le recomendaría nuestro programa?'),
            'item_05': ('5.-¿Cómo de satisfecho/a esta usted con la cantidad de ayuda que ha recibido?'),
            'item_06': ('6.-¿Los servicios que ha recibido le han ayudado a enfrentarse mejor a sus problemas?'),
            'item_07': ('7.- ¿En general, cómo de satisfecho/a está usted con los servicios que ha recibido?'),
            'item_08': ('8.-¿Si necesitara ayuda otra vez volvería a nuestro programa?'),
            'item_09': ('9.-Lo que más me ha gustado de la atención que he recibido ha sido:'),
            }
   
#     ########  ##     ## ##    ## ########
#     ##     ## ##     ## ##   ##  ##
#     ##     ## ##     ## ##  ##   ##
#     ##     ## ##     ## #####    ######
#     ##     ## ##     ## ##  ##   ##
#     ##     ## ##     ## ##   ##  ##
#     ########   #######  ##    ## ########

class DukeAdminForm(forms.ModelForm):
    class Meta:
        model = Duke
        fields = '__all__'
        widgets = {
            'item_01': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_02': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_03': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_04': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_05': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_06': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_07': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_08': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_09': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_10': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_11': forms.RadioSelect(renderer=HorizRadioRenderer),
            }
        labels = {
            'item_01': ('1.- Recibo visitas de mis amigos y familiares'),
            'item_02': ('2.- Recibo ayuda en asuntos relacionados con mi casa'),
            'item_03': ('3.- Recibo elogios y reconocimientos cuando hago bien mi trabajo'),
            'item_04': ('4.- Cuento con personas que se preocupan de lo que me sucede'),
            'item_05': ('5.- Recibo amor y afecto'),
            'item_06': ('6.- Tengo posibilidad de hablar con alguien de mis problemas de trabajo o en la casa'),
            'item_07': ('7.- Tengo la posibilidad de hablar con alguien de mis problemas personales y familiares'),
            'item_08': ('8.- Tengo la posibilidad de hablar con alguien de mis problemas económicos'),
            'item_09': ('9.- Recibo invitaciones para distraerme y salir con otras personas'),
            'item_10': ('10.- Recibo consejos útiles cuando me ocurre algún acontecimiento importante en mi vida'),
            'item_11': ('11.- Recibo ayuda cuando estoy enfermo en la cama'),
            }


# 	####  ######   ######
# 	 ##  ##    ## ##    ##
# 	 ##  ##       ##
# 	 ##  ##       ##   ####
# 	 ##  ##       ##    ##
# 	 ##  ##    ## ##    ##
# 	####  ######   ######

class Icg_geAdminForm(forms.ModelForm):
    class Meta:
        model = Icg_ge
        fields = '__all__'
        widgets = {
            'icg_ge': forms.RadioSelect(renderer=HorizRadioRenderer),
            'quien_ge': forms.RadioSelect(renderer=HorizRadioRenderer),
            }
        labels = {
            'icg_ge': ('ICG Gravedad'),
            'quien_ge': ('Aplicada por:'),
            }
    	
class Icg_meAdminForm(forms.ModelForm):
    class Meta:
        model = Icg_me
        fields = '__all__'
    icg_me = forms.ChoiceField(
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
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
    )
    quien_me = forms.ChoiceField(
    	choices = (
    		('PSQ', 'Psiquiatra'),
    		('PAC', 'Paciente'),
    		),
    	label = 'Aplicada por:',
    	widget = forms.RadioSelect(renderer=HorizRadioRenderer),
    )
    
    
    

        ##     ## ########  ########   ######
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
        widget = forms.RadioSelect,
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
        widget = forms.RadioSelect,
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
        widget = forms.RadioSelect,
        )
    item_04 = forms.ChoiceField(
        label = '4.- Insomnio precoz',
        choices = (
            (0, '0.Ausente'),
            (1, '1.Dificultades ocasionales para dormirse, por ejemplo, más de media hora'),
            (2, '2.Dificultades para dormirse cada noche'),
            ),
        widget = forms.RadioSelect,
        )
    item_05 = forms.ChoiceField(
        label = '5.- Insomnio medio',
        choices = (
            (0, '0.Ausente'),
            (1, '1.El paciente s queja de estar inquieto durante la noche'),
            (2, '2.Está despierto durante la noche; medicación, etc.'),
            ),
        widget = forms.RadioSelect,
        )
    item_06 = forms.ChoiceField(
        label = '6.- Insomnio tardío',
        choices = (
            (0, '0.Ausente'),
            (1, '1.Se despierta a primeras horas de la madrugada pero vuelve a dormirse'),
            (2, '2.No puede volver a dormirse si se levanta de la cama'),
            ),
        widget = forms.RadioSelect,
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
        widget = forms.RadioSelect,
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
        widget = forms.RadioSelect,
        )
    item_09 = forms.ChoiceField(
        label = '9.- Agitación',
        choices = (
            (0, '0.Ninguna'),
            (1, '1.“Juega” con sus manos, cabellos, etc.'),
            (2, '2.Se retuerce las manos, se muerde las uñas, los labios, se tira de los cabellos, etc.'),
            ),
        widget = forms.RadioSelect,
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
        widget = forms.RadioSelect,
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
        widget = forms.RadioSelect,
        )
    item_12 = forms.ChoiceField(
        label = '12.- Síntomas somáticos gastrointestinales',
        choices = (
            (0, '0.Ninguno'),
            (1, '1.Pérdida de apetito, pero come sin necesidad de que estimulen. Sensación de pesadez en el abdomen'),
            (2, '2.Dificultad en comer si no se le insiste. Solicita o necesita laxantes o medicación intestinal para sus síntomas gastrointestinales'),
            ),
        widget = forms.RadioSelect,
        )
    item_13 = forms.ChoiceField(
        label = '13.- Síntomas somáticos generales',
        choices = (
            (0, '0.Ninguno'),
            (1, '1.Pesadez en las extremidades, espalda o cabeza. Dorsalgias, cefalalgias, algias musculares. Pérdida de energía y fatigabilidad'),
            (2, '2.Cualquier síntoma bien definido'),
            ),
        widget = forms.RadioSelect,
        )
    item_14 = forms.ChoiceField(
        label = '14.- Síntomas genitales',
        choices = (
            (0, '0.Ausente'),
            (1, '1.Débil'),
            (2, '2.Grave'),
            (3, '3.Incapacitante'),
            ),
        widget = forms.RadioSelect,
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
        widget = forms.RadioSelect,
        )

    item_16 = forms.ChoiceField(
        label = '16.- Pérdida de peso',
        choices = (
            (0, '0.No hay pérdida de peso'),
            (1, '1.Probable pérdida de peso asociada con la enfermedad actual'),
            (2, '2.Pérdida de peso definida (según el enfermo)'),
            ),
        widget = forms.RadioSelect,
        )

    item_17 = forms.ChoiceField(
        label = '17.- Insight (conciencia de enfermedad)',
        choices = (
            (0, '0.Se da cuenta de que está deprimido y enfermo'),
            (1, '1.Se da cuenta de sy enfermedad pero atribuye la causa a la mala alimentación, clima, exceso de trabajo, virus, etc.'),
            (2, '2.Niega que esté enfermo'),
            ),
        widget = forms.RadioSelect,
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
        widget = forms.RadioSelect(),
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
        widget = forms.RadioSelect(),
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
        widget = forms.RadioSelect(),
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
        widget = forms.RadioSelect(),
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
        widget = forms.RadioSelect(),
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
        widget = forms.RadioSelect(),
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
        widget = forms.RadioSelect(),
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
        widget = forms.RadioSelect(),
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
        widget = forms.RadioSelect(),
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
        widget = forms.RadioSelect(),
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
    	(1, '1.Ausente'),
    	(2, '2.Mínimo'),
    	(3, '3.Ligero'),
    	(4, '4.Moderado'),
        (5, '5.Moderado severo'),
        (6, '6.Severo'),
        (7, '7.Extremo'),
        )
    class Meta:
        model = Panss
        fields = '__all__'
    item_p01 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='1.- Delirios.',
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_p02 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='2.- Desorganización conceptual.',
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_p03 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='3.- Conducta alucinatoria.',
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_p04 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='4.- Exitación.',
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_p05 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='5.- Grandiosidad.',
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_p06 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='6.- Suspicacia / Perjuicio.',
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_p07 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='7.- Hostilidad.',
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )

    item_n01 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='1.- Embotamiento afectivo.',
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_n02 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='2.- Retracción emocional.',
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_n03 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='3.- Pobre relación.',
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_n04 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='4.- Retracción social, apatía pasiva.',
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_n05 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='5.- Dificultad de pensamiento abstracto.',
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_n06 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='6.- Falta de espontaneidad y fluidez de la conversación.',
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_n07 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='7.- Pensamiento estereotipado',
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )

    item_g01 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='1.- Preocupaciones somáticas.',
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_g02 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='2.- Ansiedad.',
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_g03 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='3.- Sentimientos de culpa.',
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_g04 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='4.- Tensión motora.',
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_g05 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='5.- Manierismos y posturas.',
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_g06 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='6.- Depresión.',
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_g07 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='7.- Retardo motor',
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_g08 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='8.- Falta de colaboración.',
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_g09 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='9.- Inusuales contenidos del pensamiento.',
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_g10 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='10.- Desorientación.',
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_g11 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='11.- Atención deficiente.',
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_g12 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='12.- Ausencia de juicio e introspección.',
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_g13 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='13.- Trastorno de la volición.',
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_g14 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='14.- Control deficiente de impulsos.',
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_g15 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='15.- Preocupación.',
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_g16 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='16.- Evitación social activa',
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
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
        widget = forms.RadioSelect,
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
        widget = forms.RadioSelect(),
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
        widget = forms.RadioSelect(),
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
        widget = forms.RadioSelect(),
        )
    item_05 = forms.ChoiceField(
        label = '5.- Irritabilidad',
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
        widget = forms.RadioSelect(),
        )

    item_06 = forms.ChoiceField(
        label = '6.- Expresión verbal',
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
        widget = forms.RadioSelect(),
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
        widget = forms.RadioSelect(),
        )
    item_08 = forms.ChoiceField(
        label = '8.- Trastornos del contenido del pensamiento',
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
        widget = forms.RadioSelect(),
        )
    item_09 = forms.ChoiceField(
        label = '9.- Agresividad',
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
        widget = forms.RadioSelect(),
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
        widget = forms.RadioSelect(),
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
        widget = forms.RadioSelect(),
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
    class Meta:
        model = Who_das
        fields = '__all__'
        widgets = {
            'd1_1': forms.RadioSelect(renderer=HorizRadioRenderer),
            'd1_2': forms.RadioSelect(renderer=HorizRadioRenderer),
            'd1_3': forms.RadioSelect(renderer=HorizRadioRenderer),
            'd1_4': forms.RadioSelect(renderer=HorizRadioRenderer),
            'd1_5': forms.RadioSelect(renderer=HorizRadioRenderer),
            'd1_6': forms.RadioSelect(renderer=HorizRadioRenderer),
            'd2_1': forms.RadioSelect(renderer=HorizRadioRenderer),
            'd2_2': forms.RadioSelect(renderer=HorizRadioRenderer),
            'd2_3': forms.RadioSelect(renderer=HorizRadioRenderer),
            'd2_4': forms.RadioSelect(renderer=HorizRadioRenderer),
            'd2_5': forms.RadioSelect(renderer=HorizRadioRenderer),
            'd3_1': forms.RadioSelect(renderer=HorizRadioRenderer),
            'd3_2': forms.RadioSelect(renderer=HorizRadioRenderer),
            'd3_3': forms.RadioSelect(renderer=HorizRadioRenderer),
            'd3_4': forms.RadioSelect(renderer=HorizRadioRenderer),
            'd4_1': forms.RadioSelect(renderer=HorizRadioRenderer),
            'd4_2': forms.RadioSelect(renderer=HorizRadioRenderer),
            'd4_3': forms.RadioSelect(renderer=HorizRadioRenderer),
            'd4_4': forms.RadioSelect(renderer=HorizRadioRenderer),
            'd4_5': forms.RadioSelect(renderer=HorizRadioRenderer),
            'd5_1': forms.RadioSelect(renderer=HorizRadioRenderer),
            'd5_2': forms.RadioSelect(renderer=HorizRadioRenderer),
            'd5_3': forms.RadioSelect(renderer=HorizRadioRenderer),
            'd5_4': forms.RadioSelect(renderer=HorizRadioRenderer),
            'd5_5': forms.RadioSelect(renderer=HorizRadioRenderer),
            'd5_6': forms.RadioSelect(renderer=HorizRadioRenderer),
            'd5_7': forms.RadioSelect(renderer=HorizRadioRenderer),
            'd5_8': forms.RadioSelect(renderer=HorizRadioRenderer),
            'd6_1': forms.RadioSelect(renderer=HorizRadioRenderer),
            'd6_2': forms.RadioSelect(renderer=HorizRadioRenderer),
            'd6_3': forms.RadioSelect(renderer=HorizRadioRenderer),
            'd6_4': forms.RadioSelect(renderer=HorizRadioRenderer),
            'd6_5': forms.RadioSelect(renderer=HorizRadioRenderer),
            'd6_6': forms.RadioSelect(renderer=HorizRadioRenderer),
            'd6_7': forms.RadioSelect(renderer=HorizRadioRenderer),
            'd6_8': forms.RadioSelect(renderer=HorizRadioRenderer),
        }
        
   


# 	########    ###    ########  #### ########
# 	     ##    ## ##   ##     ##  ##     ##
# 	    ##    ##   ##  ##     ##  ##     ##
# 	   ##    ##     ## ########   ##     ##
# 	  ##     ######### ##   ##    ##     ##
# 	 ##      ##     ## ##    ##   ##     ##
# 	######## ##     ## ##     ## ####    ##
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
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_02 = forms.ChoiceField(
        label = '2.- ¿Siente que debido al tiempo que dedica a su familiar ya no dispone de tiempo suficiente para usted?',
        choices = LIKERT_ZARIT,
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_03 = forms.ChoiceField(
        label = '3.- ¿Se siente tenso cuando tiene que cuidar a su familiar y atender además otras responsabilidades?',
        choices = LIKERT_ZARIT,
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_04 = forms.ChoiceField(
        label = '4.- ¿Se siente avergonzado por la conducta de su familiar?',
        choices = LIKERT_ZARIT,
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_05 = forms.ChoiceField(
        label = '5.- ¿Se siente enfadado cuando está cerca de su familiar?',
        choices = LIKERT_ZARIT,
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_06 = forms.ChoiceField(
        label = '6.- ¿Cree que la situación actual afecta de manera negativa a su relación con amigos y otros miembros de su familia?',
        choices = LIKERT_ZARIT,
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_07 = forms.ChoiceField(
        label = '7.- ¿Siente temor por el futuro que le espera a su familiar?',
        choices = LIKERT_ZARIT,
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_08 = forms.ChoiceField(
        label = '8.- ¿Siente que su familiar depende de usted?',
        choices = LIKERT_ZARIT,
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_09 = forms.ChoiceField(
        label = '9.- ¿Se siente agobiado cuando tiene que estar junto a su familiar?',
        choices = LIKERT_ZARIT,
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_10 = forms.ChoiceField(
        label = '10.- ¿Siente que su salud se ha resentido por cuidar a su familiar?',
        choices = LIKERT_ZARIT,
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_11 = forms.ChoiceField(
        label = '11.- ¿Siente que no tiene la vida privada que desearía debido a su familiar?',
        choices = LIKERT_ZARIT,
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_12 = forms.ChoiceField(
        label = '12.- ¿Cree que su vida social se ha visto afectada por tener que cuidar de su familiar?',
        choices = LIKERT_ZARIT,
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_13 = forms.ChoiceField(
        label = '13.- ¿Se siente incómodo para invitar amigos a casa, a causa de su familiar?',
        choices = LIKERT_ZARIT,
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_14 = forms.ChoiceField(
        label = '14.- ¿Cree que su familiar espera que usted le cuide, como si fuera la única persona con la que puede contar?',
        choices = LIKERT_ZARIT,
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_15 = forms.ChoiceField(
        label = '15.- ¿Cree que no dispone de dinero suficiente para cuidar a su familiar además de sus otros gastos?',
        choices = LIKERT_ZARIT,
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_16 = forms.ChoiceField(
        label = '16.- ¿Siente que será incapaz de cuidar a su familiar por mucho más tiempo?',
        choices = LIKERT_ZARIT,
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_17 = forms.ChoiceField(
        label = '17.- ¿Siente que ha perdido el control sobre su vida desde que la enfermedad de su familiar se manifestó?',
        choices = LIKERT_ZARIT,
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_18 = forms.ChoiceField(
        label = '18.- ¿Desearía poder encargar el cuidado de su familiar a otras personas?',
        choices = LIKERT_ZARIT,
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_19 = forms.ChoiceField(
        label = '19.- ¿Se siente inseguro acerca de lo que debe hacer con su familiar?',
        choices = LIKERT_ZARIT,
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_20 = forms.ChoiceField(
        label = '20.- ¿Siente que debería hacer más de lo que hace por su familiar?',
        choices = LIKERT_ZARIT,
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_21 = forms.ChoiceField(
        label = '21.- ¿Cree que podría cuidar de su familiar mejor de lo que lo hace?',
        choices = LIKERT_ZARIT,
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )
    item_22 = forms.ChoiceField(
        label = '22.- En general: ¿Se siente muy sobrecargado por tener que cuidar de su familia',
        choices = LIKERT_ZARIT,
        widget = forms.RadioSelect(renderer=HorizRadioRenderer),
        )