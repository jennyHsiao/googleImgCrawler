def imgTypeMap(type):
	if("x" in type):
		type = type.replace("x-", "")
	if("portable" in type):
		type = type.replace("portable-", "")
	if ("windows" in type):
		type = type.replace("windows-", "")
	if("vnd" in type):
		type = type.replace(".vnd","")
	if("cmu" in type):
		type = type.replace("cmu-","")
	if("rn" in type):
		type = type.replace("rn-", "")
	if("wap" in type):
		type = type.replace("wap.", "")
	if("xml" in type):
		type = type.replace("+xml","")


	if (type=="jg"):
		return "art"
	if (type=="bmp"):
		return "bmp"
	if (type=="florian"):
		return "flo"
	if (type=="net-fpx"):
		return "fpx"
	if (type=="g3fax"):
		return "g3"
	if (type=="jutvision"):
		return "jut"
	if (type=="vasa"):
		return "mcf"
	if (type=="bitmap"):
		return "pbm"
	if (type=="xbitmap"):
		return "xbm"
	if (type=="graymap") or (type=="greymap"):
		return "pgm"
	if (type=="anymap"):
		return "pnm"
	if (type=="xpixmap"):
		return "pm"
	if (type=="pixmap"):
		return "ppm"
	if (type=="quicktime"):
		return "qif"
	if (type=="raster"):
		return "ras"	
	if (type=="realflash"):
		return "rf"
	if (type=="realpix"):
		return "rp"
	if (type=="dwg"):
		return "svf"
	if (type=="xwindowdump"):
		return "xwd"
	else:
		return type