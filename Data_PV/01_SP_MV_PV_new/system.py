"""===========================================================================================================================================================================
Title:        ENERGY-CARBON OPTIMIZATION PLATFORM
Created:      October-2021
Authors:      Alissa Ganter (aganter@ethz.ch)
Organization: Laboratory of Reliability and Risk Engineering, ETH Zurich

Description:  Model settings. Overwrite default values defined in default_config.py here.
==========================================================================================================================================================================="""

## System - Default dictionary
system = dict()

## System - settings update compared to default values
system['set_conversion_technologies']     = ["cell_pv_module",
                                             "wafer_cell",
                                             "ingot_wafer",
                                             "polysilica_ingot",
                                             "mining_polysilica"]
system['set_storage_technologies']        = ["pv_module_storage",
                                             "cell_storage",
                                             "wafer_storage",
                                             "ingot_storage",
                                             "polysilica_storage",
                                             "mining_storage"]
system['set_transport_technologies']      = ["pv_module_transport",
                                             "cell_transport",
                                             "wafer_transport",
                                             "ingot_transport",
                                             "polysilica_transport",
                                             "mining_transport"]

system['set_nodes']                      = ["CHE", "CHN", "DEU", "IND", "KOR", "MYS", "ROA", "ROE", "ROW", "THA", "USA", "VNM"]

# time steps
system["reference_year"]                 = 2021
system["unaggregated_time_steps_per_year"]  = 100
system["aggregated_time_steps_per_year"]    = 1
system["conduct_time_series_aggregation"]  = False

system["optimized_years"]                = 10
system["interval_between_years"]          = 1
system["use_rolling_horizon"]             = False
system["years_in_rolling_horizon"]         = 1
