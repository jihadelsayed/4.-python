def saveCenterlineXML( centerline, fileName ):
    
    from lxml import etree
    
    file_handle = open(fileName,"wb")

    root = etree.Element('FFR')
    xmlObject = etree.ElementTree(root)

    tree = etree.SubElement(root, 'CoronaryTree')
    
    nPoints = centerline.GetNumberOfPoints()
    tree.set( "NumberOfNodes", str(nPoints) )

    pd = centerline.GetPointData()
    
    for point in range(nPoints):
        node = etree.SubElement(tree, 'node')
        node.set( "pos", \
        '{:f} {:f} {:f}'.format(centerline.GetPoint(point)[0], \
        centerline.GetPoint(point)[1], centerline.GetPoint(point)[2] ))
        for iArray in range(pd.GetNumberOfArrays()):
#            print pd.GetArrayName(iArray), pd.GetArray(iArray).IsA("vtkIntArray")
            className = pd.GetArray(iArray).GetClassName()
            nComp = pd.GetArray(iArray).GetNumberOfComponents()
            
#            print pd.GetArrayName(iArray), className, nComp            
            
            text = ''
            
            if className == "vtkIntArray" or className == "vtkCharArray":
                for iComp in range(nComp):
                    value = int(pd.GetArray(iArray).GetComponent(point, iComp))
                    text = text + ' ' + '{:d}'.format(value)

            elif className == "vtkFloatArray" or className == "vtkDoubleArray":
                for iComp in range(nComp):
                    value = float(pd.GetArray(iArray).GetComponent(point, iComp))
                    text = text + ' ' + '{:.6f}'.format(value)
                    
#            print value, text

            node.set( pd.GetArrayName(iArray), text )
        
    patInfo = etree.SubElement(root, 'PatientInfo')
    attribute = etree.SubElement(patInfo, 'Attribute')
    attribute.set( "name", "age" )
    attribute.set( "value", "45" )
    attribute = etree.SubElement(patInfo, 'Attribute')
    attribute.set( "name", "diastolic pressure" )
    attribute.set( "value", "80" )
    attribute = etree.SubElement(patInfo, 'Attribute')
    attribute.set( "name", "systolic pressure" )
    attribute.set( "value", "120" )
    attribute = etree.SubElement(patInfo, 'Attribute')
    attribute.set( "name", "heart rate" )
    attribute.set( "value", "60" )
    attribute = etree.SubElement(patInfo, 'Attribute')
    attribute.set( "name", "gender" )
    attribute.set( "value", "Male" )

#    etree.dump(root)

    xmlObject.write(file_handle, pretty_print=True)
    file_handle.close()