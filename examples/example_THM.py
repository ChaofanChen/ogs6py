from ogs6py.ogs import OGS

model = OGS(PROJECT_FILE="thm_test.prj", MKL=True, OMP_NUM_THREADS=4)
model.geo.addGeom(filename="square_1x1_thm.gml")
model.mesh.addMesh(filename="quarter_002_2nd.vtu", axially_symmetric="true")
model.processes.setProcess(
    name="THERMO_HYDRO_MECHANICS",
    type="THERMO_HYDRO_MECHANICS",
    integration_order="4",
    dimension="2",
    reference_temperature="T0",
    specific_body_force="0 0")
model.processes.setConstitutiveRelation(type="LinearElasticIsotropic",
                                        youngs_modulus="E",
                                        poissons_ratio="nu")
model.processes.addProcessVariable(process_variable="displacement",
                                   process_variable_name="displacement")
model.processes.addProcessVariable(process_variable="pressure",
                                   process_variable_name="pressure")
model.processes.addProcessVariable(process_variable="temperature",
                                   process_variable_name="temperature")
model.processes.addProcessVariable(secondary_variable="sigma",
                                   output_name="sigma")
model.processes.addProcessVariable(secondary_variable="epsilon",
                                   output_name="epsilon")
model.media.addProperty(medium_id="0",
                            phase_type="AqueousLiquid",
                            name="specific_heat_capacity",
                            type="Constant",
                            value="4280.0")
model.media.addProperty(medium_id="0",
                            phase_type="AqueousLiquid",
                            name="thermal_conductivity",
                            type="Constant",
                            value="0.6")
model.media.addProperty(medium_id="0",
                            phase_type="AqueousLiquid",
                            name="density",
                            type="Linear",
                            reference_value="999.1",
                            variable_name="temperature",
                            reference_condition="273.15",
                            slope="-4e-4")
model.media.addProperty(medium_id="0",
                            phase_type="AqueousLiquid",
                            name="thermal_expansivity",
                            type="Constant",
                            value="4.0e-4")
model.media.addProperty(medium_id="0",
                            phase_type="AqueousLiquid",
                            name="viscosity",
                            type="Constant",
                            value="1.e-3")
model.media.addProperty(medium_id="0",
                            name="permeability",
                            type="Constant",
                            value="2e-20 0 0 2e-20")
model.media.addProperty(medium_id="0",
                            name="porosity",
                            type="Constant",
                            value="0.16")
model.media.addProperty(medium_id="0",
                            phase_type="Solid",
                            name="storage",
                            type="Constant",
                            value="0.0")
model.media.addProperty(medium_id="0",
                            phase_type="Solid",
                            name="density",
                            type="Constant",
                            value="2290")
model.media.addProperty(medium_id="0",
                            phase_type="Solid",
                            name="thermal_conductivity",
                            type="Constant",
                            value="1.838")
model.media.addProperty(medium_id="0",
                            phase_type="Solid",
                            name="specific_heat_capacity",
                            type="Constant",
                            value="917.654")
model.media.addProperty(medium_id="0",
                            name="biot_coefficient",
                            type="Constant",
                            value="1.0")
model.media.addProperty(medium_id="0",
                            phase_type="Solid",
                            name="thermal_expansivity",
                            type="Constant",
                            value="1.5e-5")
model.timeloop.addProcess(process="THERMO_HYDRO_MECHANICS",
                          nonlinear_solver_name="basic_newton",
                          convergence_type="PerComponentDeltaX",
                          norm_type="NORM2",
                          abstols="1e-5 1e-5 1e-5 1e-5",
                          time_discretization="BackwardEuler")
model.timeloop.setStepping(process="THERMO_HYDRO_MECHANICS",
                           type="FixedTimeStepping",
                           t_initial="0",
                           t_end="50000",
                           repeat="10",
                           delta_t="5000")
model.timeloop.addOutput(
    type="VTK",
    prefix="blubb",
    repeat="1",
    each_steps="10",
    variables=["displacement", "pressure", "temperature", "sigma", "epsilon"],
    fixed_output_times=[1,2,3])
model.timeloop.addTimeSteppingPair(process="THERMO_HYDRO_MECHANICS", repeat="15", delta_t="32")
model.timeloop.addOutputPair(repeat="12", each_steps="11")
model.parameters.addParameter(name="E", type="Constant", value="5000000000")
model.parameters.addParameter(name="nu", type="Constant", value="0.3")
model.parameters.addParameter(name="T0", type="Constant", value="273.15")
model.parameters.addParameter(name="displacement0",
                              type="Constant",
                              values="0 0")
model.parameters.addParameter(name="pressure_ic", type="Constant", value="0")
model.parameters.addParameter(name="dirichlet0", type="Constant", value="0")
model.parameters.addParameter(name="Neumann0", type="Constant", value="0.0")
model.parameters.addParameter(name="temperature_ic",
                              type="Constant",
                              value="273.15")
model.parameters.addParameter(name="pressure_bc_left",
                              type="Constant",
                              value="0")
model.parameters.addParameter(name="temperature_bc_left",
                              type="Constant",
                              value="273.15")
model.parameters.addParameter(name="temperature_source_term",
                              type="Constant",
                              value="150")
model.curves.addCurve(name="time_curve", coords=[0.0, 1e6, 1.1e6, 5e6],
                values=[1.0, 1.0, 2.0, 2.0])
model.processvars.setIC(process_variable_name="displacement",
                        components="2",
                        order="2",
                        initial_condition="displacement0")
model.processvars.addBC(process_variable_name="displacement",
                        geometrical_set="square_1x1_geometry",
                        geometry="left",
                        type="Dirichlet",
                        component="0",
                        parameter="dirichlet0")
model.processvars.addBC(process_variable_name="displacement",
                        geometrical_set="square_1x1_geometry",
                        geometry="bottom",
                        type="Dirichlet",
                        component="1",
                        parameter="dirichlet0")
model.processvars.setIC(process_variable_name="pressure",
                        components="1",
                        order="1",
                        initial_condition="pressure_ic")
model.processvars.addBC(process_variable_name="pressure",
                        geometrical_set="square_1x1_geometry",
                        geometry="out",
                        type="Dirichlet",
                        component="0",
                        parameter="pressure_bc_left")
model.processvars.setIC(process_variable_name="temperature",
                        components="1",
                        order="1",
                        initial_condition="temperature_ic")
model.processvars.addBC(process_variable_name="temperature",
                        geometrical_set="square_1x1_geometry",
                        geometry="out",
                        type="Dirichlet",
                        component="0",
                        parameter="temperature_bc_left")
model.processvars.addST(process_variable_name="temperature",
                        geometrical_set="square_1x1_geometry",
                        geometry="center",
                        type="Nodal",
                        parameter="temperature_source_term")
model.nonlinsolvers.addNonlinSolver(name="basic_newton",
                                    type="Newton",
                                    max_iter="50",
                                    linear_solver="general_linear_solver")
model.linsolvers.addLinSolver(name="general_linear_solver",
                              kind="lis",
                              solver_type="bicgstab",
                              precon_type="ilu",
                              max_iteration_step="10000",
                              error_tolerance="1e-16")
model.linsolvers.addLinSolver(name="general_linear_solver",
                              kind="eigen",
                              solver_type="PardisoLU",
                              precon_type="DIAGONAL",
                              max_iteration_step="10000",
                              error_tolerance="1e-8",
                              scaling="1")
model.linsolvers.addLinSolver(name="general_linear_solver",
                              kind="petsc",
                              prefix="sd",
                              solver_type="cg",
                              precon_type="bjacobi",
                              max_iteration_step="10000",
                              error_tolerance="1e-16")
model.writeInput()
model.runModel(LOGFILE="out_thm.log")
