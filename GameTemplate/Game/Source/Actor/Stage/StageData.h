#pragma once
#include "stdafx.h"

namespace nsApp
{
	namespace nsActor
	{
		/*
		* @brief	ステージデータ。
		*/
		class StageData
		{
		public:
			StageData();
			~StageData();
		public:
			Vector3			pos;			//座標。
			SpriteRender*	sprite;			//スプライト。
			bool			isBlock;		//当たり判定があるかどうか。
		};
	}
}
