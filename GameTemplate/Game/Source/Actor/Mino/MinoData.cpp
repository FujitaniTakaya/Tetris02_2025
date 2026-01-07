#include "stdafx.h"
#include "MinoData.h"

namespace nsApp
{
	namespace nsActor
	{
		namespace
		{
			constexpr const char* MinoFilePath[enMinoType_Num] =
			{
				"Assets/spriteData/mino/I.dds",
				"Assets/spriteData/mino/O.dds",
				"Assets/spriteData/mino/J.dds",
				"Assets/spriteData/mino/L.dds",
				"Assets/spriteData/mino/S.dds",
				"Assets/spriteData/mino/Z.dds",
				"Assets/spriteData/mino/T.dds"
			};
		}

		namespace nsMino
		{
			std::string GetMinoFilePath(EnMinoType type)
			{
				return MinoFilePath[type];
			}
		}
		


		MinoData::MinoData()
		{
		}
		MinoData::~MinoData()
		{
		}
	}
}
