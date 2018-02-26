fov = 0.5  # field-of-view in degrees
fov *= (60.0*60.0)  # field of view in arcsec
pixels = 15.0  # pixel width in um
pixels = pixels/1000  # pixel width in mm
resolution = 4.0  # resolution modulus
fwhm = 1.0  # fwhm in arcsec
dtel = 1.3  # telescope diameter in meters
dtel *= 1000  # telescope diameter in mm

platefwhm = fwhm/(2.5*pixels)  # platescale projecting 1 fwhm into 2.5 pixels in arcsec/mm
platefov = fov/(resolution*1024*pixels)  # platescale projecting the whole FOV in the entire CCD

newfov = (platefwhm*(resolution*1024*pixels))/(60*60)  # if the platefwhm is used this will be the new fov in degrees
newfovarcmin = newfov*60  # if the platefwhm is used this will be the new fov in arcmin
newfwhm = (fwhm/platefov)/pixels  # if the platefov is used that many pixels will the fwhm occupy

fwhmfno = 206265/(dtel*platefwhm)  # f/# when using the platefwhm
fovfno = 206265/(dtel*platefov)  # f/# when using the platefov

print("The fwhm-respecting platescale is %.3f arcsec/mm. This will make the FOV=%.3f degrees=%.3f arcmin."
      " The corresponding f/# is %.3f" % (platefwhm, newfov, newfovarcmin, fwhmfno))
print("The FOV-respecting platescale is %.3f arcsec/mm. This will make the fwhm occupy %.3f pixels."
      " The corresponding f/# is %.3f" % (platefov, newfwhm, fovfno))
