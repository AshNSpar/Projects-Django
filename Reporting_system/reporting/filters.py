import django_filters
from .models import Timesheet,Batch
from django import forms


class TimeSheetFilter(django_filters.Filterset):
    batch = django_filters.ModelChoiceFilter(queryset=Batch.objects.all(widget = forms.Select(attrs={"class":"form-select"})))
    date = django_filters.DateFilterFilter(widget = forms.DateInput(attrs={"type":"date"}))
    class Meta:
        model = Timesheet
        fields = ["date","batch"]
