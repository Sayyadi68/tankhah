from odoo import fields, models


class Type(models.Model):
    _name = 'expense.manager.type'
    _description = 'Expense Type'

    name = fields.Char(string='نوع هزینه', required=True)
    line_ids = fields.One2many('expense.manager.line', 'type_id', string='اقلام خرید')