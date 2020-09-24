# -*- coding: utf-8 -*-

from odoo import models, fields

class cms_category(models.Model):
    _name = 'cms.category'
    _description = 'CMS Category'
    
    name = fields.Char(string='name', required=True, translate=True)
    description = fields.Text(string='Description', translate=True)

class cms_brief(models.Model):
    _name = 'cms.brief'
    _description = 'Brief'
    
    name = fields.Char(string='Name', required=True, translate=True)
    description = fields.Char(string='Description', translate=True)
    cms_id = fields.Many2one('cms.cms', 'CMS ID')

class cms_standard(models.Model):
    _name = 'cms.standard'
    _description = 'Standard'

    name = fields.Char(string="Name", required=True)
    description = fields.Char(string="Descriptin", translate=True)
    url = fields.Char(string='URL')
    cms_id = fields.Many2one('cms.cms', 'CMS ID')
    standard_category_ids = fields.One2many('cms.standard.category', 'standard_id', string='Category')

class cms_standard_category(models.Model):
    _name = 'cms.standard.category'
    _description = 'Standard Categories'
    
    name = fiels.Char(string="Name", required=True, translate=True)
    standard_id = fields.Many2one('cms.standard', 'Standard ID')

class cms_cms(models.Model):
    _name = 'cms.cms'
    _descriptoin = 'CMS'
    
    name = fields.Char(string="Name" required=True)
    category_id = fields.Many2one('cms.category', string='Category')
    brief_ids = fields.One2many('cms.brief', 'cms_id', string='Breif Lines')
    standard_ids = fields.One2many('cms.standard', 'cms_id', string='Standards')
