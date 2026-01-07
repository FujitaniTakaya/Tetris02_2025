#include "stdafx.h"
#include "StageManager.h"
#include "Source/Actor/Mino/MinoData.h"

namespace nsApp
{
	namespace nsActor
	{
		StageManager* StageManager::m_instance = nullptr;

		StageManager::StageManager()
		{
		}
		StageManager::~StageManager()
		{
		}
		void StageManager::Start()
		{
		}
		void StageManager::Update()
		{
		}
		void StageManager::Render(RenderContext& rc)
		{
		}
		void StageManager::SetupStageData()
		{
			const Vector3* origin = &nsStage::ORIGIN_POS;
			const float blockSize = nsMino::MINO_BLOCK_SIZE;

			AccessStageData(
				[&](int x, int y)
				{
					//ステージのポジションを設定
					Vector3* pos = &m_stageDataArray[x][y].pos;
					pos->x = origin->x + x * blockSize;
					pos->y = origin->y + y * blockSize;
					pos->z = 0.0f;

					//フラグをfalseに設定
					m_stageDataArray[x][y].isBlock = false;
					//spriteRenderをnullptrに設定
					m_stageDataArray[x][y].sprite = nullptr;
				}
			);
		}


		void StageManager::AccessStageData(std::function<void(int x, int y)> cb)
		{
			for (int y = 0; y < nsStage::HEIGTH; ++y)
			{
				for (int x = 0; x < nsStage::WIDTH; ++x)
				{
					cb(x, y);
				}
			}
		}
	}
}