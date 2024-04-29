/** @odoo-module */

import {Order} from "@point_of_sale/app/store/models";
import {patch} from "@web/core/utils/patch";
import {onMounted} from "@odoo/owl";
import { ErrorPopup } from "@point_of_sale/app/errors/popups/error_popup";
import { _t } from "@web/core/l10n/translation";

patch(Order.prototype, {
    export_as_JSON() {
        const json = super.export_as_JSON(...arguments);
        json.invoice_reference = this.invoice_reference
        return json;
    },

    init_from_JSON(json) {
        super.init_from_JSON(...arguments);
        this.invoice_reference = json.invoice_reference;
    },

    export_for_printing() {
        const result = super.export_for_printing(...arguments);
        result.invoice_reference = this.invoice_reference;
        return result;
    },

    set_order_invoice_reference(invoice_reference) {
        this.invoice_reference = invoice_reference || "";
    },

});
