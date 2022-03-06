#-*-coding:utf-8-*-

# #-*-coding:utf-8-*-
from odoo import models ,fields ,api

class Plato(models.Model):
    _name='restaurante.plato'
    _description="Plato de restaurante"

    name=fields.Char(string="Titulo",required=True)
    description=fields.Text()