from django import forms

class customer_form(forms.Form):
    email = forms.CharField(label = '', max_length=50, widget = forms.EmailInput(attrs={'class': 'form-control Font-Size-20',
        'id': 'email', 'placeholder': "Email"}))

    password = forms.CharField(label = '', max_length=20, widget = forms.PasswordInput(attrs={'class': 'form-control Font-Size-20',
        'id': 'password', 'placeholder': "Password"}))

    phoneNum = forms.CharField(label = '', max_length=20, widget = forms.NumberInput(attrs={'class': 'form-control Font-Size-20',
        'id': 'phonenum', 'placeholder': "Phone Number"}))

    fname = forms.CharField(label = '', max_length=15, widget = forms.TextInput(attrs={'class': 'form-control Font-Size-20',
        'id': 'fname', 'placeholder': "First Name"}))

    name = forms.CharField(label = '', max_length=15, widget = forms.TextInput(attrs={'class': 'form-control Font-Size-20',
        'id': 'name', 'placeholder': "Last Name"}))

    nik = forms.CharField(label = '', max_length=20, widget = forms.TextInput(attrs={'class': 'form-control Font-Size-20',
        'id': 'nik', 'placeholder': "NIK"}))

    bankname = forms.CharField(label = '', max_length=20, widget = forms.TextInput(attrs={'class': 'form-control Font-Size-20',
        'id': 'bankname', 'placeholder': "Bank Name"}))

    accountno = forms.CharField(label = '', max_length=20, widget = forms.TextInput(attrs={'class': 'form-control Font-Size-20',
        'id': 'accountno', 'placeholder': "Account Number"}))

    restopay = forms.CharField(label = '', max_length=25, widget = forms.TextInput(attrs={'class': 'form-control Font-Size-20',
        'id': 'restopay', 'placeholder': "RestoPay"}))

    birthDate = forms.CharField(label = '', max_length=25, widget = forms.DateInput(attrs={'class': 'form-control Font-Size-20',
        'id': 'birthdate', 'placeholder': "Birth Date"}))
    
    sex = forms.CharField(label = '', max_length=1, widget = forms.TextInput(attrs={'class': 'form-control Font-Size-20',
        'id': 'sex', 'placeholder': "Sex"}))

