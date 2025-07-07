from datetime import datetime
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from pandas import date_range

class Revision(models.Model):
    _name = "revision"
    _description = "Una revision realizada en una tienda"

    name = fields.Char(compute="_compute_name")
    # Fecha
    fecha = fields.Datetime('Fecha', copy=False, default=datetime.now(), required=True)
    # Tipo de revisión (categoria)
    tipo = fields.Selection(
        string='Tipo de revision',
        selection=[
            ('Optometrista', 'Vista'),
            ('Otorrino', 'Audición')
        ],
        copy=False,
        required=True
    )
    # Profesional-> Optometristra u Otorrino
    profesional = fields.Many2one('res.partner', string='Profesional')
    # Observaciones de la revision
    observaciones = fields.Text('Observaciones')
    # Calificacion
    calificacion = fields.Selection(
            string='Calificación',
            selection=[
                ('mala', 'Mala'),
                ('normal', 'Normal'),
                ('muy buena', 'Muy buena'),
            ],
            copy=False,
            default='normal',
            required=True
        )
    # cliente al que se le ha hecho la revision
    cliente = fields.Many2one('res.partner', string='Cliente', required=True)
    # lugar donde se ha hecho la tienda
    tienda_id = fields.Many2one('tienda', string='Tienda', required=True)
    # Estado de la revision
    estado = fields.Selection(
        string='Estado',
        selection=[
            ('pendiente', 'Pendiente'),
            ('hecha', 'Hecha'),
            ('rechazada', 'Rechazada'),
            ('aplazada', 'Aplazada')
        ],
        copy=False,
        default='pendiente',
        required=True,
        group_expand='_function_name'
    )
    
    @api.depends('fecha', 'cliente')
    def _compute_name(self):
        for record in self:
            if record.cliente.name and record.fecha:
                record.name = "Rev_" + str(record.cliente.name)[0:3] + "_" + str(record.fecha.day) + "-" + str(record.fecha.month)
            else:
                record.name = "Nuevo"

    @api.model
    def _function_name(self, stages, domain, order):
        return [key for key, val in type(self).estado.selection]