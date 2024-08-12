# -*- coding: utf-8 -*-
###############################################################################
#
#    Code Craft System
#
#    Copyright (C) 2024-TODAY Code Craft System (<https://www.codecraftsystem.com>)
#    Author: Code Craft System (codecraftsystem@gmail.com)
#
###############################################################################
{
    "name": "POS Invoice Reference",
    'summary': "Associate  Order References with New Orders for Easy Backend Search",

    'description': """
        The POS Invoice Reference module allows users to associate old order references with new orders. When customers need to modify,
        return, or exchange items from a previous order, they can add the old order reference to the new order.
        This feature simplifies order tracking and search in the backend, making it easier for staff to locate relevant orders.
     """,

    'author': 'Ahmad Khan',
    'company': 'codecraftsystem@gmail.com',
    'maintainer': 'codecraftsystem@gmail.com',
    'category': 'Point of Sale',
    'version': '0.1',

    'depends': ['base', 'point_of_sale', 'product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],

    "assets": {
        'point_of_sale._assets_pos': [
            'pos_invoice_reference/static/src/**/*',
        ],
    },
    "images":
        [
            'images/img_2.png',
        ],

    "installable": True,
    "auto_install": False,
    'live_test_url': 'https://youtu.be/RdsbeDMhBkI',
    'license': 'OPL-1',
    'price': 9.99,
    'currency': 'USD',
}
