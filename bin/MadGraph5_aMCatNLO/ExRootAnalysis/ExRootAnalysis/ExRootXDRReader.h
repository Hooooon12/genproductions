#ifndef ExRootXDRReader_h
#define ExRootXDRReader_h

/** \class ExRootXDRReader
 *
 *  Reads XDR
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

class ExRootXDRReader
{
public:

  ExRootXDRReader();

  void SetFile(FILE *file);
  void SetBuffer(void *buffer);
  void SetOffset(int offset);

  void ReadRaw(void *value, int size);
  void ReadValue(void *value, int size);
  void ReadString(void *value, int maxSize);

private:

  FILE *fFile;
  uint8_t *fBuffer;

  int fOffset;
};

#endif // ExRootXDRReader_h
