# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ContactDynamicReport(models.Model):
    _name = 'contact.dynamic.report'
    _description = 'Vista previa del reporte dinámico de contactos'

    partner_id = fields.Many2one('res.partner', string="Cliente")
    field_data = fields.Text(string="Datos del Cliente")

    @api.model
    def create_dynamic_records(self, partners, fields):
        records = []
        for partner in partners:
            data = ', '.join([str(getattr(partner, field, '')) for field in fields])
            record = self.create({
                'partner_id': partner.id,
                'field_data': data,
            })
            records.append(record)
        return records
