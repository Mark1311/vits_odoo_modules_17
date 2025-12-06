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
import logging
from odoo import fields, models, api

_logger = logging.getLogger(__name__)


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    pos_auto_invoice_enable = fields.Boolean(string="Enable Auto Invoice")
    pos_skip_invoice_pdf_download = fields.Boolean(string="Skip Invoice PDF Download")

    @api.model
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        param = self.env['ir.config_parameter'].sudo()
        param.set_param('res.config.settings.pos_auto_invoice_enable', self.pos_auto_invoice_enable)
        param.set_param('res.config.settings.pos_skip_invoice_pdf_download', self.pos_skip_invoice_pdf_download)

        _logger.info(
            f"✅ [SET] pos_auto_invoice_enable = {self.pos_auto_invoice_enable}, {self.pos_skip_invoice_pdf_download}")

    def get_values(self):
        res = super().get_values()
        param = self.env['ir.config_parameter'].sudo()

        res.update(
            pos_auto_invoice_enable=param.get_param('res.config.settings.pos_auto_invoice_enable'),
            pos_skip_invoice_pdf_download=param.get_param('res.config.settings.pos_skip_invoice_pdf_download')
        )
        _logger.info(
            f"✅ [GET] pos_auto_invoice_enable = {self.pos_auto_invoice_enable}, {self.pos_skip_invoice_pdf_download}")
        return res

    @api.onchange('pos_auto_invoice_enable')
    def _onchange_pos_auto_invoice_enable(self):
        if self.pos_auto_invoice_enable != True:
            self.pos_skip_invoice_pdf_download = False
