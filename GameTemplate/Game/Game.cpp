#include "stdafx.h"
#include "Game.h"

namespace
{
	float moveAmount = 30.0f;
}

Game::Game()
{
}

Game::~Game()
{
}

bool Game::Start()
{
	for (int i = 0; i < 4; ++i)
	{
		m_spriteRender[i].Init("Assets/spriteData/mino/I.dds", 30.0f, 30.0f);
		m_spriteRender[i].SetPosition(Vector3(0.0f + i * 30.0f, 0.0f, 0.0f));
		m_spriteRender[i].Update();
	}
	return true;
}

void Game::Update()
{
}

void Game::Render(RenderContext& rc)
{
	for (int i = 0; i < 4; ++i)
	{
		m_spriteRender[i].Draw(rc);
	}
}