#include "stdafx.h"
#include "StageManagerObject.h"
#include "Stagemanager.h"

namespace nsApp
{
	namespace nsActor
	{
		StageManagerObject::StageManagerObject()
		{
			StageManager::CreateInstance();
		}
		StageManagerObject::~StageManagerObject()
		{
			StageManager::DeleteInstance();
		}
		bool StageManagerObject::Start()
		{
			StageManager::GetInstance()->Start();
			return true;
		}
		void StageManagerObject::Update()
		{
			StageManager::GetInstance()->Update();
		}
		void StageManagerObject::Render(RenderContext& rc)
		{
			StageManager::GetInstance()->Render(rc);
		}
	}
}
