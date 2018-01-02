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
        'security/account_security.xml',
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
        'security/ir.model.access.csv',
    ],
    'demo': [
        'demo/demo_category_details.xml',
        'demo/demo_publisher_details.xml',
        'demo/demo_auther_details.xml',
        'demo/demo_student_details.xml',
        'demo/demo_materials.xml',
        'demo/demo_book_details.xml',
        'demo/demo_issue_book.xml',
        'demo/demo_return_book.xml',
    ],
    'qweb': [
    ],
    'installable': True,
    'auto_install': False,
}