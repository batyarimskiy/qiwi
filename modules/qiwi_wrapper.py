from SimpleQIWI import QApi

class QiwiWrapper:
    def __init__(self, token, phone, proxy=None):
        self.api = QApi(token=token, phone=phone)
        
        if proxy:
            self.api._s.proxies.update(proxy)