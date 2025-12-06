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
from odoo import api, models, fields

_logger = logging.getLogger(__name__)


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    hide_header = fields.Boolean(
        string="Hide POS Header Section",
        related="pos_config_id.hide_header",
        readonly=False,
    )

    hide_inventory = fields.Boolean(
        string="Hide Inventory Menu",
        related="pos_config_id.hide_inventory",
        readonly=False,
    )

    hide_replenishment = fields.Boolean(
        string="Hide Replenishment Menu",
        related="pos_config_id.hide_replenishment",
        readonly=False,
    )

    hide_financial = fields.Boolean(
        string="Hide Financial Menu",
        related="pos_config_id.hide_financial",
        readonly=False,
    )

    hide_order = fields.Boolean(
        string="Hide Orders Menu",
        related="pos_config_id.hide_order",
        readonly=False,
    )

    hide_edit_button = fields.Boolean(
        string="Hide Order Edit Button",
        related="pos_config_id.hide_edit_button",
        readonly=False,
    )
