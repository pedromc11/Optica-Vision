from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class Tienda(models.Model):
    _name = "tienda"
    _description = "Local físico de la empresa"

    name = fields.Char(compute="_compute_name")
    nombre = fields.Char('Nombre', required=True)
    direccion = fields.Char('Direccion')
    ciudad = fields.Selection(
        string='Ciudad',
        selection=[
            ('Toledo', 'Toledo'),
            ('Talavera', 'Talavera'),
            ('Torrijos', 'Torrijos'),
            ('Móstoles', 'Móstoles'),
            ('Barajas', 'Barajas')
        ],
        copy=False,
        required=True
    )
    provincia = fields.Char(string="Provincia", compute="_compute_provincia", store=True, readonly=True)
    telefono = fields.Char('Teléfono')

    # Días de atención
    dias_ids = fields.Many2many("dia", string="Días de apertura")

    # Descripcion de la tienda
    descripcion = fields.Char("Descripcion")

    # Constrains
    _sql_constraints = [
        ("nombre_tienda_unico", "UNIQUE (nombre)", "El nombre de la tienda debe ser único")
    ]

    @api.depends('nombre')
    def _compute_name(self):
        for record in self:
            record.name = record.nombre

    @api.constrains("telefono")
    def _check_correct_number(self):
        for record in self:
            # Patrón para un número de teléfono válido: 
                # 9 dígitos, posiblemente con guiones entre grupos de 3 dígitos y que empiece por 6 o por 9
            patron = re.compile(r'^[6|9]\d{2}-?\d{3}-?\d{3}$')
            if not patron.match(record.telefono):
                raise ValidationError("El teléfono debe tener el formato correcto. Ejemplo: 999-999-999 o 999999999")
            
    @api.depends('ciudad')
    def _compute_provincia(self):
        '''Método para calcular la provincia automáticamente.'''
        for record in self:
            # Simulación de búsqueda de la provincia a partir de la ciudad
            if record.ciudad == "Toledo":
                record.provincia = "Toledo"
            elif record.ciudad == "Talavera":
                record.provincia = "Toledo"
            elif record.ciudad == "Torrijos":
                record.provincia = "Toledo" 
            elif record.ciudad == "Móstoles":
                record.provincia = "Comunidad de Madrid"
            elif record.ciudad == "Barajas":
                record.provincia = "Comunidad de Madrid"     
            else:
                record.provincia = ""

    def action_abrir_finde_semana(self):
        for record in self:
            # Valores a verificar y agregar si no están presentes
            valores_a_verificar = [('nombre', '=', 'Sábado'), ('nombre', '=', 'Domingo')]

            # Busca los valores que ya están presentes
            valores_existentes = record.dias_ids.mapped('nombre')

            # Agrega los valores faltantes
            valores_faltantes = []
            for valor in valores_a_verificar:
                if valor[2] not in valores_existentes:
                    dia_obj = self.env['dia'].search([('nombre', '=', valor[2])], limit=1)
                    if dia_obj:
                        valores_faltantes.append((4, dia_obj.id))

            if valores_faltantes:
                record.write({'dias_ids': valores_faltantes})
            
        return True
    
    def action_cerrar_finde_semana(self):
        for record in self:
            # Valores a eliminar si están presentes
            valores_a_eliminar = ['Sábado', 'Domingo']

            # Filtra los valores que no están en la lista a eliminar
            nuevos_dias = record.dias_ids.filtered(lambda x: x.nombre not in valores_a_eliminar)

            # Actualiza los valores del campo Many2many
            record.write({'dias_ids': [(6, 0, nuevos_dias.ids)]})
            
        return True