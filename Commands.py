# -*- coding: utf-8 -*-

import os
import FreeCADGui as Gui
import FreeCAD
# import math

_icondir_ = os.path.join(os.path.dirname(__file__), 'resources')

class ExportAsStlFilesCommand():
    '''This class will be loaded when the workbench is activated in FreeCAD. You must restart FreeCAD to apply changes in this class'''  
      
    def Activated(self):
        '''Will be called when the feature is executed.'''
        # selection = Gui.Selection.getSelectionEx()
        # Gui.doCommand('import OpticsWorkbench')
        # Gui.doCommand('objects = []')
        # for sel in selection:
        #     Gui.doCommand('objects.append(FreeCAD.ActiveDocument.getObject("%s"))'%(sel.ObjectName))
            
        # Gui.doCommand('OpticsWorkbench.makeGrating(objects)')              

    def IsActive(self):
        '''Here you can define if the command must be active or not (greyed) if certain conditions
        are met or not. This function is optional.'''
        if FreeCAD.ActiveDocument:
            return(True)
        else:
            return(False)
        
    def GetResources(self):
        '''Return the icon which will appear in the tree view. This method is optional and if not defined a default icon is shown.'''
        return {'Pixmap'  : os.path.join(_icondir_, 'template_resource.svg'),
                'Accel' : '', # a default shortcut (optional)
                'MenuText': 'Export(stl files)',
                'ToolTip' : 'Export pars as stl files.' }               
                
Gui.addCommand('Export(stl files)', ExportAsStlFilesCommand())
