from django.http import HttpResponse
from django.template.loader import get_template

def addToQueryString(queryString, fieldname, value):
    if len(value) > 0:
        if len(queryString) > 0:
            queryString = queryString + "&"
        else:
            queryString = queryString + "?"
        queryString = queryString + fieldname + "=" + value
    return queryString

def createCommaDelimitedString(source_list):
    results = ""
    for list_key in source_list:
        if len(results) > 0:
            results = results + ","
        results = results + list_key
    return results

def convertCommaDelimitedList(pk_string):
    results = []
    if len(pk_string) > 0:
        pk_array = pk_string.split(",")
        for pk in pk_array:
            results.append(int(pk))
    return results

def addZeros(source, digits):
    while len(source) < digits:
        source = "0" + source
    return source
