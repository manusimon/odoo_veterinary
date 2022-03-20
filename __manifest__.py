# -*- coding: utf-8 -*-
{
    'name': "odoo_veterinary",

    'summary': """
        Gestor de animales de un veterinario
        """,

    'description': """
        Gestionar las altas de los animales para un veterinario
    """,

    'author': "Simón Barreiro",
    'website': "http://gitlab.com/a20simonbg/odoo_veterinary",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [],

    # carga la vista y los permisos
    'data': [
        'security/ir.model.access.csv',
        'views/veterinary_view_patient.xml',
        'views/veterinary_view_incident.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}
