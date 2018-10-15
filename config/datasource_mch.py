# data source specifications
root_path  = "/home/eugene/pysteps-data"
path_fmt   = "radar/mch/%Y%m%d"
fn_pattern = "AQC%y%j%H%M?_00005.801"
fn_ext     = "gif"
importer   = "mch_gif"
timestep   = 5.

# importer arguments
importer_kwargs = {
    "product"   :   "AQC",
    "unit"      :   "mm",
    "accutime"  :   5.
}