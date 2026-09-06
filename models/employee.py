from odoo import models, fields


class Employee(models.Model):
    _name = 'expense.employee'
    _description = 'Employee'

    first_name = fields.Char(string='نام', required=True)
    last_name = fields.Char(string='نام خانوادگی', required=True)
    employee_code = fields.Char(string='کد پرسنلی', required=True)
    phone = fields.Char(string='شماره تماس')
    email = fields.Char(string='ایمیل')
    active = fields.Boolean(string='فعال', default=True)