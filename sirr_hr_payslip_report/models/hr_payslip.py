# coding: utf-8

from dateutil.relativedelta import relativedelta
import time
from odoo import models, api, fields
from odoo.tools.float_utils import float_round


class Hrpayslip(models.Model):
    _inherit = 'hr.payslip'
    
    
    def _get_holidays(self):
        total_data = self.env['hr.leave.allocation'].read_group([
            ('employee_id', '=', self.employee_id.id),
            ('holiday_status_id.active', '=', True),
            ('state', '=', 'validate'),
            ('holiday_status_id.leave_sub_type','=', 'paid_leave'),
        ], ['number_of_days:sum', 'employee_id'], ['employee_id'])
        total_results = dict((d['employee_id'][0], d['number_of_days']) for d in total_data)
        
        
        taken_data = self.env['hr.leave'].read_group([
            ('employee_id', '=', self.employee_id.id),
            ('holiday_status_id.active', '=', True),
            ('state', '=', 'validate'),
            ('holiday_status_id.leave_sub_type','=', 'paid_leave'),
            ('date_from','>=',self.date_from),
            ('date_to','<=',self.date_to)
        ], ['number_of_days:sum', 'employee_id'], ['employee_id'])
        taken_results = dict((d['employee_id'][0], d['number_of_days']) for d in taken_data)
        
        for payslip in self:
            payslip.taken_holidays = float_round(taken_results.get(payslip.employee_id.id, 0.0), precision_digits=2)
            payslip.total_allocation_holidays = float_round(total_results.get(payslip.employee_id.id, 0.0), precision_digits=2) - payslip.taken_holidays
            
            
    def _get_cef(self):
        total_data = self.env['hr.leave.allocation'].read_group([
            ('employee_id', '=', self.employee_id.id),
            ('holiday_status_id.active', '=', True),
            ('state', '=', 'validate'),
            ('holiday_status_id.leave_sub_type','=', 'cef'),
        ], ['number_of_days:sum', 'employee_id'], ['employee_id'])
        total_results = dict((d['employee_id'][0], d['number_of_days']) for d in total_data)
        
        taken_data = self.env['hr.leave'].read_group([
            ('employee_id', '=', self.employee_id.id),
            ('holiday_status_id.active', '=', True),
            ('state', '=', 'validate'),
            ('date_from','>=',self.date_from),
            ('date_to','<=',self.date_to),
            ('holiday_status_id.leave_sub_type','=', 'cef'),
        ], ['number_of_days:sum', 'employee_id'], ['employee_id'])
        taken_results = dict((d['employee_id'][0], d['number_of_days']) for d in taken_data)
        
        for payslip in self:
            payslip.taken_cef = float_round(taken_results.get(payslip.employee_id.id, 0.0), precision_digits=2)
            payslip.total_cef = float_round(total_results.get(payslip.employee_id.id, 0.0), precision_digits=2) - payslip.taken_cef
            
            
        
    total_allocation_holidays = fields.Float('Total Holidays', compute="_get_holidays")
    taken_holidays = fields.Float('Taken Holidays', compute="_get_holidays")
    taken_cef = fields.Float('Taken Holidays', compute="_get_cef")
    total_cef = fields.Float('Total CEF', compute="_get_cef")
    
    
    
