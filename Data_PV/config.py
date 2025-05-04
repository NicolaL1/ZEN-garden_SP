"""===========================================================================================================================================================================
Title:        ZEN-GARDEN
Created:      October-2021
Authors:      Alissa Ganter (aganter@ethz.ch)
Organization: Laboratory of Reliability and Risk Engineering, ETH Zurich

Description:  Model settings. Overwrite default values defined in default_config.py here.
==========================================================================================================================================================================="""

from zen_garden.model import Config
import os

# create a config
config = Config()

## Analysis - Default dictionary
analysis = config.analysis
## Solver - Default dictionary
solver = config.solver

## Analysis - settings update compared to default values
analysis["dataset"] = os.path.join(os.path.dirname(__file__), "01_SP_MV_PV_new")
analysis["objective"] = "total_cost"
# use greenfield or brownfield approach
analysis["use_capacities_existing"] = True

## Solver - settings update compared to default values
solver["name"] = "gurobi" # free solver
solver["analyze_numerics"] = True
solver["immutable_unit"] = ["hour","km"]

# Performance improvements
solver["method"] = 2
solver["crossover"] = 1
solver["numeric_focus"] = 2
solver["barconv_tol"] = 1e-8
solver["feasibility_tol"] = 1e-6
solver["optimality_tol"] = 1e-6
solver["presolve"] = 2
solver["aggregate"] = 1
solver["scaleflag"] = 1
