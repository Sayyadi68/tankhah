{
    'name': 'تنخواه گردون',
    'version': '17.0.1.0.0',
    'category': 'تنخواه/تنخواه',
    'summary': 'سامانه مدیریت تنخواه کارکنان',
    'description': 'سامانه مدیریت تنخواه کارکنان',
    'author': 'صیادی-فهیم-پورشهامی',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/groups.xml',
        'security/security.xml',
        'security/ir.model.access.csv',

        'views/employee_views.xml',
        'views/expense_views.xml',
        'views/line_views.xml',
        'views/type_views.xml',
        'views/line_views.xml',

        'views/menu.xml',

    ],
    'application': True,
    'installable': True,
}
