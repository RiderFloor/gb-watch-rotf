from publitio import PublitioAPI
from utilities.all_imports import *


class Publitio:
	def __init__(self):
		pass
	def upload_file(self, file):
		apireq = PublitioAPI('Z6zle7lg9wz25MX5sDte','du0AGHNTuNbrkAABrk0RNsi5rZA5WHAr')
		res = apireq.create_file(file=open(file, 'rb'), title='name_test', describtion='test')
		return res
