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

    # notice_fee_withdrawal = fields.Monetary(
    #     compute='_compute_notice_fee', string="Notice Fee")
    # amount_total_withdrawal = fields.Monetary(
    #     compute='_compute_total_amount', string="total withdrawal")
    refund_receive = fields.Char(
        compute='_compute_refund_receive', string="Receivable/Refundable")

    # def _compute_notice_fee(self):
    #     if self.move_type == "out_refund":
    #         if self.x_studio_charges:
    #             self.notice_fee_withdrawal = self.x_studio_charges.invoice_line_ids.price_subtotal

    # def _compute_total_amount(self):
    #     if self.move_type == "out_refund":
    #         self.amount_total_withdrawal = abs(
    #             self.notice_fee_withdrawal-self.invoice_line_ids.price_subtotal)

    def _compute_refund_receive(self):

        if self.x_studio_charges:

            if self.move_type == "out_refund":
                for i in self.x_studio_charges.invoice_line_ids:
                    receive = i.price_subtotal
                for j in self.invoice_line_ids:
                    refund = j.price_subtotal
                if receive > refund:
                    self.refund_receive = "Receivable"
                else:
                    self.refund_receive = "Refundable"

            if self.move_type == "out_invoice":
                for i in self.x_studio_charges.invoice_line_ids:
                    refund = i.price_subtotal
                for j in self.invoice_line_ids:
                    receive = j.price_subtotal
                if receive > refund:
                    self.refund_receive = "Receivable"
                else:
                    self.refund_receive = "Refundable"

        # if self.x_studio_charges:

        #     if self.x_studio_charges.invoice_line_ids:

        #         for i in self.x_studio_charges.invoice_line_ids:
        #             refund = i.price_subtotal
        #     if self.invoice_line_ids:
        #         for j in self.invoice_line_ids:
        #             receive = j.price_subtotal

        #     if receive > refund:
        #         self.refund_receive = 'Receivable'
        #     else:
        #         self.refund_receive = 'Refundable'
        # else:
        #     self.refund_receive = 'Refundable'

#   record.write({'x_receivable_refundable': 'receivable'})
