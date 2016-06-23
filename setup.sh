#!/bin/bash

wget https://code.jquery.com/jquery-2.2.4.min.js

#todo:
#pip install gi
#webkitgtk/etc

cd ..; mv PyWebKitGtk-wrapper pwkg; echo ".pwkg" >>.gitignore; cd pwkg
