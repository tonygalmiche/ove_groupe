# -*- coding: utf-8 -*-

{
    'name': 'OVE - Groupe',
    'version': '1.0',
    'category': 'InfoSaône',
    'description': """
OVE - Groupe
""",
    'author': 'Tony GALMICHE',
    'maintainer': 'InfoSaone',
    'website': 'http://www.infosaone.com',
    'depends': ['base', 'is_ove'],
    'data': ["security/ir.model.access.csv",
             "ove_groupe_view.xml",
             ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
