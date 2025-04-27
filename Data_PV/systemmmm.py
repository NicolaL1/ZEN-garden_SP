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
system['set_conversion_technologies']     = ["silica_polysilicon",
                                             "polysilicon_wafer",
                                             "wafer_cell",
                                             "cell_pv_module",
                                             "pv_module_pv_plant",
                                             "pv_plant_electricity_grid"]
system['set_storage_technologies']        = ["silica_storage",
                                             "polysilicon_storage",
                                             "wafer_storage",
                                             "cell_storage",
                                             "pv_module_storage",
                                             "pv_plant_storage"]
system['set_transport_technologies']      = ["silica_transport",
                                             "polysilicon_transport",
                                             "wafer_transport",
                                             "cell_transport",
                                             "pv_module_transport",
                                             "pv_plant_transport"]

system['set_nodes']                      = ["CHE", "CHN", "DEU", "IND", "KOR", "MYS", "ROA", "ROE", "ROW", "THA", "USA", "VNM"]

# time steps
system["reference_year"]                 = 2021
system["unaggregated_time_steps_per_year"]  = 1
system["aggregated_time_steps_per_year"]    = 1
system["conduct_time_series_aggregation"]  = False

system["optimized_years"]                = 10
system["interval_between_years"]          = 1
system["use_rolling_horizon"]             = False
system["years_in_rolling_horizon"]         = 1

