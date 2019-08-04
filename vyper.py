from cefpython3 import cefpython as cef
import base64
import platform
import sys
import threading
import os

def main():
    sys.excepthook = cef.ExceptHook
    cef.Initialize()
    browser = cef.CreateBrowserSync(url=os.getcwd()+'/dist/index.html', window_title="Vyper")
    set_javascript_bindings(browser)
    cef.MessageLoop()
    cef.Shutdown()

def set_javascript_bindings(browser):
    external = External(browser)
    bindings = cef.JavascriptBindings(bindToFrames=False, bindToPopups=False)
    bindings.SetObject("external", external)
    browser.SetJavascriptBindings(bindings)

class External(object):
    def __init__(self, browser):
        self.browser = browser
        
    def py_function(self, js_callback):
        print('py function')
        
        def py_callback(msg):
            print(msg)
        js_callback.Call('python function')

if __name__ == '__main__':
    main()