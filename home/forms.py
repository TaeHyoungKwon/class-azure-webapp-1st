from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User




class SignupForm(UserCreationForm):
	
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(SignupForm, self).__init__(*args, **kwargs)

    username = forms.RegexField(
        max_length=20,
        regex=r'^[\w.@+-]+$',
        error_messages={
            'invalid': "This value may contain only letters, numbers and "
                         "@/./+/-/_ characters."
        },
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '위와 같은 양식으로 작성하세요.',
                'required': 'True',
            }
        ),
    )


    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email 주소 입력',
                'required': 'True',
            }
        )
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'required': 'True',
            }
        )
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password confirmation',
                'required': 'True',
            }
        ),
        help_text="위에서 입력한 패스워드와 동일하게 입력하세요!"
    )

    class Meta:
        model = User
        fields = ("username","email", "password1", "password2",)