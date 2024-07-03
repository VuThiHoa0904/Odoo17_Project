from odoo import api, fields, models


class WarehouseCus(models.Model):
    _name = "warehouse.cus"
    _description = "Warehouse Custom"

    name = fields.Char('Name', required=True)
    company_id = fields.Many2one(
        'res.company', 'Company', default=lambda self: self.env.company,
        readonly=True, required=True,
        help='The company is automatically set from your user preferences.')
    address = fields.Char('Address')
    product_product_ids = fields.One2many('product.product', 'wh_cus_id', string='Products' )
