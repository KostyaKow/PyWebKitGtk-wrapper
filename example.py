#!/usr/bin/env python

import sys, time
sys.path.append('..')
import pwkg

def setupElectron(index_path, on_event):
   w = pwkg.Window(100, 100, "PWKG Window", debug=True)
   w.load(index_path)
   w.on_gui_event += on_event
   return w

def sleep(x):
   time.sleep(x)

def on_js_event(msg):
   print(msg)
   print(msg['testdict'])

#TODO: this blocks main thread
def on_update(w):
   #from multiprocessing import Process
   #p = Process(target=lambda:adblib.screenshot(pic_path))
   #p.start()
   print("yo")
   line = "hi" #sys.stdin.readline()
   print(line)
   w.exec_js('console.log("hi")');

def main():
   w = setupElectron('index.html', on_js_event)
   w.run(on_update, 1000)

main()

