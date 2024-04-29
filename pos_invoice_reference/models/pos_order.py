from odoo import models, fields, api


class ProductPriceList(models.Model):
    _inherit = 'product.pricelist'

    invoice_reference = fields.Boolean(string='Invoice Reference')


class PosOrder(models.Model):
    _inherit = 'pos.order'

    invoice_reference = fields.Char(string='Invoice Reference')

    @api.model
    def _order_fields(self, ui_order):
        result = super(PosOrder, self)._order_fields(ui_order)
        if ui_order.get('invoice_reference'):
            result['invoice_reference'] = ui_order['invoice_reference']
        return result

