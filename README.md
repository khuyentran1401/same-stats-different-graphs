# Same Stats Different Graphs

A Python tool to create datasets whose graphs are different from one another but their statistics are the same. This is a modified version of the code provided at [Autodesk](https://www.autodesk.com/research/publications/same-stats-different-graphs). 

This library makes it easy for you to turn one shape to another and create GIFs for this transformation on the command line.

## Installation
To install the package, type:
```bash
pip install same-stats
```

## Usage
To turn a dinosaur shape into a bull eye shape, type:
```bash
python -m same_stats --shape_start=dino --shape_end=bullseye
```
And a GIF like below will be saved to the `gifs` directory as `dino_bullseye.gif`:
![gif](https://github.com/khuyentran1401/same-stats-different-graphs/blob/master/gifs/dino_bullseye.gif?raw=True)

Argument options:
* `--shape_start`: Shape start
    Options: `dino`, `rando`, `slant`, `big_slant`
* `--shape_end`: Target shape
    Options: `x`, `h_lines`, `v_lines`, `wide_lines`, `high_lines`,`slant_up`, `slant_down`, `center`, `star`, `down_parab`, `circle`,`bullseye`, `dots`
* `--iters`: Number of iteration
* `--decimals`: Number of decimals
* `--frames`: Number of frames


