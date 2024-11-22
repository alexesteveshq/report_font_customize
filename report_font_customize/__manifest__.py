# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Report Font Customize',
    'summary': 'Adjust font size in reports. (Report Font Configurator | Report Font | Report Font Size | Font Size)',
    'description': 'Adjust font size in reports',
    'version': '18.0.1.0',
    'category': 'Reports',
    'author': 'Visionee',
    'license': 'OPL-1',
    'website': 'https://visionee.net',
    'depends': [
        'base', 'web'
    ],
    'data': [
        'views/base_document_layout_views.xml',
        'views/report_templates.xml',
    ],
    'images': [
        'static/description/banner.png',
    ],
    'price': 25,
    'currency': "EUR",
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
}
