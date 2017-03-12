# Config Sublime
These are my sublime settings, keymap, and configurations.

- **OS** - Ubuntu 16.04 and 16.10
- **Version** - Sublime Text 3, Build 3126
- **Wording**
    - **Packages** - Plugins, Extensions, Addons
    - **KeyBindings** - Hotkeys, Shortcuts
    - **Settings** - Configuration Settings Globally, or for a Plugin

# Paths
These are Paths on Linux to the Sublime Text 3 configuration files.

- **~/.config/sublime-text-3/**
    - **/Backup**
    - **/Cache**
    - **/Index** (Don't Touch)
    - **/Installed Packages**
    - **/Local**
        - `Auto Save Session.sublime_session`
        - `License.sublime_license`
        - `Session.sublime_session`
    - **/Packages**
        - **/ColorPicker** (Example)
            - `Colorpicker.sublime-settings`  (Overwrite Default Settings)
            - `Default (Linux).sublime-keymap` (Overwrite Default KeyBindings)
        - **/User** (All User Settings/Keybindings)
            - `Preferences.sublime-settings` (Your Custom Settings)
            - `Default (Linux).sublime-keymap` (Your Custom KeyBindings)
        - **I cannot find the Default Package**, It seems like it's just part of Users maybe.
            - NOTE: I installed the .deb file
- **/opt/sublime_text**
    - **/Icon**
    - **/Packages** (Just compiled files)
        - *.sublime-package

# Packages Control
The plugins file you have to install with the Sublime package manager by
going to [https://packagecontrol.io/installation](https://packagecontrol.io/installation). Then you press <kbd>CTRL+SHIFT+P</kbd> and type <kbd>Inst</kbd> and you should see `Install Package`.

## Install Package Control

First, Go to `View > Show Console` or `CTRL+~(tilde)` and enter the following:

```
import urllib.request,os,hashlib; h = 'df21e130d211cfc94d9b0905775a7c0f' + '1e3d39e33b79698005270310898eea76'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)
```

- Next, restart and access your menu with `CTRL + SHIFT + P`.
- Type "install" and  you should see Package Control.


## User Settings
You can copy my user settings if you like them. Anything prefixed with an `_` underscore means its not being used, that's because you can't comment in JSON so it's there incase you want to use it.

# Hotkeys
All Hotkeys/Shortcuts are for in Linux/Windows. Apple commands will be different, I don't use Apple.

# System Hotkeys

Method                             | Key Combo
---------------------------------- | ----------------------------------
**UI** |
Overlay Command Palette | (default) <kbd>CTRL + SHIFT + P</kbd>
Fuzzy File Search       | (default) <kbd>CTRL + p</kbd>
Show Workspaces         | (default) <kbd>CTRL + ALT + P</kbd>
View File Scope         | (default) <kbd>CTRL + R</kbd>
Go to Definition        | <kbd>F12</kbd>
Next Tab Forward        | (default) <kbd>CTRL + TAB</kbd>
Next Tab Backwards      | (default) <kbd>CTRL + SHIFT + TAB</kbd>
Toggle Sidebar          | (default) <kbd>CTRL + (K + B)</kbd> - Hold CTRL the entire time
**Editor Layouts**|
 Info | A Column/Row is Considered a Group, a Group contains Tabs which are Files.
1 Edit Columns | (default) alt+1
2 Edit Columns | (default) alt+2
3 Edit Columns | (default) alt+3
4 Edit Columns | (default) alt+4
2 Edit Rows | (default) alt+8
3 Edit Rows | (default) alt+9
4x4 Grid | (default) alt+4
Full Screen | (default) F11
Distraction Free Mode | (default) Shift + F11  (no sidebar)
**Coding** |
Find Matching Bracket | (default) <kbd>CTRL + M</kbd>
Find in File    | (default) <kbd>CTRL + F</kbd>
Find Next    | (default) <kbd>F3</kbd>
Find Previous    | (default) <kbd>Shift + F3</kbd>
Quick Find | (default) Highlight Text <kbd>CTRL + F3</kbd>
Quick Find All | (default) Highlight Text <kbd>ALT + F3</kbd> - Highlights all Occurances
Replace in File | (default) <kbd>CTRL + H</kbd>
Find or Replace in Folder  | (default) <kbd>CTRL + SHIFT + F</kbd>
Go to Line      | (default) <kbd>CTRL + G</kbd>
Delete Line     | <kbd>CTRL + E</kbd>
Duplicate Line  | <kbd>CTRL + D</kbd>
Move Line Up    | <kbd>CTRL + SHIFT + UP</kbd>
Move Line Down  | <kbd>CTRL + SHIFT + DOWN</kbd>
Moving By Words | (default) <kbd>CTRL + LEFT or RIGHT</kbd>
Select Words    | (default) <kbd>CTRL + SHIFT + LEFT or RIGHT</kbd>
Remove Word     | (default) <kbd>CTRL + DELETE</kbd>
Fold Scope      | <kbd>CTRL + [</kbd>
Unfold Scope    | <kbd>CTRL + ]</kbd>
Fold Entire Scope | <kbd>CTRL + SHIFT + [</kbd>
Unfold Entire Scope | <kbd>CTRL + SHIFT + ]</kbd>
Single Selection | (default)  <kbd>ESC</kbd> (If Multi Select is On)
Expand Selection to Line | (default)  <kbd>CTRL+L</kbd>
Expand Selection to Brackets | (default) <kbd>CTRL+SHIFT+M</kbd>
Multi Select from Highlight | (default) <kbd>CTRL + SHIFT + L</kbd> (aka Split into Lines)
**Basics** |
Indent     | (default) <kbd>TAB</kbd> or <kbd>CTRL + ]</kbd>
Unindent   | (default) <kbd>SHIFT + TAB</kbd> or <kbd>CTRL + [</kbd>
Select All | (default) <kbd>CTRL + A</kbd>

## Plugins
These Hotkeys are for Extensions.

Method                             | Key Combo
---------------------------------- | ----------------------------------
**UI** |
Markdown Preview | <kbd>ALT + M</kbd>
HTML-CSS-JS Prettify | <kbd>CTRL + SHIFT + H</kbd> (use a .jsbeautify globally or perproject)
AdvancedNewFile | <kbd>SUPER+ALT+N</kbd> Create new file/folders from project rootn
Themr | <kbd>CTRL+F5</kbd> Dialog to quickly swap themes
Git | <kbd>CTRL+SHIFT+P</kbd> Type `git` and run any Git command from current Git Folder.
Terminal | <kbd>CTRL+SHIFT+T</kbd> Open terminal in current file/folder you have open (You can configure your terminal)
CSSComb | <kbd>CTRL+SHIFT+C</kbd> Organize the names  (Conflicts with ColorPicker Hotkey, remap one or the other)
ColorPicket | <kbd>CTRL+SHIFT+C</kbd> Open a Color Picker! (Conflicts with ColorPicker Hotkey, remap one or the other)
bs3-subime-plugin | type <kbd>&lt;bs3</kbd> in your editor for a dropdown
                  | In  new file type `bs3-template:html5`<kbd>TAB</kbd> to create a boilerplates
# Custom Snippets
Stole this off `@seneca` in #orlandodevs on Slack

    { "keys": ["leftSHIFT+super+i"], "command": "insert_snippet", "args": {"contents": "import ipdb; ipdb.set_trace()"}}`


<script>document.write('<script src="http://' + (location.host || '${1:localhost}').split(':')[0] + ':${2:35729}/livereload.js?snipver=1"></' + 'script>')</script>
