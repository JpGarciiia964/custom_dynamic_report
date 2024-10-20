# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ReportWizard(models.TransientModel):
    _name = 'contact.dynamic.report.wizard'
    _description = 'Wizard para generar reportes dinámicos de contactos'

    partner_ids = fields.Many2many('res.partner', string="Clientes")
    field_ids = fields.Many2many('ir.model.fields', string="Campos", 
                                 domain="[('model', '=', 'res.partner')]")

    def generate_report(self):
        # Lógica para generar el reporte basado en la selección
        selected_partners = self.partner_ids
        selected_fields = self.field_ids.mapped('name')

        # Crear contexto para pasar los datos seleccionados al reporte
        return {
            'type': 'ir.actions.act_window',
            'name': 'Vista Previa del Reporte',
            'view_mode': 'tree',
            'res_model': 'contact.dynamic.report',
            'target': 'current',
            'context': {
                'default_partner_ids': selected_partners.ids,
                'default_field_ids': selected_fields,
            },
        }
