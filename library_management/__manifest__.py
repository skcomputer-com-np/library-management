# -*- coding: utf-8 -*-
{
    'name' : 'Library Management System',
    'version' : '1',
    'summary': 'Manage book related transections',
    'description': """
This is description for library management system.
    """,

    'depends': [
        'sale','web',
    ],

    'data': [
        'views/book_details_view.xml',
        'views/issue_book_view.xml',
        'views/return_book_view.xml',
        'views/student_details.xml',
        'views/category_view.xml',
        'views/publisher_view.xml',
        'views/author_view.xml',
        'wizard/make_price.xml',
        'wizard/make_student_divison.xml',
        'wizard/student_wizard_report.xml',
        'report/report_menu_item.xml',
        'report/student_report.xml',
        'report/student_wizard_report_view.xml',
    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'auto_install': False,
}