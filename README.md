## Image to ASCII (automatic ASCII art)
Using PIL, scan an image and create an ASCII replica!

## How to use
When running the script, you will be prompted for a filename and pixel size. The pixel size determines exactly how many pixels correspond to one ASCII character. For instance, if you have a 400 x 400 image and set pixel size to be 5, you will get out a (400 / 5) x (400 / 5) = 80 x 80 text file.

The final prompt is on 'contrast', which corresponds to the exponent used in the function `n_greyscale`. 1 will give the highest contrast images, while increasing the value decreases contrast.

## Examples (click to see full size)
| Profile picture | A glitched guitar | Hollow Knight |
| --- | --- | --- |
| ![](https://i.imgur.com/KyenB53.png) | ![](https://i.imgur.com/SHYiQos.png) | ![](https://i.imgur.com/sypioYM.png) |

All of these were made with a pixel size of 1 or 2. The images are screenshots from [Notepad++](http://notepad-plus-plus.org/). Increase the value to get more pixellated images. The glitched effect on the guitar was achieved by making one of the `charset` characters two wide, such as "`d".

## Further settings in `convert.py`

### `charset`
`charset` is an array of characters. They correspond to the different brightness levels you have available, and can be customised to any degree. For example, if you set `charset = [" ", "@"]`, your output ASCII art will only have two brightness levels, drawn with spaces and @-symbols. It goes from light to dark. You can also improve the contrast of your images by giving your charset less middle-brightness characters and sticking to bright and dark ones like ".", ",", "-", and "#", "@", "%". Experiment!

## Displaying the ASCII art
By necessity, if you use a very small pixel size and a large image, the text files may be enormous. This can make it hard to see the 'picture' in there. Additionally, some text editors lack sophisticated zooming features. I've found that Notepad++ zooms most easily, and using a theme (Settings -> Style Configurator) like 'Choco' makes the images really 'pop'. I display the text file on a large monitor and take a screeenshot. Experiment at your leisure, and tell me if you find a better way.

![](https://i.imgur.com/nz1pf1M.png)