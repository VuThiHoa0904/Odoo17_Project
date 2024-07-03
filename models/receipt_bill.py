from odoo import api, fields, models


class ReceiptBill(models.Model):
    _name = "receipt.bill"
    _description = "Receipt Bill"

    name = fields.Char(string='Name', required=True)
    company_id = fields.Many2one(
        'res.company', string='Company', default=lambda self: self.env.company,
        readonly=True, required=True,
        help='The company is automatically set from your user preferences.')
    driver_id = fields.Many2one('res.users', string='Deliver')
    date = fields.Date(string="Date")
    address = fields.Char(string='Address')
    warehouse_id = fields.Many2one('warehouse.cus', string='Warehouse')
    bill_line_ids = fields.One2many('receipt.bill.line', 'bill_id', string='Bill line')
    total_amount_bill = fields.Float(string="Total", compute='_compute_total_amount_bill', store=True)
    fleet_id = fields.Many2one('fleet.vehicle', string='Fleet')
    vendor_id = fields.Many2one('res.partner', string="Vendor")
    state = fields.Selection([('new', 'New'), ('open', 'In Progress'), ('done', 'Done'), ('fail', 'Fail')],
                             string='Status', default='new',
                             readonly=True)

    @api.depends('bill_line_ids', 'bill_line_ids.total_amount')
    def _compute_total_amount_bill(self):
        amount = 0
        for rec in self:
            for i in rec.bill_line_ids:
                amount += i.total_amount
            rec.total_amount_bill = amount

    def action_submitted(self):
        for rec in self:
            rec.update({
                'state': 'open'
            })

    def action_done(self):
        for rec in self:
            rec.update({
                'state': 'done'
            })
            for i in rec.bill_line_ids:
                i.product_id.update({
                    'number': i.product_id.number + i.quantity
                })

    def action_fail(self):
        for rec in self:
            rec.update({
                'state': 'fail'
            })


class ReceiptBillLine(models.Model):
    _name = "receipt.bill.line"
    _description = "Receipt Bill Line"

    bill_id = fields.Many2one('receipt.bill', string='Bill')
    product_id = fields.Many2one('product.product', string='Product')
    quantity = fields.Integer(string="Quantity")
    price = fields.Float(string="Price", related='product_id.lst_price', readonly=False)
    total_amount = fields.Float(string="Total amount", compute='_compute_total_amount', store=True)

    @api.depends('price', 'quantity')
    def _compute_total_amount(self):
        for rec in self:
            rec.total_amount = rec.quantity * rec.price
