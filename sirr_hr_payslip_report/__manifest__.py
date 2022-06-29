# -*- encoding: utf-8 -*-

{
    'name': 'SIRR hr payroll payslip balance of accounts printed',
    'version': '1.0',
    'category': '',
    'sequence': -4,
    'summary': '',

    'author': 'eTech Consulting',
    "website": 'http://www.etechconsulting-mg.com',

    'depends': ['base','web','hr_payroll','hr_holidays', 'account','partner_fisc'],

    'description': """
Manage SIRR hr payroll payslip balance of accounts
===================================================
This module allows to print Payslip or the ballance of accounts

    """,
    'data': [
        'data/report_payslip_paperformat.xml',
        'views/report_payslip_templates.xml',
        'views/hr_salary_rule_views.xml',
        'report/report_payslip.xml',
        'views/hr_payslip_views.xml',
        'views/hr_leave_type_views.xml'
    ],
    'qweb': [],
    'demo': [],
    'installable': True,
    'application': False,
}
