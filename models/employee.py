from odoo import fields, models


class Employee(models.Model):
    _name = 'expense.manager.employee'
    _description = 'Employee'

    name = fields.Char(string='نام کارمند', required=True)
    user_id = fields.Many2one('res.users', string='کاربر', required=True)
    expense_ids = fields.One2many('expense.manager.expense', 'employee_id', string='درخواست‌های هزینه')