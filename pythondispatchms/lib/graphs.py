# -*- coding: utf-8 -*-
"""The base Controller API."""

from pygal.style import Style
from pythondispatchms.lib.rest import TelefonicaRest
from tg import app_globals
import pygal

class GraphApi(TelefonicaRest):
    def __init__(self):
        TelefonicaRest.__init__(self)

    def simVolume(self):
        colors = Style(plot_background='#FFFFFF', foreground='#53E89B', background='#000000',foreground_strong='#53A0E8')
        gauge = pygal.SolidGauge(inner_radius=.70, style=colors)
        percent_formatter = lambda x: '{:.10g}%'.format(x)
        gauge.value_formatter = percent_formatter
        id=app_globals.apiUser
        url = "https://m2m-api.telefonica.com:8010/services/REST/GlobalM2M/Customers/v2/r12/customer/" + id
        data = self.get(url,{})
        if 'error' in data:
            return data
        total = data['customerData']['subscriptionCount']
        gauge.add('SIMS \n' + str(total), [{'value': 100, 'max_value': 100}])
        return gauge.render_data_uri()

    def getPosition(self):
        icc = '8952020616170020641'
        url = "https://m2m-api.telefonica.com:8010/services/REST/GlobalM2M/Inventory/v5/r12/sim/icc:" + str(icc) + "/location"
        data = self.get(url, {})
        if 'error' in data:
            return data
        return data

    def poligon(self):
        from math import cos
        xy_chart = pygal.XY()
        xy_chart.title = 'XY Cosinus'
        xy_chart.add('x = cos(y)', [(cos(x / 10.), x / 10.) for x in range(-50, 50, 5)])
        xy_chart.add('y = cos(x)', [(x / 10., cos(x / 10.)) for x in range(-50, 50, 5)])
        xy_chart.add('x = 1', [(1, -5), (1, 5)])
        xy_chart.add('x = -1', [(-1, -5), (-1, 5)])
        xy_chart.add('y = 1', [(-5, 1), (5, 1)])
        xy_chart.add('y = -1', [(-5, -1), (5, -1)])
        xy_chart.render()
        return xy_chart.render_data_uri()
