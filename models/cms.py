# -*- coding: utf-8 -*-

from odoo import models, fields

class CMSStandards(models.Model):
    _name = 'cms.standards'
    _description = 'Standards'

    name = fields.Char(string="Name", required=True)
    description = fields.Char(string="Descriptin", translate=True)
    url = fields.Char(string="URL")
