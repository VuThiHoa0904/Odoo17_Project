from odoo import api, fields, models


class Product(models.Model):
    _inherit = "product.product"

    wh_shelf_id = fields.Many2one('warehouse.shelf', string="Warehouse Shelf")
    wh_cus_id = fields.Many2one('warehouse.cus', string="Warehouse")
    number = fields.Integer(string="Number")

    @api.onchange('wh_shelf_id')
    def onchange_wh(self):
        for rec in self:
            rec.wh_cus_id = rec.wh_shelf_id.wh_cus_id.id
    # def write(self, vals):
    #     res = super(Product, self).write(vals)
    #     if vals.get('wh_cus_id'):
    #         ls = []
    #         for i in vals.get('wh_cus_id'):
    #             ls.append(i[1])
    #         wh_ids = self.env['warehouse.cus'].search([('id', 'in', ls)])
    #         for w in wh_ids:
    #             w.product_product_ids = [(4, self.id)]
    #     return res

    @api.model
    def _name_search(self, name, domain=None, operator='ilike', limit=None, order=None):
        if self.env.context.get('warehouse_id'):
            wh_ids = self.env.context.get('warehouse_id')
            domain = [('wh_cus_id', 'in', [wh_ids]), ('number', '>', 0)]
        return super()._name_search(name, domain, operator, limit, order)
