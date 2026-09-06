from odoo import api, fields, models


class Expense(models.Model):
    _name = 'expense.manager.expense'
    _description = 'Expense Request'

    name = fields.Char(string='شماره درخواست', required=True)
    employee_id = fields.Many2one('expense.manager.employee', string='کارمند', required=True, ondelete='restrict')
    date = fields.Date(string='تاریخ درخواست', required=True, default=fields.Date.context_today)
    line_ids = fields.One2many('expense.manager.line', 'expense_id', string='اقلام هزینه')
    total_amount = fields.Float(string='جمع کل', compute='_compute_total_amount', store=True)
    state = fields.Selection([('draft', 'پیش‌نویس'), ('submitted', 'ارسال شده'), ('approved', 'تایید شده'), ('rejected', 'رد شده')], string='وضعیت', default='draft', required=True)

    @api.depends('line_ids.total_amount')
    def _compute_total_amount(self):
        for record in self:
            record.total_amount = sum(record.line_ids.mapped('total_amount'))