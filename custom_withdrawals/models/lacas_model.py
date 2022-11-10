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
