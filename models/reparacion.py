from odoo import models, fields, api
from datetime import datetime

class Reparacion(models.Model):
    _name = "reparacion"
    _description = "Información sobre reparaciones de productos en garantía"

    name = fields.Char(compute="_compute_name")
    fecha = fields.Date('Fecha de reparación', default=datetime.now(), required=True)
    descripcion_trabajo = fields.Text('Descripción del trabajo realizado', required=True)
    tecnico_responsable = fields.Many2one('res.partner', string='Técnico responsable', domain="[('title','=','Técnico')]", required=True)
    costo_reparacion = fields.Float('Costo de la reparación', required=True)
    estado = fields.Selection(
        string='Estado',
        selection=[
            ('en_curso', 'En curso'),
            ('completada', 'Completada'),
        ],
        default='en_curso',
        required=True
    )
    garantia_id = fields.Many2one('garantia', string='Garantía', required=True, ondelete='cascade')

    @api.depends('fecha')
    def _compute_name(self):
        for record in self:
            if record.garantia_id.name and record.fecha:
                record.name = "Rep_" + str(record.garantia_id.name) + "_" + str(record.fecha.day) + "-" + str(record.fecha.month)
            else:
                record.name = "Nuevo"
