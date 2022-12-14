from odoo import http
from odoo.http import request
#Sé que hay muchos errores pero hay cosas que no entendí cómo funcionan en odoo e hice sólo la estructura de la parte lógica
class usuario(http.request):
	#En la ruta no pude encontrar dónde se guardan los contactos
	@http.route([‘/contactsdata/’], type=”http”, auth=”public”)
	def createContact(self, **kw):
		for key,value in kw:
			#Con contacts a la información de los contactos pero no se en que formato estaría, si fuera como un objeto creo que funcionaría así, igual en los otros métodos
			Contacts.key.value=kw.key.value
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
                Contacts = [ele for ele in Contacts if ele.key.value != kw.key.value]
