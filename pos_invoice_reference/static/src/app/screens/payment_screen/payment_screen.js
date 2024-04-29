/** @odoo-module */

import { PaymentScreen } from "@point_of_sale/app/screens/payment_screen/payment_screen";
import { patch } from "@web/core/utils/patch";
const { Component,  useState } = owl;
import { ErrorPopup } from "@point_of_sale/app/errors/popups/error_popup";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { _t } from "@web/core/l10n/translation";
import { useAutofocus, useService } from '@web/core/utils/hooks';

patch(PaymentScreen.prototype, {
     setup() {
            super.setup(...arguments);
            const selectedOrder = this.pos.get_order();
            this.state = useState({
                invoice_reference: selectedOrder.invoice_reference || '',
            })
     },
     async validateOrder(isForceValidate) {
          const invoice_reference = this.state.invoice_reference;
          await super.validateOrder(...arguments);
    },
    invoiceReference: function (ev) {
        const selectedOrder = this.pos.get_order()
        var newValue = ev.target.value;
        this.state.invoice_reference = newValue;
        selectedOrder.set_order_invoice_reference(this.state.invoice_reference)
     },
});