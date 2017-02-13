# state file generated using paraview version 4.4.0

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [792, 538]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.StereoType = 0
renderView1.CameraPosition = [1.931084982331457, 2.6631977880480147, -0.06965194884807177]
renderView1.CameraViewUp = [-0.27656609302235, 0.17582898820393422, -0.9447726515397945]
renderView1.CameraParallelScale = 0.8516115354228021
renderView1.Background = [0.32, 0.34, 0.43]

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Sphere'
sphere1 = Sphere()

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from sphere1
sphere1Display = Show(sphere1, renderView1)
# trace defaults for the display properties.
sphere1Display.ColorArrayName = [None, '']
