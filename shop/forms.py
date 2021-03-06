from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from cart.models import CartItem
from .models import Profile
from django.forms.widgets import SelectDateWidget
from .sizes_and_quantities import TAMANIOS, CANTIDADES


my_default_errors = {
    'required': 'Este campo es obligatorio',
    'unique': 'Ese nombre de usuario ya está tomado'
}


class SignUpForm(UserCreationForm):
    error_messages = {
        'password_mismatch': "Las contraseñas no coinciden.",
    }

    first_name = forms.CharField(label="Nombre", max_length=100, required=True)
    last_name = forms.CharField(label='Apellido', max_length=100, required=True)
    username = forms.CharField(label='Nombre de usuario', max_length=100, required=True,
                               error_messages={'invalid': "you custom error message"})
    email = forms.EmailField(label='Correo electrónico', max_length=60, required=True)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1',
                  'password2')
     

class ProfileForm(ModelForm):
    MONTHS = {
        1:'ene', 2:'feb', 3:'mar', 4:'abr',
        5:'may', 6:'jun', 7:'jul', 8:'ago',
        9:'set', 10:'oct', 11:'nov', 12:'dic'
    }

    def __init__(self, district_list, province_list, department_list, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['shipping_district'] = forms.ChoiceField(label='Distrito', choices=tuple([(name, name) for name in district_list]))
        self.fields['shipping_province'] = forms.ChoiceField(label='Provincia', choices=tuple([(name, name) for name in province_list]))
        self.fields['shipping_department'] = forms.ChoiceField(label='Departamento', choices=tuple([(name, name) for name in department_list]))


    dni = forms.CharField(label='DNI', max_length=100, required=True)
    phone_number = forms.CharField(label='Celular')
    birthdate = forms.DateField(label='Fecha de nacimiento', widget=SelectDateWidget(years=range(1980, 2012), months=MONTHS))
    shipping_address1 = forms.CharField(label='Dirección de envío', max_length=100, required=True)
    shipping_address2 = forms.CharField(label='Referencia (opcional)', max_length=100, required=False)

    class Meta:
        model = Profile
        fields = ('dni', 'phone_number', 'birthdate', 'shipping_address1',
                  'shipping_address2', 'shipping_department', 'shipping_province', 'shipping_district')






class StepOneForm(forms.Form):
    size = forms.ChoiceField(choices=TAMANIOS, widget=forms.RadioSelect(), label='Selecciona un tamaño', initial='5 cm x 5 cm')
    quantity = forms.ChoiceField(choices=CANTIDADES, widget=forms.RadioSelect(), label='Selecciona la cantidad')


class StepTwoForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = CartItem
        fields = ('file_a', 'file_b', 'comment')

    def __init__(self, *args, **kwargs):
        super(StepTwoForm, self).__init__(*args, **kwargs)
        self.fields['comment'].required = False
        self.fields['file_a'].required = False
        self.fields['file_b'].required = False

    def save(self, commit=True):
        instance = super(StepTwoForm, self).save(commit=commit)
        return instance




### SAMPLES FORM ####


class StepOneForm_Sample(forms.Form):
    size = forms.ChoiceField(choices=TAMANIOS, widget=forms.RadioSelect(), label='Selecciona un tamaño')


#Se utiliza el StepTwo que se usa para los otros productos que no son muestra

class StepTwoForm_Sample(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = CartItem
        fields = ('file_a', 'file_b', 'comment')

    def __init__(self, *args, **kwargs):
        super(StepTwoForm_Sample, self).__init__(*args, **kwargs)
        self.fields['comment'].required = False
        self.fields['file_a'].required = False
        self.fields['file_b'].required = False

    def save(self, commit=True):
        instance = super(StepTwoForm_Sample, self).save(commit=commit)
        # self.send_email()
        return instance






