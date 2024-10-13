from odoo import models, fields, api
from odoo.exceptions import ValidationError

class MasterRuangan(models.Model):
    _name = 'master.ruangan'
    _description = 'Master Ruangan'

    nama_ruangan = fields.Char(string='Nama Ruangan', required=True)
    tipe_ruangan = fields.Selection([
        ('kecil', 'Meeting Room Kecil'),
        ('besar', 'Meeting Room Besar'),
        ('aula', 'Aula')
    ], string='Tipe Ruangan', required=True)
    lokasi_ruangan = fields.Selection([
        ('1a', '1A'),
        ('1b', '1B'),
        ('1c', '1C'),
        ('2a', '2A'),
        ('2b', '2B'),
        ('2c', '2C')
    ], string='Lokasi Ruangan', required=True)
    foto_ruangan = fields.Binary(string='Foto Ruangan',required=True)
    kapasitas_ruangan = fields.Integer(string='Kapasitas Ruangan', required=True)
    keterangan = fields.Text(string='Keterangan')
    


    def name_get(self):
        result = []
        for record in self:
            name = f"{record.nama_ruangan}"
            result.append((record.id, name))
        return result


    @api.constrains('nama_ruangan')
    def _check_unique_room_name(self):
        for record in self:
            if self.search([('nama_ruangan', '=', record.nama_ruangan), ('id', '!=', record.id)]):
                raise ValidationError("Nama Ruangan sudah ada.")
