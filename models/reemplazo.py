from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime

class Reemplazo(models.Model):
    _name = "reemplazo"
    _description = "Información sobre reemplazos de productos en garantía"

    name = fields.Char(compute="_compute_name")
    fecha = fields.Date('Fecha de reemplazo', default=datetime.now(), required=True)
    motivo_reemplazo = fields.Text('Motivo del reemplazo', required=True)
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

    @api.depends('fecha', 'garantia_id')
    def _compute_name(self):
        for record in self:
            if record.garantia_id.name and record.fecha:
                record.name = "Reem_" + str(record.garantia_id.name) + "_" + str(record.fecha.day) + "-" + str(record.fecha.month)
            else:
                record.name = "Nuevo"