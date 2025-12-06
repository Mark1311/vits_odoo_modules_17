/** @odoo-module **/

import VariantMixin from "@website_sale/js/sale_variant_mixin";
import { rpc } from "@web/core/network/rpc";

const oldOnChangeCombination = VariantMixin._onChangeCombination;

VariantMixin._onChangeCombination = function (ev, $parent, combination) {

    oldOnChangeCombination.apply(this, arguments);

    if (!combination.product_id) {
        return;
    }

    rpc("/get_variant_default_code", {
        product_id: combination.product_id,
    }).then(default_code => {

        const refEl = document.querySelector("#variant_default_code");
        if (refEl) {
            refEl.textContent = default_code || "";
        }
    });
};
