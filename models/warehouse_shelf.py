from odoo import api, fields, models

class WarehouseShelf(models.Model):
    _name = "warehouse.shelf"
    _description = "Warehouse Shelf"

    name = fields.Char('Name', required=True)
    position = fields.Char('Position Warehouse Shelf')
    size = fields.Char('Size')
    wh_cus_id = fields.Many2one('warehouse.cus', string="Warehouse")