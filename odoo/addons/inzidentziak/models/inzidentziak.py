from odoo import models, fields

class inzidentziak(models.Model):
    _name = 'inzidentziak'
    _description = 'Inzidentzia Informatikoak'

    name = fields.Char(string="Inzidentzia Izena", required=True)
    code = fields.Char(string="Inzidentzia Gela")
    irakaslea_id = fields.Many2one('res.users', string="Irakaslea")

