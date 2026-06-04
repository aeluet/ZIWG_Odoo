from odoo import models, fields

class nike(models.Model):
    _name = 'nike'
    _description = 'Nike Oinetakoak'

    izena = fields.Char(string='Izena', required=True)
    modeloa = fields.Char(string='Modeloa')
    tamaina = fields.Integer(string='Tamaina')
    prezioa = fields.Float(string='Prezioa')
    dendaria = fields.Many2one('res.users', string="Dendaria")
