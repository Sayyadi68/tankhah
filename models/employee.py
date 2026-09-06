from odoo import fields, models


class Employee(models.Model):
    _name = 'expense.manager.employee'
    _description = 'Employee'
    _rec_name = 'user_id'

    user_id = fields.Many2one('res.users', string='نام کارمند', required=True)
    expense_ids = fields.One2many('expense.manager.expense', 'employee_id', string='درخواست‌های هزینه')