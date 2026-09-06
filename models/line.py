from odoo import api, fields, models


class Line(models.Model):
    _name = 'expense.manager.line'
    _description = 'Expense Line'

    expense_id = fields.Many2one('expense.manager.expense', string='درخواست هزینه', required=True, ondelete='cascade')
    type_id = fields.Many2one('expense.manager.type', string='نوع هزینه', required=True, ondelete='restrict')
    quantity = fields.Float(string='تعداد', required=True, default=1.0)
    unit_price = fields.Float(string='قیمت واحد', required=True)
    total_amount = fields.Float(string='مبلغ کل', compute='_compute_total_amount', store=True)

    @api.depends('quantity', 'unit_price')
    def _compute_total_amount(self):
        for record in self:
            record.total_amount = record.quantity * record.unit_price