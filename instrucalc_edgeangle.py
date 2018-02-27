dtelmm = 0.0  # diameter of the telescope's primary mirror in mm
dtelm = 1.290  # diameter of the telescope's primary mirror in m
dcolmm = 65.0  # diameter of collimmator in mm
dcolin = 0.0  # diameter of collimmator in inches
fov = 0.5  # full field-of-view in degrees
hfov = 0.0  # half field of view in degrees
fno = 7.63753  # telescope f/#

dtelmm = float(dtelmm)
dtelm = float(dtelm)
dcolmm = float(dcolmm)
dcolin = float(dcolin)
fov = float(fov)
hfov = float(hfov)

if dtelm == 0.0 and dtelmm == 0.0:
    raise ValueError("No input diameter for the telescope's primary mirror")
elif dtelmm == 0.0 and dtelm != 0:
    dtelmm = dtelm*1000
elif dtelmm != 0.0 and dtelm != 0:
    raise ValueError("The diameter of the telescope's primary mirror is multiply defined")

if dcolin == 0.0 and dcolmm == 0.0:
    raise ValueError("No input diameter for the collimmator")
elif dcolmm == 0.0 and dcolin != 0.0:
    dcolmm = dcolin*25.4
elif dcolmm != 0.0 and dcolin != 0.0:
    raise ValueError("The diameter of the collimmator is multiply defined")

if fov == 0.0 and hfov == 0.0:
    raise ValueError("No input field of view or half field of view")
elif hfov == 0.0 and fov != 0.0:
    hfov = fov/2
elif hfov != 0.0 and fov != 0.0:
    raise ValueError("The field of view is multiply defined")
fov = 2 * hfov

edgeha = (dtelmm * hfov)/dcolmm
splamin = 2*edgeha
plsfp = 206265.0/(fno*dtelmm)

print("The telescope's diameter is %.3f mm" % dtelmm)
print("The collimmator's diameter is %.3f mm" % dcolmm)
print("The field of view is %.2fx%.2f degrees" % (fov, fov))
print("The half-field of view is %.2fx%.2f degrees" % (hfov, hfov))
print('The edge half angle will be %.3f degrees' % edgeha)
print('The minimum split angle required will be %.3f degrees' % splamin)
print('The platescale at the focal plane is %.3f arcsec/mm' % plsfp)
