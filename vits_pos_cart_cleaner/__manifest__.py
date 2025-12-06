# -*- coding: utf-8 -*-
###############################################################################
# Author      : Varanval IT Solutions
# Copyright   : (c) 2025 Varanval IT Solutions. All Rights Reserved.
#
# This software and associated files are the copyrighted property of Varanval IT Solutions.
# Unauthorized copying, redistribution, or modification of any part of this code
# is strictly prohibited unless expressly permitted by the author.
#
# This module is a paid product. It is licensed for use only by the customer
# who has purchased it, and only for the number of users specified at purchase.
#
# For licensing inquiries, contact: markvaranval@gmail.com
###############################################################################
{
    'name': 'Pos Cart Cleaner | Cart Cleaner',
    'version': '17.1.1',
    'category': 'Point of Sale',
    'sequence': 1,
    'summary': "Clear POS cart instantly, POS clear cart button, Remove all products, Reset POS order, POS cart cleaner, POS empty cart, One-click POS cart clear, POS cart management tool",
    'description': """Clear POS cart instantly with a single click. Adds a 'Clear Cart' button in the POS interface to remove all cart items quickly. 
                        POS clear cart module helps in faster order resets, better POS control, and improves cashier efficiency. 
                        Reset POS cart, clear POS order lines, empty cart in one tap. Seamless POS cart cleaner solution for shops and restaurants using Odoo POS. 
                        POS cart management made easier — clean cart, speed up workflow, and start fresh orders instantly.""",
    'depends': ['base', 'web', 'sale_management', 'point_of_sale'],
    'keywords': [
    'pos', 'clear cart', 'cart cleaner', 'odoo pos', 'reset pos cart', 'remove all products', 
    'point of sale', 'pos customization', 'fast pos order', 'one click pos cart reset',],
    'author': 'Varanval IT Solutions',
    'company': 'Varanval IT Solutions',
    'price': '4.00',
    'currency': 'USD',
    'data': [
        'views/res_config_settings.xml.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'vits_pos_cart_cleaner/static/src/xml/cart_clean_button.xml',
            'vits_pos_cart_cleaner/static/src/js/inherit_ControleButton.js',
        ],
    },
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',
}
