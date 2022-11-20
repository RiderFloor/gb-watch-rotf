from utilities.all_imports import *


def print_log(mess, level='INFO'):

    lib = {
        'INFO': Fore.LIGHTBLACK_EX,
        'ERROR': Fore.RED,
        'DEBUG': Fore.CYAN,
        'ALERT': Fore.YELLOW,
        'MESS': Fore.LIGHTGREEN_EX}
    print(lib[level], f'LOG MESS: #{level}: {mess}')
    print(Fore.RESET, end='\r')

    
def take_screenshot(pyautogui:object, name:str):
    from DataBase.Publitio import Publitio
    print_log(f'helpers.take_screenshot - {name}', level='DEBUG')
    file = pyautogui.screenshot(f'{name}.png')
    up = Publitio().upload_file
    up(f'{name}.png')
    os.remove(f'{name}.png')
    

def print_debug(mess):
    print(Fore.MAGENTA)
    print(f'debug message:')
    pprint(mess)
    print(Fore.RESET, end='\r')


def log(mess):
    with open('log.txt', 'a') as f:
        f.write(f'{mess}\n')
        f.close()
    print(Fore.LIGHTBLACK_EX, f'log message: {mess}')
    print(Fore.RESET, end='\r')


def load_config():
    url = 'https://LibraryAPIv20.riderfloor.repl.co/get_script'
    data = {'script': 'config'}
    res = requests.get(url, json=data).json()
    with open('config.py', 'w') as f:
        f.write(res)


def get_post(post_params:dict):
    print_log(f'helpers.get_post - getting post')
    url = f"{params['LibraryAPI']['url']}{params['LibraryAPI']['get_post']}"
    res = requests.post(url=url, json=post_params).json()
    if res:
        print_log('helpers.get_post - post found')
        return res


def remove_emojs(string:str):
    emoji_pattern = re.compile("["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            "]+", flags=re.UNICODE)
    res = emoji_pattern.sub(r'', string) # no emoji
    return res

def download_file(file:dict):
    print_log('helpers.download_file - downloading file...')
    url = file['publitio_link']
    res = requests.get(url)

    file_name = file['name']
    if '.' in file_name:
        file_name = file_name.split('.')[0]
    file_path = f"/app/Bot/FILES/{file_name}.{file['type']}"
    
    file['file_path'] = file_path

    with open(file_path, 'wb') as fp:
        fp.write(res.content)
        print_log('helpers.download_file - file downloaded')

    return file


def delete_file(file:dict):
    print_log('helpers.delete file - deleting file...')
    path = file['absolut_path']
    name = file['name']
    typ = file['type']
    full_path = fr'{path}\{name}.{typ}'
    os.remove(full_path)
    print_log('helpers.delete file - file deleted...')


def get_script(script:str):
    data = {'script': script}
    url = 'https://LibraryAPIv20.riderfloor.repl.co/get_script'
    return requests.get(url, json=data)


def get_instagram_caption(post:dict):
    if post['caption']:
        line1 = post['caption']
        line2 = f'{line1}\n.\n.\n.\n.\n.\n'
        for i in post['hashtags']:
            line2 += f'\n{i}'
        return line2
    else:
        return None


def wait(n:float=1):
    time.sleep(n)
