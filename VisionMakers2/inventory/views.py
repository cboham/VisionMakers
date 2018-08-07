from django.shortcuts import render, redirect, get_object_or_404
from .models import Type, Pair
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic
from .filters import TypeFilter
import xlwt
from django.http import HttpResponse
from .forms import ExportForm, MultiTypeForm, PairForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='')
def index(request):
    inventory = Type.objects.all()
    for item in inventory:
        item.update_on_hand()
    context = {
        'inventory': inventory,
        }
    return render(request, 'inventory/index.html', context)

class DetailView(generic.DetailView):
    template_name = 'inventory/detail.html'
    model = Type

class TypeDelete(DeleteView):
    model = Type
    success_url = reverse_lazy('inventory:index')

class TypeCreate(CreateView):
    model = Type
    fields = [
        'sku',
        'vendor',
        # 'comments',
        'style',
        'desc',
        'VID',
        'HCFA',
        'wholesale',
        'retail',
        'cost',
       'taxable',
       'on_hand',
       'on_order',
       'reorder_point',
       'lead_time',
       'eye',
       'bridge',
       'temple',
       'A',
       'B',
       'ED',
       'DBL',
       'sold_this_week',
       'sold_this_month',
       'sold_this_year',
       'color',
       'comments',

        ]
    success_url = reverse_lazy('inventory:index')

class TypeUpdate(UpdateView):
    model = Type
    fields = [
        'vendor',
        'comments',
        'style',
        'color',
        'desc',
        'VID',
        'HCFA',
        'wholesale',
        'retail',
        'cost',
       'taxable',
       'on_hand',
       'on_order',
       'reorder_point',
       'lead_time',
       'eye',
       'bridge',
       'temple',
       'A',
       'B',
       'ED',
       'DBL',
       'sold_this_week',
       'sold_this_month',
       'sold_this_year',
        ]
    success_url = reverse_lazy('inventory:submission')


def pair_create(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = PairForm(request.POST)
        # check whether it's valid:

        if form.is_valid():
            # process the data in form.cleaned_data as required
            currentObj = Type.objects.all().get(pk = form.cleaned_data['type'])
            pair = Pair(
                type = currentObj,
                location = form.cleaned_data['location'],
                date_added = form.cleaned_data['date_added'],
                comments = form.cleaned_data['comments']
            )
            pair.save()
            currentObj.pair_set.add(pair)
            currentObj.save()
            # redirect to a new URL:
            return index(request)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PairForm()

    return render(request, 'inventory/pair-form.html', {'form': form})
@login_required
def  print_page(request, pk):
    obj = get_object_or_404(Type, pk = pk)

    return render(request, 'inventory/print.html', {'item': obj})
@login_required
def search(request):
    type_list = Type.objects.all()
    type_filter = TypeFilter(request.GET, queryset=type_list)
    return render(request, 'inventory/filter.html', {'filter': type_filter})


@login_required
def submission(request):
    return render(request, 'inventory/submission.html')


@login_required
def export_to_xls(request, location, title):

    response = HttpResponse(content_type = 'application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename = "' + title + '.xls"'

    wb = xlwt.Workbook(encoding = 'utf-8')
    ws = wb.add_sheet(title)

    #Sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    ws.write(row_num, 0, location.title(), font_style)
    row_num += 2
    columns = ['SKU', 'Vendor', 'Desc', 'Style', 'Color', 'Size', 'Cost', 'Retail', 'On Hand']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    #Sheet Body, remaining rows
    font_style = xlwt.XFStyle()

    inventory = Type.objects.all()
    for item in inventory:
        item.update_on_hand()
    if location.lower() == 'all locations':
        rows = Type.objects.all().values_list('sku', 'vendor', 'desc', 'style', 'color', 'eye','cost', 'retail', 'on_hand')
        for row in rows:
            row_num += 1

            for col_num in range(len(row)):
                if columns[col_num] == 'Size':
                    ws.write(row_num, col_num, Type.objects.all().get(pk = row[0]).size(), font_style)
                else:
                    ws.write(row_num, col_num, row[col_num], font_style)

    elif location.lower() == 'beavercreek':
        rows = Type.objects.all().values_list('sku', 'vendor', 'desc', 'style', 'color', 'eye','cost', 'retail', 'on_hand')
        for row in rows:
            row_num += 1

            for col_num in range(len(row)):
                if columns[col_num] == 'On Hand':
                    ws.write(row_num, col_num, Type.objects.all().get(pk = row[0]).get_stock_bv())
                elif columns[col_num] == 'Size':
                    ws.write(row_num, col_num, Type.objects.all().get(pk = row[0]).size(), font_style)
                else:
                    ws.write(row_num, col_num, row[col_num], font_style)
    elif location.lower() == 'woodman':
        rows = Type.objects.all().values_list('sku', 'vendor', 'desc', 'style', 'color', 'eye','cost', 'retail', 'on_hand')
        for row in rows:
            row_num += 1

            for col_num in range(len(row)):
                if columns[col_num] == 'On Hand':
                    ws.write(row_num, col_num, Type.objects.all().get(pk = row[0]).get_stock_wd())
                elif columns[col_num] == 'Size':
                    ws.write(row_num, col_num, Type.objects.all().get(pk = row[0]).size(), font_style)
                else:
                    ws.write(row_num, col_num, row[col_num], font_style)
    elif location.lower() == 'pittsburgh':
        rows = Type.objects.all().values_list('sku', 'vendor', 'desc', 'style', 'color', 'eye','cost', 'retail', 'on_hand')
        for row in rows:
            row_num += 1

            for col_num in range(len(row)):
                if columns[col_num] == 'On Hand':
                    ws.write(row_num, col_num, Type.objects.all().get(pk = row[0]).get_stock_pa())
                elif columns[col_num] == 'Size':
                    ws.write(row_num, col_num, Type.objects.all().get(pk = row[0]).size(), font_style)
                else:
                    ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    return response

@login_required
def get_export(request):

    if request.method == 'POST':
        form = ExportForm(request.POST)
        if form.is_valid():
            return render(request, 'inventory/export.html', { 'location': form.cleaned_data['location'],
                                                            'file_name': form.cleaned_data['file_name'],
                                                            })
    else:
        form = ExportForm()

    return render(request, 'inventory/export.html', {'form': form})

def multiupdate(request, skus):
    skus_list = skus.split("_")

    if request.method == 'POST':

        form = MultiTypeForm(request.POST)
        if form.is_valid():
            for sku in skus_list:
                #make changes in all of the skus
                currentObj = Type.objects.get(pk = sku)
                for key in form.cleaned_data:

                    if key == "vendor" and form.cleaned_data[key] != '':
                        currentObj.vendor = form.cleaned_data[key]
                    elif key == "color" and form.cleaned_data[key] != '':
                        currentObj.color = form.cleaned_data[key]
                    elif key == "HCFA" and form.cleaned_data[key] != '':
                        currentObj.HCFA = form.cleaned_data[key]
                    elif key == "taxable" :
                        if form.cleaned_data[key] == 'yes':
                            currentObj.taxable = True
                        elif form.cleaned_data[key] == 'no':
                            currentObj.taxable = False
                    elif key == "eye" and form.cleaned_data[key] is not None:
                        currentObj.eye = form.cleaned_data[key]
                    elif key == "B" and form.cleaned_data[key] is not None:
                        currentObj.B = form.cleaned_data[key]
                    elif key == "comments" and form.cleaned_data[key] != '':
                        currentObj.comments = form.cleaned_data[key]
                    elif key == "style" and form.cleaned_data[key] != '':
                        currentObj.style = form.cleaned_data[key]
                    elif key == "wholesale" and form.cleaned_data[key] is not None:
                        currentObj.wholesale = form.cleaned_data[key]
                    elif key == "on_order" and form.cleaned_data[key] is not None:
                        currentObj.on_order = form.cleaned_data[key]
                    elif key == "bridge" and form.cleaned_data[key] is not None:
                        currentObj.bridge = form.cleaned_data[key]
                    elif key == "ED" and form.cleaned_data[key] is not None:
                        currentObj.ED = form.cleaned_data[key]
                    elif key == "desc" and form.cleaned_data[key] != '':
                        currentObj.desc = form.cleaned_data[key]
                    elif key == "retail" and form.cleaned_data[key] is not None:
                        currentObj.retail = form.cleaned_data[key]
                    elif key == "reorder_point" and form.cleaned_data[key] is not None:
                        currentObj.reorder_point = form.cleaned_data[key]
                    elif key == "temple" and form.cleaned_data[key] is not None:
                        currentObj.temple = form.cleaned_data[key]
                    elif key == "DBL" and form.cleaned_data[key] is not None:
                        currentObj.DBL = form.cleaned_data[key]
                    elif key == "VID" and form.cleaned_data[key] is not None:
                        currentObj.VID = form.cleaned_data[key]
                    elif key == "cost" and form.cleaned_data[key] is not None:
                        currentObj.cost = form.cleaned_data[key]
                    elif key == "lead_time" and form.cleaned_data[key] is not None:
                        currentObj.lead_time = form.cleaned_data[key]
                    elif key == "A" and form.cleaned_data[key] is not None:
                        currentObj.A = form.cleaned_data[key]

                    currentObj.save()
            return submission(request)
    else:
        form = MultiTypeForm()
    return render(request, 'inventory/multiupdate.html', {'form': form})
