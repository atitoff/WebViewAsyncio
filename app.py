import webview

from lib.wv_async import WVAsync, JsApi
from app_lib import TestApp


# add user function
class Js(JsApi):
    def minimize(self):
        window.minimize()

    def close_app(self):
        wv_app.on_closing()


wv_app = WVAsync()
js_api = Js(wv_app.jq)

app = TestApp(wv_app)

window = webview.create_window(
    'Test', 'web/index.html', frameless=True, easy_drag=False, js_api=js_api,
    width=800, height=600
)
window_slave = webview.create_window('Slave', hidden=True, url='web/slave.html', js_api=js_api, frameless=True)

window.events.loaded += app.on_loaded

wv_app.start(window, window_slave)

webview.start()
