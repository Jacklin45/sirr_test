# coding: utf-8

from dateutil.relativedelta import relativedelta
import time
from odoo import models, api, fields
from odoo.tools.float_utils import float_round


class HrLeaveType(models.Model):
    _inherit = 'hr.leave.type'
    
    leave_sub_type = fields.Selection([('paid_leave','Paid Leave'),('cef','CEF')], string="Leave Sub Type")
    
    
    
    
    
    
    
