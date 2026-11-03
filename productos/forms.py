from django import forms

from .models import Producto


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


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto

        fields = [
            'categoria',
            'nombre',
            'descripcion',
            'precio',
            'stock',
            'marca',
            'imagen',
            'activo',
        ]

        widgets = {
            'categoria': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre del producto'
                }
            ),

            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Descripción del producto',
                    'rows': 4
                }
            ),

            'precio': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'step': '0.01'
                }
            ),

            'stock': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'marca': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Marca del producto'
                }
            ),

            'imagen': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'activo': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            ),
        }