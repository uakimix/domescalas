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
        label='¿Toma de forma habitual algún medicamento como aspirinas o pastillas para dormir?',
        choices = CHOICES,
        widget = forms.RadioSelect,
        )
    item_02 = forms.ChoiceField(
        label='¿Tiene dificultades para conciliar el sueño?',
        choices = CHOICES,
        widget = forms.RadioSelect,
        )
    item_03 = forms.ChoiceField(
        label='¿A veces nota que podría perder el control sobre sí mismo/a?',
        choices = CHOICES,
        widget = forms.RadioSelect,
        )
    item_04 = forms.ChoiceField(
        label='¿Tiene poco interés en relacionarse con la gente?',
        choices = CHOICES,
        widget = forms.RadioSelect,
        )
    item_05 = forms.ChoiceField(
        label='¿Ve su futuro con más pesimismo que optimismo?',
        choices = CHOICES,
        widget = forms.RadioSelect,
        )
    item_06 = forms.ChoiceField(
        label='¿Se ha sentido alguna vez inútil o inservible?',
        choices = CHOICES,
        widget = forms.RadioSelect,
        )
    item_07 = forms.ChoiceField(
        label='¿Ve su futuro sin ninguna esperanza?',
        choices = CHOICES,
        widget = forms.RadioSelect,
        )
    item_08 = forms.ChoiceField(
        label='¿Se ha sentido alguna vez fracasado/a, que sólo quería meterse en la cama y abandonarlo todo?',
        choices = CHOICES,
        widget = forms.RadioSelect,
        )
    item_09 = forms.ChoiceField(
        label='¿Está deprimido/a ahora?',
        choices = CHOICES,
        widget = forms.RadioSelect,
        )
    item_10 = forms.ChoiceField(
        label='¿Está vd. separado/a, divorciado/a o viudo/a?',
        choices = CHOICES,
        widget = forms.RadioSelect,
        )
    item_11 = forms.ChoiceField(
        label='¿Sabe si alguien de su familia ha intentado suicidarse alguna vez?',
        choices = CHOICES,
        widget = forms.RadioSelect,
        )
    item_12 = forms.ChoiceField(
        label='¿Alguna vez se ha sentido tan enfadado/a que habría sido capaz de matar a alguien?',
        choices = CHOICES,
        widget = forms.RadioSelect,
        )
    item_13 = forms.ChoiceField(
        label='¿Ha pensado alguna vez en suicidarse?',
        choices = CHOICES,
        widget = forms.RadioSelect,
        )
    item_14 = forms.ChoiceField(
        label='¿Le ha comentado a alguien, en alguna ocasión, que quería suici- darse?',
        choices = CHOICES,
        widget = forms.RadioSelect,
        )
    item_15 = forms.ChoiceField(
        label='¿Ha intentado alguna vez quitarse la vida?',
        choices = CHOICES,
        widget = forms.RadioSelect,
        )

class Plutchik_vAdminForm(forms.ModelForm):
    class Meta:
        model = Plutchik_v
        fields = '__all__'

    item_01 = forms.ChoiceField(
        choices=LIKERT4,
        label='¿Se enfada con facilidad?',
        widget = forms.RadioSelect,
        )
    item_02 = forms.ChoiceField(
        choices=LIKERT4,
        label='¿Se enfada continuamente con la gente ?',
        widget = forms.RadioSelect,
        )
    item_03 = forms.ChoiceField(
        choices=LIKERT4,
        label='¿Se enfurece sin motivo?',
        widget = forms.RadioSelect,
        )
    item_04 = forms.ChoiceField(
        choices=LIKERT4,
        label='Cuando se enfada, ¿Coge un arma?',
        widget = forms.RadioSelect,
        )
    item_05 = forms.ChoiceField(
        choices=LIKERT4,
        label='¿Ha lastimado alguna vez a alguien en una pelea?',
        widget = forms.RadioSelect,
        )
    item_06 = forms.ChoiceField(
        choices=LIKERT4,
        label='¿Ha pegado o atacado alguna vez a algún familiar?',
        widget = forms.RadioSelect,
        )
    item_07 = forms.ChoiceField(
        choices=LIKERT4,
        label='¿Ha pegado o atacado algunas vez a alquien que no sea famililar suyo?',
        widget = forms.RadioSelect,
        )
    item_08 = forms.ChoiceField(
        choices=LIKERT4,
        label='¿Ha usado alguna vez un objeto para agredir a alguien?',
        widget = forms.RadioSelect,
        )
    item_09 = forms.ChoiceField(
        choices=LIKERT4,
        label='¿Podría conseguir un arma con facilidad?',
        widget = forms.RadioSelect,
        )
    item_10 = forms.ChoiceField(
        choices=LIKERT4,
        label='¿Cuantas veces ha sido vd. detenido por delitos no violentos como irse de un tienda o falsificar documentos?',
        widget = forms.RadioSelect,
        )
    item_11 = forms.ChoiceField(
        choices=LIKERT4,
        label='¿Cuántas veces ha sido vd. detenido por delitos como robo a mano armada o agresión violenta?',
        widget = forms.RadioSelect,
        )
    item_12 = forms.ChoiceField(
        choices=CHOICES,
        label = '¿Guarda o colecciona armas en su casa y sabe cómo utilizarlas?',
        widget = forms.RadioSelect,
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
        label = '¿Cómo evalúa la calidad de los servicios que ha recibido?',
        widget = forms.RadioSelect,
        choices=(
            (4, 'Excelente'),
            (3, 'Buena'),
            (2, 'Regular'),
            (1, 'Mala'),
            ),
        )
    item_2 = forms.ChoiceField(
        label = '¿Recibió la clase de servicio que usted requería?',
        widget = forms.RadioSelect,
        choices=(
            (4, 'No definitivamente'),
            (3, 'En muy pocos casos'),
            (2, 'Si en general'),
            (1, 'Si definitívamente'),
            ),
        )
    item_3 = forms.ChoiceField(
        label = '¿Hasta qué punto ha ayudado nuestro programa a solucinar sus probelmas?',
        widget = forms.RadioSelect,
        choices= (
            (4, 'En casi todos'),
            (3, 'En la mayor parte de'),
            (2, 'Sólo en algunos'),
            (1, 'En ninguno'),
            ),
        )
    item_4 = forms.ChoiceField(
        label = '¿Si un/a amigo/a estuviera en necesidad de ayuda similar, le recomendaría nuestro programa?',
        widget = forms.RadioSelect,
        choices=(
            (4, 'No definitivamente'),
            (3, 'No, creo que no'),
            (2, 'Si, creo que si'),
            (1, 'Si definitivamente'),
            ),
        )
    item_5 = forms.ChoiceField(
        label = '¿Cómo de satisfecho/a está usted con la cantidad de ayuda que ha recibido?',
        widget = forms.RadioSelect,
        choices=(
            (4, 'Nada satisfecho/a'),
            (3, 'Indiferente o moderadamente no satisfecho/a'),
            (2, 'Moderadamente satisfecho/a'),
            (1, 'Muy satisfecho/a'),
            ),
        )
    item_6 = forms.ChoiceField(
        label = '¿Los servicios que ha recibido le han ayudado a enfrentarse mejor a sus problemas?',
        widget = forms.RadioSelect,
        choices=(
            (4, 'Si me ayudaron mucho'),
            (3, 'Si me ayudaron algo'),
            (2, 'No, realmente no me ayudaron'),
            (1, 'No, parecían poner las cosas peor'),
            ),
        )
    item_7 = forms.ChoiceField(
        label = '¿En general, cómo de satisfecho/a está usted con los servicios que ha recibido?',
        widget = forms.RadioSelect,
        choices=(
            (4, 'Muy satisfecho/a'),
            (3, 'Moderadamente satisfecho/a'),
            (2, 'Algo insatisfecho/a'),
            (1, 'Muy insatisfecho'),
            ),
        )
    item_8 = forms.ChoiceField(
        label = '¿Si necesitara ayuda otra vez , volvería a nuestro programa?',
        widget = forms.RadioSelect,
        choices=(
            (4, 'No definitívamente'),
            (3, 'No posiblemente'),
            (2, 'Si, creo que si'),
            (1, 'Si con seguridad'),
            ),
        )
    item_9 = forms.CharField(
        label= 'Lo que mas me ha gustado de la atencion que he recibido ha sido',
        widget = forms.Textarea,
        )
    item_10 = forms.CharField(
        label= 'Creo que se tendría que mejorar',
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
        label='Preocupación somática',
        widget = forms.RadioSelect,
        )
    item_02 = forms.ChoiceField(
        choices=LIKERT6,
        label='Ansiedad psíquica',
        widget = forms.RadioSelect,
        )   
    item_03 = forms.ChoiceField(
        choices=LIKERT6,
        label='Aislamiento emocional',
        widget = forms.RadioSelect,
        )
    item_04 = forms.ChoiceField(
        choices=LIKERT6,
        label='Desorganización conceptual (incoherencia)',
        widget = forms.RadioSelect,
        )
    item_05 = forms.ChoiceField(
        choices=LIKERT6,
        label='Autodesprecio y sentimientos de culpa',
        widget = forms.RadioSelect,
        )
    item_06 = forms.ChoiceField(
        choices=LIKERT6,
        label='Tensión. Ansiedad somática',
        widget = forms.RadioSelect,
        )   
    item_07 = forms.ChoiceField(
        choices=LIKERT6,
        label='Manierismo y postura extraña',
        widget = forms.RadioSelect,
        )
    item_08 = forms.ChoiceField(
        choices=LIKERT6,
        label='Grandeza',
        widget = forms.RadioSelect,
        )
    item_09 = forms.ChoiceField(
        choices=LIKERT6,
        label='Humor depresivo',
        widget = forms.RadioSelect,
        )
    item_10 = forms.ChoiceField(
        choices=LIKERT6,
        label='Hostilidad',
        widget = forms.RadioSelect,
        )
    item_11 = forms.ChoiceField(
        choices=LIKERT6,
        label='Suspicacia',
        widget = forms.RadioSelect,
        )
    item_12 = forms.ChoiceField(
        choices=LIKERT6,
        label='Alucinaciones',
        widget = forms.RadioSelect,
        )   
    item_13 = forms.ChoiceField(
        choices=LIKERT6,
        label='Enlentecimiento motor',
        widget = forms.RadioSelect,
        )
    item_14 = forms.ChoiceField(
        choices=LIKERT6,
        label='Falta de cooperación',
        widget = forms.RadioSelect,
        )   
    item_15 = forms.ChoiceField(
        choices=LIKERT6,
        label='Contenido insusual del pensamiento',
        widget = forms.RadioSelect,
        )
    item_16 = forms.ChoiceField(
        choices=LIKERT6,
        label='Embotamiento, aplanamiento afectivo',
        widget = forms.RadioSelect,
        )   
    item_17 = forms.ChoiceField(
        choices=LIKERT6,
        label='Exitación',
        widget = forms.RadioSelect,
        )
    item_18 = forms.ChoiceField(
        choices=LIKERT6,
        label='Desorientación y confusión',
        widget = forms.RadioSelect,
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
        label='Delirios.',
        widget = forms.RadioSelect,
        )
    item_p02 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='Desorganización conceptual.',
        widget = forms.RadioSelect,
        )
    item_p03 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='Conducta alucinatoria.',
        widget = forms.RadioSelect,
        )
    item_p04 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='Exitación.',
        widget = forms.RadioSelect,
        )
    item_p05 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='Grandiosidad.',
        widget = forms.RadioSelect,
        )
    item_p06 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='Suspicacia / Perjuicio.',
        widget = forms.RadioSelect,
        )
    item_p07 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='Hostilidad.',
        widget = forms.RadioSelect,
        )

    item_n01 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='Embotamiento afectivo.',
        widget = forms.RadioSelect,
        )
    item_n02 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='Retracción emocional.',
        widget = forms.RadioSelect,
        )
    item_n03 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='Pobre relación.',
        widget = forms.RadioSelect,
        )
    item_n04 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='Retracción social, apatía pasiva.',
        widget = forms.RadioSelect,
        )
    item_n05 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='Dificultad de pensamiento abstracto.',
        widget = forms.RadioSelect,
        )
    item_n06 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='Falta de espontaneidad y fluidez de la conversación.',
        widget = forms.RadioSelect,
        )
    item_n07 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='Pensamiento estereotipado',
        widget = forms.RadioSelect,
        )

    item_g01 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='Preocupaciones somáticas.',
        widget = forms.RadioSelect,
        )
    item_g02 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='Ansiedad.',
        widget = forms.RadioSelect,
        )
    item_g03 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='Sentimientos de culpa.',
        widget = forms.RadioSelect,
        )
    item_g04 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='Tensión motora.',
        widget = forms.RadioSelect,
        )
    item_g05 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='Manierismos y posturas.',
        widget = forms.RadioSelect,
        )
    item_g06 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='Depresión.',
        widget = forms.RadioSelect,
        )
    item_g07 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='Retardo motor',
        widget = forms.RadioSelect,
        )
    item_g08 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='Falta de colaboración.',
        widget = forms.RadioSelect,
        )
    item_g09 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='Inusuales contenidos del pensamiento.',
        widget = forms.RadioSelect,
        )
    item_g10 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='Desorientación.',
        widget = forms.RadioSelect,
        )
    item_g11 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='Atención deficiente.',
        widget = forms.RadioSelect,
        )
    item_g12 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='Ausencia de juicio e introspección.',
        widget = forms.RadioSelect,
        )
    item_g13 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='Trastorno de la volición.',
        widget = forms.RadioSelect,
        )
    item_g14 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='Control deficiente de impulsos.',
        widget = forms.RadioSelect,
        )
    item_g15 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='Preocupación.',
        widget = forms.RadioSelect,
        )
    item_g16 = forms.ChoiceField(
        choices=LIKERT_PANSS,
        label='Evitación social activa',
        widget = forms.RadioSelect,
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
        label = 'Euforia',
        choices = (
            (0, 'Ausente'),
            (1, 'Posible o moderada, sólo cuando se le pregunta'),
            (2, 'Clara aunque subjetiva y apropiada al contenido: optimista, seguro de sí mismo/a, alegre'),
            (3, 'Elevada e inapropiada'),
            (4, 'Claramente eufórico/a, risa inadecuada, canta durante la entrevista, etc.'),
            ),
        widget = forms.RadioSelect,
        )
    item_02 = forms.ChoiceField(
        label = 'Hiperactividad',
        choices = (
            (0, 'Ausente'),
            (1, 'Subjetivamente aumentada'),
            (2, 'Vigoroso/a, hipergestual'),
            (3, 'Energía excesiva, hiperactividad fluctuante, inquietud (puede ser calmado/a)'),
            (4, 'Agitación o hiperactividad constante (no puede ser calmado/a)'),
            ),
        widget = forms.RadioSelect,
        )
    item_03 = forms.ChoiceField(
        label = 'Impulso sexual',
        choices = (
            (0, 'Normal, no aumentado'),
            (1, 'Posible o moderadamente aumentado'),
            (2, 'Claro aumento al preguntar'),
            (3, 'Referido como elevado de forma espontánea, contenido sexual del discurso, preocupación por temas sexuales'),
            (4, 'Actos o incitaciones sexuales evidentes (hacia pacientes, personal o entrevistador)'),
            ),
        widget = forms.RadioSelect,
        )
    item_04 = forms.ChoiceField(
        label = 'Sueño',
        choices = (
            (0, 'No reducido'),
            (1, 'Disminución en menos de 1 ,hora'),
            (2, 'Disminución en más de 1 hora'),
            (3, 'Refiere disminución de la necesidad de dormir'),
            (4, 'Niega necesidad de dormir'),
            ),
        widget = forms.RadioSelect,
        )
    item_05 = forms.ChoiceField(
        label = 'Irritabilidad',
        choices = (
            (0, 'Ausente'),
            (2, 'Subjetivamente aumentada'),
            (4, 'Irritabilidad fluctuante durante la entrevista, episodios recientes de rabia o enfado'),
            (6, 'Predominantemente irritable durante la entrevista, brusco y cortante'),
            (8, 'Hostil, no colaborador/a, entrevista imposible'),
            ),
        widget = forms.RadioSelect,
        )

    item_06 = forms.ChoiceField(
        label = 'Expresión verbal',
        choices = (
            (0, 'No aumentada'),
            (2, 'Sensación de locuacidad'),
            (4, 'Aumentada de forma fluctuante, verborrea ocasional'),
            (6, 'Claramente aumentada en ritmo y cantidad, difícil de interrumpir, intrusiva'),
            (8, 'Verborrea ininterrumpible y continua'),
            ),
        widget = forms.RadioSelect,
        )
    item_07 = forms.ChoiceField(
        label = 'Trastornos del curso del pensamiento y el lenguaje',
        choices = (
            (0, 'Ausentes'),
            (1, 'Circunstancialidad, distraibilidad moderada, aceleración del pensamiento'),
            (2, 'Distraibilidad clara, descarrilamiento, taquipsiquia'),
            (3, 'Fuga de ideas, tangencialidad, discurso difícil de seguir, rimas, ecolalia'),
            (4, 'Incoherencia, ininteligibilidad, comunicación imposible'),
            ),
        widget = forms.RadioSelect,
        )
    item_08 = forms.ChoiceField(
        label = 'Trastornos del contenido del pensamiento',
        choices = (
            (0, 'Ausentes'),
            (2, 'Planes discutibles, nuevos intereses'),
            (4, 'Proyectos especiales, misticismo'),
            (6, 'Ideas grandiosas o paranoides, ideas de referencia'),
            (8, 'Delirios, alucinaciones'),
            ),
        widget = forms.RadioSelect,
        )
    item_09 = forms.ChoiceField(
        label = 'Agresividad',
        choices = (
            (0, 'Ausente, colaborador/a'),
            (2, 'Sarcástico/a, enfático/a, lacónico/a'),
            (4, 'Querulante, pone en guardia'),
            (6, 'Amenaza al entrevistador, habla a gritos, entrevista difícil'),
            (8, 'Claramente agresivo/a, destructivo/a, entrevista imposible'),
            ),
        widget = forms.RadioSelect,
        )
    item_10 = forms.ChoiceField(
        label = 'Apariencia',
        choices = (
            (0, 'Higiene e indumentaria apropiada '),
            (1, 'Ligeramente descuidada'),
            (2, 'Mal arreglado/a, moderadamente despeinado/a, indumentaria sobrecargada'),
            (3, 'Despeinado/a, semidesnudo/a, maquillaje llamativo'),
            (4, 'Completamente desaseado/a, adornado/a, indumentaria extravagante'),
            ),
        widget = forms.RadioSelect,
        )
    item_11 = forms.ChoiceField(
        label = 'Conciencia de enfermedad',
        choices = (
            (0, 'Presente, admite la enfermedad, acepta tratamiento'),
            (1, 'Según él/ella, posiblemente enfermo/a'),
            (2, 'Admite cambio de conducta, pero niega enfermedad'),
            (3, 'Admite posible cambio de conducta, niega enfermedad'),
            (4, 'Niega cualquier cambio de conduct'),
            ),
        widget = forms.RadioSelect,
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
        label = 'Humor deprimido',
        choices = (
            (0, 'Ausente'),
            (1, 'Estas sensaciones se indican solamente al ser preguntado'),
            (2, 'Estas sensaciones se relatan oral y espontáneamente'),
            (3, 'Sensaciones no comunicadas verbalmente, es decir, por la expresión facial, la postura, la voz y la tendencia al llanto'),
            (4, 'El paciente manifiesta estas sensaciones en su comunicación verbal y no verbal de forma espontánea'),
            ),
        widget = forms.RadioSelect,
        )
    item_02 = forms.ChoiceField(
        label = 'Sensación de culpabilidad',
        choices = (
            (0, 'Ausente'),
            (1, 'Se culpa a si mismos, cree haber decepcionado a la gente'),
            (2, 'Ideas de culpabilidad, o meditación sobre errores pasados o malas acciones'),
            (3, 'La enfermedad actual es un castigo. Ideas delirantes de culpabilidad'),
            (4, ' Oye  voces  acusatorias  o  de  denuncia  y/o  experiemtna  alucinaciones  visuales amenazadoras'),
            ),
        widget = forms.RadioSelect,
        )
    item_03 = forms.ChoiceField(
        label = 'Suicidio',
        choices = (
            (0, 'Ausente'),
            (1, 'Le parece que la vida no merece la pena ser vivida'),
            (2, 'Desearía estar muerto o tiene pensamientos sobre la posibilidad de morirse'),
            (3, 'Ideas de suicidio o amenazas'),
            (4, ' Intentos de suicidio (cualuqier intento serio se califica 4)'),
            ),
        widget = forms.RadioSelect,
        )
    item_04 = forms.ChoiceField(
        label = 'Insomnio precoz',
        choices = (
            (0, 'Ausente'),
            (1, 'Dificultades ocasionales para dormirse, por ejemplo, más de media hora'),
            (2, 'Dificultades para dormirse cada noche'),
            ),
        widget = forms.RadioSelect,
        )
    item_05 = forms.ChoiceField(
        label = 'Insomnio medio',
        choices = (
            (0, 'Ausente'),
            (1, 'El paciente s queja de estar inquieto durante la noche'),
            (2, 'Está despierto durante la noche; medicación, etc.'),
            ),
        widget = forms.RadioSelect,
        )
    item_06 = forms.ChoiceField(
        label = 'Insomnio tardío',
        choices = (
            (0, 'Ausente'),
            (1, 'Se despierta a primeras horas de la madrugada pero vuelve a dormirse'),
            (2, 'No puede volver a dormirse si se levanta de la cama'),
            ),
        widget = forms.RadioSelect,
        )
    item_07 = forms.ChoiceField(
        label = 'Trabajo y actividades',
        choices = (
            (0, ' Ausente'),
            (1, 'Ideas  y  sentimientos  de  incapacidad.  Fatiga  o  debilidad  relcionadas  con  su actividad,trabajo o aficiones'),
            (2, 'Pérdida de interés en su actividad, aficiones, o trabajo, ,anifestado directamete por el enfermo o indirectamente por desatención, indecisión y vacilación'),
            (3, 'Disminución del tiempo dedicado a actividades o descenso en la productividad'),
            (4, 'Dejó de trabajar por la presente enfermedad'),
            ),
        widget = forms.RadioSelect,
        )
    item_08 = forms.ChoiceField(
        label = 'Inhibición',
        choices = (
            (0, 'Palabra y pensamiento normales'),
            (1, 'Ligero retras en el diálogo'),
            (2, 'Evidente retraso en el diálogo'),
            (3, 'Diálogo difícil'),
            (4, 'Torpeza absoluta'),
            ),
        widget = forms.RadioSelect,
        )
    item_09 = forms.ChoiceField(
        label = 'Agitación',
        choices = (
            (0, 'Ninguna'),
            (1, '“Juega” con sus manos, cabellos, etc.'),
            (2, 'Se retuerce las manos, se muerde las uñas, los labios, se tira de los cabellos, etc.'),
            ),
        widget = forms.RadioSelect,
        )
    item_10 = forms.ChoiceField(
        label = 'Ansiedad psíquica',
        choices = (
            (0, 'No hay dificultad'),
            (1, 'Tensión subjetiva e irritable'),
            (2, 'Preocupación por pequeñas cosas'),
            (3, 'Actitud aprensiva aparente en la expresión o en el habla'),
            (4, 'Terrores expresados sin preguntarle'),
            ),
        widget = forms.RadioSelect,
        )
    item_11 = forms.ChoiceField(
        label = 'Ansiedad somática',
        choices = (
            (0, 'Ausente'),
            (1, 'Ligera'),
            (2, 'Moderada'),
            (3, 'Grave'),
            (4, 'Incapacitante'),
            ),
        widget = forms.RadioSelect,
        )
    item_12 = forms.ChoiceField(
        label = 'Síntomas somáticos gastrointestinales',
        choices = (
            (0, 'Ninguno'),
            (1, 'Pérdida de apetito, pero come sin necesidad de que estimulen. Sensación de pesadez en el abdomen'),
            (2, 'Difucultad en comer si no se le insiste. Solicita o necesita laxantes o medicación intestinal para sus síntomas gastrointestinales'),
            ),
        widget = forms.RadioSelect,
        )
    item_13 = forms.ChoiceField(
        label = 'Síntomas somáticos generales',
        choices = (
            (0, 'Ninguno'),
            (1, 'Pesadez en las extremidades, espalda o cabeza. Dorsalgias, cefalalgias, algias musculares. Pérdida de energía y fatigabilidad'),
            (2, 'Cualquier síntoma bien definido'),
            ),
        widget = forms.RadioSelect,
        )
    item_14 = forms.ChoiceField(
        label = 'Síntomas genitales',
        choices = (
            (0, 'Ausente'),
            (1, 'Débil'),
            (2, 'Grave'),
            (3, 'Incapacitante'),
            ),
        widget = forms.RadioSelect,
        )
    item_15 = forms.ChoiceField(
        label = 'Hipocondría',
        choices = (
            (0, 'No la hay'),
            (1, 'Preocupado de sí mismo (corporalmente)'),
            (2, 'Preocupado por su sald'),
            (3, 'Se lamenta constantemente, solicita ayudas, etc.'),
            (4, 'Ideas delirantes hipocondríacas'),
            ),
        widget = forms.RadioSelect,
        )

    item_16 = forms.ChoiceField(
        label = 'Pérdida de peso',
        choices = (
            (0, 'No hay pérdida de peso'),
            (1, 'Probable pérdida de peso asociada con la enfermedad actual'),
            (2, 'Pérdida de peso definida (según el enfermo)'),
            ),
        widget = forms.RadioSelect,
        )

    item_17 = forms.ChoiceField(
        label = 'Insight (conciencia de enfermedad)',
        choices = (
            (0, 'Se da cuenta de que está deprimido y enfermo'),
            (1, 'Se da cuenta de sy enfermedad pero atribuye la causa a la mala alimentación, clima, exceso de trabajo, virus, etc.'),
            (2, 'Niega que esté enfermo'),
            ),
        widget = forms.RadioSelect,
        )