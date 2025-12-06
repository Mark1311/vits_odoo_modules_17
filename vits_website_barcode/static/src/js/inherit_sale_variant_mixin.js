/** @odoo-module **/

import VariantMixin from "@website_sale/js/sale_variant_mixin";
import { rpc } from "@web/core/network/rpc";

const oldOnChangeCombination = VariantMixin._onChangeCombination;

VariantMixin._onChangeCombination = function (ev, $parent, combination) {

    oldOnChangeCombination.apply(this, arguments);

    const productId = combination.product_id || combination.variant_id;

    if (!productId) {
        return;
    }

    rpc("/get_variant_barcode", { product_id: productId })
        .then(code => {
            console.log("Variant Code:", code);

            const el = document.querySelector("#variant_barcode");
            if (el) {
                el.textContent = code || "";
            }
        });
};
