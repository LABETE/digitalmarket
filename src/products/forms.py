from django import forms

from .models import Product

PUBLISH_CHOICES = (
    ("publish", "Publish"),
    ("draft", "Draft"),
)

class ProductModelForm(forms.ModelForm):
    title = forms.CharField(label='Your Title', widget=forms.TextInput(
        attrs = {
            "class": "custom-class",
            "placeholder": "Title"
            }
        ))
    description = forms.CharField(widget=forms.Textarea(
        attrs = {
            "class": "my-custom-class",
            "placeholder": "Description",
            "some-attr": "this"
            }
        ))
    tags = forms.CharField(label='Related Tags', required=False)
    publish = forms.ChoiceField(widget=forms.RadioSelect, choices=PUBLISH_CHOICES, required=False)
    class Meta:
        model = Product
        fields = (
            "title",
            "description",
            "price",
            "media"
        )

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price <= 1.00:
            raise forms.ValidationError("Price must be greater than $1.00.")
        elif price >= 100.00:
            raise forms.ValidationError("Price must be less than $100.00.")
        else:
            return price

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) <= 3:
            raise forms.ValidationError("Title must be greater than 3 characters long.")
        return title
