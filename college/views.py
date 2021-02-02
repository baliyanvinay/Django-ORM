from django.shortcuts import render

from college.querysetAPI import (
    method_returning_new_queryset,
    method_not_returning_new_queryset,
    queryset_field_lookup,
    complex_queries_q_objects
)

def index(request):
    context_01 = method_returning_new_queryset(request)
    context_02 = method_not_returning_new_queryset(request)
    context_03 = queryset_field_lookup(request)
    context_04 = complex_queries_q_objects(request)

    return render(request, 'college/index.html', context={
        'context_01': context_01,
        'context_02': context_02,
        'context_03': context_03,
        'context_04': context_04,
        })
