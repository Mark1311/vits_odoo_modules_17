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
    'name': 'Remove/Hide Powered by Odoo Footer',
    'version': '17.1.1',
    'category': 'website',
    'sequence': 1,
    'summary': "Remove/Hide Powered by Odoo Footer | Clean Login and Website Pages | Hide Odoo Branding | Odoo UI customization | Professional website look | Remove default Odoo footer text | Branding control for Odoo pages | Simple backend toggle | Enhance user experience | Customizable login and website interface | Odoo website module | Footer visibility management | Easy Odoo customization | Clean and professional interface",
    'description': """Easily remove or hide the "Powered by Odoo" footer from login pages and website pages with this Odoo 18 module. Customize your website and login interface for a professional look, enhance user experience, and maintain clean branding. Simple backend toggle allows instant control of footer visibility. Ideal for businesses and developers seeking a polished Odoo interface. Seamless integration ensures easy setup, improved website aesthetics, and a clutter-free UI.""",
    'depends': ['base', 'website'],
    'keywords': [
        'Remove Powered by Odoo',
        'Hide Powered by Odoo',
        'Odoo login footer remove',
        'Odoo website footer hide',
        'Odoo branding remove',
        'Hide Odoo footer',
        'Odoo footer customization',
        'Professional Odoo interface',
        'Clean Odoo login page',
        'Odoo UI customization',
        'Odoo 18 module',
        'Website branding control',
        'Odoo footer toggle',
        'Remove Odoo branding',
        'Login page customization',
        'Website page footer hide',
        'Odoo interface polish',
        'Odoo UI optimization',
        'Clutter-free Odoo login',
        'Odoo admin toggle',
        'Advance Hide Powered by Odoo'
    ],
    'author': 'Varanval IT Solutions',
    'company': 'Varanval IT Solutions',
    'price': '3.00',
    'currency': 'USD',
    'data': [
        'views/weblogin_template.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
        ],
    },
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',
}
