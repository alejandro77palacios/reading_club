from django.shortcuts import render, redirect

from club.models import FormModel, FormRecord, FormData


def index(request):
    data = {
        "records": FormRecord.objects.all(),
    }
    return render(request, "index.html", data)


def register(request):
    participants_form = FormModel.objects.get(name="participants")
    fields_manager = participants_form.formfield_set
    if request.method == "GET":
        form = fields_manager.all()
    else:
        collected_data = request.POST
        record = FormRecord.objects.create()
        for field in fields_manager.all():
            FormData.objects.create(value=collected_data[field.name], record=record, field=field,
                                    form=participants_form)
        return redirect("index")
    data = {
        "form": form,
    }
    return render(request, "register.html", data)
