from django import forms
from .models import CoffeeCup


class CoffeeCreateForm(forms.ModelForm):
    class Meta:
        model = CoffeeCup
        fields = [
            "drink_name",
            "preview",
            "description",
            "price",
            "caloric_of_drink",
            "publication_flag",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["drink_name"].widget.attrs.update(
            {
                "class": "contact-form-catalog",
                "placeholder": "Введите наименование продукта",
            }
        )
        self.fields["preview"].widget.attrs.update({"class": "img"})
        self.fields["description"].widget.attrs.update(
            {
                "class": "contact-form-catalog",
                "placeholder": "Введите описание продукта",
            }
        )
        self.fields["price"].widget.attrs.update(
            {"class": "contact-form-catalog", "type": "date"}
        )
        self.fields["caloric_of_drink"].widget.attrs.update({"class": "form-check"})

    # def clean(self):
    #     data_array = super().clean()
    #     description = data_array.get("description")
    #     name = data_array.get("name")

    #     repetitions_name = 0
    #     item = ""
    #     for i, value in enumerate(name):  # type: ignore
    #         if i > 0:
    #             if item == value:
    #                 repetitions_name += 1
    #             item = value
    #         elif i == 0:
    #             item = value

    #     repetitions_description = 0
    #     item = ""
    #     for i, value in enumerate(description):  # type: ignore
    #         if i > 0:
    #             if item == value:
    #                 repetitions_description += 1
    #             item = value
    #         elif i == 0:
    #             item = value

    #     if repetitions_name > 5:
    #         self.add_error("name", "Странно много повторяющихся символов...")
    #     elif repetitions_description > 5:
    #         self.add_error("description", "Странно много повторяющихся символов...")

    #     return data_array

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:  # type: ignore
            self.add_error("price", "Цена продукта не должна быть отрицательной")

        return price


class CoffeeUpdateForm(forms.ModelForm):
    class Meta:
        model = CoffeeCup
        fields = [
            "preview",
            "description",
            "price",
            "caloric_of_drink",
            "publication_flag",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["preview"].widget.attrs.update({"class": "contact-form"})
        self.fields["description"].widget.attrs.update(
            {
                "class": "contact-form-catalog",
                "placeholder": "Введите описание продукта",
            }
        )
        self.fields["price"].widget.attrs.update(
            {"class": "contact-form-catalog", "type": "date"}
        )
        self.fields["caloric_of_drink"].widget.attrs.update({"class": "form-check"})

    # def clean(self):
    #     data_array = super().clean()
    #     name = data_array.get("name")
    #     description = data_array.get("description")

    #     repetitions_name = 0
    #     item = ""
    #     for i, value in enumerate(name):  # type: ignore
    #         if i > 0:
    #             if item == value:
    #                 repetitions_name += 1
    #             item = value
    #         elif i == 0:
    #             item = value

    #     repetitions_description = 0
    #     item = ""
    #     if description:
    #         for i, value in enumerate(description):  # type: ignore
    #             if i > 0:
    #                 if item == value:
    #                     repetitions_description += 1
    #                 item = value
    #             elif i == 0:
    #                 item = value

    #     if repetitions_name > 5:
    #         self.add_error("name", "Странно много повторяющихся символов...")
    #     elif repetitions_description > 5:
    #         self.add_error("description", "Странно много повторяющихся символов...")

    #     return data_array

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:  # type: ignore
            self.add_error("price", "Цена продукта не должна быть отрицательной")

        return price
