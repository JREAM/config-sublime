# config-sublime

- Useful when setting up your text editor, or resetting it up!
- Feel free to fork or simply copy for yourself.

## Plugins
The plugins file you have to install with the Sublime package manager by 
going to (https://packagecontrol.io/installation)[https://packagecontrol.io/installation]. Then you press `CTRL + SHIFT + P` and type 'Inst' and you should see `Install Package`. 

## User Settings
You can copy my user settings if you like them. Anything prefixed with an `_` underscore means its not being used, that's because you can't comment in JSON so it's there incase you want to use it.

## Hotkeys!
All Commands below are for in Windows and Linux, as they will be the same. Apple commands will be different, sorry I don't use Apple.

### Overlay Command Palette

    CTRL + SHIFT + P


### Fuzzy File Search

    CTRL + P

### Managing Lines and Words
    
    Delete Line     = CTRL + E 
    Duplicate Line  = CTRL + D 

    Move Line Up    = CTRL + SHIFT + UP
    Move Line Down  = CTRL + SHIFT + DOWN

    Moving By Words = CTRL + (LEFT or RIGHT)
                  * Hold SHIFT to Select Words
                  * (CTRL + DELETE) to remove word


### Goto Hot Keys
These are little dream keys!

    Go to Line       = CTRL + G
    View Scope       = CTRL + R
    Go to Definition = F12

### Indent/Unindent

    tab         = indent
    SHIFT + tab = unindent

### Multi Selection Edit
    
    right mouse + SHIFT & drag
    cltr + alt & up or down (esc to cancel)

## Custom Snippets
Stole this off `@seneca` in #orlandodevs on Slack

    { "keys": ["leftSHIFT+super+i"], "command": "insert_snippet", "args": {"contents": "import ipdb; ipdb.set_trace()"}}`
