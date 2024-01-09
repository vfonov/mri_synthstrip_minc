import nibabel as nib
import numpy as np

def save_nifti_volume(fn, img, aff):
    _img=np.ascontiguousarray(img.transpose([2,1,0]))
    _aff=aff
    nifty = nib.Nifti1Image(_img, _aff)
    nib.save(nifty, fn)

def load_nifti_volume(fn,as_byte=False):
    nifty=nib.load(fn)
    img=np.ascontiguousarray(nifty.get_fdata().transpose([2,1,0]))
    aff=nifty.affine
    if as_byte:
        img=img.astype(np.uint8)
    return img, aff

