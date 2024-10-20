# -*- coding: utf-8 -*-
{
    'name': "custom_dynamic_report",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts', 'report_xlsx'],

    # always loaded
    'data': [
        'views/menu_items.xml',
        'views/report_wizard_view.xml',
        'views/dynamic_report_view.xml',
        'reports/contact_report_template.xml',
        'security/ir.model.access.csv',
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
