# Sublime Indent and braces
Sublime text 2 & 3 plugin to indent selection and wrap it in braces. Useful to add if () statements for example.

![Alt text](http://fat.gfycat.com/HelpfulFittingCrownofthornsstarfish.gif)

Installation
============

* Install [Package manger](http://packagecontrol.io/) if you haven't already
* Press ctr+shift+p -> install package -> indent and braces
* Add the following shortcut to your keybindings (customize keys as desired)

````
{ "keys": ["ctrl+i"], "command": "indent_and_braces" },
````

Options
=======

__`opening_brace` & `closing_brace`:__ These options allow you to modify the kind of braces the plugin will insert.<br>

    { "keys": ["ctrl+shift+i"], "command": "indent_and_braces", "args": { "opening_brace": "[", "closing_brace": "]" } },
    
__`from_cursor`:__ Normally the plugin will determine intelligently wether or not to place the opening brace on a new line. If you want to force this, you can use `from_cursor`.<br>

    { "keys": ["ctrl+j"], "command": "indent_and_braces", "args": { "from_cursor": false} },