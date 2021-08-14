editable = await message.reply_text("Please wait ...")
 
            await editable.edit(
                f"**Your File Stored in my Database!**\n\nHere is the Permanent Link of your file:  \n\nJust Click the link to get your file!",
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("♻️Open Link♻️", url=https://t.me/mhdfajisn/5)],
                     [InlineKeyboardButton("🔊Channel", url="https://t.me/Mo_Tech_Yt"),
                      InlineKeyboardButton("👨‍💼Group", url="https://t.me/Mo_Tech_Group")]]
                )
