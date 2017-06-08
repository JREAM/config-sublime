## Make Bracket Highlighter Even Better

![outline](https://user-images.githubusercontent.com/145959/26934786-5d4f4488-4c38-11e7-876f-5a3372c5a1cc.jpg)
![background](https://user-images.githubusercontent.com/145959/26934787-5d59c76e-4c38-11e7-84cb-78ea9ce24379.jpg)

---

## Instructions

1: Preferences > Package Settings > BracketHighlighter > Bracket Settings
2: Add the following to the user side:
```
{
  "high_visibility_enabled_by_default": true,
  "high_visibility_style": "outline",                 // <-- You can swap this with "background" if you like too!
  "high_visibility_color": "__bracket__",             // <-- This has to be bracket for custom colors
  "bracket_styles": {
    "default": {
        "color": "comment.block.bracket_highlighter"   // <-- This will come from our active Theme. 
                                                          <-- we must use a real scope (comment.block) 
    }
  }
}
```

## Edit Your Active Theme

1: If you don't know it just look in Preferences > Settings, and look for `color_scheme`, it's the one that ends in `tmTheme`
2: Go to Preferences > Browse Packages (Opens a Window to Explore)
3: Go to the User folder
4: Open the file `<Your-Active-Theme>.tmTheme` in Sublime Text.
5: It only kind-of matters where we put this, so scroll down to around line 60-ish and you'll see something like this:
```
...
    <array>
        <dict>
            <key>settings</key>
            <dict>
                <key>activeGuide</key>
                <string>#7fb11b</string>
                ...
            </dict>
        </dict>
        ( This is where we can add our color setting )
...
```

6: We have to apply a real scope, so we'll use the comment.block one just like in our configuration up top. Add this:
```
        <dict>
            <key>name</key>
                <string>BracketHighlighter</string>
                <key>scope</key>
                <string>comment.block.custom</string>
                <key>settings</key>
                <dict>
                    <key>foreground</key>
                    <string>#525252</string>
                </dict>
            </dict>
```

7: It doesn't matter that the "key" says "foreground" you can apply this to an outline, background, underline. 
8: Now change the `<string>#hex-color</string>` to whatever you like.
   Be sure to try changing this also for fun: `"high_visibility_style": "background"`
   
   
