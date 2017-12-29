# -*- coding: utf-8 -*-
{
    'name' : 'Library Management System',
    'version' : '1',
    'summary': 'Manage book related transections',
    'description': """
This is description for library management system.
    """,

    'depends': [
        'sale',
    ],

    'data': [
        'views/book_details_view.xml',
        'views/issue_book_view.xml',
        'views/return_book_view.xml',
        'views/student_details.xml',
        'views/category_view.xml',
        'views/publisher_view.xml',
        'views/author_view.xml',
    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'auto_install': False,
}
