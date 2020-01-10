#ifndef ExRootSTDHEPReader_h
#define ExRootSTDHEPReader_h

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

#include <stdio.h>
#include <stdint.h>

#include "ExRootAnalysis/ExRootXDRReader.h"

class ExRootTreeBranch;
class ExRootFactory;

class ExRootSTDHEPReader
{
public:
  enum STDHEPBlock
  {
    GENERIC = 0,
    FILEHEADER = 1,
    EVENTTABLE = 2,
    EVENTHEADER = 4,
    MCFIO_STDHEP = 101,
    MCFIO_STDHEPBEG = 106,
    MCFIO_STDHEPEND = 107,
    MCFIO_STDHEP4 = 201
  };

  ExRootSTDHEPReader();
  ~ExRootSTDHEPReader();

  void SetInputFile(FILE *inputFile);

  void Clear();
  bool EventReady();

  bool ReadBlock(ExRootTreeBranch *branch);

  void AnalyzeEvent(ExRootTreeBranch *branch, long long eventNumber);

private:

  void AnalyzeParticles(ExRootTreeBranch *branch);

  void SkipBytes(int size);
  void SkipArray(int elsize);

  void ReadFileHeader();
  void ReadEventTable();
  void ReadEventHeader();
  void ReadSTDCM1();
  void ReadSTDHEP();
  void ReadSTDHEP4();

  FILE *fInputFile;

  ExRootXDRReader fReader[7];

  uint8_t *fBuffer;

  uint32_t fEntries;
  int32_t fBlockType, fEventNumber, fEventSize;
  double fWeight, fAlphaQCD, fAlphaQED;

  uint32_t fScaleSize;
  double fScale[10];
};

#endif // ExRootSTDHEPReader_h


