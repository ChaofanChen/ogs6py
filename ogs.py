# -*- coding: utf-8 -*-
import os
import sys
from lxml import etree as ET
from classes import *


class OGS(object):
    def __init__(self, **args):
        self.geo = geo.GEO()
        self.mesh = mesh.MESH()
        self.processes = processes.PROCESSES()
        self.media = media.MEDIA()
        self.timeloop = timeloop.TIMELOOP()
        self.parameters = parameters.PARAMETERS()
        self.processvars = processvars.PROCESSVARS()
        self.linsolvers = linsolvers.LINSOLVERS()
        self.nonlinsolvers = nonlinsolvers.NONLINSOLVERS()
        sys.setrecursionlimit(10000)
        self.tag = []
        ogs_name = ""
        if "PROJECT_FILE" in args:
            self.prjfile = args['PROJECT_FILE']
        else:
            print("PROJECT_FILE not given. Calling it default.prj.")
            self.prjfile = "default.prj"

    def runModel(self, **args):
        if sys.platform == "win32":
            self.ogs_name = "ogs.exe"
        else:
            self.ogs_name = "ogs"
        cmd = self.ogs_name + " " + self.prjfile + " >out"
        print("OGS running...")
        os.system(cmd)
        print("OGS finished")

    def dict2xml(self, parent, dictionary):
        for entry in dictionary:
            self.tag.append(ET.SubElement(parent, dictionary[entry]['tag']))
            self.tag[-1].text = dictionary[entry]['text']
            for attr in dictionary[entry]['attr']:
                self.tag[-1].set(attr, dictionary[entry]['attr'][attr])
            if len(dictionary[entry]['children']) > 0:
                self.dict2xml(self.tag[-1], dictionary[entry]['children'])

    def writeInput(self):
        self.root = ET.Element("OpenGeoSysProject")
        self.dict2xml(self.root, self.geo.tree)
        self.dict2xml(self.root, self.mesh.tree)
        self.dict2xml(self.root, self.processes.tree)
        if len(self.media.tree['media']['children']) > 0:
            self.dict2xml(self.root, self.media.tree)
        self.dict2xml(self.root, self.timeloop.tree)
        self.dict2xml(self.root, self.parameters.tree)
        self.dict2xml(self.root, self.processvars.tree)
        self.dict2xml(self.root, self.nonlinsolvers.tree)
        self.dict2xml(self.root, self.linsolvers.tree)
        # Reparsing for pretty_print to work properly
        parser = ET.XMLParser(remove_blank_text=True)
        self.tree_string = ET.tostring(self.root, pretty_print=True)
        self.tree = ET.fromstring(self.tree_string, parser=parser)
        self.tree_ = ET.ElementTree(self.tree)
        self.tree_.write(self.prjfile,
                         encoding="ISO-8859-1",
                         xml_declaration=True,
                         pretty_print=True)
        return True


