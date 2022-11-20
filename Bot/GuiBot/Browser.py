from utilities.all_imports import *
from utilities.helpers import *


class Browser:
    def __set_disp(self):
        disp = Display(visible=True, size=(1366, 768), backend="xvfb", use_xauth=True)
        disp.start()
        print_log('Browser.setUp - display started')
    def _set_driver(self):
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        #chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("start-maximized")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        self.driver = webdriver.Chrome(options=chrome_options)
        print_log('Browser.setUp - driver started')
    def __set_interface(self):
        from pynput.mouse import Button, Controller
        self.mouseButton = Button
        self.mouse = Controller()
    
        import pyautogui
        self.pyautogui = pyautogui
        self.pyautogui._pyautogui_x11._display = Xlib.display.Display(os.environ['DISPLAY'])
        print_log('Browser.setUp - interface loaded')
    def _set_up(self, site):
        self.__set_disp()
        self.__set_interface()
        self.locators = params['locators'][site]
    """"""
    def _take_snapshot(self, name=None):
        take_screenshot(self.pyautogui, name)
    """"""
    def open(self, url):
        print_log(f'Browser.open - opening {url}')
        self._set_driver()
        self.driver.get(url)    
    def open_link(self, site, link):
        #self.__setUp(site)
        url = link
        self.driver.get(url)
        if self.await_element('browser_open'):
            print_log(f'Browser.open_link - opening {site} link: {url}')
            
            while True:
                if self.await_element('browser_is_loading', timeout=2):
                    continue
                if self.await_element('browser_is_loaded', timeout=2):
                    return True  
    def open_site(self, site):
        #self._set_up(site)
        url = params[site]['login_url']

        if self.await_element('browser_open_site'):
            print_log(f'Browser.open_site - opening {site}')

            self.driver.get(url)
            while True:
                if self.await_element('browser_is_loading', timeout=2):
                    continue
                if self.await_element('browser_is_loaded', timeout=2):
                    return True
    """"""
    def find_element(self, locator, confidence=0.99):
        img = f"/app/SCREENSHOTS/{self.locators[locator]}"
        return self.pyautogui.locateOnScreen(img, confidence=confidence)
    def await_element(self, locator, timeout=30, confidence=0.99):
        print_log(f'Browser.await_elem - {locator}')
        start = dt.now()
        element = None
        while element is None:
            element = self.find_element(locator, confidence=confidence)
            time_spend = round((dt.now() - start).total_seconds(), 2)
            if element:
                print_log(f'Browser.await_elem - {locator} FOUND|{time_spend}s')
                return element
            if time_spend > timeout:
                print_log( f'Browser.await_elem - {locator} TIMEOUT|{timeout}sec', level='ALERT')
                return None

    def await_loading(self):
        while True:
            if self.await_element('browser_is_loading', timeout=2):
                continue
            if self.await_element('browser_is_loaded', timeout=2):
                return True

    """"""
    def click_element(self, locator, confidence=0.99, clicktype='click'):
        print_log(f'Browser.click_element - {locator}')
        lib = {
            'click': self.pyautogui.click,
            'doubleclick': self.pyautogui.doubleClick,
            'tripleclick': self.pyautogui.tripleClick}

        element = self.find_element(locator=locator, confidence=confidence)
        if element:
            lib[clicktype](element)
            print_log(f'Browser.click_element - element clicked: {locator}')
            return True
        else:
            print_log(f'Browser.click_element - element:{element}', level='ERROR')
    def write_element(self, locator, text, offset=None, confidence=0.99, clicktype='click'):
        print_log(f'Browser.write_element - {locator}')

        lib = {
            'click': self.pyautogui.click,
            'doubleclick': self.pyautogui.doubleClick,
            'tripleclick': self.pyautogui.tripleClick}

        element = self.find_element(locator, confidence=confidence)
        
        if element:
            self.pyautogui.moveTo(element)

            if offset:
                self.pyautogui.move(offset[0], offset[1])

            lib[clicktype]()
            self.pyautogui.write(text)
            return True
        else:
            print_log(f'Browser.write_element - element:{element}', level='ERROR')
    """"""
    def hit_key(self, key):
        self.pyautogui.press(key)
    def click(self, position=None, pyauto=True):
        if position:
            print_log(f'Browser.click{position}')
            self.pyautogui.click(position)
        return True
    def move(self, position):
        self.mouse.position = position
        return True
    def write(self, text):
        self.pyautogui.write(text)
        return True
    def scroll(self, n):
        self.pyautogui.scroll(n)
        return True
    """"""
    def close_browser(self):
        self.driver.quit()
    """"""
    def switch_tab(self, target_tab):
        self.driver.switch_to.window(target_tab)
    def close_tabs(self, target_window, all_windows):
        print_log('Browser.close_tabs - closing other tabs')
        for window in all_windows:
            if window != target_window:
                self.switch_tab(window)
                self.close_current_tab()
    def get_current_tab_id(self):
        return self.driver.current_window_handle
    def close_current_tab(self):
        self.driver.close()
    def get_open_tabs_id(self):
        return self.driver.window_handles
