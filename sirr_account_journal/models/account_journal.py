# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountJournal(models.Model):
    _inherit = "account.journal"

    user_id = fields.Many2one('res.users', string="User concerned")
    # user_id = fields.Many2one('res.users', string="User concerned",
    #                           domain=[('company_id.name', '=', 'ABC'), ('group_id.name', '=', 'CAISSE')])
