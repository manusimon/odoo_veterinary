
from odoo import api, fields, models

class VeterinaryIncident(models.Model):
    _name = "veterinary.incident"
    _description = "Veterinary Incident"

    specie = fields.Selection([
        ('Dog','dog'),
        ('Cat','cat'),
        ('Bird','bird'),
        ('Rodent','rodent'),
        ('Livestock','livestock')
    ],related='name.specie', required = True, default = 'dog')
    
    name = fields.Many2one('veterinary.patient', string = 'Name', required = True)
    breed = fields.Char(string = 'Breed', related='name.breed', required = True)
    date_incident = fields.Date(string = 'Date')
    description = fields.Text(string = 'Incident description')
    