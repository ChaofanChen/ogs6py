import numpy as np


class PARAMETERS(object):
    def __init__(self, **args):
        self.parameters = np.array(
            [['name', 'type', 'value', 'mesh', 'field_name', 'expression']])

    def addParameter(self, **args):
        if "name" in args:
            if "type" in args:
                if args["type"] == "Constant":
                    self.parameters = np.append(self.parameters, [[
                        args['name'], args['type'], args['value'], '', '', ''
                    ]],
                                                axis=0)
                elif args["type"] == "MeshElement" \
                        or args["type"] == "MeshNode":
                    self.parameters = np.append(self.parameters, [[
                        args['name'], args['type'], '', args['mesh'],
                        args['field_name'], ''
                    ]],
                                                axis=0)
                elif args["type"] == "Function":
                    self.parameters = np.append(self.parameters, [[
                        args['name'], args['type'], '', '', '',
                        args['expression']
                    ]],
                                                axis=0)
                else:
                    raise KeyError("Parameter type not supported (yet).")
            else:
                raise KeyError("Parameter type not given.")
        else:
            raise KeyError("No parameter name given.")
