from django.db import models


class FormModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"Form {self.name}"


class FormField(models.Model):
    name = models.CharField(max_length=100)
    label = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    form = models.ForeignKey(FormModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"Field {self.name} for from {self.form.name}"


class FormRecord(models.Model):
    date = models.DateField(auto_now=True)

    def get_field_value_by_name(self, field):
        return self.formdata_set.get(field__name=field).value

    def get_name(self):
        return self.get_field_value_by_name("name")

    def get_age(self):
        return self.get_field_value_by_name("age")

    def get_book(self):
        return self.get_field_value_by_name("favourite_book")


class FormData(models.Model):
    value = models.CharField(max_length=100)
    field = models.ForeignKey(FormField, on_delete=models.CASCADE)
    form = models.ForeignKey(FormModel, on_delete=models.CASCADE)
    record = models.ForeignKey(FormRecord, on_delete=models.CASCADE)
