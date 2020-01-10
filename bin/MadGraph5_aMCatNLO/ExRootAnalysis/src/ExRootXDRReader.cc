
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

#include "ExRootAnalysis/ExRootXDRReader.h"

#include <stdio.h>
#include <stdint.h>
#include <string.h>

//------------------------------------------------------------------------------

ExRootXDRReader::ExRootXDRReader() :
  fFile(0), fBuffer(0), fOffset(0)
{
}

//------------------------------------------------------------------------------

void ExRootXDRReader::SetFile(FILE *file)
{
  fFile = file;
}

//------------------------------------------------------------------------------

void ExRootXDRReader::SetBuffer(void *buffer)
{
  fBuffer = (uint8_t *)buffer;
  fOffset = 0;
}

//------------------------------------------------------------------------------

void ExRootXDRReader::SetOffset(int offset)
{
  fOffset = offset;
}

//------------------------------------------------------------------------------

void ExRootXDRReader::ReadRaw(void *value, int size)
{
  int rndup;

  rndup = size % 4;
  if(rndup > 0)
  {
    rndup = 4 - rndup;
  }

  if(fFile)
  {
    fread(value, 1, size + rndup, fFile);
  }
}

//------------------------------------------------------------------------------

void ExRootXDRReader::ReadValue(void *value, int size)
{
  int i;
  uint8_t *dst, buffer[8];

  dst = (uint8_t *)value;

  if(fBuffer)
  {
    fOffset += size;
    for(i = 0; i < size; ++i) dst[i] = fBuffer[fOffset - 1 - i];
  }
  else if(fFile)
  {
    ReadRaw(buffer, size);
    for(i = 0; i < size; ++i) dst[i] = buffer[size - 1 - i];
  }
}

//------------------------------------------------------------------------------

void ExRootXDRReader::ReadString(void *value, int maxSize)
{
  int32_t size;

  ReadValue(&size, 4);

  if(size > maxSize) size = maxSize;
    
  if(fBuffer)
  {
    memcpy(value, fBuffer + fOffset, size);
    fOffset += size;
  }
  else if(fFile)
  {
    ReadRaw(value, size);
  }
}

//------------------------------------------------------------------------------
