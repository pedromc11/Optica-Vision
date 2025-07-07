from odoo import models, fields, api, exceptions
from dateutil.relativedelta import relativedelta
from datetime import datetime

class Garantia(models.Model):
    _name = "garantia"
    _description = "Garantía de un producto expedida en una tienda"

    name = fields.Char(compute="_compute_name")
    numero_garantia = fields.Char('Número de garantía', required=True, copy=False)
    fecha_compra = fields.Date('Fecha de compra', default=datetime.now(), required=True, readonly=True)
    producto_id = fields.Many2one('product.product', string='Producto', domain="[('sale_ok','=',True)]", required=True)
    cliente_id = fields.Many2one('res.partner', string='Cliente', required=True)
    tipo_garantia = fields.Selection(
        string='Tipo de garantía',
        selection=[
            ('fabricante', 'Fabricante'),
            ('tienda', 'Tienda'),
        ],
        required=True
    )
    periodo_cobertura = fields.Integer('Período de cobertura (meses)', required=True, default=6)
    descripcion_problema = fields.Text('Descripción del problema', required=True)
    estado = fields.Selection(
        string='Estado',
        selection=[
            ('activa', 'Activa'),
            ('vencida', 'Vencida'),
            ('reclamada', 'Reclamada'),
        ],
        default='activa',
        required=True
    )
    estado_descripcion = fields.Char('Estado (descripción)', compute='_compute_estado_descripcion', readonly=True)
    reparacion_ids = fields.One2many('reparacion', 'garantia_id', string='Reparaciones')

    # Constrains
    _sql_constraints = [
        ("numero_garantia_unico", "UNIQUE (numero_garantia)", "El número de garantía debe ser único")
    ]

    @api.depends('numero_garantia')
    def _compute_name(self):
        for record in self:
            if record.numero_garantia:
                record.name = "Gar_" + str(record.numero_garantia)
            else:
                record.name = "Nuevo"

    @api.depends('periodo_cobertura')
    def _compute_estado_descripcion(self):
        for record in self:
            if record.estado == 'activa':
                record.estado_descripcion = "Vigente hasta: " + str(record.fecha_compra + relativedelta(months=+record.periodo_cobertura))
            elif record.estado == 'vencida':
                record.estado_descripcion = "Vencida desde: " + str(record.fecha_compra + relativedelta(months=+record.periodo_cobertura))
            else:
                record.estado_descripcion = ""

    # Actions
    def action_reclamar_garantia(self):
        for record in self:
            if record.estado == "reclamada":
                raise exceptions.UserError("La garantía ya está reclamada")
            else:
                record.estado = "reclamada"
        return True
    
    def action_ampliar_garantia(self):
        for record in self:
            if record.estado == "activa":
                record.periodo_cobertura += 12
            else:
                raise exceptions.UserError("La garantía ya está vencida o reclamada")
        return True