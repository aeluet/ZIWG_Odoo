from odoo import models, fields

class Inzidentziak(models.Model):
    _name = 'Inzidentziak'
    _description = 'Inzidentzia Informatikoak'

    name = fields.Char(string="Inzidentzia Izena", required=True)
    code = fields.Char(string="Inzidentzia Gela")
    irakasle_id = fields.Many2one('res.users', string="Irakaslea")

