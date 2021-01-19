## Image to ASCII (automatic ASCII art)
Using PIL, scan an image and create an ASCII replica!

## How to use
When running the script, you will be prompted for a filename and pixel size. The pixel size determines exactly how many pixels correspond to one ASCII character. For instance, if you have a 400 x 400 image and set pixel size to be 5, you will get out a (400 / 5) x (400 / 5) = 80 x 80 text file.

## Examples (click to see full size)
| Profile picture | A glitched guitar | Radical Edward |
| --- | --- | --- |
| ![woops](https://raw.githubusercontent.com/not-legato/autoascii/main/extras/pfp_high_detail.png) | ![woops](https://raw.githubusercontent.com/not-legato/autoascii/main/extras/glitch_guitar.png) | ![woops](https://raw.githubusercontent.com/not-legato/autoascii/main/extras/ed.png) |

All of these were made with a pixel size of 1 or 2. The images are screenshots from [Notepad++](http://notepad-plus-plus.org/). Increase the value to get more pixellated images. The glitched effect on the guitar was achieved by making one of the `charset` characters two wide, such as "`d".

## Further settings in `convert.py`

### `charset`
`charset` is an array of characters. They correspond to the different brightness levels you have available, and can be customised to any degree. For example, if you set `charset = [" ", "@"]`, your output ASCII art will only have two brightness levels, drawn with spaces and @-symbols. It goes from light to dark.
## `n-greyscale`
By default, the script uses a RMS (root-mean-square) function to convert the RGB value to a greyscale one. Using the function `n-greyscale`, you can get adjust the spread of greyscale values by increasing the value n (default 2).