#pragma once
class Actor : public IGameObject
{
public:
	Actor();
	virtual ~Actor()override;
	virtual bool Start()override = 0;
	virtual void Update()override = 0;
	virtual void Render(RenderContext& rc)override = 0;
};

