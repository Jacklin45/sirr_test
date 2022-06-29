# -*- coding: utf-8 -*-

from odoo import models, fields, api

from datetime import date, timedelta

from odoo.tools import date_utils


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    bank_name = fields.Many2one('list.bank', string="Bank name")
    sirr_check_number = fields.Char("SIRR Check number")
    due_date = fields.Date("Due date")


class AccountMove(models.Model):
    _inherit = "account.move"

    def _get_starting_sequence(self):
        self.ensure_one()
        if self.invoice_filter_type_domain == 'purchase':
        # if self.journal_id.type == 'purchase':
            starting_sequence = "%s/%04d/000000" % (self.journal_id.code, self.date.year)
            return starting_sequence
        else:
            return super(AccountMove, self)._get_starting_sequence()

    def _get_accounting_date(self, invoice_date, has_tax):
        res = super(AccountMove, self)._get_accounting_date(invoice_date, has_tax)
        if self.invoice_filter_type_domain == 'purchase':
        # if self.move_type in ('in_invoice'):
            today = fields.Date.today()
            highest_name = self.highest_name or self._get_last_sequence(relaxed=True)
            number_reset = self._deduce_sequence_number_reset(highest_name)
            if self.invoice_filter_type_domain == 'purchase':
                if not highest_name or number_reset == 'month':
                    if (today.year, today.month) > (self.invoice_date.year, self.invoice_date.month):
                        return max(self.invoice_date, today)
        return res
