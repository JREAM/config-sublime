# config-sublime

- Useful when setting up your text editor, or re-setting it up!
- Feel free to fork or simply copy for yourself.

## Plugins
The plugins file you have to install with the Sublime package manager by
going to [https://packagecontrol.io/installation](https://packagecontrol.io/installation). Then you press <kbd>CTRL+SHIFT+P</kbd> and type <kbd>Inst</kbd> and you should see `Install Package`.

## Install Package Control

Go to `View > Show Console menu` or `CTRL+~(tilde)` and enter the following, then restart. Once installed type `CTRL + SHIFT + P` and type Install and you should see Package Control.

```
import urllib.request,os,hashlib; h = 'df21e130d211cfc94d9b0905775a7c0f' + '1e3d39e33b79698005270310898eea76'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)
```

## User Settings
You can copy my user settings if you like them. Anything prefixed with an `_` underscore means its not being used, that's because you can't comment in JSON so it's there incase you want to use it.

## Hotkeys
All Commands below are for in Windows and Linux, as they will be the same. Apple commands will be different, sorry I don't use Apple.

Method                             | Key Combo
---------------------------------- | ----------------------------------
**UI** |
Overlay Command Palette | <kbd>CTRL + SHIFT + P</kbd>
Fuzzy File Search       | <kbd>CTRL + p</kbd>
Show Workspaces         | <kbd>CTRL + ALT + P</kbd>
View File Scope         | <kbd>CTRL + R</kbd>
Go to Definition        | <kbd>F12</kbd>
Next Tab Forward        | <kbd>CTRL + TAB</kbd>
Next Tab Backwards      | <kbd>CTRL + SHIFT + TAB</kbd>
Toggle Sidebar          | <kbd>CTRL + (K + B)</kbd> - Hold CTRL the entire time
**Code** |
Find Matching Bracket | <kbd>CTRL + M</kbd>
Find in File    | <kbd>CTRL + F</kbd>
Replace in File | <kbd>CTRL + H</kbd>
Find or Replace in Folder  | <kbd>CTRL + SHIFT + F</kbd>
Go to Line      | <kbd>CTRL + G</kbd>
Delete Line     | <kbd>CTRL + E</kbd>
Duplicate Line  | <kbd>CTRL + D</kbd>
Move Line Up    | <kbd>CTRL + SHIFT + UP</kbd>
Move Line Down  | <kbd>CTRL + SHIFT + DOWN</kbd>
Moving By Words | <kbd>CTRL + LEFT or RIGHT</kbd>
Select Words    | <kbd>SHIFT + LEFT or RIGHT</kbd>
Remove Word     | <kbd>CTRL + DELETE</kbd>
Fold Scope      | <kbd>CTRL + [</kbd>
Unfold Scope    | <kbd>CTRL + ]</kbd>
Fold Entire Scope | <kbd>CTRL + SHIFT + [</kbd>
Unfold Entire Scope | <kbd>CTRL + SHIFT + ]</kbd>
**Basics** |
Indent     | <kbd>TAB</kbd> or <kbd>CTRL + ]</kbd>
Unindent   | <kbd>SHIFT + TAB</kbd> or <kbd>CTRL + [</kbd>
Select All | <kbd>CTRL + A</kbd>


## Custom Snippets
Stole this off `@seneca` in #orlandodevs on Slack

    { "keys": ["leftSHIFT+super+i"], "command": "insert_snippet", "args": {"contents": "import ipdb; ipdb.set_trace()"}}`
