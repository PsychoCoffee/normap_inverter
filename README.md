# normap_inverter
![](https://github.com/PsychoCoffee/normap_inverter/blob/main/banner_ni.png)
This is a python script, that can be used for inverting normal map textures to suit your game engine needs (OpenGL or DirectX).

# How it works
It uses the PIL library to invert the red and green channels of the normal map
![](https://github.com/PsychoCoffee/normap_inverter/blob/main/invert_action.png)
This can be useful for game engines and texturing programs, as you don't need to do this manually with photoshop anymore, or external software. 

# How to run
You can run this in Python IDLE or Python 3.10 by just double clicking on it. You might need to run Command Prompt as admin, and then run `pip install Pillow` and `pip install os` to install opencv2 and be able to run it.

# With which file type does it work
Well, to be honest, I'm not sure. As far as I tested, it works with jpeg, png, jpg, tiff, tif and bmp files. If something doesn't work feel free to report an issue on github.

