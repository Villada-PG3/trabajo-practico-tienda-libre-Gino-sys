from django import forms


class ContactoForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        label='Nombre',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingresá tu nombre'
            }
        )
    )

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingresá tu email'
            }
        )
    )

    telefono = forms.CharField(
        max_length=20,
        label='Teléfono',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingresá tu teléfono (opcional)'
            }
        )
    )

    asunto = forms.CharField(
        max_length=150,
        label='Asunto',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingresá el asunto'
            }
        )
    )

    mensaje = forms.CharField(
        label='Mensaje',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Escribí tu mensaje',
                'rows': 5
            }
        )
    )