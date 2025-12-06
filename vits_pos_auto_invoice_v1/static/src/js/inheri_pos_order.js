/**
 * ###########################################################################
 * Author      : Varanval IT Solutions
 * Copyright   : (c) 2025 Varanval IT Solutions. All Rights Reserved.
 *
 * This JavaScript file is part of a paid Odoo module developed by Varanval IT Solutions.
 *
 * This module is licensed only for use by the customer who has purchased it,
 * and only for the number of users specified at the time of purchase.
 *
 * For licensing inquiries, contact: markvaranval@gmail.com
 * ###########################################################################
 */
import {PosOrder} from "@point_of_sale/app/models/pos_order";
import {patch} from "@web/core/utils/patch";
import {rpc} from "@web/core/network/rpc";

let autoInvoiceEnable = false;

rpc("/web/dataset/call_kw/ir.config_parameter/get_param", {
    model: 'ir.config_parameter',
    method: 'get_param',
    args: ['res.config.settings.pos_auto_invoice_enable'],
    kwargs: {},
}).then((result) => {
    autoInvoiceEnable = result === 'True';
});

patch(PosOrder.prototype, {
    setup() {
        super.setup(...arguments);
        if (autoInvoiceEnable) {
            this.to_invoice = true;
        }
    },
});
