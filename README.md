# Sublime Indent and braces
Sublime text 3 plugin to indent selection and wrap it in braces. Useful to add if () statements for example.

![Alt text](http://fat.gfycat.com/HelpfulFittingCrownofthornsstarfish.gif)

Installation
============

* Install [Package manger](http://packagecontrol.io/) if you haven't already
* Press ctr+shift+p -> install package -> indent and braces
* Add the following shortcut to your keybindings (customize keys as desired)
````
    { "keys": ["ctrl+i"], "command": "indent_and_braces", "args": { "from_cursor": true} },
    { "keys": ["ctrl+j"], "command": "indent_and_braces", "args": { "from_cursor": false} },
````
