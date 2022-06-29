# -*- coding: utf-8 -*-

from odoo import models, fields


class AccountPaymentRegister(models.TransientModel):
    _inherit = 'account.payment.register'

    bank_name = fields.Many2one('list.bank', "Bank name")
    sirr_check_number = fields.Char("SIRR Check number")
    date_due = fields.Date(string=u"Date d'échéance chèque/traite")
    date_instrument = fields.Date(string="Date d'instrument")

    def _create_payment_vals_from_wizard(self):
        invoice_id = self.env['account.move'].browse(self._context.get('active_id'))

        if 'model_active' in self._context:
            payment_vals = {
                'date': self.payment_date,
                'amount': self.amount,
                'payment_type': self.payment_type,
                'partner_type': self.partner_type,
                'ref': self.communication,
                'journal_id': self.journal_id.id,
                'currency_id': self.currency_id.id,
                'partner_id': self.partner_id.id,
                'partner_bank_id': self.partner_bank_id.id,
                'payment_method_id': self.payment_method_id.id,
                'destination_account_id': self.line_ids[0].account_id.id,
                'bank_id': self.bank_name.id,
                'check_number_2': self.sirr_check_number,
                'date_instrument': self.date_instrument,
                'invoice_due_date': self.date_due,
            }

        else:
            payment_vals = {
                'date': self.payment_date,
                'amount': self.amount,
                'payment_type': self.payment_type,
                'partner_type': self.partner_type,
                'ref': self.communication,
                'journal_id': self.journal_id.id,
                'currency_id': self.currency_id.id,
                'partner_id': self.partner_id.id,
                'partner_bank_id': self.partner_bank_id.id,
                'payment_method_id': self.payment_method_id.id,
                'destination_account_id': self.line_ids[0].account_id.id,
                'bank_id': self.bank_name.id,
                'check_number_2': self.sirr_check_number,
                'date_instrument': self.date_instrument,
                'invoice_due_date': self.date_due if self.date_due else invoice_id.invoice_date_due,
            }

        if not self.currency_id.is_zero(self.payment_difference) and self.payment_difference_handling == 'reconcile':
            payment_vals['write_off_line_vals'] = {
                'name': self.writeoff_label,
                'amount': self.payment_difference,
                'account_id': self.writeoff_account_id.id,
            }

        return payment_vals