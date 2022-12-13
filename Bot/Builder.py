from pprint import pprint
import os, requests


class ScriptBuilder:
	def __init__(self):
		self.api_url = 'https://LibraryAPIv30.riderfloor.repl.co'
		self.route = '/get_script'

	def build(self, scripts:dict):

		for directory in scripts.keys():

			if directory == 'main':
				path = '/app/Bot/'

			else:
				path = f'/app/Bot/{directory}'
			dir_exist = os.path.exists(path)
		
			if not dir_exist:
				os.mkdir(path)
				
			for script in scripts[directory]:
				code = ''  # get script from Library api
				data = {'script': script}
				try:
					code = requests.get(f'{self.api_url}{self.route}', json=data).json()
					print('script found: ', script)
					
					with open(f'{path}/{script}.py', 'w') as f:
						f.write(code)
				except Exception as e:
					print('script not found: ', script)
					print('err mess: ', e)
