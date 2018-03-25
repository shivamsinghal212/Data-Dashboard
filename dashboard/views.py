from django.shortcuts import render
from .models import DashboardData

# Create your views here.


def test_view(request):
    test_dict = {'test': 'Test'}
    return render(request, template_name='test_template.html', context=test_dict)


def get_sector_list():
    sector_list = []
    sector = DashboardData.objects.values('sector').distinct()
    for i in sector:
        for k, v in i.items():
            if v != '':
                sector_list.append(v)
    return sector_list


def get_topic_list():
    topic_list = list()
    topic = DashboardData.objects.values('topic').distinct()
    for i in topic:
        for k, v in i.items():
            if v != '':
                topic_list.append(v)
    return topic_list


def get_region_list():
    region_list = list()
    region = DashboardData.objects.values('region').distinct()
    for i in region:
        for k, v in i.items():
            if v != '':
                region_list.append(v)
    return region_list


def get_pestle_list():
    pestle_list = list()
    pestle = DashboardData.objects.values('pestle').distinct()
    for i in pestle:
        for k, v in i.items():
            if v != '':
                pestle_list.append(v)
    return pestle_list


def get_x_prop(arg):
    x_int = {}
    x_rel = {}
    x_like = {}
    prop_var = ''
    prop_function = {'sector': get_sector_list(),
                     'pestle': get_pestle_list(),
                     'topic': get_topic_list(),
                     'region': get_region_list(),
                     'year': get_year_list()
                     }
    if arg == 'sector':
        prop_var = prop_function['sector']
    elif arg == 'pestle':
        prop_var = prop_function['pestle']
    elif arg == 'topic':
        prop_var = prop_function['topic']
    elif arg == 'region':
        prop_var = prop_function['region']
    elif arg == 'start_year':
        prop_var = prop_function['year']

    for i in prop_var:
        v_list = list()
        v_list1 = list()
        v_list2 = list()
        for data in DashboardData.objects.values('intensity', 'relevance', 'likelihood').filter(
                **{arg: i}):  # Energy queryset in form of list
            if 'intensity' in data:
                if data['intensity'] != '':
                    for v in data['intensity']:
                        v = int(v)
                        v_list.append(v)
                x_int[i] = sum(v_list) / len(v_list)
            if 'relevance' in data:
                if data['relevance'] != '':
                    for v in data['relevance']:
                        v = int(v)
                        v_list1.append(v)
                x_rel[i] = sum(v_list1) / len(v_list1)
            if 'likelihood' in data:
                if data['likelihood'] != '':
                    for v in data['likelihood']:
                        v = int(v)
                        v_list2.append(v)
                x_like[i] = sum(v_list2) / len(v_list2)
    return x_int, x_rel, x_like


def get_year_list():
    year_list = list()
    year = DashboardData.objects.values('start_year').distinct()
    for i in year:
        for k, v in i.items():
            if v != '':
                year_list.append(v)
    return year_list


def home(request):
    query = DashboardData.objects.values('title','topic','start_year','intensity','region','sector','pestle')
    q_list = list()
    for i in query:
        q_list.append(i)

    context = {
        'topic': get_topic_list(),
        'sector': get_sector_list(),
        'region': get_region_list(),
        'pestle': get_pestle_list(),
        'year': get_year_list(),
        'table_data': q_list
    }

    if request.method == 'POST' and 'submit' in request.POST:
        property = request.POST.get('get_property')
        sector = request.POST.get('get_sector')
        topic = request.POST.get('get_topic')
        region = request.POST.get('get_region')
        pestle = request.POST.get('get_pestle')
        year = request.POST.get('get_year')

        if property == 'sector':
            if sector == 'All':
                context = {
                    'property': property,
                    'prop_value': sector,
                    'topic': get_topic_list(),
                    'sector': get_sector_list(),
                    'region': get_region_list(),
                    'pestle': get_pestle_list(),
                    'year': get_year_list(),
                    'data_int': get_x_prop(property)[0],
                    'data_rel': get_x_prop(property)[1],
                    'data_like': get_x_prop(property)[2],
                    'table_data': q_list
                }
            else:
                context = {
                    'property': property,
                    'prop_value': sector,
                    'topic': get_topic_list(),
                    'sector': get_sector_list(),
                    'region': get_region_list(),
                    'pestle': get_pestle_list(),
                    'year': get_year_list(),
                    'data_int': {sector: get_x_prop(property)[0][sector]},
                    'data_rel': {sector: get_x_prop(property)[1][sector]},
                    'data_like': {sector: get_x_prop(property)[2][sector]},
                    'table_data': q_list
                }
                return render(request, template_name='home.html', context=context)

        elif property == 'topic':
            if topic == 'All':
                context = {
                    'property': property,
                    'prop_value': topic,
                    'topic': get_topic_list(),
                    'sector': get_sector_list(),
                    'region': get_region_list(),
                    'pestle': get_pestle_list(),
                    'year': get_year_list(),
                    'data_int': get_x_prop(property)[0],
                    'data_rel': get_x_prop(property)[1],
                    'data_like': get_x_prop(property)[2],
                    'table_data': q_list
                }
            else:
                context = {
                    'property': property,
                    'prop_value': topic,
                    'topic': get_topic_list(),
                    'sector': get_sector_list(),
                    'region': get_region_list(),
                    'pestle': get_pestle_list(),
                    'year': get_year_list(),
                    'data_int': {topic: get_x_prop(property)[0][topic]},
                    'data_rel': {topic: get_x_prop(property)[1][topic]},
                    'data_like': {topic: get_x_prop(property)[2][topic]},
                    'table_data': q_list
                }
                return render(request, template_name='home.html', context=context)

        elif property == 'region':
            if region == 'All':
                context = {
                    'property': property,
                    'prop_value': region,
                    'topic': get_topic_list(),
                    'sector': get_sector_list(),
                    'region': get_region_list(),
                    'pestle': get_pestle_list(),
                    'year': get_year_list(),
                    'data_int': get_x_prop(property)[0],
                    'data_rel': get_x_prop(property)[1],
                    'data_like': get_x_prop(property)[2],
                    'table_data': q_list
                }
            else:
                context = {
                    'property': property,
                    'prop_value': region,
                    'topic': get_topic_list(),
                    'sector': get_sector_list(),
                    'region': get_region_list(),
                    'pestle': get_pestle_list(),
                    'year': get_year_list(),
                    'data_int': {region: get_x_prop(property)[0][region]},
                    'data_rel': {region: get_x_prop(property)[1][region]},
                    'data_like': {region: get_x_prop(property)[2][region]},
                    'table_data': q_list
                }
                return render(request, template_name='home.html', context=context)

        elif property == 'pestle':
            if pestle == 'All':
                context = {
                    'property': property,
                    'prop_value': pestle,
                    'topic': get_topic_list(),
                    'sector': get_sector_list(),
                    'region': get_region_list(),
                    'pestle': get_pestle_list(),
                    'year': get_year_list(),
                    'data_int': get_x_prop(property)[0],
                    'data_rel': get_x_prop(property)[1],
                    'data_like': get_x_prop(property)[2],
                    'table_data': q_list
                }
            else:
                context = {
                    'property': property,
                    'prop_value': pestle,
                    'topic': get_topic_list(),
                    'sector': get_sector_list(),
                    'region': get_region_list(),
                    'pestle': get_pestle_list(),
                    'year': get_year_list(),
                    'data_int': {pestle: get_x_prop(property)[0][pestle]},
                    'data_rel': {pestle: get_x_prop(property)[1][pestle]},
                    'data_like': {pestle: get_x_prop(property)[2][pestle]},
                    'table_data': q_list
                }
                return render(request, template_name='home.html', context=context)

        elif property == 'start_year':
            if year == 'All':
                context = {
                    'property': property,
                    'prop_value': year,
                    'topic': get_topic_list(),
                    'sector': get_sector_list(),
                    'region': get_region_list(),
                    'pestle': get_pestle_list(),
                    'year': get_year_list(),
                    'data_int': get_x_prop(property)[0],
                    'data_rel': get_x_prop(property)[1],
                    'data_like': get_x_prop(property)[2],
                    'table_data': q_list
                }
            else:
                context = {
                    'property': property,
                    'prop_value': year,
                    'topic': get_topic_list(),
                    'sector': get_sector_list(),
                    'region': get_region_list(),
                    'pestle': get_pestle_list(),
                    'year': get_year_list(),
                    'data_int': {year: get_x_prop(property)[0][year]},
                    'data_rel': {year: get_x_prop(property)[1][year]},
                    'data_like': {year: get_x_prop(property)[2][year]},
                    'table_data': q_list
                }
                return render(request, template_name='home.html', context=context)

    return render(request, template_name='home.html', context=context)