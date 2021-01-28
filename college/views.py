from django.shortcuts import render

from college.querysetAPI import (
    method_returning_new_queryset,
    method_not_returning_new_queryset,
    queryset_field_lookup
)

def index(request):
    # Method to be called here for homepage
    method_returning_new_queryset(request)
    method_not_returning_new_queryset(request)
    queryset_field_lookup(request)

    return render(request, 'college/index.html', context={})
