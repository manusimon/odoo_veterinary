
from odoo import api, fields, models

class VeterinaryPatient(models.Model):
    _name = "veterinary.patient"
    _description = "Veterinary Patient"
    
    #Campo de tipo selection
    specie = fields.Selection([
        ('Dog','dog'),
        ('Cat','cat'),
        ('Bird','bird'),
        ('Rodent','rodent'),
        ('Livestock','livestock')
    ], required = True, default = 'dog')
    
    #Campos de tipo Char
    name = fields.Char(string = 'Name', required = True)
    breed = fields.Char(string = 'Breed', required = True)

    #Campo de tipo Date
    birth = fields.Date(string = 'Birth Date')

    #Campo calculado
    incidents = fields.Integer(string = 'Number of incidents', compute='_compute_incidents')

    #Funcion del campo calculado
    def _compute_incidents(self):
        incident_count = self.env['veterinary.incident'].search_count([('name', '=', self.id)])
        self.incidents = incident_count
    
    