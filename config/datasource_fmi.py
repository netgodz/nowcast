# data source specifications
root_path  = "/home/ubuntu/pysteps-data"
path_fmt   = "radar/fmi/%Y%m%d"
fn_pattern = "%Y%m%d%H%M_fmi.radar.composite.lowest_FIN_SUOMI1"
fn_ext     = "pgm.gz"
importer   = "fmi_pgm"
timestep   = 5.

# importer arguments
importer_kwargs = {
    "gzipped"   :   True
}
