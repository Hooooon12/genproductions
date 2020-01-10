{
TChain* fChain;

fChain = new TChain("LHEF");
fChain->Add("/data8/Users/jihkim/test/CMSSW_9_3_8/src/genproductions/bin/MadGraph5_aMCatNLO/ExRootAnalysis/HeavyMajoranaNeutrino_SSDiLepton_Tchannel_NLO_ptcut5_EMu_M50.root");

vector<int>* Rwgt_size;

Rwgt_size = 0;

fChain->SetBranchAddress("Rwgt_size",&Rwgt_size);

cout << Rwgt_size->at(0) << endl;

//Long64_t nentries = fChain->GetEntries();
//
//cout << nentries << endl;
//
//for(Long64_t jentry=0; jentry<nentries; jentry++){
//
//  fChain->GetEntry(jentry);
//
//  cout << Particle_PID->size() << endl;
//
  //std::cout << jentry << " :" << muon_pt->size() << std::endl;

//}

}
