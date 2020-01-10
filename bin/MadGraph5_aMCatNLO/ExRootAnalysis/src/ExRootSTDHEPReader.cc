
/** \class ExRootSTDHEPReader
 *
 *  Reads STDHEP file
 *
 *
 *  $Date$
 *  $Revision$
 *
 *
 *  \author P. Demin - UCL, Louvain-la-Neuve
 *
 */

#include "ExRootAnalysis/ExRootSTDHEPReader.h"

#include <stdexcept>
#include <iostream>
#include <sstream>

#include <stdio.h>
#include <errno.h>
#include <stdint.h>
#include <string.h>

#include "TLorentzVector.h"

#include "ExRootAnalysis/ExRootClasses.h"
#include "ExRootAnalysis/ExRootFactory.h"
#include "ExRootAnalysis/ExRootXDRReader.h"
#include "ExRootAnalysis/ExRootTreeBranch.h"

using namespace std;

static const int kBufferSize  = 1000000;

//---------------------------------------------------------------------------

ExRootSTDHEPReader::ExRootSTDHEPReader() :
  fInputFile(0), fBuffer(0), fBlockType(-1)
{
  fBuffer = new uint8_t[kBufferSize*96 + 24];
}

//---------------------------------------------------------------------------

ExRootSTDHEPReader::~ExRootSTDHEPReader()
{
  if(fBuffer) delete fBuffer;
}

//---------------------------------------------------------------------------

void ExRootSTDHEPReader::SetInputFile(FILE *inputFile)
{
  fInputFile = inputFile;
  fReader[0].SetFile(inputFile);
  ReadFileHeader();
}

//---------------------------------------------------------------------------

void ExRootSTDHEPReader::Clear()
{
  fBlockType = -1;
}

//---------------------------------------------------------------------------

bool ExRootSTDHEPReader::EventReady()
{
  return (fBlockType == MCFIO_STDHEP) || (fBlockType == MCFIO_STDHEP4);
}

//---------------------------------------------------------------------------

bool ExRootSTDHEPReader::ReadBlock(ExRootTreeBranch *branch)
{
  fReader[0].ReadValue(&fBlockType, 4);

  if(feof(fInputFile)) return kFALSE;

  SkipBytes(4);

  if(fBlockType == EVENTTABLE)
  {
    ReadEventTable();
  }
  else if(fBlockType == EVENTHEADER)
  {
    ReadEventHeader();
  }
  else if(fBlockType == MCFIO_STDHEPBEG ||
          fBlockType == MCFIO_STDHEPEND)
  {
    ReadSTDCM1();
  }
  else if(fBlockType == MCFIO_STDHEP)
  {
    ReadSTDHEP();
    AnalyzeParticles(branch);
  }
  else if(fBlockType == MCFIO_STDHEP4)
  {
    ReadSTDHEP();
    AnalyzeParticles(branch);
    ReadSTDHEP4();
  }
  else
  {
    throw runtime_error("Unsupported block type.");
  }

  return kTRUE;
}

//---------------------------------------------------------------------------

void ExRootSTDHEPReader::SkipBytes(int size)
{
  int rc;
  int rndup;

  rndup = size % 4;
  if(rndup > 0)
  {
    rndup = 4 - rndup;
  }

  rc = fseek(fInputFile, size + rndup, SEEK_CUR);

  if(rc != 0 && errno == ESPIPE)
  {
    fReader[0].ReadRaw(fBuffer, size);
  }
}

//---------------------------------------------------------------------------

void ExRootSTDHEPReader::SkipArray(int elsize)
{
  uint32_t size;
  fReader[0].ReadValue(&size, 4);
  SkipBytes(size*elsize);
}

//---------------------------------------------------------------------------

void ExRootSTDHEPReader::ReadFileHeader()
{
  u_int i;
  enum STDHEPVersion {UNKNOWN, V1, V2, V21} version;

  fReader[0].ReadValue(&fBlockType, 4);
  if (fBlockType != FILEHEADER)
  {
    throw runtime_error("Header block not found. File is probably corrupted.");
  }

  SkipBytes(4);

  // version
  fReader[0].ReadString(fBuffer, 100);
  if(fBuffer[0] == '\0' || fBuffer[1] == '\0') version = UNKNOWN;
  else if(fBuffer[0] == '1') version = V1;
  else if(strncmp((char *)fBuffer, "2.01", 4) == 0) version = V21;
  else if(fBuffer[0] == '2') version = V2;
  else version = UNKNOWN;

  if(version == UNKNOWN)
  {
    throw runtime_error("Unknown file format version.");
  }

  SkipArray(1);
  SkipArray(1);
  SkipArray(1);

  if(version == V21)
  {
    SkipArray(1);
  }

  // Expected number of events
  SkipBytes(4);

  // Number of events
  fReader[0].ReadValue(&fEntries, 4);

  SkipBytes(8);

  // Number of blocks
  uint32_t nBlocks = 0;
  fReader[0].ReadValue(&nBlocks, 4);

  // Number of NTuples
  uint32_t nNTuples = 0;
  if(version != V1)
  {
    fReader[0].ReadValue(&nNTuples, 4);
  }

  if(nNTuples != 0)
  {
    throw runtime_error("Files containing n-tuples are not supported.");
  }

  // Processing blocks extraction
  if(nBlocks != 0)
  {
    SkipArray(4);

    for(i = 0; i < nBlocks; i++)
    {
      SkipArray(1);
    }
  }
}

//---------------------------------------------------------------------------

void ExRootSTDHEPReader::ReadEventTable()
{
  // version
  fReader[0].ReadString(fBuffer, 100);
  if(strncmp((char *)fBuffer, "1.00", 4) == 0)
  {
    SkipBytes(8);

    SkipArray(4);
    SkipArray(4);
    SkipArray(4);
    SkipArray(4);
    SkipArray(4);
  }
  else if(strncmp((char *)fBuffer, "2.00", 4) == 0)
  {
    SkipBytes(12);

    SkipArray(4);
    SkipArray(4);
    SkipArray(4);
    SkipArray(4);
    SkipArray(8);
  }
}

//---------------------------------------------------------------------------

void ExRootSTDHEPReader::ReadEventHeader()
{
  bool skipNTuples = false;
  int skipSize = 4;

  // version
  fReader[0].ReadString(fBuffer, 100);
  if(strncmp((char *)fBuffer, "2.00", 4) == 0)
  {
    skipNTuples = true;
  }
  else if(strncmp((char *)fBuffer, "3.00", 4) == 0)
  {
    skipNTuples = true;
    skipSize = 8;
  }

  SkipBytes(20);

  uint32_t dimBlocks = 0;
  fReader[0].ReadValue(&dimBlocks, 4);

  uint32_t dimNTuples = 0;
  if(skipNTuples)
  {
    SkipBytes(4);
    fReader[0].ReadValue(&dimNTuples, 4);
  }

  // Processing blocks extraction
  if(dimBlocks > 0)
  {
    SkipArray(4);
    SkipArray(skipSize);
  }

  // Processing blocks extraction
  if(skipNTuples && dimNTuples > 0)
  {
    SkipArray(4);
    SkipArray(skipSize);
  }
}

//---------------------------------------------------------------------------

void ExRootSTDHEPReader::ReadSTDCM1()
{
  // version
  fReader[0].ReadString(fBuffer, 100);

  // skip 5*4 + 2*8 = 36 bytes
  SkipBytes(36);

  if((strncmp((char *)fBuffer, "1.", 2) == 0) || (strncmp((char *)fBuffer, "2.", 2) == 0) ||
     (strncmp((char *)fBuffer, "3.", 2) == 0) || (strncmp((char *)fBuffer, "4.", 2) == 0) ||
     (strncmp((char *)fBuffer, "5.00", 4) == 0))
  {
    return;
  }

  SkipArray(1);
  SkipArray(1);

  if(strncmp((char *)fBuffer, "5.01", 4) == 0)
  {
    return;
  }

  SkipBytes(4);
}

//---------------------------------------------------------------------------

void ExRootSTDHEPReader::ReadSTDHEP()
{
  uint32_t idhepSize, isthepSize, jmohepSize, jdahepSize, phepSize, vhepSize;

  // version
  fReader[0].ReadString(fBuffer, 100);

  // Extracting the event number
  fReader[0].ReadValue(&fEventNumber, 4);

  // Extracting the number of particles
  fReader[0].ReadValue(&fEventSize, 4);

  if(fEventSize >= kBufferSize)
  {
    throw runtime_error("too many particles in event");
  }

  // 4*n + 4*n + 8*n + 8*n + 40*n + 32*n +
  // 4 + 4 + 4 + 4 + 4 + 4 = 96*n + 24

  fReader[0].ReadRaw(fBuffer, 96*fEventSize + 24);

  fReader[1].SetBuffer(fBuffer);
  fReader[2].SetBuffer(fBuffer + 4*1 + 4*1*fEventSize);
  fReader[3].SetBuffer(fBuffer + 4*2 + 4*2*fEventSize);
  fReader[4].SetBuffer(fBuffer + 4*3 + 4*4*fEventSize);
  fReader[5].SetBuffer(fBuffer + 4*4 + 4*6*fEventSize);
  fReader[6].SetBuffer(fBuffer + 4*5 + 4*16*fEventSize);

  fReader[1].ReadValue(&idhepSize, 4);
  fReader[2].ReadValue(&isthepSize, 4);
  fReader[3].ReadValue(&jmohepSize, 4);
  fReader[4].ReadValue(&jdahepSize, 4);
  fReader[5].ReadValue(&phepSize, 4);
  fReader[6].ReadValue(&vhepSize, 4);

  if(fEventSize < 0 ||
     fEventSize != (int)idhepSize      || fEventSize != (int)isthepSize     ||
     (2*fEventSize) != (int)jmohepSize || (2*fEventSize) != (int)jdahepSize ||
     (5*fEventSize) != (int)phepSize   || (4*fEventSize) != (int)vhepSize)
  {
    throw runtime_error("Inconsistent size of arrays. File is probably corrupted.");
  }

  fWeight = 1.0;
  fAlphaQED = 0.0;
  fAlphaQCD = 0.0;
  fScaleSize = 0;
  memset(fScale, 0, 10*sizeof(double));
}

//---------------------------------------------------------------------------

void ExRootSTDHEPReader::ReadSTDHEP4()
{
  uint32_t number;

  // Extracting the event weight
  fReader[0].ReadValue(&fWeight, 8);

  // Extracting alpha QED
  fReader[0].ReadValue(&fAlphaQED, 8);

  // Extracting alpha QCD
  fReader[0].ReadValue(&fAlphaQCD, 8);

  // Extracting the event scale
  fReader[0].ReadValue(&fScaleSize, 4);
  for(number = 0; number < fScaleSize; ++number)
  {
    fReader[0].ReadValue(&fScale[number], 8);
  }

  SkipArray(8);
  SkipArray(4);

  SkipBytes(4);
}

//---------------------------------------------------------------------------

void ExRootSTDHEPReader::AnalyzeEvent(ExRootTreeBranch *branch, long long eventNumber)
{
  TRootLHEFEvent *element;

  element = static_cast<TRootLHEFEvent *>(branch->NewEntry());

  element->Number = fEventNumber;

  element->ProcessID = 0;

  element->Weight = fWeight;
  element->ScalePDF = fScale[0];
  element->CouplingQED = fAlphaQED;
  element->CouplingQCD = fAlphaQCD;
}

//---------------------------------------------------------------------------

void ExRootSTDHEPReader::AnalyzeParticles(ExRootTreeBranch *branch)
{
  TRootGenParticle *element;

  Double_t signPz, cosTheta;
  TLorentzVector momentum;

  int number;
  int32_t pid, status, m1, m2, d1, d2;
  double px, py, pz, e, mass;
  double x, y, z, t;

  for(number = 0; number < fEventSize; ++number)
  {
    fReader[1].ReadValue(&status, 4);
    fReader[2].ReadValue(&pid, 4);
    fReader[3].ReadValue(&m1, 4);
    fReader[3].ReadValue(&m2, 4);
    fReader[4].ReadValue(&d1, 4);
    fReader[4].ReadValue(&d2, 4);

    fReader[5].ReadValue(&px, 8);
    fReader[5].ReadValue(&py, 8);
    fReader[5].ReadValue(&pz, 8);
    fReader[5].ReadValue(&e, 8);
    fReader[5].ReadValue(&mass, 8);

    fReader[6].ReadValue(&x, 8);
    fReader[6].ReadValue(&y, 8);
    fReader[6].ReadValue(&z, 8);
    fReader[6].ReadValue(&t, 8);

    element = static_cast<TRootGenParticle*>(branch->NewEntry());

    element->PID = pid;
    element->Status = status;

    element->M1 = m1 - 1;
    element->M2 = m2 - 1;

    element->D1 = d1 - 1;
    element->D2 = d2 - 1;

    element->E = e;
    element->Px = px;
    element->Py = py;
    element->Pz = pz;

    momentum.SetPxPyPzE(px, py, pz, e);

    cosTheta = TMath::Abs(momentum.CosTheta());
    signPz = (momentum.Pz() >= 0.0) ? 1.0 : -1.0;

    element->PT = momentum.Perp();
    element->Phi = momentum.Phi();
    element->Eta = (cosTheta == 1.0 ? signPz*999.9 : momentum.Eta());
    element->Rapidity = (cosTheta == 1.0 ? signPz*999.9 : momentum.Rapidity());

    element->T = t;
    element->X = x;
    element->Y = y;
    element->Z = z;
  }
}

//---------------------------------------------------------------------------
