# Ported by X_ImFine
# Recode by @mrismanaziz

from telethon.tl.functions.contacts import BlockRequest, UnblockRequest

from indomie import CMD_HANDLER as cmd
from indomie import CMD_HELP, DEVS
from indomie.events import register
from indomie.utils import get_user_from_event, indomie_cmd


@indomie_cmd(pattern="gkick(?: |$)(.*)")
@register(pattern=r"^\.cgkick(?: |$)(.*)", sudo=True)
async def gspide(rk):
    lazy = rk
    sender = await lazy.get_sender()
    me = await lazy.client.get_me()
    if sender.id != me.id:
        rkp = await lazy.reply("`Processing...`")
    else:
        rkp = await lazy.edit("`Processing...`")
    me = await rk.client.get_me()
    await rkp.edit("`Memproses Global Kick Kang Caper Tolol!`")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    await rk.get_chat()
    a = b = 0
    if rk.is_private:
        user = rk.chat
        reason = rk.pattern_match.group(1)
    try:
        user, reason = await get_user_from_event(rk)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await rkp.edit("**Gagal Global Kick! Pengguna tidak dikenal.**")
    if user:
        if user.id == DEVS:
            return await rkp.edit("**Lu Mau Ngapain Anjg Gkick Tuhan Gua? Goblok Mana Bisa Lah Anjg!!!**")
        try:
            await rk.client(BlockRequest(user))
            await rk.client(UnblockRequest(user))
        except BaseException:
            pass
        testrk = [
            d.entity.id
            for d in await rk.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testrk:
            try:
                await rk.client.edit_permissions(i, user, view_messages=False)
                await rk.client.edit_permissions(i, user, send_messages=True)
                a += 1
                await rkp.edit(
                    f"`Memproses Global Kick Kang Caper Tolol! Gkicked di {a} Group Chats..`"
                )

            except BaseException:
                b += 1
    else:
        await rkp.edit("`Reply ke Chat Penggunanya Goblok!!`")

    return await rkp.edit(
        f"**Berhasil GKicked** [{user.first_name}](tg://user?id={user.id}) **di {a} Group Chats**"
    )


CMD_HELP.update(
    {
        "gkick": f"**Plugin : **`gkick`\
        \n\n  •  **Syntax :** `{cmd}gkick` <alasan>\
        \n  •  **Function : **kick pengguna secara global dari semua Administrasi Grup di mana Anda berada.\
    "
    }
)
