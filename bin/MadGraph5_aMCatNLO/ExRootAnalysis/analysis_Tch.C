void analysis(TString tag){

  TString filename = "/data8/Users/jihkim/test/CMSSW_9_3_8/src/genproductions/bin/MadGraph5_aMCatNLO/ExRootAnalysis/" + tag + ".root";
  cout << filename << endl;

  // Load shared library
  gSystem->Load("libExRootAnalysis.so");
  gSystem->Load("libPhysics");

  // Create chain of root trees
  TChain chain("LHEF");
  //chain.Add("HeavyMajoranaNeutrino_SSDiLepton_Tchannel_NLO_ptcut5_EMu_M50.root");
  chain.Add(filename);
  
  // Create object of class ExRootTreeReader
  ExRootTreeReader *treeReader = new ExRootTreeReader(&chain);
  Long64_t numberOfEntries = treeReader->GetEntries();
  
  // Get pointers to branches used in this analysis
  TClonesArray *branchParticle = treeReader->UseBranch("Particle");
  
  // Book histograms
  TH1 *histl0PT = new TH1D("l0_pt", "Leading lepton p_{T}", 2000, 0.0, 2000.0);
  TH1 *histl1PT = new TH1D("l1_pt", "Sub-leading lepton p_{T}", 2000, 0.0, 2000.0);
  TH1 *histj0PT = new TH1D("j0_pt", "Leading jet p_{T}", 2000, 0.0, 2000.0);
  TH1 *histj1PT = new TH1D("j1_pt", "Sub-leading jet p_{T}", 2000, 0.0, 2000.0);
  TH1 *histj0ETA = new TH1D("j0_eta", "Leading jet \eta", 50, -5, 5);
  TH1 *histj1ETA = new TH1D("j1_eta", "Sub-leading jet \eta", 50, -5, 5);
  TH1 *histMass = new TH1D("mass", "M(e_{1}, e_{2})", 100, 40.0, 140.0);

  int Nevent = 0;

  // Loop over all events
  for(Int_t entry = 0; entry < numberOfEntries; ++entry) {

    // Load selected branches with data from specified event
    treeReader->ReadEntry(entry);
  
    // If event contains at least 1 particle
    if(branchParticle->GetEntries() > 0) {

      int lepcharge = 1;

      for(int Nparticle = 0; Nparticle < branchParticle->GetEntries(); Nparticle++){

        TRootLHEFParticle *particle_tmp = (TRootLHEFParticle*) branchParticle->At(Nparticle);
        
        if(particle_tmp->PID==11||particle_tmp->PID==13) lepcharge *= -1;
        else if(particle_tmp->PID==-11||particle_tmp->PID==-13) lepcharge *= 1;
             
      }

      //if(lepcharge == 1){
      if(1){

        vector<double> lepton_pt_tmp;
        vector<double> lepton_pt;
        vector<double> jet_pt_tmp;
        vector<double> jet_pt;
        vector<double> jet_eta_tmp;
        vector<double> jet_eta;

        for(int Nparticle = 0; Nparticle < branchParticle->GetEntries(); Nparticle++){
          TRootLHEFParticle *particle = (TRootLHEFParticle*) branchParticle->At(Nparticle);
          //if(abs(particle->PID)==11||abs(particle->PID)==13) lepton_pt_tmp.push_back(particle->PT);
          if(abs(particle->PID)==11||abs(particle->PID)==13) lepton_pt.push_back(particle->PT);
          if(abs(particle->PID)<=6&&particle->Mother1==0) jet_pt_tmp.push_back(particle->PT);
          if(abs(particle->PID)<=6&&particle->Mother1==0) jet_eta_tmp.push_back(particle->Eta);
          cout << particle->PID << ", Status : " << particle->Status << ", Mothers : " << particle->Mother1 << ", " << particle->Mother2 << ", pt : " << particle->PT << endl;
        }
        
        //if(lepton_pt_tmp.at(0)>lepton_pt_tmp.at(1)) {
        //  lepton_pt.push_back(lepton_pt_tmp.at(0));
        //  lepton_pt.push_back(lepton_pt_tmp.at(1));
        //}
        //else {
        //  lepton_pt.push_back(lepton_pt_tmp.at(1));
        //  lepton_pt.push_back(lepton_pt_tmp.at(0));
        //}

        if(jet_pt_tmp.at(0)>jet_pt_tmp.at(1)) {
          jet_pt.push_back(jet_pt_tmp.at(0));
          jet_pt.push_back(jet_pt_tmp.at(1));
          jet_eta.push_back(jet_eta_tmp.at(0));
          jet_eta.push_back(jet_eta_tmp.at(1));
        }
        else {
          jet_pt.push_back(jet_pt_tmp.at(1));
          jet_pt.push_back(jet_pt_tmp.at(0));
          jet_eta.push_back(jet_eta_tmp.at(1));
          jet_eta.push_back(jet_eta_tmp.at(0));
        }


        cout << "leading lepton pt : " << lepton_pt.at(0) << endl;
        //cout << "subleading lepton pt : " << lepton_pt.at(1) << endl;
        cout << "leading jet pt : " << jet_pt.at(0) << endl;
        cout << "subleading jet pt : " << jet_pt.at(1) << endl;
        cout << "leading jet eta : " << jet_eta.at(0) << endl;
        cout << "subleading jet eta : " << jet_eta.at(1) << endl;

        //if(lepton_pt.at(0) < 20) cout << "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" << endl;
        if(jet_pt.at(0) < 5) cout << "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" << endl;

        histl0PT->Fill(lepton_pt.at(0));
        //histl1PT->Fill(lepton_pt.at(1));
        histj0PT->Fill(jet_pt.at(0));
        histj1PT->Fill(jet_pt.at(1));
        histj0ETA->Fill(jet_eta.at(0));
        histj1ETA->Fill(jet_eta.at(1));

        Nevent++;

      }

      cout << "===========================" << endl;

    }

//    TRootElectron *elec1, *elec2;
//    TLorentzVector vec1, vec2;

//      // Create two 4-vectors for the electrons
//      vec1.SetPtEtaPhiM(elec1->PT, elec1->Eta, elec1->Phi, 0.0);
//      vec2.SetPtEtaPhiM(elec2->PT, elec2->Eta, elec2->Phi, 0.0);
//
//      // Plot their invariant mass
//      histMass->Fill((vec1 + vec2).M());
//    }

  }

  //cout << "N of same-sign event : " << Nevent << endl;
  cout << "Nevent : " << Nevent << endl;
  cout << "output file : " << tag+"_output.root" << endl;

  // Show resulting histograms
  outfile = new TFile(tag+"_output.root","RECREATE");
  outfile->cd();
  histl0PT->Write();
  //histl1PT->Write();
  histj0PT->Write();
  histj1PT->Write();
  histj0ETA->Write();
  histj1ETA->Write();
  
  //TCanvas* c1 = new TCanvas();
  //histl0PT->Draw();
  //TCanvas* c2 = new TCanvas();
  //histl1PT->Draw();
  //histMass->Draw();
}
