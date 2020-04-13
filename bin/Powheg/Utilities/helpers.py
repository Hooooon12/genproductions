import string 

def fillTemplatedFile(template_file_name, out_file_name, template_dict, openmode = "a"):
    with open(template_file_name, "r") as templateFile:
        source = string.Template(templateFile.read())
        result = source.substitute(template_dict)
    with open(out_file_name, openmode) as outFile:
        outFile.write(result)

def runGetSource_patch(process) :
  return {
    "WZ" : "patch -l -p0 -i ${patches_dir}/lhapdf_zanderighi.patch",
    "ZZ" : "patch -l -p0 -i ${patches_dir}/lhapdf_zanderighi.patch",
    "b_bbar_4l" : "cd POWHEG-BOX\npatch -l -p0 -i ${patches_dir}/res_openloops_long_install_dir.patch\ncd ..",
    "ttb_NLO_dec" : "patch -l -p0 -i ${patches_dir}/pwhg_ttb_NLO_dec_gen_radiation_hook.patch",
    "ZZ" : "patch -l -p0 -i ${patches_dir}/zz_m4lcut.patch",
    "WWJ" : "patch -l -p0 -i ${patches_dir}/wwj-weights.patch\ncp ${patches_dir}/rwl_write_weights2_extra.f POWHEG-BOX/$$process/",
    "Zj" : "patch -l -p0 -i ${patches_dir}/pwhg_write_weights_nnlo.patch",
    "Wj" : "patch -l -p0 -i ${patches_dir}/pwhg_write_weights_nnlo.patch"   
    }.get(process,"")

