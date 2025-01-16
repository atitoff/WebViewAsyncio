## This library adds async functionality to the popular project PyWebView

### Async call JS -> Python

```js
pywebview.api.call('show_slave_window')
```

app_lib.py
```python
class TestApp:
    def __init__(self, wv_app: WVAsync):
        # .....
        # registry function
        self.wv_app.registry('show_slave_window', self._show_slave_window)
    
    async def _hide_slave_window(self):
        self.wv_app.window_slave.hide()
```