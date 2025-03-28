# 📢 NoneBot 插件：broadcast_announcement

一个简单实用的 NoneBot2 插件，支持由超级管理员通过私聊向所有群发送统一公告消息。

---

## 🧩 插件功能

- 💬 支持 `.公告 内容` 私聊指令发布全群公告
- 🛡️ 仅限超级管理员（SUPERUSER）可触发
- 📡 自动获取所有已加入的群并逐个发送消息

---

## 📦 安装方法

1. 将插件文件放入插件目录中：

```
plugins/broadcast_announcement/__init__.py
```

2. 在 `.env.*` 或 `bot.py` 中配置超级管理员：

```env
SUPERUSERS=["你的QQ号"]
```

3. 修改插件中管理员 QQ（可选）：

打开 `__init__.py`，将 `ADMIN_ID` 修改为你的 QQ：

```python
ADMIN_ID = "你的QQ号"
```

⚠️ 如果你使用 SUPERUSER 权限判断，可以不设置此变量。

---

## 🚀 使用方法

在 QQ 私聊中对机器人发送如下指令：

```
.公告 今天晚上的活动改为8点开始，请大家注意时间安排！
```

Bot 会将该内容自动转发至所有已加入的群：

```
🎉bot公告：今天晚上的活动改为8点开始，请大家注意时间安排！
```

---

## ⚙️ 参数说明

| 变量名 | 说明 |
|--------|------|
| `ADMIN_ID` | 限制发送者为该管理员 ID（字符串格式） |
| `SUPERUSER` | NoneBot 权限控制（推荐启用） |
| `priority=10` | 控制事件优先级（可自定义） |

---

## 🔒 权限控制建议

建议同时结合 `SUPERUSER` 使用权限控制，确保只有你能发送公告：

```python
from nonebot.permission import SUPERUSER

announcement_matcher = on_message(priority=10, block=True, permission=SUPERUSER)
```

---

## 🪪 License

MIT License

---

## 🙏 感谢使用

由 [@Doya16](https://github.com/Doya16) 构建与维护。欢迎提出建议与改进意见！
