#include "stdafx.h"
#include "StageData.h"

namespace nsApp
{
	namespace nsActor
	{
		StageData::StageData()
			: pos(Vector3::Zero)
			, sprite(nullptr)
			, isBlock(false)
		{
		}
		StageData::~StageData()
		{
		}
	}
}
