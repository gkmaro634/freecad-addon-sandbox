# -*- coding: utf-8 -*-
__title__ = 'FreeCAD Sandbox Workbench - Init file'
__author__ = 'Kazuma Goto'
__url__ = ['http://www.freecadweb.org']
__doc__ = 'Sandbox Workbench workbench'
__version__ = '0.0.1'

class SandboxWorkbench (Workbench):
    def __init__(self):
        import os
        import SandboxWorkbench
        self.__class__.MenuText = 'Sandbox'
        self.__class__.ToolTip = 'This is sandbox'
        self.__class__.Icon = os.path.join(SandboxWorkbench.get_module_path(), 'template_resource.svg')

    def Initialize(self):
        '''This function is executed when FreeCAD starts'''
        import Commands
        
        self.list = ['Export(stl files)']
        self.menu = self.list
        self.appendToolbar(self.__class__.MenuText, self.list)
        self.appendMenu(self.__class__.MenuText, self.menu)
        # import here all the needed files that create your FreeCAD commands
        # import Ray
        # import OpticalObject
        # from examples import example1, example3D, example_dispersion
        
        # self.list = ['Ray (monochrome)', 'Ray (sun light)', 'Beam', '2D Radial Beam', 'Spherical Beam', 'Mirror', "Grating", 'Absorber', 'Lens', 'Off', 'Start'] # A list of command names created in the line above
        # self.menu = self.list + ['Example2D', 'Example3D', 'ExampleDispersion']
        
        # self.appendToolbar(self.__class__.MenuText, self.list) # creates a new toolbar with your commands
        # self.appendMenu(self.__class__.MenuText, self.menu) # creates a new menu

    def Activated(self):
        '''This function is executed when the workbench is activated'''
        return

    def Deactivated(self):
        '''This function is executed when the workbench is deactivated'''
        return

    def ContextMenu(self, recipient):
        '''This is executed whenever the user right-clicks on screen'''
        # 'recipient' will be either 'view' or 'tree'
        # self.appendContextMenu(self.__class__.MenuText, self.list) # add commands to the context menu

    def GetClassName(self):
        # this function is mandatory if this is a full python workbench
        return 'Gui::PythonWorkbench'


Gui.addWorkbench(SandboxWorkbench())

# import os
# import FreeCADGui as Gui
# import FreeCAD as App
# from freecad.workbench_starterkit import ICONPATH


# class TemplateWorkbench(Gui.Workbench):
#     """
#     class which gets initiated at startup of the gui
#     """

#     MenuText = "template workbench"
#     ToolTip = "a simple template workbench"
#     Icon = os.path.join(ICONPATH, "template_resource.svg")
#     toolbox = []

#     def GetClassName(self):
#         return "Gui::PythonWorkbench"

#     def Initialize(self):
#         """
#         This function is called at the first activation of the workbench.
#         here is the place to import all the commands
#         """
#         from freecad.workbench_starterkit import my_numpy_function
#         App.Console.PrintMessage("switching to workbench_starterkit\n")
#         App.Console.PrintMessage("run a numpy function: sqrt(100) = {}\n".format(my_numpy_function.my_foo(100)))

#         self.appendToolbar("Tools", self.toolbox)
#         self.appendMenu("Tools", self.toolbox)

#     def Activated(self):
#         '''
#         code which should be computed when a user switch to this workbench
#         '''
#         pass

#     def Deactivated(self):
#         '''
#         code which should be computed when this workbench is deactivated
#         '''
#         pass


# Gui.addWorkbench(TemplateWorkbench())