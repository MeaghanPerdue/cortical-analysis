# before starting python, run 'conda activate cortex' to use this script
# must run with older version of numpy to avoid error with numpy.bool

import os
import brainspace
from brainspace import mesh
from brainspace.mesh import mesh_io


# define data paths
macruise = '/Volumes/catherine_team-1/Project_Folders/MaCRUISE/PS_MaCRUISE1mm/1_Processed_Output/'
subject = '10006_PS20_012_Session7/Lebel_Peds-x-10006-x-10006_PS20_012_Session7-x-biscuit_mc_v2-x-5354db8f-b70a-4597-9fb7-315acf79ff7c/'
out = '/Users/meaghan/Projects/cortical-analysis/data/'



# read native space gray matter surfaces into brainspace format
## left hemisphere
lh_gray = brainspace.mesh.mesh_io.read_surface(os.path.join(macruise, subject, 'surf', 'lh.gray.vtk'), itype='vtk')

## right hemisphere
rh_gray = brainspace.mesh.mesh_io.read_surface(os.path.join(macruise, subject, 'surf', 'rh.gray.vtk'), itype='vtk')

# write registered gray matter surfaces to freesurfer format
##left hemisphere
brainspace.mesh.mesh_io.write_surface(lh_gray, opth = os.path.join(out,'test','lh.pial'), oformat='binary', otype='fs')

## right hemisphere
brainspace.mesh.mesh_io.write_surface(rh_gray, opth = os.path.join(out,'test','rh.pial'), oformat='binary', otype='fs')


# read registered gray matter surfaces into brainspace format
## left hemisphere
lh_reg_gray = brainspace.mesh.mesh_io.read_surface(os.path.join(macruise, subject, 'reg', 'lh.gray.reg.vtk'), itype='vtk')

## right hemisphere
rh_reg_gray = brainspace.mesh.mesh_io.read_surface(os.path.join(macruise, subject, 'reg', 'rh.gray.reg.vtk'), itype='vtk')

# write registered gray matter surfaces to freesurfer format
##left hemisphere
brainspace.mesh.mesh_io.write_surface(lh_reg_gray, opth = os.path.join(out,'test','lh.reg.pial'), oformat='binary', otype='fs')

## right hemisphere
brainspace.mesh.mesh_io.write_surface(rh_reg_gray, opth = os.path.join(out,'test','rh.reg.pial'), oformat='binary', otype='fs')


# convert quant files (ASCII) to FS format
