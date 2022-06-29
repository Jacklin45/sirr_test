# coding: utf-8

from dateutil.relativedelta import relativedelta
import time
from odoo import models, api, fields


class HrSalaryRule(models.Model):
    _inherit = 'hr.salary.rule'
    
    type = fields.Selection(selection=[('gain','Gain'),('retenu','Retenu')])

    
