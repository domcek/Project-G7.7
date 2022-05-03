# Project-G7.7
Chapter 6 in my thesis (https://dare.uva.nl/search?identifier=02fc2156-9402-4784-9ab0-4bac107db6e4)

Full project details including accompanying dataset will be published after the conclusion of a referee process. Currently following files are included:

"zenodo_g7_image_diagnostics.ipynb" 

- Filtering individual images 
- Image airmass comparison
- PSF matching

"zenodo_g7_flux_calibration.ipynb"

- Matching PanStarrs star catalogue with positions of stars detected in obtained images
- Pandas filtering of the catalogue to use only reliable stars (magnitude range, match distance range, bad fit temperatures, NaN values exclusion..)
- Interpolating star temperatures and narrow-band filter fluxes
- Fitting zero point correction values for the images (using sigma clipping and least squares)
- Correcting images and subtracting background

"zenodo_g7_figures.ipynb"
- Images from Chapter 6

Helper scripts

"make_png.py" - produce figures from raw data
"move_filters.py" - split individual files based on filter used
"move_sources.py" - split datasets based on the observing target
Source EXtractor script and settings
