from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.validators import RegexValidator
from .models import Record

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'})
    )

    first_name = forms.CharField(
        label="",
        max_length=50,
        validators=[RegexValidator(r'^[a-zA-Z\s]*$', 'Only letters and spaces are allowed.')],
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
        strip=True
    )
    
    last_name = forms.CharField(
        label="",
        max_length=50,
        validators=[RegexValidator(r'^[a-zA-Z\s]*$', 'Only letters and spaces are allowed.')],
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
        strip=True
    )

    password1 = forms.CharField(
        label="",
        min_length=8,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        error_messages={
            'required': 'Please provide a password.',
            'min_length': 'Password must be at least 8 characters long.'
        },
    )

    password2 = forms.CharField(
        label="",
        min_length=8,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        error_messages={
            'required': 'Please confirm your password.',
            'min_length': 'Password must be at least 8 characters long.'
        },
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Please ensure your email is valid.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError("Please choose another username.")
        return username

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

# Create Add Record Form 
class AddRecordForm(forms.ModelForm):
	first_name = forms.CharField(required=True, max_length=50, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="", validators=[RegexValidator(r'^[a-zA-Z\s]*$', 'Only letters and spaces are allowed.')],)
	last_name = forms.CharField(required=True,  max_length=50, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="", validators=[RegexValidator(r'^[a-zA-Z\s]*$', 'Only letters and spaces are allowed.')],)
	email = forms.EmailField(required=True, max_length=100, widget=forms.widgets.EmailInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
	phone = forms.CharField(required=True, max_length=15, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="", validators=[RegexValidator(r'^\+?1?\d{9,15}$', 'Enter a valid phone number.')],)
	address = forms.CharField(required=True, max_length=100, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), label="")
	city = forms.CharField(required=True, max_length=50, widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), label="")
	state = forms.CharField(required=True, max_length=50, widget=forms.widgets.TextInput(attrs={"placeholder":"State", "class":"form-control"}), label="")
	zip_code = forms.CharField(required=True, max_length=20, widget=forms.widgets.TextInput(attrs={"placeholder":"Zipcode", "class":"form-control"}), label="", validators=[RegexValidator(r'^\d{5}(-\d{4})?$', 'Enter a valid ZIP code.')],)

	class Meta:
		model = Record
		exclude = ("user",)