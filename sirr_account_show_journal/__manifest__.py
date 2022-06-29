# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2019 eTech Consulting (<http://www.etechconsulting-mg.com>). All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'SIRR account show journal',
    'version': '1.0',
    'category': '',
    'sequence': -4,
    'summary': '',

    'author': 'eTech Consulting',
    "website": 'http://www.etechconsulting-mg.com',

    'depends': ['base', 'account'],

    'description': """
Manage SIRR account journal item
=================================
This modules show the journal item menu even though the debug mode is not activated

    """,
    'data': [
        # security
        # data
        # views
        'views/account_menuitem.xml',
    ],
    'qweb': [],
    'demo': [],
    'installable': True,
    'application': False,
}