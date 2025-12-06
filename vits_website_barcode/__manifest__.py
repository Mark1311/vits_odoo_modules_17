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
    'name': 'Website Product Barcode',
    'version': '17.1.1',
    'category': 'Point of Sale',
    'sequence': 1,
    'summary': "Website Product Barcode | Show Barcode on Odoo Website | Display Product Variant Barcode | Variant-wise Dynamic Barcode View | Auto Switch Barcode on Attribute Selection | Enhance Product Identification | Improve Online Shopping Accuracy | Odoo eCommerce Product Barcode Display | Better User Experience for Website Customers | Barcode Visibility for Shop Page & Product Page",
    'description': """Website Product Barcode | Show Barcode on Odoo Website | Display Product Variant Barcode | Variant-wise Dynamic Barcode View | Auto Switch Barcode on Attribute Selection | Enhance Product Identification | Improve Online Shopping Accuracy | Odoo eCommerce Product Barcode Display | Better User Experience for Website Customers | Barcode Visibility for Shop Page & Product Page""",
    'depends': ['base', 'sale_management', 'website', 'website_sale'],
    'keywords': [
        'website product barcode',
        'odoo website barcode display',
        'show barcode on website product page',
        'variant-wise product barcode',
        'Product Multiple Barcodes',
        'odoo e-commerce barcode module',
        'display barcode on product variants',
        'POS Multi Barcodes-Product Multi Barcode'
        'product barcode visibility in website shop',
        'barcode for product variants odoo',
        'enhance website product details barcode',
        'barcode on product page Odoo 18',
        'odoo website product customization',
        'ecommerce product barcode addon',
        'product variant barcode integration',
        'odoo webshop barcode support',
        'scan-ready barcode for customers',
        'barcode preview on product page',
        'Odoo website sale barcode module',
        'barcode for online store products',
        'variant selection updates barcode',
        'dynamic barcode with attribute variants'
    ],
    'author': 'Varanval IT Solutions',
    'company': 'Varanval IT Solutions',
    'price': '5.00',
    'currency': 'USD',
    'data': [
        'views/website_sales_template.xml',
        'views/res_config_settings.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'vits_website_barcode/static/src/js/inherit_sale_variant_mixin.js',
        ],
    },
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',
}
