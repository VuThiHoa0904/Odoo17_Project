from odoo import api, fields, models

class DeliveryBill(models.Model):
    _name = "delivery.bill"
    _description = "Delivery Bill"

    name = fields.Char(string='Name', required=True)
    company_id = fields.Many2one(
        'res.company', string='Company', default=lambda self: self.env.company,
        readonly=True, required=True,
        help='The company is automatically set from your user preferences.')
    driver_id = fields.Many2one('res.users', string='Deliver')
    date = fields.Date(string="Date")
    address = fields.Char(string='Address')
    warehouse_id = fields.Many2one('warehouse.cus', string='Warehouse')
    bill_line_ids = fields.One2many('delivery.bill.line', 'bill_id', string='Bill line')
    total_amount_bill = fields.Float(string="Total")
    fleet_id = fields.Many2one('fleet.vehicle', string='Fleet')

class DeliveryBillLine(models.Model):
    _name = "delivery.bill.line"
    _description = "Delivery Bill Line"

    bill_id = fields.Many2one('delivery.bill', string='Bill')
    product_id = fields.Many2one('product.product', string='Product')
    quantity = fields.Float(string="Quantity")
    price = fields.Float(string="Price")
    total_amount = fields.Float(string="Total amount")

