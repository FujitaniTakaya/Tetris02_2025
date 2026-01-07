#pragma once
#include "Source/Actor/Actor.h"

namespace nsApp
{
	namespace nsActor
	{
		/*
		* @brief	ステージマネージャーオブジェクト。
		*/
		class StageManagerObject : public Actor
		{
		public:
			StageManagerObject();
			virtual ~StageManagerObject()override;
			virtual bool Start()override;
			virtual void Update()override;
			virtual void Render(RenderContext& rc)override;
		};
	}
}

