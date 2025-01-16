from lib.wv_async import WVAsync, JsAsync


class TestApp:
    def __init__(self, wv_app: WVAsync):
        super().__init__()
        self.wv_app = wv_app

        self.wv_app.registry('on_closing', self._on_closing)
        self.wv_app.registry('hide_slave_window', self._hide_slave_window)
        self.wv_app.registry('show_slave_window', self._show_slave_window)

    async def _on_closing(self, d):
        print('closing')
        ret = await JsAsync.call(
            """new BsDialogs().ok_cancel('', 'Are you sure you want to close the application?')""", self.wv_app.window
        )
        if ret == 'ok':
            self.wv_app.window.minimize()
            self.wv_app.window_slave.minimize()
            self.wv_app.jq.sync_q.put_nowait({'closing': True})
            self.wv_app.window.hide()
        else:
            return False

    async def _hide_slave_window(self):
        self.wv_app.window_slave.hide()

    async def _show_slave_window(self):
        self.wv_app.window_slave.show()

    def on_loaded(self):
        """ on load dom main window """
        print('load dom main window')
