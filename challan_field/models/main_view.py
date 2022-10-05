from odoo import models, fields,api
from odoo.exceptions import UserError

class account_fields(models.Model):
    _inherit = "account.move"
    room  = fields.Char("Class")
    
     
    
    photograph_charges = fields.Char("Photograph Charges")
    student_security = fields.Char("Student Security")
    admission_fee = fields.Char("Admission Fee")
    father_name = fields.Char("Father Name")  
    start_session = fields.Date("Start Session" )
    end_session = fields.Date("End Session")
    Registration_id = fields.Char("Registration ID")