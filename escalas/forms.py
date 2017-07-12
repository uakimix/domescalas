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
            'icg_ge': forms.RadioSelect(renderer=HorizRadioRenderer)        ,
            'quien forms.RadioSelect(renderer=HorizRadioRenderer),_ge': forms.RadioSelect(renderer=HorizRadioRenderer),
            }
        labels = {
            'icg_ge': ('ICG Gravedad'),
            'quien_ge': ('Aplicada por:'),
            }
    	
class Icg_meAdminForm(forms.ModelForm):
    class Meta:
        model = Icg_me
        fields = '__all__'
        widgets = {
            'icg_me': forms.RadioSelect(renderer=HorizRadioRenderer),
            'quien_me': forms.RadioSelect(renderer=HorizRadioRenderer),
            }
        labels = {
            'icg_me': ('ICG Mejoría'),
            'quien_me': ('Aplicada por:'),
            }
    
    

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
        widgets = {
            'item_01': forms.RadioSelect(),
            'item_02': forms.RadioSelect(),
            'item_03': forms.RadioSelect(),
            'item_04': forms.RadioSelect(),
            'item_05': forms.RadioSelect(),
            'item_06': forms.RadioSelect(),
            'item_07': forms.RadioSelect(),
            'item_08': forms.RadioSelect(),
            'item_09': forms.RadioSelect(),
            'item_10': forms.RadioSelect(),
            'item_11': forms.RadioSelect(),
            'item_12': forms.RadioSelect(),
            'item_13': forms.RadioSelect(),
            'item_14': forms.RadioSelect(),
            'item_15': forms.RadioSelect(),
            'item_16': forms.RadioSelect(),
            'item_17': forms.RadioSelect(),
            }
        labels = {
            'item_01': ('01.- Humor deprimido'),
            'item_02': ('02.- Sensación de culpabilidad'),
            'item_03': ('03.- Suicidio'),
            'item_04': ('04.- Insomnio precoz'),
            'item_05': ('05.- Insomnio medio'),
            'item_06': ('06.- Insomnio tardío'),
            'item_07': ('07.- Trabajo y actividades'),
            'item_08': ('08.- Inhibición'),
            'item_09': ('09.- Agitación'),
            'item_10': ('10.- Ansiedad psíquica'),
            'item_11': ('11.- Ansiedad somática'),
            'item_12': ('12.- Síntomas somáticos gastrointestinales'),
            'item_13': ('13.- Síntomas somáticos generales'),
            'item_14': ('14.- Síntomas genitales'),
            'item_15': ('15.- Hipocondría'),
            'item_16': ('16.- Pérdida de peso'),
            'item_17': ('17.- Insight (conciencia de enfermedad)'),
            }
    

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
        widgets = {
            'item_01': forms.RadioSelect(),
            'item_02': forms.RadioSelect(),
            'item_03': forms.RadioSelect(),
            'item_04': forms.RadioSelect(),
            'item_05': forms.RadioSelect(),
            'item_06': forms.RadioSelect(),
            'item_07': forms.RadioSelect(),
            'item_08': forms.RadioSelect(),
            'item_09': forms.RadioSelect(),
            'item_10': forms.RadioSelect(),
            }
        labels = {
            'item_01': ('1.- Tristeza observada'),
            'item_02': ('2.- Tristeza declarada por el paciente'),
            'item_03': ('3.- Tensión interna'),
            'item_04': ('4.- Sueño reducido'),
            'item_05': ('5.- Apetito reducido'),
            'item_06': ('6. Dificultades para concentrarse'),
            'item_07': ('7. Lasitud'),
            'item_08': ('8. Incapacidad para sentir'),
            'item_09': ('9. Pensamientos pesimistas'),
            'item_10': ('10. Pensamientos suicidas'),
            }
    

#     ########     ###    ##    ##  ######   ######
#     ##     ##   ## ##   ###   ## ##    ## ##    ##
#     ##     ##  ##   ##  ####  ## ##       ##
#     ########  ##     ## ## ## ##  ######   ######
#     ##        ######### ##  ####       ##       ##
#     ##        ##     ## ##   ### ##    ## ##    ##
#     ##        ##     ## ##    ##  ######   ######
#

class PanssAdminForm(forms.ModelForm):
    
    class Meta:
        model = Panss
        fields = '__all__'
        
        widgets = {
            'item_p01': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_p02': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_p03': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_p04': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_p05': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_p06': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_p07': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_n01': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_n02': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_n03': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_n04': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_n05': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_n06': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_n07': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_g01': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_g02': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_g03': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_g04': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_g05': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_g06': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_g07': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_g08': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_g09': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_g10': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_g11': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_g12': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_g13': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_g14': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_g15': forms.RadioSelect(renderer=HorizRadioRenderer),
            'item_g16': forms.RadioSelect(renderer=HorizRadioRenderer),
            }
        labels = {
            'item_p01': ('1.- Delirios.'),
            'item_p02': ('2.- Desorganización conceptual.'),
            'item_p03': ('3.- Conducta alucinatoria.'),
            'item_p04': ('4.- Exitación.'),
            'item_p05': ('5.- Grandiosidad.'),
            'item_p06': ('6.- Suspicacia / Perjuicio.'),
            'item_p07': ('7.- Hostilidad.'),
            'item_n01': ('1.- Embotamiento afectivo.'),
            'item_n02': ('2.- Retracción emocional.'),
            'item_n03': ('3.- Pobre relación.'),
            'item_n04': ('4.- Retracción social, apatía pasiva.'),
            'item_n05': ('5.- Dificultad de pensamiento abstracto.'),
            'item_n06': ('6.- Falta de espontaneidad y fluidez de la conversación.'),
            'item_n07': ('7.- Pensamiento estereotipado'),
            'item_g01': ('1.- Preocupaciones somáticas.'),
            'item_g02': ('2.- Ansiedad.'),
            'item_g03': ('3.- Sentimientos de culpa.'),
            'item_g04': ('4.- Tensión motora.'),
            'item_g05': ('5.- Manierismos y posturas.'),
            'item_g06': ('6.- Depresión.'),
            'item_g07': ('7.- Retardo motor'),
            'item_g08': ('8.- Falta de colaboración.'),
            'item_g09': ('9.- Inusuales contenidos del pensamiento.'),
            'item_g10': ('10.- Desorientación.'),
            'item_g11': ('11.- Atención deficiente.'),
            'item_g12': ('12.- Ausencia de juicio e introspección.'),
            'item_g13': ('13.- Trastorno de la volición.'),
            'item_g14': ('14.- Control deficiente de impulsos.'),
            'item_g15': ('15.- Preocupación.'),
            'item_g16': ('16.- Evitación social activa'),
        }

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
        widgets = {
            'item_01': forms.RadioSelect(),
            'item_02': forms.RadioSelect(),
            'item_03': forms.RadioSelect(),
            'item_04': forms.RadioSelect(),
            'item_05': forms.RadioSelect(),
            'item_06': forms.RadioSelect(),
            'item_07': forms.RadioSelect(),
            'item_08': forms.RadioSelect(),
            'item_09': forms.RadioSelect(),
            'item_10': forms.RadioSelect(),
            'item_11': forms.RadioSelect(),
        }
        labels= {
            'item_01': ('1.- Euforia'),
            'item_02': ('2.- Hiperactividad'),
            'item_03': ('3.- Impulso sexual'),
            'item_04': ('4.- Sueño'),
            'item_05': ('5.- Irritabilidad'),
            'item_06': ('6.- Expresión verbal'),
            'item_07': ('7.- Trastornos del curso del pensamiento y el lenguaje'),
            'item_08': ('8.- Trastornos del contenido del pensamiento'),
            'item_09': ('9.- Agresividad'),
            'item_10': ('10.- Apariencia'),
            'item_11': ('11.- Conciencia de enfermedad'),
            }
            
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


class ZaritAdminForm(forms.ModelForm):
    class Meta:
        model = Zarit
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
            'item_01': ('1.- ¿Siente que su familiar solicita más ayuda de la que realmente necesita?'),
            'item_02': ('2.- ¿Siente que debido al tiempo que dedica a su familiar ya no dispone de tiempo suficiente para usted?'),
            'item_03': ('3.- ¿Se siente tenso cuando tiene que cuidar a su familiar y atender además otras responsabilidades?'),
            'item_04': ('4.- ¿Se siente avergonzado por la conducta de su familiar?'),
            'item_05': ('5.- ¿Se siente enfadado cuando está cerca de su familiar?'),
            'item_06': ('6.- ¿Cree que la situación actual afecta de manera negativa a su relación con amigos y otros miembros de su familia?'),
            'item_07': ('7.- ¿Siente temor por el futuro que le espera a su familiar?'),
            'item_08': ('8.- ¿Siente que su familiar depende de usted?'),
            'item_09': ('9.- ¿Se siente agobiado cuando tiene que estar junto a su familiar?'),
            'item_10': ('10.- ¿Siente que su salud se ha resentido por cuidar a su familiar?'),
            'item_11': ('11.- ¿Siente que no tiene la vida privada que desearía debido a su familiar?'),
            'item_12': ('12.- ¿Cree que su vida social se ha visto afectada por tener que cuidar de su familiar?'),
            'item_13': ('13.- ¿Se siente incómodo para invitar amigos a casa, a causa de su familiar?'),
            'item_14': ('14.- ¿Cree que su familiar espera que usted le cuide, como si fuera la única persona con la que puede contar?'),
            'item_15': ('15.- ¿Cree que no dispone de dinero suficiente para cuidar a su familiar además de sus otros gastos?'),
            'item_16': ('16.- ¿Siente que será incapaz de cuidar a su familiar por mucho más tiempo?'),
            'item_17': ('17.- ¿Siente que ha perdido el control sobre su vida desde que la enfermedad de su familiar se manifestó?'),
            'item_18': ('18.- ¿Desearía poder encargar el cuidado de su familiar a otras personas?'),
            'item_19': ('19.- ¿Se siente inseguro acerca de lo que debe hacer con su familiar?'),
            'item_20': ('20.- ¿Siente que debería hacer más de lo que hace por su familiar?'),
            'item_21': ('21.- ¿Cree que podría cuidar de su familiar mejor de lo que lo hace?'),
            'item_22': ('22.- En general: ¿Se siente muy sobrecargado por tener que cuidar de su familia'),
            }