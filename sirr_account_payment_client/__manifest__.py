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
    'name': 'SIRR account payment client',
    'version': '1.0',
    'category': '',
    'sequence': -4,
    'summary': '',

    'author': 'eTech Consulting',
    "website": 'http://www.etechconsulting-mg.com',

    'depends': ['base', 'account'],
    # 'depends': ['base', 'account', 'account_batch_payment', 'sirr_check_printing'],

    'description': """
Manage SIRR account payment client
===============================================
This modules add tax fields on payment

    """,
    'data': [
        # security
        # data
        # views
        # 'views/account_payment_view.xml',
        # 'views/account_batch_payment_views.xml',
        # 'views/account_move_views.xml',
        # 'views/hr_expense_views.xml',
        # 'wizard/account_payment_register_views.xml',
    ],
    'qweb': [],
    'demo': [],
    'installable': True,
    'application': False,
}
