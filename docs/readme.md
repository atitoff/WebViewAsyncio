## This library adds async functionality to the popular project PyWebView

### Async call JS -> Python

html java script
```js
pywebview.api.call('show1')
pywebview.api.call('show2', d)
```

app_lib.py
```python
class TestApp:
    def __init__(self, wv_app: WVAsync):
        # .....
        # registry function
        self.wv_app.registry('show1', self._show1)
        self.wv_app.registry('show2', self._show2)
    
    async def _show1(self):
        # .....

    async def _hide_slave_window(self, d):
        print(d)
```
Does not return a value, but can be queried with a function `window.evaluate_js` from Python
```python
async def _show1(self):
    d = window.evaluate_js('get_data()')
    # .....
```

### Async call Python -> JS

```python
ret = await JsAsync.call(
    """new BsDialogs().ok_cancel('', 'Are you sure you want to close the application?')""",
    self.wv_app.window
)
```