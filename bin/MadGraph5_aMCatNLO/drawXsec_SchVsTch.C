{
vector <string> s;
//s.push_back("NLO_XsecEMu_BRmultiplied.txt");
s.push_back("Sch_NLO_XsecMuMu_BRmultiplied.txt");
s.push_back("Tch_NLO_XsecEE_BRmultiplied.txt");

int i[2] = {0,0};
int j[2] = {0,0};
//double X[2];
//double Y[2];
//double x[2][34];
//double y[2][34]; //for ee, emu comparison
string line;
double x1[34];
double y1[34];
double x2[16];
double y2[16];


//for (int I=0;I<s.size();I++){
//
//ifstream in(s[I].c_str());
//while(getline(in,line)){
//istringstream is(line);
//string a,b;
//is >> a;
//is >> b;
//if (a == "Mass") continue;
//X[I] = atof(a.c_str());
//Y[I] = atof(b.c_str());
//x[I][i[I]++] = X[I];
//y[I][j[I]++] = Y[I];
//}
//} //for ee, emu comparison

ifstream in(s[0].c_str()); //Schannel xsec
while(getline(in,line)){
istringstream is(line);
string a,b;
is >> a;
is >> b;
if (a == "Mass") continue;
x1[i[0]++] = atof(a.c_str());
y1[j[0]++] = atof(b.c_str());
}

ifstream in(s[1].c_str()); //Tchannel xsec
while(getline(in,line)){
istringstream is(line);
string a,b;
is >> a;
is >> b;
if (a == "Mass") continue;
x2[i[1]++] = atof(a.c_str());
y2[j[1]++] = atof(b.c_str());
}



TCanvas* c1 = new TCanvas("c1","HN xsec",200,10,900,800);
//c1->Divide(1,2);
//c1->cd(1);

//gPad->SetPad(0,0.35,1,1);
//gPad->SetTopMargin(0.05);
//gPad->SetBottomMargin(0.02);


//========================xsec 1========================//
//TGraph* gr1 = new TGraph(34,x[0],y[0]);
TGraph* gr1 = new TGraph(34,x1,y1);
gr1->SetMarkerStyle(20);
gr1->SetMarkerColor(2);
gr1->SetLineWidth(3);
gr1->SetLineColor(2);
gr1->SetTitle("S-ch vs T-ch xsec comparison");
gr1->Draw("APC");
//gr1->GetXaxis()->SetLabelSize(0);
gr1->GetXaxis()->SetTitle("m(N) (GeV)");
gr1->GetYaxis()->SetTitle("#scale[1.5]{#sigma (pb)}");
gr1->GetYaxis()->SetTitleOffset(1.2);
gPad->SetLogx();
gPad->SetLogy();
gr1->GetHistogram()->SetMinimum(1e-10);
gr1->GetHistogram()->SetMaximum(10); 


//=======================xsec 2======================//
/* for emu xsec
TGraph* gr2 = new TGraph(34,x[1],y[1]);
gr2->SetMarkerStyle(22);
gr2->SetMarkerColor(4);
//gr2->SetLineWidth(2);
gr2->SetLineColor(4);
gr2->Draw("PC"); */

// Tch xsec
TGraph* gr2 = new TGraph(16,x2,y2);
gr2->SetMarkerStyle(22);
gr2->SetMarkerColor(4);
//gr2->SetLineWidth(2);
gr2->SetLineColor(4);
gr2->Draw("PC");


//========================AN xsec=======================//
/*
ifstream in("XsecAN.txt");
int i3 = 0;
int j3 = 0;
double X3;
double Y3;
double x3[34];
double y3[34];
while(getline(in,line)){
istringstream is(line);
string a,b;
is >> a;
is >> b;
if (a == "Mass") continue;
X3 = atof(a.c_str());
Y3 = atof(b.c_str());
x3[i3++] = X3;
y3[j3++] = Y3;
}
x3[33]=3000;y3[33]=0;x3[32]=3000;y3[32]=0;x3[31]=3000;y3[31]=0;

TGraph* gr3 = new TGraph(34,x3,y3);
gr3->SetMarkerStyle(20);
gr3->SetMarkerSize(0.75);
//gr3->SetLineWidth(2);
//gr3->SetLineColor(4);
gr3->Draw("PC"); */


//===================Legend=====================//
TLegend* legend = new TLegend(0.15,0.2,0.35,0.4);
legend->AddEntry(gr1,"#mu#mu + jj (s-ch)","lp");
//legend->AddEntry((TObject*)0,"#lower[-0.2]{#scale[0.8]{|V_{#muN}|=|V_{eN}|=0.01}}","");
legend->AddEntry(gr2,"#mu#mu + jj (t-ch)","lp");
legend->AddEntry((TObject*)0,"#lower[-0.2]{#scale[0.8]{|V_{#muN}|=0.01, |V_{eN}|=0}}","");
//legend->AddEntry(gr3,"lljj (s-ch) for 2016 result","lp");
legend->Draw();


//=================ratio plot===============//
/*
double x4[34];
double y4[34];

for (int I=0;I<34;I++){
x4[I] = x[1][I];
//y4[I] = y3[I]/y[1][I];
y4[I] = y[0][I]/y[1][I];
}

c1->cd(2);
gPad->SetPad(0,0,1,0.35);
gPad->SetTopMargin(0.05);
gPad->SetBottomMargin(0.15);

TGraph* gr4 = new TGraph(34,x4,y4);
gr4->SetTitle("");
gr4->SetMarkerStyle(3);
gr4->SetMarkerSize(0.8);
gr4->SetMarkerColor(9);
//gr4->SetMarkerColor(8);
gr4->Draw("AP");
gPad->SetLogx();
gPad->SetGridy();
gr4->GetHistogram()->SetMinimum(0.495);
gr4->GetHistogram()->SetMaximum(0.506);
gr4->GetXaxis()->SetLabelSize(0.06);
//gr4->GetXaxis()->SetTickSize(0.04);
gr4->GetXaxis()->SetTitle("#scale[2.2]{m(N) (GeV)}");
gr4->GetXaxis()->SetTitleOffset(1.5);
gr4->GetYaxis()->SetLabelSize(0.05);
//gr4->GetYaxis()->SetTitle("#scale[2.2]{2016 / reprod.}");
gr4->GetYaxis()->SetTitle("#scale[2.2]{mumu / emu}"); */


}

