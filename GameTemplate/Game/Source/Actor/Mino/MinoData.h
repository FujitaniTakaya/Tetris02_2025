#pragma once
#include "stdafx.h"


namespace nsApp
{
	namespace nsActor
	{
		/*
		* ミノのタイプのenum 
		*/
		enum EnMinoType
		{
			enMinoType_I = 0,
			enMinoType_O,
			enMinoType_J,
			enMinoType_L,
			enMinoType_S,
			enMinoType_Z,
			enMinoType_T,
			enMinoType_Num,
			enMinoType_None = -1
		};

		namespace nsMino
		{

			constexpr float MINO_BLOCK_SIZE = 30.0f;	//ミノのブロックのサイズ

			/*
			* @brief	ミノのファイルパスを取得
			*/
			std::string GetMinoFilePath(EnMinoType type);
		}

		/*
		* @brief	ゲーム内のアクターの基底クラス。
		*/
		class MinoData
		{
		private:
			MinoData();
			~MinoData();
		};
	}
}

