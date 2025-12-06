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

import {usePos} from "@point_of_sale/app/store/pos_hook";
import {patch} from "@web/core/utils/patch";
import {ControlButtons} from "@point_of_sale/app/screens/product_screen/control_buttons/control_buttons";
import {ConfirmationDialog, AlertDialog} from "@web/core/confirmation_dialog/confirmation_dialog";
import {_t} from "@web/core/l10n/translation";

patch(ControlButtons.prototype, {
    setup() {
        super.setup();
        this.pos = usePos();
    },

    async clearCart() {
        const order = this.pos.get_order();
        if (!order || order.get_orderlines().length === 0) {
            this.dialog.add(AlertDialog, {
                title: _t("Already Clear"),
                body: _t("The cart is already empty."),
            });
            return;
        }

        this.dialog.add(ConfirmationDialog, {
            title: _t("Clear Cart?"),
            body: _t("This will remove all items from the cart. This action cannot be undone."),
            confirm: () => {
                const lines = order.get_orderlines().slice();
                lines.forEach(line => order.removeOrderline(line));
            },
        });
    }
});
