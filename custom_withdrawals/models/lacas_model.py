from odoo import api, fields, models, _


class academics_tab(models.Model):

    _inherit = 'account.move'
    facts_id_cred_custom = fields.Char(string='Facts Id')
    udid_cred_custom = fields.Char(string='UDID')
    acadamic_status = fields.Char(string='Status')
    rollno_cred_custom = fields.Char(string='Roll No')
    remarks_cred_custom = fields.Char(string='REMARKS')
    relationship_cred_custom = fields.Selection([('Father', 'Father'), ('Mother', 'Mother'), ('Uncle', 'Uncle'), ('Aunt', 'Aunt'), ('Brother', 'Brother'), (
        'Sister', 'Sister'), ('Grandparent', 'Grandparent'), ('Friend', 'Friend'), ('Guardian', 'Guardian'), ('Other', 'Other')], string="Relation With Student")
    financial_responsibilty_cred_custom = fields.Selection(
        [('Yes', 'Yes'), ('No', 'No')], string="Financial Responsibilty")

    refund_receive = fields.Char(
        compute='_compute_refund_receive', string="Receivable/Refundable")

    def _compute_refund_receive(self):
        if self.x_studio_charges:
            refund = 0
            receive = 0
            if self.x_studio_charges.invoice_line_ids:

                for i in self.x_studio_charges.invoice_line_ids:
                    refund = i.price_subtotal
            if self.invoice_line_ids:
                for j in self.invoice_line_ids:
                    receive = j.price_subtotal

            if receive > refund:
                self.refund_receive = 'Receivable'
            else:
                self.refund_receive = 'Refundable'
        else:
            self.refund_receive = ""
#   record.write({'x_receivable_refundable': 'receivable'})
