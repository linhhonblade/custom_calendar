# -*- coding: utf-8 -*-
{
    'name': "custom_calendar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['calendar'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/calendar_views.xml',
    ],
    'qweb': [],
    # only loaded in demonstration mode
    'demo': [],
}
