# -*- coding: utf-8 -*-

from odoo import models, fields

class Room(models.Model):
    _name = 'calendar.room'
    _description = 'Meeting Room'

    name = fields.Char(string='Room Name')

class Meeting(models.Model):
    _inherit = 'calendar.event'

    room_id = fields.Many2one('calendar.room', 'Room')
