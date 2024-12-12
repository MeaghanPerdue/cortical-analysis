# before starting python, run 'conda activate cortex' to use this script

import os
import brainspace
from brainspace import mesh
from brainspace.mesh import mesh_io
import bool

# define data paths
macruise = '/Volumes/catherine_team-1/Project_Folders/MaCRUISE/PS_MaCRUISE1mm/1_Processed_Output/'
subject = '10006_PS20_012_Session7/Lebel_Peds-x-10006-x-10006_PS20_012_Session7-x-biscuit_mc_v2-x-5354db8f-b70a-4597-9fb7-315acf79ff7c/surf/'
out = '~/Projects/cortical-analysis/data/'

# read subject-specific LH gray matter surface into brainspace format
lh_gray = brainspace.mesh.mesh_io.read_surface(os.path.join(macruise, subject, 'lh.gray.vtk'), itype='vtk')

# write subject-specific LH gray matter surface to freesurfer format
brainspace.mesh.mesh_io.write_surface(lh_gray, os.path.join(out,'test','lh.pial'), otype='fs')

