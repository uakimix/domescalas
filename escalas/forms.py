# forms.py
from django import forms
from escalas.models import *

CHOICES = (
    (0, 'No'),
    (1, 'Si'),
    )
LIKERT4 = (
        (4, 'Casi Siempre'),
        (3, 'A menudo'),
        (2, 'A veces'),
        (1, 'Nunca'),
        )
LIKERT6 = (
        (6, 'Muy Grave'),
        (5, 'Grave'),
        (4, 'Bastante acentuado'),
        (3, 'Moderado'),
        (2, 'Leve'),
        (1, 'Muy leve'),
        (0, 'Ausente'),
        )
VARFORM = forms.Select

#     ########  ##       ##     ## ########  ######  ##     ## #### ##    ##
#     ##     ## ##       ##     ##    ##    ##    ## ##     ##  ##  ##   ##
#     ##     ## ##       ##     ##    ##    ##       ##     ##  ##  ##  ##
#     ########  ##       ##     ##    ##    ##       #########  ##  #####
#     ##        ##       ##     ##    ##    ##       ##     ##  ##  ##  ##
#     ##        ##       ##     ##    ##    ##    ## ##     ##  ##  ##   ##
#     ##        ########  #######     ##     ######  ##     ## #### ##    ##

class Plutchik_sAdminForm(forms.ModelForm):
    class Meta:
        model = Plutchik_s
        fields = '__all__' 
    item_01 = forms.ChoiceField(
        label='1.- ¿Toma de forma habitual algún medicamento como aspirinas o pastillas para dormir?',
        choices = CHOICES,
        widget = VARFORM,
        )
    item_02 = forms.ChoiceField(
        label='2.- ¿Tiene dificultades para conciliar el sueño?',
        choices = CHOICES,
        widget = VARFORM,
        )
    item_03 = forms.ChoiceField(
        label='3.- ¿A veces nota que podría perder el control sobre sí mismo/a?',
        choices = CHOICES,
        widget = VARFORM,
        )
    item_04 = forms.ChoiceField(
        label='4.- ¿Tiene poco interés en relacionarse con la gente?',
        choices = CHOICES,
        widget = VARFORM,
        )
    item_05 = forms.ChoiceField(
        label='5.- ¿Ve su futuro con más pesimismo que optimismo?',
        choices = CHOICES,
        widget = VARFORM,
        )
    item_06 = forms.ChoiceField(
        label='6.- ¿Se ha sentido alguna vez inútil o inservible?',
        choices = CHOICES,
        widget = VARFORM,
        )
    item_07 = forms.ChoiceField(
        label='7.- ¿Ve su futuro sin ninguna esperanza?',
        choices = CHOICES,
        widget = VARFORM,
        )
    item_08 = forms.ChoiceField(
        label='8.- ¿Se ha sentido alguna vez fracasado/a, que sólo quería meterse en la cama y abandonarlo todo?',
        choices = CHOICES,
        widget = VARFORM,
        )
    item_09 = forms.ChoiceField(
        label='9.- ¿Está deprimido/a ahora?',
        choices = CHOICES,
        widget = VARFORM,
        )
    item_10 = forms.ChoiceField(
        label='10.- ¿Está vd. separado/a, divorciado/a o viudo/a?',
        choices = CHOICES,
        widget = VARFORM,
        )
    item_11 = forms.ChoiceField(
        label='11.- ¿Sabe si alguien de su familia ha intentado suicidarse alguna vez?',
        choices = CHOICES,
        widget = VARFORM,
        )
    item_12 = forms.ChoiceField(
        label='12.- ¿Alguna vez se ha sentido tan enfadado/a que habría sido capaz de matar a alguien?',
        choices = CHOICES,
        widget = VARFORM,
        )
    item_13 = forms.ChoiceField(
        label='13.- ¿Ha pensado alguna vez en suicidarse?',
        choices = CHOICES,
        widget = VARFORM,
        )
    item_14 = forms.ChoiceField(
        label='14.- ¿Le ha comentado a alguien, en alguna ocasión, que quería suici- darse?',
        choices = CHOICES,
        widget = VARFORM,
        )
    item_15 = forms.ChoiceField(
        label='15.- ¿Ha intentado alguna vez quitarse la vida?',
        choices = CHOICES,
        widget = VARFORM,
        )

class Plutchik_vAdminForm(forms.ModelForm):
    class Meta:
        model = Plutchik_v
        fields = '__all__'

    item_01 = forms.ChoiceField(
        choices=LIKERT4,
        label='1.- ¿Se enfada con facilidad?',
        widget = VARFORM,
        )
    item_02 = forms.ChoiceField(
        choices=LIKERT4,
        label='2.- ¿Se enfada continuamente con la gente ?',
        widget = VARFORM,
        )
    item_03 = forms.ChoiceField(
        choices=LIKERT4,
        label='3.- ¿Se enfurece sin motivo?',
        widget = VARFORM,
        )
    item_04 = forms.ChoiceField(
        choices=LIKERT4,
        label='4.- Cuando se enfada, ¿Coge un arma?',
        widget = VARFORM,
        )
    item_05 = forms.ChoiceField(
        choices=LIKERT4,
        label='5.- ¿Ha lastimado alguna vez a alguien en una pelea?',
        widget = VARFORM,
        )
    item_06 = forms.ChoiceField(
        choices=LIKERT4,
        label='6.- ¿Ha pegado o atacado alguna vez a algún familiar?',
        widget = VARFORM,
        )
    item_07 = forms.ChoiceField(
        choices=LIKERT4,
        label='7.- ¿Ha pegado o atacado algunas vez a alquien que no sea famililar suyo?',
        widget = VARFORM,
        )
    item_08 = forms.ChoiceField(
        choices=LIKERT4,
        label='8.- ¿Ha usado alguna vez un objeto para agredir a alguien?',
        widget = VARFORM,
        )
    item_09 = forms.ChoiceField(
        choices=LIKERT4,
        label='9.- ¿Podría conseguir un arma con facilidad?',
        widget = VARFORM,
        )
    item_10 = forms.ChoiceField(
        choices=LIKERT4,
        label='10.- ¿Cuantas veces ha sido vd. detenido por delitos no violentos como irse de un tienda o falsificar documentos?',
        widget = VARFORM,
        )
    item_11 = forms.ChoiceField(
        choices=LIKERT4,
        label='11.- ¿Cuántas veces ha sido vd. detenido por delitos como robo a mano armada o agresión violenta?',
        widget = VARFORM,
        )
    item_12 = forms.ChoiceField(
        choices=CHOICES,
        label = '12.- ¿Guarda o colecciona armas en su casa y sabe cómo utilizarlas?',
        widget = VARFORM,
        )

#      #######   #######
#     ##     ## ##     ##
#     ##     ## ##     ##
#     ##     ##  #######
#     ##  ## ## ##     ##
#     ##    ##  ##     ##
#      ##### ##  #######
#
class SatisfaccionAdminForm(forms.ModelForm):
    class Meta:
        model = Satisfaccion
        fields = '__all__'
    item_1 = forms.ChoiceField(
        label = '1.- ¿Cómo evalúa la calidad de los servicios que ha recibido?',
        widget = VARFORM,
        choices=(
            (4, 'Excelente'),
            (3, 'Buena'),
            (2, 'Regular'),
            (1, 'Mala'),
            ),
        )
    item_2 = forms.ChoiceField(
        label = '2.- ¿Recibió la clase de servicio que usted requería?',
        widget = VARFORM,
        choices=(
            (4, 'No definitivamente'),
            (3, 'En muy pocos casos'),
            (2, 'Si en general'),
            (1, 'Si definitívamente'),
            ),
        )
    item_3 = forms.ChoiceField(
        label = '3.- ¿Hasta qué punto ha ayudado nuestro programa a solucinar sus probelmas?',
        widget = VARFORM,
        choices= (
            (4, 'En casi todos'),
            (3, 'En la mayor parte de'),
            (2, 'Sólo en algunos'),
            (1, 'En ninguno'),
            ),
        )
    item_4 = forms.ChoiceField(
        label = '4.- ¿Si un/a amigo/a estuviera en necesidad de ayuda similar, le recomendaría nuestro programa?',
        widget = VARFORM,
        choices=(
            (4, 'No definitivamente'),
            (3, 'No, creo que no'),
            (2, 'Si, creo que si'),
            (1, 'Si definitivamente'),
            ),
        )
    item_5 = forms.ChoiceField(
        label = '5.- ¿Cómo de satisfecho/a está usted con la cantidad de ayuda que ha recibido?',
        widget = VARFORM,
        choices=(
            (4, 'Nada satisfecho/a'),
            (3, 'Indiferente o moderadamente no satisfecho/a'),
            (2, 'Moderadamente satisfecho/a'),
            (1, 'Muy satisfecho/a'),
            ),
        )
    item_6 = forms.ChoiceField(
        label = '6.- ¿Los servicios que ha recibido le han ayudado a enfrentarse mejor a sus problemas?',
        widget = VARFORM,
        choices=(
            (4, 'Si me ayudaron mucho'),
            (3, 'Si me ayudaron algo'),
            (2, 'No, realmente no me ayudaron'),
            (1, 'No, parecían poner las cosas peor'),
            ),
        )
    item_7 = forms.ChoiceField(
        label = '7.- ¿En general, cómo de satisfecho/a está usted con los servicios que ha recibido?',
        widget = VARFORM,
        choices=(
            (4, 'Muy satisfecho/a'),
            (3, 'Moderadamente satisfecho/a'),
            (2, 'Algo insatisfecho/a'),
            (1, 'Muy insatisfecho'),
            ),
        )
    item_8 = forms.ChoiceField(
        label = '8.- ¿Si necesitara ayuda otra vez , volvería a nuestro programa?',
        widget = VARFORM,
        choices=(
            (4, 'No definitívamente'),
            (3, 'No posiblemente'),
            (2, 'Si, creo que si'),
            (1, 'Si con seguridad'),
            ),
        )
    item_9 = forms.CharField(
        label= '9.- Lo que mas me ha gustado de la atencion que he recibido ha sido',
        widget = forms.Textarea,
        )
    item_10 = forms.CharField(
        label= '10.- Creo que se tendría que mejorar',
        widget = forms.Textarea,
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

LIKERT_PANSS = (
        (7, 'Extremo'),
        (6, 'Severo'),
        (5, 'Moderado severo'),
        (4, 'Moderado'),
        (3, 'Ligero'),
        (2, 'Mínimo'),
        (1, 'Ausente'),
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
            (0, 'Ausente'),
            (1, 'Posible o moderada, sólo cuando se le pregunta'),
            (2, 'Clara aunque subjetiva y apropiada al contenido: optimista, seguro de sí mismo/a, alegre'),
            (3, 'Elevada e inapropiada'),
            (4, 'Claramente eufórico/a, risa inadecuada, canta durante la entrevista, etc.'),
            ),
        widget = VARFORM,
        )
    item_02 = forms.ChoiceField(
        label = '2.- Hiperactividad',
        choices = (
            (0, 'Ausente'),
            (1, 'Subjetivamente aumentada'),
            (2, 'Vigoroso/a, hipergestual'),
            (3, 'Energía excesiva, hiperactividad fluctuante, inquietud (puede ser calmado/a)'),
            (4, 'Agitación o hiperactividad constante (no puede ser calmado/a)'),
            ),
        widget = VARFORM,
        )
    item_03 = forms.ChoiceField(
        label = '3.- Impulso sexual',
        choices = (
            (0, 'Normal, no aumentado'),
            (1, 'Posible o moderadamente aumentado'),
            (2, 'Claro aumento al preguntar'),
            (3, 'Referido como elevado de forma espontánea, contenido sexual del discurso, preocupación por temas sexuales'),
            (4, 'Actos o incitaciones sexuales evidentes (hacia pacientes, personal o entrevistador)'),
            ),
        widget = VARFORM,
        )
    item_04 = forms.ChoiceField(
        label = '4.- Sueño',
        choices = (
            (0, 'No reducido'),
            (1, 'Disminución en menos de 1 ,hora'),
            (2, 'Disminución en más de 1 hora'),
            (3, 'Refiere disminución de la necesidad de dormir'),
            (4, 'Niega necesidad de dormir'),
            ),
        widget = VARFORM,
        )
    item_05 = forms.ChoiceField(
        label = '5.- Irritabilidad',
        choices = (
            (0, 'Ausente'),
            (2, 'Subjetivamente aumentada'),
            (4, 'Irritabilidad fluctuante durante la entrevista, episodios recientes de rabia o enfado'),
            (6, 'Predominantemente irritable durante la entrevista, brusco y cortante'),
            (8, 'Hostil, no colaborador/a, entrevista imposible'),
            ),
        widget = VARFORM,
        )

    item_06 = forms.ChoiceField(
        label = '6.- Expresión verbal',
        choices = (
            (0, 'No aumentada'),
            (2, 'Sensación de locuacidad'),
            (4, 'Aumentada de forma fluctuante, verborrea ocasional'),
            (6, 'Claramente aumentada en ritmo y cantidad, difícil de interrumpir, intrusiva'),
            (8, 'Verborrea ininterrumpible y continua'),
            ),
        widget = VARFORM,
        )
    item_07 = forms.ChoiceField(
        label = '7.- Trastornos del curso del pensamiento y el lenguaje',
        choices = (
            (0, 'Ausentes'),
            (1, 'Circunstancialidad, distraibilidad moderada, aceleración del pensamiento'),
            (2, 'Distraibilidad clara, descarrilamiento, taquipsiquia'),
            (3, 'Fuga de ideas, tangencialidad, discurso difícil de seguir, rimas, ecolalia'),
            (4, 'Incoherencia, ininteligibilidad, comunicación imposible'),
            ),
        widget = VARFORM,
        )
    item_08 = forms.ChoiceField(
        label = '8.- Trastornos del contenido del pensamiento',
        choices = (
            (0, 'Ausentes'),
            (2, 'Planes discutibles, nuevos intereses'),
            (4, 'Proyectos especiales, misticismo'),
            (6, 'Ideas grandiosas o paranoides, ideas de referencia'),
            (8, 'Delirios, alucinaciones'),
            ),
        widget = VARFORM,
        )
    item_09 = forms.ChoiceField(
        label = '9.- Agresividad',
        choices = (
            (0, 'Ausente, colaborador/a'),
            (2, 'Sarcástico/a, enfático/a, lacónico/a'),
            (4, 'Querulante, pone en guardia'),
            (6, 'Amenaza al entrevistador, habla a gritos, entrevista difícil'),
            (8, 'Claramente agresivo/a, destructivo/a, entrevista imposible'),
            ),
        widget = VARFORM,
        )
    item_10 = forms.ChoiceField(
        label = '10.- Apariencia',
        choices = (
            (0, 'Higiene e indumentaria apropiada '),
            (1, 'Ligeramente descuidada'),
            (2, 'Mal arreglado/a, moderadamente despeinado/a, indumentaria sobrecargada'),
            (3, 'Despeinado/a, semidesnudo/a, maquillaje llamativo'),
            (4, 'Completamente desaseado/a, adornado/a, indumentaria extravagante'),
            ),
        widget = VARFORM,
        )
    item_11 = forms.ChoiceField(
        label = '11.- Conciencia de enfermedad',
        choices = (
            (0, 'Presente, admite la enfermedad, acepta tratamiento'),
            (1, 'Según él/ella, posiblemente enfermo/a'),
            (2, 'Admite cambio de conducta, pero niega enfermedad'),
            (3, 'Admite posible cambio de conducta, niega enfermedad'),
            (4, 'Niega cualquier cambio de conduct'),
            ),
        widget = VARFORM,
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
            (0, 'Ausente'),
            (1, 'Estas sensaciones se indican solamente al ser preguntado'),
            (2, 'Estas sensaciones se relatan oral y espontáneamente'),
            (3, 'Sensaciones no comunicadas verbalmente, es decir, por la expresión facial, la postura, la voz y la tendencia al llanto'),
            (4, 'El paciente manifiesta estas sensaciones en su comunicación verbal y no verbal de forma espontánea'),
            ),
        widget = VARFORM,
        )
    item_02 = forms.ChoiceField(
        label = '2.- Sensación de culpabilidad',
        choices = (
            (0, 'Ausente'),
            (1, 'Se culpa a si mismos, cree haber decepcionado a la gente'),
            (2, 'Ideas de culpabilidad, o meditación sobre errores pasados o malas acciones'),
            (3, 'La enfermedad actual es un castigo. Ideas delirantes de culpabilidad'),
            (4, ' Oye  voces  acusatorias  o  de  denuncia  y/o  experiemtna  alucinaciones  visuales amenazadoras'),
            ),
        widget = VARFORM,
        )
    item_03 = forms.ChoiceField(
        label = '3.- Suicidio',
        choices = (
            (0, 'Ausente'),
            (1, 'Le parece que la vida no merece la pena ser vivida'),
            (2, 'Desearía estar muerto o tiene pensamientos sobre la posibilidad de morirse'),
            (3, 'Ideas de suicidio o amenazas'),
            (4, ' Intentos de suicidio (cualuqier intento serio se califica 4)'),
            ),
        widget = VARFORM,
        )
    item_04 = forms.ChoiceField(
        label = '4.- Insomnio precoz',
        choices = (
            (0, 'Ausente'),
            (1, 'Dificultades ocasionales para dormirse, por ejemplo, más de media hora'),
            (2, 'Dificultades para dormirse cada noche'),
            ),
        widget = VARFORM,
        )
    item_05 = forms.ChoiceField(
        label = '5.- Insomnio medio',
        choices = (
            (0, 'Ausente'),
            (1, 'El paciente s queja de estar inquieto durante la noche'),
            (2, 'Está despierto durante la noche; medicación, etc.'),
            ),
        widget = VARFORM,
        )
    item_06 = forms.ChoiceField(
        label = '6.- Insomnio tardío',
        choices = (
            (0, 'Ausente'),
            (1, 'Se despierta a primeras horas de la madrugada pero vuelve a dormirse'),
            (2, 'No puede volver a dormirse si se levanta de la cama'),
            ),
        widget = VARFORM,
        )
    item_07 = forms.ChoiceField(
        label = '7.- Trabajo y actividades',
        choices = (
            (0, ' Ausente'),
            (1, 'Ideas  y  sentimientos  de  incapacidad.  Fatiga  o  debilidad  relcionadas  con  su actividad,trabajo o aficiones'),
            (2, 'Pérdida de interés en su actividad, aficiones, o trabajo, ,anifestado directamete por el enfermo o indirectamente por desatención, indecisión y vacilación'),
            (3, 'Disminución del tiempo dedicado a actividades o descenso en la productividad'),
            (4, 'Dejó de trabajar por la presente enfermedad'),
            ),
        widget = VARFORM,
        )
    item_08 = forms.ChoiceField(
        label = '8.- Inhibición',
        choices = (
            (0, 'Palabra y pensamiento normales'),
            (1, 'Ligero retras en el diálogo'),
            (2, 'Evidente retraso en el diálogo'),
            (3, 'Diálogo difícil'),
            (4, 'Torpeza absoluta'),
            ),
        widget = VARFORM,
        )
    item_09 = forms.ChoiceField(
        label = '9.- Agitación',
        choices = (
            (0, 'Ninguna'),
            (1, '“Juega” con sus manos, cabellos, etc.'),
            (2, 'Se retuerce las manos, se muerde las uñas, los labios, se tira de los cabellos, etc.'),
            ),
        widget = VARFORM,
        )
    item_10 = forms.ChoiceField(
        label = '10.- Ansiedad psíquica',
        choices = (
            (0, 'No hay dificultad'),
            (1, 'Tensión subjetiva e irritable'),
            (2, 'Preocupación por pequeñas cosas'),
            (3, 'Actitud aprensiva aparente en la expresión o en el habla'),
            (4, 'Terrores expresados sin preguntarle'),
            ),
        widget = VARFORM,
        )
    item_11 = forms.ChoiceField(
        label = '11.- Ansiedad somática',
        choices = (
            (0, 'Ausente'),
            (1, 'Ligera'),
            (2, 'Moderada'),
            (3, 'Grave'),
            (4, 'Incapacitante'),
            ),
        widget = VARFORM,
        )
    item_12 = forms.ChoiceField(
        label = '12.- Síntomas somáticos gastrointestinales',
        choices = (
            (0, 'Ninguno'),
            (1, 'Pérdida de apetito, pero come sin necesidad de que estimulen. Sensación de pesadez en el abdomen'),
            (2, 'Difucultad en comer si no se le insiste. Solicita o necesita laxantes o medicación intestinal para sus síntomas gastrointestinales'),
            ),
        widget = VARFORM,
        )
    item_13 = forms.ChoiceField(
        label = '13.- Síntomas somáticos generales',
        choices = (
            (0, 'Ninguno'),
            (1, 'Pesadez en las extremidades, espalda o cabeza. Dorsalgias, cefalalgias, algias musculares. Pérdida de energía y fatigabilidad'),
            (2, 'Cualquier síntoma bien definido'),
            ),
        widget = VARFORM,
        )
    item_14 = forms.ChoiceField(
        label = '14.- Síntomas genitales',
        choices = (
            (0, 'Ausente'),
            (1, 'Débil'),
            (2, 'Grave'),
            (3, 'Incapacitante'),
            ),
        widget = VARFORM,
        )
    item_15 = forms.ChoiceField(
        label = '15.- Hipocondría',
        choices = (
            (0, 'No la hay'),
            (1, 'Preocupado de sí mismo (corporalmente)'),
            (2, 'Preocupado por su sald'),
            (3, 'Se lamenta constantemente, solicita ayudas, etc.'),
            (4, 'Ideas delirantes hipocondríacas'),
            ),
        widget = VARFORM,
        )

    item_16 = forms.ChoiceField(
        label = '16.- Pérdida de peso',
        choices = (
            (0, 'No hay pérdida de peso'),
            (1, 'Probable pérdida de peso asociada con la enfermedad actual'),
            (2, 'Pérdida de peso definida (según el enfermo)'),
            ),
        widget = VARFORM,
        )

    item_17 = forms.ChoiceField(
        label = '17.- Insight (conciencia de enfermedad)',
        choices = (
            (0, 'Se da cuenta de que está deprimido y enfermo'),
            (1, 'Se da cuenta de sy enfermedad pero atribuye la causa a la mala alimentación, clima, exceso de trabajo, virus, etc.'),
            (2, 'Niega que esté enfermo'),
            ),
        widget = VARFORM,
        )