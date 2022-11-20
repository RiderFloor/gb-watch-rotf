from DataBase.SupaBase import SupaBase
from DataBase.Publitio import Publitio

from utilities.helpers import *


class DataBase(SupaBase, Publitio):

    def __init__(self):
        super().__init__()
        print_log("DataBase.__init__ - DataBase initiated")

    def update_file_post_history(self, job, post):
        table = self.tables['all_files_table']
        column = 'name'
        row = post['file']['name']

        # READ POST HISTORY
        post_hist = post['file']['post_history']
        if post_hist:
            post_hist = ast.literal_eval(post_hist)
            post_hist.append(job['task']['site'])
        else:
            post_hist = [job['task']['site']]

        data = {
            'last_posted': int(time.time() * 1000),
            'post_history': post_hist}

        res = self.update_entry(table, column, row, data)
        if res:
            print_log(f'#INFO: Database.update_catalog - post history added for file: {post["file"]["name"]}')
            return res

    def update_posts_table(self, job, post):
        table = self.tables['post_history_table']
        data = {
            'post_id': int(time.time() * 1000),
            'platform': job['task']['site'],
            'file': post['file']['name'],
            'topic': job['task']['job']['use_topic'],
            'nsfw': job['task']['job']['nsfw'],
            'premium': job['task']['job']['premium'],
            'caption': post['caption']}

        res = self.add_to_table(table, data)
        if res:
            print_log(f'#INFO: Database.update_post_table - post added to posts table: {post["file"]["name"]}')
            return res

    def get_task(self):
        table = self.tables['tasks_table']
        tasks = self.read_table(table)
        for task in tasks:
            if task['status'] == 'NEW':
                return task


    def mark_video_watched(self, vid_id):
        table = 'VideosToWatch'
        column = 'id'
        row = vid_id
        data = {'watched': True}
        return self.update_entry(table, column, row, data)
