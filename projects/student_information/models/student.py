# -*- coding: utf-8 -*-

from odoo import models, fields,api

class ResPub(models.Model):
	_name = 'res.pub'

	name = fields.Char('Name')
	student_id = fields.Many2one('student.student', string='Student')
	#feed_id = fields.Many2one('student.student', string='Feedback')

class FeedFeed(models.Model):
	_name = 'feed.feed'


	feed = fields.Char('Feedback Subject')
	dec = fields.Text('Description')
	fname = fields.Char('First name')
	lname = fields.Char('Last name')
	mail = fields.Char('E-mail')
	contact = fields.Char('Contact')



class StudentStudent(models.Model):
	_name = 'student.student'
	

	name = fields.Char('Name', required=True)
	s_id = fields.Char('Student Id')
	mobile = fields.Char('Mobile No')
	address = fields.Char('Address')
	age = fields.Char('Age')
	gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string='Gender')
	student_dob = fields.Date(string="Date of Birth")
	nationality_id = fields.Many2one('res.country', string='Nationality')
	users_ids = fields.Many2many('res.users', 'res_users_rel','users_id','student_id', string='Users')
	
	pub_ids = fields.Many2many('res.pub', 'res_pub_rel', 'pub_id','char_id', string='Pub')

	pub_lines = fields.One2many('res.pub','student_id' ,string='Pub Line')
	#fees_ids = fields.One2many('res.fees', 'fees', required=True, index=True, ondelete='cascade')
	photo = fields.Binary()
	#fee = fields.One2many('res.fee' , 'feed_id',string='feedb' )
	