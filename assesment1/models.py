from odoo import http
from odoo.http import request

class usuario(http.request):
	@http.route([‘/contactsdata/’], type=”http”, auth=”public”)
	def createContact(self, **kw):
		return{
			'success': True,
			'status': 'OK',
			'code': 200
		}
	def getContactByName(self, **kw):
		users_name = request.env[‘Contacs.name’].sudo().search([ ])
		for value in users_name:
			if value==kw.value:
				return{
					'success': True,
					'status': 'OK',
					'code': 200
				}	
		return{
			'success': False,
			'status': 'OK',
			'code': 400
		}			
	def updateContact(self, **kw):
		users_name = request.env[‘Contacs.name’].sudo().search([ ])
		for value in users_name:
                        if value==kw.value:
                                for key,value in kw:
					Contacts.key.value=kw.key.value
				return{
                                        'success': True,
                                        'status': 'OK',
                                        'code': 200
				}
                 return{
                	 'success': False,
                         'status': 'OK',
                         'code': 400
                 }
	def deleteContact(self, **kw):
                Contacts = [ele for ele in Contacts if ele != kw.value]
