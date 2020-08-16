import re

print("Hello, World!")
fileName = "#{prj_code}_#{app_code}_#{brc_code}_docs_V#{rls_ver}.tar.gz"

reExpr = r"#\{\w*\}"
reIt = re.finditer(reExpr, fileName)

prjPara = {}
prjPara["prj_code"] = "jtwlwV8"
prjPara["sys_code"] = "billing"
prjPara["app_code"] = "billing"
prjPara["brc_code"] = "testage_jtwlwV8"

listSeg = []
lastPos = 0
for it in reIt:
	listSeg.append(fileName[lastPos:it.start()])
	print(" listSeg is:%s" %listSeg)
	varName = it.group()[2:-1]
	print( "varName is :%s" %varName)
	if varName in prjPara:
		listSeg.append(prjPara[varName])
	else:
		listSeg.append("#{%s}" % varName)
		print("varName : %s not found!!" %varName)
	print("lastPot : %s" %it.end())
	lastPos = it.end()

if lastPos < len(fileName)-1:
    listSeg.append(fileName[lastPos:])

print ("".join(listSeg))

	