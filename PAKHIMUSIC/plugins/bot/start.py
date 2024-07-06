import time
import asyncio
import random
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
import config
from PAKHIMUSIC import app
from PAKHIMUSIC.misc import _boot_
from PAKHIMUSIC.plugins.sudo.sudoers import sudoers_list
from PAKHIMUSIC.utils.database import get_served_chats, get_served_users, get_sudoers
from PAKHIMUSIC.utils import bot_sys_stats
from PAKHIMUSIC.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)
from PAKHIMUSIC.utils.decorators.language import LanguageStart
from PAKHIMUSIC.utils.formatters import get_readable_time
from PAKHIMUSIC.utils.inline import help_pannel, private_panel, start_panel
from config import BANNED_USERS, AMOP
from strings import get_string
