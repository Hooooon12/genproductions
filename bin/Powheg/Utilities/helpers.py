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
    "ZZ" : "patch -l -p0 -i ${patches_dir}/lhapdf_zanderighi.patch\n\
patch -l -p0 -i ${patches_dir}/zz_m4lcut.patch",
    "b_bbar_4l" : "cd POWHEG-BOX\n\
patch -l -p0 -i ${patches_dir}/res_openloops_long_install_dir.patch\n\
cd ..",
    "ttb_NLO_dec" : "patch -l -p0 -i ${patches_dir}/pwhg_ttb_NLO_dec_gen_radiation_hook.patch",
    "WWJ" : "patch -l -p0 -i ${patches_dir}/wwj-weights.patch\n\
cp ${patches_dir}/rwl_write_weights2_extra.f POWHEG-BOX/$$process/",
    "Zj" : "patch -l -p0 -i ${patches_dir}/pwhg_write_weights_nnlo.patch",
    "Wj" : "patch -l -p0 -i ${patches_dir}/pwhg_write_weights_nnlo.patch", #first patch
    "gg_H" : "",
    "ggHH" : "",
    "ggHH_EWChL" : "",
    "trijet" : "",
    "VBF_HJJJ" : "",
    "VBF_H" : "",
    "VBF_Z_Z" : "",
    "Wgamma" : "",
    "W_ew-BMNNP" : "",
    "HW_ew" : "",
    "HZ_ew" : "",
    "HZJ_ew" : "",
    "HWJ_ew" : "",
    "bbH" : "",
    "ttJ" : "",
    "ttH" : "",
    "gg_H_MSSM" : "",
    "gg_H_2HDM" : "",
    "directphoton" : "",
    "vbs-ssww-nloew" : "",
    "HJ" : "",
    "ST_wtch_DR" : "",
    "ST_wtch_DS" : "",
    }.get(process,"")
