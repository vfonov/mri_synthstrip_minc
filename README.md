# SynthStrip minc version

Quick hack based on the https://github.com/freesurfer/freesurfer/tree/dev/mri_synthstrip

## Limitations:
Volume is assumed to be 1x1x1mm^3 , no resampling is done, as opposed to the origin code

## Running (Hacked version):

`python mri_synthstrip_minc -i input.mnc -m mask.mnc --model synthstrip.1.pt` 

## Running Onnx version 

`python `

## Dependiencies

- pytorch 2.0
- minc2-simple
- numpy
- scipy
