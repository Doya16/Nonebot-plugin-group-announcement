# plugins/broadcast_announcement/__init__.py

import re
from nonebot import on_message, get_bot
from nonebot.adapters.onebot.v11 import Bot, PrivateMessageEvent
from nonebot.permission import SUPERUSER

# 管理员QQ
ADMIN_ID = "替换成你的QQ号"

# 匹配格式为“.公告 内容”
announcement_matcher = on_message(priority=10, block=True)

@announcement_matcher.handle()
async def handle_announcement(event: PrivateMessageEvent, bot: Bot):
    # 判断是否为管理员发送的私聊消息
    if str(event.user_id) != ADMIN_ID:
        return

    text = event.get_plaintext().strip()
    if not text.startswith(".公告"):
        return

    content = text[3:].strip()
    if not content:
        await bot.send(event=event, message="❗公告内容不能为空")
        return

    # 获取所有群聊列表
    try:
        group_list = await bot.get_group_list()
    except Exception as e:
        await bot.send(event=event, message=f"❌ 获取群列表失败：{e}")
        return

    success = 0
    for group in group_list:
        group_id = group["group_id"]
        try:
            await bot.send_group_msg(
                group_id=group_id,
                message=f"🎉遐蝶bot公告：{content}"
            )
            success += 1
        except Exception as e:
            print(f"[公告插件] ❌ 发送至群 {group_id} 失败: {e}")

    await bot.send(event=event, message=f"✅ 公告已成功发送至 {success} 个群。")
