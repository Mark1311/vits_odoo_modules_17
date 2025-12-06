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
    'name': 'Website Product Internal Reference Variantwise',
    'version': '17.1.1',
    'category': 'website',
    'sequence': 1,
    'summary': "Website Product Internal Reference Variantwise | Display Internal Reference on Website Shop | Show Variant-wise Product Internal Code | Website Product Internal Reference (Default Code) | Ecommerce Product Internal Reference Display | Shop Product Extra Details Customers | Improve Product Identification on Website | Transparent Variant-wise SKU Display Odoo E-Commerce | Enhance customer buying confidence accurate product reference details | Odoo Website Product SKU Customization Module",
    'description': """Website Product Internal Reference Variantwise | Display Internal Reference on Website Shop | Show Variant-wise Product Internal Code | Website Product Internal Reference (Default Code) | Ecommerce Product Internal Reference (SKU) Display | Shop Product Extra Details Customers | Improve Product Identification on Website | Transparent Variant-wise SKU Display Odoo E-Commerce | Enhance customer buying confidence accurate product reference details | Odoo Website Product SKU Customization Module""",
    'depends': ['base', 'sale_management', 'website'],
    'keywords': [
        'website product internal reference',
        'odoo website show internal reference',
        'ecommerce product sku display',
        'variant wise internal reference',
        'show default code on website',
        'odoo website product variant code',
        'internal reference for product variants',
        'website product extra details',
        'display sku on product page',
        'odoo ecommerce product code',
        'variant internal reference customization',
        'product internal reference on shop page',
        'sku display system odoo',
        'odoo product page enhancement',
        'dynamic internal reference update',
        'product variant info ecommerce',
        'odoo website variant details visibility',
        'variant default code on product view',
        'ecommerce sku management',
        'shop product internal reference',
    ],
    'author': 'Varanval IT Solutions',
    'company': 'Varanval IT Solutions',
    'price': '6.00',
    'currency': 'USD',
    'data': [
        'views/website_sales_template.xml',
        'views/res_config_settings.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'vits_website_default_code/static/src/js/inherit_sale_variant_mixin.js',
        ],
    },
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',
}
