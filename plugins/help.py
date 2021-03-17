from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Currently Only supports Youtube Single(No playlist)🤗 /n Just Send Youtube Url /n Develop by @Ez_Tee"
    await message.reply_text(helptxt)
