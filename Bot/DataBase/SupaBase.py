from utilities.helpers import *
import requests, json


class SupaBase:
    def __init__(self):
        self.api_key = params['supabase']['api_key']
        self.url = params['supabase']['api_url']
        self.tables = params['supabase']['tables']



    def read_table(self, table):
        SUPABASE_HEADERS = {
            'apikey': self.api_key,
            'Authorization': 'Bearer' + self.api_key}

        response = requests.get(f'{self.url}/{table}',
                                headers=SUPABASE_HEADERS)
        res = json.loads(response.text)
        return res

    def add_to_table(self, table, data):
        SUPABASE_HEADERS = {
            'apikey': self.api_key,
            'Authorization': 'Bearer' + self.api_key,
            'content-Type': 'application/json',
            'Prefer': 'return=representation'}

        response = requests.post(f'{self.url}/{table}',
                                 headers=SUPABASE_HEADERS,
                                 json=data)
        res = json.loads(response.text)
        #pprint(res)
        return res

    def update_entry(self, table, column, row, data):
        SUPABASE_HEADERS = {
            'apikey': self.api_key,
            'Authorization': 'Bearer' + self.api_key,
            'content-Type': 'application/json',
            'Prefer': 'return=representation'}

        response = requests.patch(f'{self.url}/{table}?{column}=eq.{row}', headers=SUPABASE_HEADERS, json=data)
        res = json.loads(response.text)
        #pprint(res)
        return res
