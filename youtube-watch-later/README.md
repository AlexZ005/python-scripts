# Description

This is a support code for [Save Youtube 'Watch Later' List of Videos to Spreadheet](https://youtu.be/L7zCHch8b4g)

# Usage

1. Copy repository or simply download concatenate.py
1. Go to Watch Later list: https://www.youtube.com/playlist?list=WL
1. Copy contents starting from the first video. Here are some tips:
    * Scroll to the bottom of the page (holding Page Down button can list thousands of videos in under a minute)
    * Scroll back to the top of the page and select drag from number 1
    * Release your mouse and move slider to the bottom
    * Hold Shift button and click on the right bottom corner
    * Press Ctrl+C to copy all the selected text.
1. Create input.txt at the same location where concatenate.py exists
1. Execute script by running ```python concatenate.py```
1. The output.csv will contain list of your videos

# Optional: copy video links

The links can be copied by copying the video list the same as its done in step 3, but pasting it into [Online WYSIWYG Editor](https://wysiwyghtml.com/) or similar (can be pasted into word and exported as HTML for example).  

VSCode have support of regexp, which can help to filter out all href links in H3 tags, here are a few used in the video:
|RegExp|Meaning|
|--|--|
|^<h3.* | Get all new lines starting with H3 tags|
|https?:\/\/[^\s]+" | Get all HTTPS links within lines|
|^\d{1,4}\s* | Remove 4 first leading numbers with space|

To select all the matches found by RegExp press Ctrl+Shift+L.  
This will allow to cut/copy all matches at the same time.

# ToDo

The links also can be copied automatically if script is rewritten to take contents from HTML code.  
However, the HTML change and copying the text from a 'Watch Later' page for processing seems to be more robust.  
Feel free to propose improvements by opening a new [issue](https://github.com/AlexZ005/python-scripts/issues/new) or opening a [pull request](https://github.com/AlexZ005/python-scripts/pulls).