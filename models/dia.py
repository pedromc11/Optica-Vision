from odoo import models, fields, api

class Dia(models.Model):
    _name = "dia"
    _description = "Día de la semana de apertura de una tienda"

    name = fields.Char(compute="_compute_name")
    nombre = fields.Char(required = True)
    
    # Constrains
    _sql_constraints = [
        ("nombre_unico", "UNIQUE (nombre)", "El nombre del día debe ser único")
    ]

    @api.depends('nombre')
    def _compute_name(self):
        for record in self:
            record.name = record.nombre