#pragma once
#include "stdafx.h"
#include "StageData.h"

namespace nsApp
{
	namespace nsActor
	{
		namespace nsStage
		{
			constexpr int WIDTH = 10;	//横幅
			constexpr int HEIGTH = 22;	//立幅

			const Vector3 ORIGIN_POS = { -45.0f, 50.0f, 0.0f };
		}


		/*
		* @brief	ステージマネージャー。
		*/
		class StageManager
		{
		private:
			/** ステージマネージャーのインスタンス */
			static StageManager* m_instance;


		public:
			/** インスタンスの生成 */
			static void CreateInstance()
			{
				if (!m_instance)
				{
					m_instance = new StageManager();
				}
			}

			/** インスタンスの取得 */
			static StageManager* GetInstance()
			{
				return m_instance;
			}

			/** インスタンスの破棄 */
			static void DeleteInstance()
			{
				if (m_instance)
				{
					delete m_instance;
					m_instance = nullptr;
				}
			}


		public:
			/*
			* @brief	ステージデータを取得
			*/
			const StageData& GetStageData(int x, int y)const
			{
				return m_stageDataArray[x][y];
			}


		private:
			std::array<std::array<StageData, nsStage::HEIGTH>, nsStage::WIDTH> m_stageDataArray;


		private:
			StageManager();
			~StageManager();


		public:
			void Start();
			void Update();
			void Render(RenderContext& rc);


		private:
			/*
			*　@brief	ステージデータの初期設定
			*/
			void SetupStageData();

			/*
			* @brief	ステージ全体に対してアクセスする
			* @param	cb	コールバック関数
			*/
			void AccessStageData(std::function<void(int x, int y)> cb);
		};

	}
}

