from django.forms import ModelForm, widgets, Form, CharField
from user.models import Profile
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField


class ShippingForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user', 'profile_image', 'role']


class PaymentForm(Form):
    cardholder_name = CharField(max_length=255, label="Cardholder's Name")
    card_number = CardNumberField(label='Card Number')
    expiry_date = CardExpiryField(label='Expiration Date')
    cvc = SecurityCodeField(label='CVV/CVC')

    # card_number = CharField(max_length=16, min_length=16, label="Card Number")
   #  expiry_date = CharField(max_length=5, label="Expiration Date")
  #   cvc = CharField(max_length=3, label="CVC/CVV")
