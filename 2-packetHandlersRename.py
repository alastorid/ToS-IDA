#!/usr/bin/python
"""
Tree of Savior IDAPython Script
Packet handlers renaming
"""

import idaapi
import idautils
import idc
from enum import Enum

packetsType = [None] * 10000;
packetsType[3] = "CB_LOGIN" # Size = 4457
packetsType[4] = "CB_LOGIN_BY_PASSPORT" # Size = 1154
packetsType[5] = "CB_LOGOUT" # Size = 10
packetsType[12] = "CB_START_GAME" # Size = 13
packetsType[6] = "CB_START_BARRACK" # Size = 11
packetsType[7] = "CB_COMMANDER_CREATE" # Size = 93
packetsType[9] = "CB_COMMANDER_DESTROY" # Size = 18
packetsType[10] = "CB_CHECK_CLIENT_INTEGRITY" # Size = 74
packetsType[11] = "CB_CLIENT_INTEGRITY_FAIL" # Size = 1035
packetsType[83] = "CB_NOT_AUTHORIZED_ADDON_LIST" # Size = 1039
packetsType[15] = "CB_ECHO" # Size = 30
packetsType[13] = "CB_BARRACKNAME_CHANGE" # Size = 74
packetsType[14] = "CB_COMMANDER_MOVE" # Size = 31
packetsType[16] = "BC_LOGINOK" # Size = 156
packetsType[17] = "BC_CYOU_LOGIN_FAIL" # Size = 10
packetsType[18] = "BC_LOGIN_PACKET_RECEIVED" # Size = 10
packetsType[19] = "BC_LOGOUTOK" # Size = 10
packetsType[23] = "BC_START_GAMEOK" # Size = 37
packetsType[24] = "BC_SINGLE_INFO" # Size = 353
packetsType[20] = "BC_COMMANDER_LIST" # Size = 0
packetsType[8] = "BC_COMMANDER_CREATE_SLOTID" # Size = 11
packetsType[21] = "BC_COMMANDER_CREATE" # Size = 362
packetsType[22] = "BC_COMMANDER_DESTROY" # Size = 11
packetsType[25] = "BC_MESSAGE" # Size = 0
packetsType[26] = "BC_ECHO" # Size = 30
packetsType[50] = "CB_IES_MODIFY_INFO" # Size = 0
packetsType[51] = "BC_IES_MODIFY_INFO" # Size = 0
packetsType[52] = "BC_IES_MODIFY_LIST" # Size = 0
packetsType[53] = "CB_IES_REVISION_DELETE" # Size = 0
packetsType[54] = "BC_IES_REVISION_DELETE" # Size = 0
packetsType[27] = "BC_MYPAGE_MAP" # Size = 0
packetsType[28] = "BC_BARRACKNAME_CHANGE" # Size = 79
packetsType[57] = "CB_VISIT" # Size = 74
packetsType[58] = "CB_BUY_THEMA" # Size = 22
packetsType[59] = "BC_ACCOUNT_PROP" # Size = 0
packetsType[60] = "CB_CURRENT_BARRACK" # Size = 39
packetsType[82] = "CB_GEMSCOOL_PCINFO" # Size = 1290
packetsType[61] = "BC_NORMAL" # Size = 0
packetsType[62] = "CB_POSE" # Size = 15
packetsType[63] = "CB_PLACE_CMD" # Size = 46
packetsType[81] = "CB_NGS" # Size = 0
packetsType[64] = "CB_CHAT" # Size = 0
packetsType[65] = "BC_CHAT" # Size = 0
packetsType[66] = "CB_ECHO_NORMAL" # Size = 0
packetsType[71] = "CB_JUMP" # Size = 19
packetsType[72] = "BC_JUMP" # Size = 19
packetsType[73] = "BC_SERVER_ENTRY" # Size = 22
packetsType[74] = "CB_PET_PC" # Size = 26
packetsType[75] = "CB_PET_COMMAND" # Size = 27
packetsType[69] = "CB_CHANGE_BARRACK_LAYER" # Size = 22
packetsType[70] = "CB_SELECT_BARRACK_LAYER" # Size = 14
packetsType[55] = "CB_SCREENSHOT_HASH" # Size = 42
packetsType[67] = "CB_REQ_SLOT_PRICE" # Size = 10
packetsType[68] = "BC_REQ_SLOT_PRICE" # Size = 14
packetsType[76] = "CB_REQ_CHANGE_POSTBOX_STATE" # Size = 23
packetsType[78] = "CB_REQ_POSTBOX_PAGE" # Size = 14
packetsType[77] = "CB_REQ_GET_POSTBOX_ITEM" # Size = 1051
packetsType[79] = "BC_WAIT_QUEUE_ORDER" # Size = 14
packetsType[80] = "CB_CANCEL_SERVER_WAIT_QUEUE" # Size = 10
packetsType[56] = "CB_REQ_CHANNEL_TRAFFIC" # Size = 14
packetsType[84] = "CB_DEBUG_LOG_FILE" # Size = 0
packetsType[2901] = "CS_LOGIN" # Size = 91
packetsType[2902] = "SC_NORMAL" # Size = 0
packetsType[2903] = "SC_FROM_INTEGRATE" # Size = 0
packetsType[2904] = "CS_REGISTER_SNS_ID" # Size = 24
packetsType[2905] = "CS_REQ_SNS_PC_INFO" # Size = 0
packetsType[2906] = "CS_REQ_ADD_FRIEND" # Size = 74
packetsType[2907] = "CS_REQ_BLOCK_FRIEND" # Size = 74
packetsType[2908] = "CS_FRIEND_CMD" # Size = 32
packetsType[2909] = "CS_FRIEND_SET_ADDINFO" # Size = 168
packetsType[2910] = "CS_CHAT" # Size = 0
packetsType[2911] = "CS_GROUP_CHAT_INVITE" # Size = 114
packetsType[2912] = "CS_GROUP_CHAT_INVITE_BY_TAG" # Size = 26
packetsType[2913] = "CS_ALLOW_GROUP_CHAT_TAG_INVITE" # Size = 50
packetsType[2914] = "CS_REFRESH_GROUP_CHAT" # Size = 10
packetsType[2916] = "CS_REQ_CHAT_HISTORY" # Size = 26
packetsType[2917] = "CS_REQ_OUT_ROOM" # Size = 18
packetsType[2929] = "CS_ADD_RELATION_SCORE" # Size = 96
packetsType[2930] = "CS_GET_LIKE_COUNT" # Size = 24
packetsType[2926] = "CS_LIKE_IT" # Size = 96
packetsType[2927] = "CS_UNLIKE_IT" # Size = 32
packetsType[2928] = "CS_LIKE_IT_CONFIRM" # Size = 24
packetsType[2918] = "CS_REQ_RELATED_PC_SESSION" # Size = 24
packetsType[2919] = "CS_REDIS_SKILLPOINT" # Size = 26
packetsType[2915] = "CS_CREATE_GROUP_CHAT" # Size = 10
packetsType[2920] = "CS_PARTY_CLIENT_INFO_SEND" # Size = 0
packetsType[2921] = "CS_NORMAL_GAME_START" # Size = 10
packetsType[2922] = "CS_REQUEST_PVP_RANKING" # Size = 92
packetsType[2923] = "CS_REQUEST_ALL_SEASON_TOP_PVP_RANKING" # Size = 84
packetsType[2924] = "CS_INVITE_PARTY_PVP" # Size = 14
packetsType[2925] = "CS_ACCEPT_PARTY_PVP" # Size = 23
packetsType[3001] = "CZ_CONNECT" # Size = 1239
packetsType[3006] = "CZ_GAME_READY" # Size = 10
packetsType[3167] = "CZ_KEYBOARD_MOVE" # Size = 41
packetsType[3168] = "CZ_EXPECTED_STOP_POS" # Size = 31
packetsType[3172] = "CZ_MOVE_PATH" # Size = 27
packetsType[3173] = "CZ_MOVE_STOP" # Size = 35
packetsType[3169] = "CZ_JUMP" # Size = 11
packetsType[3170] = "CZ_DASHRUN" # Size = 12
packetsType[3174] = "CZ_REST_SIT" # Size = 10
packetsType[3175] = "CZ_REQ_CHAR_SLOT" # Size = 11
packetsType[3176] = "CZ_ON_AIR" # Size = 10
packetsType[3177] = "CZ_ON_GROUND" # Size = 10
packetsType[3171] = "CZ_SKILL_JUMP_REQ" # Size = 30
packetsType[3008] = "CZ_LOGOUT" # Size = 11
packetsType[3009] = "CZ_MOVE_BARRACK" # Size = 11
packetsType[3004] = "CZ_MOVE_ZONE_OK" # Size = 10
packetsType[3178] = "CZ_MOVEMENT_INFO" # Size = 23
packetsType[3613] = "CZ_NGS" # Size = 0
packetsType[3179] = "CZ_SKILL_TARGET" # Size = 19
packetsType[3180] = "CZ_SKILL_TARGET_ANI" # Size = 23
packetsType[3181] = "CZ_SKILL_GROUND" # Size = 61
packetsType[3182] = "CZ_SKILL_SELF" # Size = 35
packetsType[3183] = "CZ_SKILL_CANCEL" # Size = 12
packetsType[3184] = "CZ_HOLD" # Size = 11
packetsType[3192] = "CZ_SHOUT" # Size = 0
packetsType[3189] = "CZ_CHAT" # Size = 0
packetsType[3190] = "CZ_SELF_CHAT" # Size = 0
packetsType[3191] = "CZ_CHAT_LOG" # Size = 0
packetsType[3195] = "CZ_ITEM_USE" # Size = 22
packetsType[3196] = "CZ_ITEM_USE_TO_ITEM" # Size = 30
packetsType[3197] = "CZ_ITEM_USE_TO_GROUND" # Size = 30
packetsType[3193] = "CZ_ITEM_DROP" # Size = 22
packetsType[3200] = "CZ_ITEM_EQUIP" # Size = 19
packetsType[3201] = "CZ_ITEM_UNEQUIP" # Size = 11
packetsType[3202] = "CZ_REQ_DELETE_EXPIRED_ITEMS" # Size = 18
packetsType[3218] = "CZ_REQ_OPEN_ITEM_DUNGEON" # Size = 19
packetsType[3219] = "CZ_ANSWER_OPEN_ITEM_DUNGEON" # Size = 19
packetsType[3220] = "CZ_SEND_ITEM_PROP_TO_ALCHMIST" # Size = 28
packetsType[3221] = "CZ_EXCUTE_ITEM_DUNGEON" # Size = 34
packetsType[3222] = "ZC_RECIVE_ITEM_PROP_TO_TARGET" # Size = 0
packetsType[3203] = "ZC_CHECK_INVINDEX" # Size = 34
packetsType[3194] = "CZ_ITEM_DELETE" # Size = 0
packetsType[3198] = "CZ_ITEM_BUY" # Size = 0
packetsType[3199] = "CZ_ITEM_SELL" # Size = 0
packetsType[3234] = "CZ_DIALOG_ACK" # Size = 14
packetsType[3235] = "CZ_DIALOG_SELECT" # Size = 11
packetsType[3236] = "CZ_DIALOG_STRINGINPUT" # Size = 138
packetsType[3122] = "CZ_LEAVE_TO_DUNGEON" # Size = 10
packetsType[3255] = "CZ_MOVE_CAMP" # Size = 18
packetsType[3256] = "CZ_CAMPINFO" # Size = 18
packetsType[3257] = "ZC_CAMPINFO" # Size = 22
packetsType[3259] = "CZ_TARGET_JOB_INFO" # Size = 18
packetsType[3260] = "ZC_TARGET_JOB_INFO" # Size = 18
packetsType[3166] = "CZ_CLICK_TRIGGER" # Size = 15
packetsType[3185] = "CZ_ROTATE" # Size = 18
packetsType[3186] = "CZ_HEAD_ROTATE" # Size = 18
packetsType[3187] = "CZ_TARGET_ROTATE" # Size = 18
packetsType[3188] = "CZ_POSE" # Size = 34
packetsType[3616] = "CZ_SYSTEM_LOG_TO_SERVER" # Size = 1099
packetsType[3618] = "CZ_CANCEL_INDUN_MATCHING" # Size = 10
packetsType[3619] = "CZ_CANCEL_INDUN_PARTY_MATCHING" # Size = 10
packetsType[3624] = "CZ_PARTY_SHARED_QUEST" # Size = 278
packetsType[3648] = "CZ_REQ_FORGERY" # Size = 30
packetsType[3651] = "CZ_REQ_BUILD_FOODTABLE" # Size = 79
packetsType[3653] = "CZ_REQ_FISHING" # Size = 23
packetsType[3654] = "CZ_REQ_GET_FISHING_ITEM" # Size = 10
packetsType[3662] = "CZ_REQ_FISHING_RANK" # Size = 78
packetsType[3663] = "ZC_ENABLE_ROTATE" # Size = 79
packetsType[3667] = "CZ_REQ_ADVENTURE_BOOK_RANK" # Size = 142
packetsType[3668] = "CZ_REQ_ADVENTURE_BOOK_REWARD" # Size = 74
packetsType[3670] = "CZ_REQ_QUEST_COMPLETE" # Size = 14
packetsType[3671] = "CZ_REQ_GUILD_ASSET_LOG" # Size = 10
packetsType[3101] = "ZC_ENTER_PC" # Size = 366
packetsType[3102] = "ZC_ENTER_MONSTER" # Size = 0
packetsType[3103] = "ZC_ENTER_DUMMYPC" # Size = 328
packetsType[3104] = "ZC_UPDATED_DUMMYPC" # Size = 286
packetsType[3105] = "ZC_ENTER_ITEM" # Size = 107
packetsType[3106] = "ZC_LEAVE" # Size = 16
packetsType[3107] = "ZC_MOVE_PATH" # Size = 46
packetsType[3108] = "ZC_MOVE_POS" # Size = 47
packetsType[3109] = "ZC_MOVE_BEZIER" # Size = 79
packetsType[3112] = "ZC_MSPD" # Size = 18
packetsType[3113] = "ZC_MOVE_SPEED" # Size = 23
packetsType[3110] = "ZC_MOVE_DIR" # Size = 44
packetsType[3111] = "ZC_EXPECTED_STOPPOS" # Size = 39
packetsType[3114] = "ZC_MOVE_STOP" # Size = 27
packetsType[3115] = "ZC_REST_SIT" # Size = 16
packetsType[3116] = "ZC_JUMP" # Size = 23
packetsType[3117] = "ZC_JUMP_DIR" # Size = 38
packetsType[3118] = "ZC_ORDER_SKILL_JUMP" # Size = 14
packetsType[3119] = "ZC_SKILL_JUMP" # Size = 42
packetsType[3120] = "ZC_SET_POS" # Size = 27
packetsType[3121] = "ZC_FILE_MOVE" # Size = 50
packetsType[3012] = "ZC_MESSAGE" # Size = 0
packetsType[3002] = "ZC_CONNECT_OK" # Size = 0
packetsType[3005] = "ZC_CONNECT_FAILED" # Size = 0
packetsType[3014] = "ZC_START_GAME" # Size = 30
packetsType[3003] = "ZC_MOVE_ZONE" # Size = 11
packetsType[3010] = "ZC_MOVE_BARRACK" # Size = 10
packetsType[3007] = "ZC_MOVE_ZONE_OK" # Size = 61
packetsType[3152] = "ZC_DEAD" # Size = 0
packetsType[3153] = "ZC_RESURRECT" # Size = 22
packetsType[3155] = "ZC_RESURRECT_DIALOG" # Size = 14
packetsType[3163] = "CZ_RESURRECT" # Size = 19
packetsType[3164] = "ZC_RESURRECT_SAVE_POINT_ACK" # Size = 11
packetsType[3165] = "ZC_RESURRECT_HERE_ACK" # Size = 11
packetsType[3123] = "ZC_UPDATED_PCAPPEARANCE" # Size = 286
packetsType[3124] = "ZC_UPDATED_MONSTERAPPEARANCE" # Size = 0
packetsType[3128] = "ZC_ADD_HP" # Size = 26
packetsType[3231] = "ZC_UPDATE_SP" # Size = 19
packetsType[3233] = "ZC_UPDATE_MHP" # Size = 18
packetsType[3225] = "ZC_EXP_UP" # Size = 26
packetsType[3226] = "ZC_EXP_UP_BY_MONSTER" # Size = 30
packetsType[3227] = "ZC_PC_LEVELUP" # Size = 18
packetsType[3228] = "ZC_PC_STAT_AVG" # Size = 34
packetsType[3229] = "ZC_MAX_EXP_CHANGED" # Size = 38
packetsType[3268] = "ZC_UPDATE_ALL_STATUS" # Size = 30
packetsType[3154] = "ZC_CHANGE_RELATION" # Size = 15
packetsType[3214] = "ZC_QUICK_SLOT_LIST" # Size = 0
packetsType[3215] = "ZC_SKILL_LIST" # Size = 0
packetsType[3216] = "ZC_SKILL_ADD" # Size = 0
packetsType[3129] = "ZC_SKILL_CAST_CANCEL" # Size = 14
packetsType[3130] = "ZC_SKILL_CAST" # Size = 42
packetsType[3131] = "ZC_SKILL_READY" # Size = 54
packetsType[3133] = "ZC_SKILL_USE_CANCEL" # Size = 14
packetsType[3132] = "ZC_SKILL_DISABLE" # Size = 19
packetsType[3134] = "ZC_SKILL_MELEE_TARGET" # Size = 0
packetsType[3136] = "ZC_SKILL_FORCE_TARGET" # Size = 0
packetsType[3135] = "ZC_SKILL_MELEE_GROUND" # Size = 0
packetsType[3137] = "ZC_SKILL_FORCE_GROUND" # Size = 0
packetsType[3138] = "ZC_SKILL_HIT_INFO" # Size = 0
packetsType[3217] = "ZC_ABILITY_LIST" # Size = 0
packetsType[3223] = "CZ_DISPEL_DEBUFF_TOGGLE" # Size = 14
packetsType[3224] = "CZ_JUNGTAN_TOGGLE" # Size = 24
packetsType[3139] = "ZC_BUFF_LIST" # Size = 0
packetsType[3140] = "ZC_BUFF_ADD" # Size = 0
packetsType[3141] = "ZC_BUFF_UPDATE" # Size = 0
packetsType[3142] = "ZC_BUFF_REMOVE" # Size = 24
packetsType[3143] = "ZC_BUFF_CLEAR" # Size = 15
packetsType[3144] = "CZ_BUFF_REMOVE" # Size = 14
packetsType[3145] = "CZ_INTE_WARP" # Size = 14
packetsType[3156] = "ZC_HIT_INFO" # Size = 69
packetsType[3157] = "ZC_HEAL_INFO" # Size = 34
packetsType[3159] = "ZC_CAUTION_DAMAGE_INFO" # Size = 19
packetsType[3160] = "ZC_CAUTION_DAMAGE_RELEASE" # Size = 14
packetsType[3161] = "ZC_KNOCKBACK_INFO" # Size = 74
packetsType[3162] = "ZC_KNOCKDOWN_INFO" # Size = 75
packetsType[3125] = "ZC_CHAT" # Size = 0
packetsType[3126] = "ZC_CHAT_WITH_TEXTCODE" # Size = 18
packetsType[3271] = "ZC_SHOUT" # Size = 0
packetsType[3272] = "ZC_SHOUT_FAILED" # Size = 11
packetsType[3230] = "ZC_TEXT" # Size = 0
packetsType[3015] = "ZC_QUIET" # Size = 11
packetsType[3241] = "ZC_DIALOG_CLOSE" # Size = 10
packetsType[3237] = "ZC_DIALOG_OK" # Size = 0
packetsType[3238] = "ZC_DIALOG_NEXT" # Size = 0
packetsType[3239] = "ZC_DIALOG_SELECT" # Size = 0
packetsType[3242] = "ZC_DIALOG_TRADE" # Size = 43
packetsType[3243] = "ZC_DIALOG_COMMON_TRADE" # Size = 43
packetsType[3240] = "ZC_DIALOG_ITEM_SELECT" # Size = 0
packetsType[3244] = "ZC_DIALOG_NUMBERRANGE" # Size = 0
packetsType[3245] = "ZC_DIALOG_STRINGINPUT" # Size = 0
packetsType[3127] = "ZC_STANCE_CHANGE" # Size = 18
packetsType[3210] = "ZC_ITEM_ADD" # Size = 0
packetsType[3206] = "ZC_ITEM_INVENTORY_LIST" # Size = 0
packetsType[3207] = "ZC_ITEM_INVENTORY_DIVISION_LIST" # Size = 0
packetsType[3208] = "ZC_ITEM_INVENTORY_INDEX_LIST" # Size = 0
packetsType[3209] = "ZC_ITEM_EQUIP_LIST" # Size = 0
packetsType[3211] = "ZC_ITEM_REMOVE" # Size = 24
packetsType[3212] = "ZC_ITEM_USE" # Size = 18
packetsType[3213] = "ZC_ITEM_USE_TO_GROUND" # Size = 26
packetsType[3013] = "ZC_RESET_VIEW" # Size = 10
packetsType[3232] = "ZC_RESTORATION" # Size = 16
packetsType[3146] = "ZC_ROTATE" # Size = 24
packetsType[3147] = "ZC_ROTATE_RESERVED" # Size = 22
packetsType[3148] = "ZC_HEAD_ROTATE" # Size = 22
packetsType[3149] = "ZC_TARGET_ROTATE" # Size = 22
packetsType[3150] = "ZC_QUICK_ROTATE" # Size = 22
packetsType[3151] = "ZC_POSE" # Size = 38
packetsType[3270] = "ZC_DUMP_PROPERTY" # Size = 0
packetsType[3269] = "ZC_OBJECT_PROPERTY" # Size = 0
packetsType[3246] = "ZC_ADDON_MSG" # Size = 0
packetsType[3247] = "CZ_UI_EVENT" # Size = 0
packetsType[3011] = "ZC_LOGOUT_OK" # Size = 10
packetsType[3248] = "ZC_PLAY_SOUND" # Size = 19
packetsType[3249] = "ZC_STOP_SOUND" # Size = 18
packetsType[3250] = "ZC_PLAY_MUSICQUEUE" # Size = 18
packetsType[3251] = "ZC_STOP_MUSICQUEUE" # Size = 18
packetsType[3252] = "ZC_PLAY_ANI" # Size = 28
packetsType[3253] = "ZC_PLAY_ANI_SELFISH" # Size = 23
packetsType[3254] = "ZC_CHANGE_ANI" # Size = 48
packetsType[3264] = "ZC_PLAY_ALARMSOUND" # Size = 87
packetsType[3265] = "ZC_STOP_ALARMSOUND" # Size = 14
packetsType[3266] = "ZC_PLAY_EXP_TEXT" # Size = 18
packetsType[3267] = "ZC_PLAY_NAVI_EFFECT" # Size = 154
packetsType[3273] = "CZ_EXCHANGE_REQUEST" # Size = 14
packetsType[3274] = "ZC_EXCHANGE_REQUEST_ACK" # Size = 76
packetsType[3275] = "ZC_EXCHANGE_REQUEST_RECEIVED" # Size = 75
packetsType[3276] = "CZ_EXCHANGE_ACCEPT" # Size = 10
packetsType[3277] = "CZ_EXCHANGE_DECLINE" # Size = 10
packetsType[3278] = "ZC_EXCHANGE_DECLINE_ACK" # Size = 10
packetsType[3279] = "ZC_EXCHANGE_START" # Size = 76
packetsType[3280] = "CZ_EXCHANGE_OFFER" # Size = 30
packetsType[3281] = "ZC_EXCHANGE_OFFER_ACK" # Size = 0
packetsType[3282] = "CZ_EXCHANGE_AGREE" # Size = 10
packetsType[3283] = "ZC_EXCHANGE_AGREE_ACK" # Size = 11
packetsType[3284] = "CZ_EXCHANGE_FINALAGREE" # Size = 10
packetsType[3285] = "ZC_EXCHANGE_FINALAGREE_ACK" # Size = 11
packetsType[3286] = "CZ_EXCHANGE_CANCEL" # Size = 10
packetsType[3287] = "ZC_EXCHANGE_CANCEL_ACK" # Size = 10
packetsType[3288] = "ZC_EXCHANGE_SUCCESS" # Size = 10
packetsType[3289] = "ZC_COOLDOWN_LIST" # Size = 0
packetsType[3290] = "ZC_COOLDOWN_CHANGED" # Size = 31
packetsType[3291] = "ZC_OVERHEAT_CHANGED" # Size = 34
packetsType[3292] = "ZC_TEST_AGENT" # Size = 22
packetsType[3293] = "CZ_COMMON_SHOP_LIST" # Size = 10
packetsType[3294] = "ZC_COMMON_SHOP_LIST" # Size = 12
packetsType[3295] = "ZC_TIME_FACTOR" # Size = 14
packetsType[3296] = "ZC_PARTY_ENTER" # Size = 0
packetsType[3297] = "ZC_PARTY_OUT" # Size = 28
packetsType[3298] = "ZC_PARTY_DESTROY" # Size = 19
packetsType[3299] = "ZC_PARTY_INFO" # Size = 0
packetsType[3300] = "ZC_PARTY_LIST" # Size = 0
packetsType[3301] = "ZC_PARTY_CHAT" # Size = 0
packetsType[3302] = "ZC_PARTY_INST_INFO" # Size = 0
packetsType[3303] = "ZC_CHANGE_EQUIP_DURABILITY" # Size = 15
packetsType[3304] = "CZ_DIALOG_TX" # Size = 0
packetsType[3305] = "CZ_REQ_RECIPE" # Size = 0
packetsType[3306] = "ZC_CUSTOM_DIALOG" # Size = 79
packetsType[3307] = "ZC_SESSION_OBJECTS" # Size = 0
packetsType[3308] = "ZC_SESSION_OBJ_ADD" # Size = 0
packetsType[3309] = "ZC_SESSION_OBJ_REMOVE" # Size = 14
packetsType[3310] = "ZC_SESSION_OBJ_TIME" # Size = 18
packetsType[3311] = "CZ_S_OBJ_VALUE_C" # Size = 26
packetsType[3312] = "CZ_REQ_NORMAL_TX" # Size = 45
packetsType[3313] = "ZC_COMMANDER_LOADER_INFO" # Size = 0
packetsType[3314] = "ZC_MOVE_SINGLE_ZONE" # Size = 22
packetsType[3315] = "ZC_BACKTO_ORIGINAL_SERVER" # Size = 12
packetsType[3316] = "CZ_BACKTO_ORIGINAL_SERVER" # Size = 12
packetsType[3317] = "CZ_REQ_NORMAL_TX_NUMARG" # Size = 0
packetsType[3318] = "ZC_UI_OPEN" # Size = 43
packetsType[3319] = "ZC_ENABLE_CONTROL" # Size = 79
packetsType[3320] = "ZC_CHANGE_CAMERA" # Size = 35
packetsType[3321] = "ZC_MONSTER_SDR_CHANGED" # Size = 15
packetsType[3322] = "ZC_MOVE_IGNORE_COLLISION" # Size = 34
packetsType[3323] = "ZC_CHANGE_CAMERA_ZOOM" # Size = 38
packetsType[3324] = "ZC_PLAY_SKILL_ANI" # Size = 86
packetsType[3325] = "ZC_PLAY_SKILL_CAST_ANI" # Size = 34
packetsType[3326] = "CZ_REQ_ITEM_GET" # Size = 14
packetsType[3327] = "ZC_ITEM_GET" # Size = 22
packetsType[3328] = "CZ_GUARD" # Size = 19
packetsType[3329] = "ZC_GUARD" # Size = 23
packetsType[3330] = "ZC_STAMINA" # Size = 14
packetsType[3331] = "ZC_ADD_STAMINA" # Size = 14
packetsType[3332] = "ZC_GM_ORDER" # Size = 14
packetsType[3333] = "ZC_MYPC_ENTER" # Size = 23
packetsType[3334] = "ZC_LOCK_KEY" # Size = 79
packetsType[3204] = "CZ_PREMIUM_ENCHANTCHIP" # Size = 26
packetsType[3205] = "CZ_PREMIUM_GACHACUBE" # Size = 10
packetsType[3335] = "ZC_SAVE_INFO" # Size = 10
packetsType[3336] = "CZ_SAVE_INFO" # Size = 0
packetsType[3337] = "ZC_OPTION_LIST" # Size = 0
packetsType[3338] = "ZC_SKILLMAP_LIST" # Size = 0
packetsType[3340] = "CZ_FOOD_TABLE_TITLE" # Size = 79
packetsType[3341] = "CZ_USE_TP_AND_ENTER_INDUN" # Size = 522
packetsType[3342] = "CZ_USE_RANKRESET_ITEM" # Size = 18
packetsType[3343] = "CZ_REQ_RANKRESET_SYSTEM" # Size = 19
packetsType[3339] = "CZ_GIVEITEM_TO_DUMMYPC" # Size = 22
packetsType[3344] = "ZC_SET_LAYER" # Size = 15
packetsType[3345] = "ZC_CREATE_LAYERBOX" # Size = 42
packetsType[3346] = "ZC_RESET_BOX" # Size = 15
packetsType[3347] = "ZC_CREATE_SCROLLLOCKBOX" # Size = 42
packetsType[3348] = "ZC_REMOVE_SCROLLLOCKBOX" # Size = 14
packetsType[3349] = "CZ_DYNAMIC_CASTING_START" # Size = 25
packetsType[3350] = "CZ_DYNAMIC_CASTING_END" # Size = 20
packetsType[3351] = "CZ_SKILL_CANCEL_SCRIPT" # Size = 10
packetsType[3352] = "ZC_LEAVE_TRIGGER" # Size = 10
packetsType[3353] = "ZC_BORN" # Size = 14
packetsType[3354] = "ZC_ACHIEVE_POINT_LIST" # Size = 0
packetsType[3355] = "ZC_ACHIEVE_POINT" # Size = 22
packetsType[3356] = "CZ_ACHIEVE_EQUIP" # Size = 14
packetsType[3357] = "ZC_ACHIEVE_EQUIP" # Size = 22
packetsType[3358] = "CZ_ACHIEVE_REWARD" # Size = 14
packetsType[3359] = "CZ_CHANGE_CONFIG" # Size = 18
packetsType[3360] = "CZ_CHANGE_CONFIG_STR" # Size = 34
packetsType[3361] = "ZC_WORLD_MSG" # Size = 47
packetsType[3362] = "ZC_ENABLE_SHOW_ITEM_GET" # Size = 12
packetsType[3363] = "ZC_LOGIN_TIME" # Size = 18
packetsType[3364] = "ZC_GIVE_EXP_TO_PC" # Size = 50
packetsType[3365] = "ZC_LAYER_PC_LIST" # Size = 0
packetsType[3366] = "ZC_LAYER_PC_SOBJ_PROP" # Size = 0
packetsType[3367] = "CZ_CUSTOM_COMMAND" # Size = 26
packetsType[3515] = "CZ_ADD_HELP" # Size = 14
packetsType[3368] = "ZC_LAYER_INFO" # Size = 14
packetsType[3369] = "CZ_CHAT_MACRO" # Size = 146
packetsType[3370] = "ZC_CHAT_MACRO_LIST" # Size = 0
packetsType[3371] = "ZC_RULLET_LIST" # Size = 0
packetsType[3372] = "ZC_QUICKSLOT_REGISTER" # Size = 50
packetsType[3373] = "CZ_QUICKSLOT_LIST" # Size = 0
packetsType[3374] = "CZ_DOUBLE_ITEM_EQUIP" # Size = 28
packetsType[3375] = "ZC_TRICK_PACKET" # Size = 0
packetsType[3376] = "ZC_COOLDOWN_RATE" # Size = 26
packetsType[3377] = "ZC_MAP_REVEAL_LIST" # Size = 0
packetsType[3378] = "CZ_MAP_REVEAL_INFO" # Size = 146
packetsType[3379] = "CZ_MAP_SEARCH_INFO" # Size = 55
packetsType[3380] = "ZC_EXEC_CLIENT_SCP" # Size = 0
packetsType[3381] = "ZC_SET_NPC_STATE" # Size = 22
packetsType[3382] = "ZC_NPC_STATE_LIST" # Size = 0
packetsType[3383] = "CZ_QUEST_NPC_STATE_CHECK" # Size = 14
packetsType[3384] = "ZC_RANK_ACHIEVE_ADD" # Size = 18
packetsType[3385] = "CZ_IES_MODIFY_INFO" # Size = 0
packetsType[3386] = "ZC_IES_MODIFY_INFO" # Size = 0
packetsType[3387] = "ZC_IES_MODIFY_LIST" # Size = 0
packetsType[3388] = "CZ_IES_REVISION_DELETE" # Size = 0
packetsType[3389] = "ZC_IES_REVISION_DELETE" # Size = 0
packetsType[3390] = "ZC_EQUIP_ITEM_REMOVE" # Size = 22
packetsType[3391] = "ZC_SOLD_ITEM_LIST" # Size = 0
packetsType[3392] = "ZC_SOLD_ITEM_DIVISION_LIST" # Size = 0
packetsType[3393] = "CZ_SOLD_ITEM" # Size = 19
packetsType[3394] = "CZ_WAREHOUSE_CMD" # Size = 32
packetsType[3395] = "CZ_SWAP_ETC_INV_CHANGE_INDEX" # Size = 35
packetsType[3396] = "CZ_SORT_INV" # Size = 12
packetsType[3397] = "CZ_EXTEND_WAREHOUSE" # Size = 11
packetsType[3398] = "CZ_CAST_CONTROL_SHOT" # Size = 10
packetsType[3399] = "ZC_PC_PROP_UPDATE" # Size = 15
packetsType[3400] = "CZ_CLIENT_DAMAGE" # Size = 14
packetsType[3401] = "CZ_CLIENT_ATTACK" # Size = 15
packetsType[3402] = "ZC_SYSTEM_MSG" # Size = 0
packetsType[3403] = "ZC_FSM_MOVE" # Size = 0
packetsType[3404] = "CZ_QUEST_CHECK_SAVE" # Size = 50
packetsType[3405] = "CZ_SPRAY_REQ_INFO" # Size = 14
packetsType[3406] = "CZ_SPRAY_DRAW_INFO" # Size = 0
packetsType[3407] = "ZC_SPRAY_ID" # Size = 22
packetsType[3408] = "ZC_SPRAY_DRAW_INFO" # Size = 0
packetsType[3409] = "ZC_MONSTER_LIFETIME" # Size = 18
packetsType[3410] = "ZC_SPRAY_LIKE_LIST" # Size = 0
packetsType[3411] = "ZC_SHARED_MSG" # Size = 14
packetsType[3412] = "CZ_REQ_TX_ITEM" # Size = 0
packetsType[3413] = "ZC_TEST_DBG" # Size = 0
packetsType[3414] = "ZC_MONSTER_DIST" # Size = 0
packetsType[3415] = "ZC_RESET_SKILL_FORCEID" # Size = 14
packetsType[3416] = "ZC_EMOTICON" # Size = 22
packetsType[3417] = "ZC_SHOW_EMOTICON" # Size = 22
packetsType[3418] = "ZC_TREASUREMARK_BY_MAP" # Size = 0
packetsType[3419] = "ZC_SHOW_MAP" # Size = 0
packetsType[216] = "ZC_TREASUREMARK_LIST_MAP" # Size = 0
packetsType[3258] = "ZC_FIX_ANIM" # Size = 18
packetsType[3261] = "ZC_MOVE_ANIM" # Size = 16
packetsType[3420] = "CZ_FLEE_OBSTACLE" # Size = 26
packetsType[3421] = "ZC_HOLD_MOVE_PATH" # Size = 15
packetsType[3422] = "ZC_ENTER_HOOK" # Size = 14
packetsType[3423] = "ZC_LEAVE_HOOK" # Size = 14
packetsType[3424] = "ZC_MONSTER_PROPERTY" # Size = 0
packetsType[3425] = "ZC_GROUND_EFFECT" # Size = 54
packetsType[3426] = "ZC_FLY" # Size = 22
packetsType[3428] = "ZC_FLY_MATH" # Size = 27
packetsType[3427] = "ZC_FLY_OPTION" # Size = 18
packetsType[3429] = "ZC_FLY_HEIGHT" # Size = 18
packetsType[3430] = "ZC_UPDATE_SHIELD" # Size = 18
packetsType[3431] = "ZC_SHOW_MODEL" # Size = 19
packetsType[3432] = "ZC_SKILL_RANGE_DBG" # Size = 62
packetsType[3433] = "ZC_SKILL_RANGE_FAN" # Size = 44
packetsType[3434] = "ZC_SKILL_RANGE_SQUARE" # Size = 44
packetsType[3435] = "ZC_SKILL_RANGE_CIRCLE" # Size = 32
packetsType[3436] = "ZC_SKILL_RANGE_DONUTS" # Size = 36
packetsType[3437] = "ZC_TEAMID" # Size = 15
packetsType[3438] = "ZC_PC" # Size = 0
packetsType[3439] = "CZ_LOG" # Size = 0
packetsType[3440] = "ZC_MOTIONBLUR" # Size = 15
packetsType[3441] = "ZC_PLAY_FORCE" # Size = 82
packetsType[3442] = "ZC_CAST_TARGET" # Size = 18
packetsType[3443] = "ZC_START_INFO" # Size = 0
packetsType[3444] = "ZC_JOB_EXP_UP" # Size = 26
packetsType[3445] = "ZC_JOB_PTS" # Size = 22
packetsType[3446] = "ZC_MON_STAMINA" # Size = 26
packetsType[3447] = "CZ_CUSTOM_SCP" # Size = 14
packetsType[3448] = "ZC_VIEW_FOCUS" # Size = 28
packetsType[3449] = "ZC_HARDCODED_SKILL" # Size = 30
packetsType[3450] = "CZ_HARDCODED_SKILL" # Size = 34
packetsType[3451] = "ZC_FORCE_MOVE" # Size = 34
packetsType[3452] = "ZC_HSKILL_CONTROL" # Size = 26
packetsType[3453] = "ZC_CANCEL_DEADEVENT" # Size = 14
packetsType[3454] = "ZC_ACTION_PKS" # Size = 39
packetsType[3455] = "CZ_HARDCODED_ITEM" # Size = 22
packetsType[3457] = "CZ_BRIQUET" # Size = 32
packetsType[3456] = "CZ_CANCEL_TRANSFORM_SKILL" # Size = 10
packetsType[3458] = "ZC_VIBRATE" # Size = 34
packetsType[3459] = "ZC_COUNTER_MOVE" # Size = 14
packetsType[3460] = "CZ_COUNTER_ATTACK" # Size = 14
packetsType[3461] = "CZ_CLIENT_DIRECT" # Size = 30
packetsType[3462] = "ZC_CLIENT_DIRECT" # Size = 34
packetsType[3463] = "ZC_OWNER" # Size = 18
packetsType[3464] = "ZC_GD_RANK" # Size = 14
packetsType[3465] = "CZ_RUN_BGEVENT" # Size = 74
packetsType[3466] = "ZC_ADD_SKILL_EFFECT" # Size = 22
packetsType[3467] = "ZC_ITEM_DROPABLE" # Size = 14
packetsType[3468] = "CZ_ITEM_DROP_TO_OBJECT" # Size = 26
packetsType[3469] = "ZC_NORMAL" # Size = 0
packetsType[3470] = "CZ_G_QUEST_CHECK" # Size = 14
packetsType[3471] = "ZC_MOVE_PATH_MATH" # Size = 34
packetsType[3488] = "ZC_SHOW_GROUND_ITEM_MARK" # Size = 34
packetsType[3489] = "ZC_HELP_LIST" # Size = 0
packetsType[3490] = "ZC_HELP_ADD" # Size = 15
packetsType[3262] = "ZC_STD_ANIM" # Size = 15
packetsType[3491] = "CZ_CLIENT_HIT_LIST" # Size = 0
packetsType[3492] = "ZC_PC_ATKSTATE" # Size = 15
packetsType[3493] = "ZC_SEND_PREMIUM_STATE" # Size = 20
packetsType[3494] = "CZ_HELP_READ_TYPE" # Size = 18
packetsType[3495] = "CZ_MOVE_PATH_END" # Size = 10
packetsType[3496] = "ZC_COLL_DAMAGE" # Size = 15
packetsType[3497] = "CZ_KEYBOARD_BEAT" # Size = 10
packetsType[3498] = "CZ_MOVEHIT_SCP" # Size = 22
packetsType[3499] = "ZC_SYNC_START" # Size = 18
packetsType[3500] = "ZC_SYNC_END" # Size = 18
packetsType[3501] = "ZC_SYNC_EXEC" # Size = 14
packetsType[3502] = "ZC_SYNC_EXEC_BY_SKILL_TIME" # Size = 22
packetsType[3503] = "CZ_STOP_TIMEACTION" # Size = 11
packetsType[3504] = "CZ_REQ_DUMMYPC_INFO" # Size = 18
packetsType[3505] = "CZ_VISIT_BARRACK" # Size = 74
packetsType[3506] = "CZ_SPC_SKILL_POS" # Size = 22
packetsType[3510] = "CZ_REQ_MINITEXT" # Size = 266
packetsType[3511] = "ZC_PC_MOVE_STOP" # Size = 39
packetsType[3521] = "CZ_SKILL_TOOL_GROUND_POS" # Size = 26
packetsType[3507] = "CZ_CHANGE_HEAD" # Size = 74
packetsType[3508] = "CZ_CREATE_ARROW_CRAFT" # Size = 14
packetsType[3509] = "CZ_EXCHANGE_ANTIQUE" # Size = 22
packetsType[3620] = "CZ_REQ_GM_ORDER" # Size = 202
packetsType[3621] = "CZ_REPORT_AUTOBOT" # Size = 74
packetsType[3622] = "CZ_REPORT_PVP_ZOOM" # Size = 10
packetsType[3642] = "CZ_SCREENSHOT_HASH" # Size = 43
packetsType[3643] = "CZ_REQ_MOVE_TO_INDUN" # Size = 18
packetsType[3644] = "CZ_CLEAR_INDUN_REG" # Size = 10
packetsType[3645] = "CZ_REQ_REGISTER_TO_INDUN" # Size = 14
packetsType[3646] = "CZ_REQ_GUILD_MEMBER_AUTHORITY" # Size = 23
packetsType[3647] = "CZ_TPSHOP_RTPP_FOR_TEST" # Size = 10
packetsType[3649] = "CZ_REQ_UNDERSTAFF_ENTER_ALLOW" # Size = 10
packetsType[3650] = "CZ_REQ_UNDERSTAFF_ENTER_ALLOW_WITH_PARTY" # Size = 14
packetsType[3652] = "ZC_PLAY_PAIR_ANIMATION" # Size = 38
packetsType[3655] = "ZC_PLAY_ATTACH_MODEL_ANIM" # Size = 26
packetsType[3661] = "ZC_FISHING_ITEM_LIST" # Size = 0
packetsType[3665] = "ZC_ADVENTURE_BOOK_INFO" # Size = 0
packetsType[3672] = "ZC_COLONY_OCCUPATION_INFO" # Size = 0
packetsType[3673] = "ZC_BROAD_CAST_MY_INFO" # Size = 30
packetsType[3674] = "CZ_REQ_RETURN_TO_CITY_FROM_COLONY_WAR" # Size = 10
packetsType[3681] = "ZC_ATTENDANCE_RECEIPT_REWARD" # Size = 0
packetsType[3682] = "CZ_REGISTER_NEW_GUILD_EMBLEM" # Size = 20095
packetsType[3683] = "CZ_CHANGE_GUILD_EMBLEM" # Size = 20096
packetsType[3684] = "ZC_UPDATE_GUILD_EMBLEM" # Size = 20048
packetsType[3685] = "CZ_REQUEST_CERTAIN_GUILD_EMBLEM" # Size = 20
packetsType[3686] = "ZC_RESPONSE_CERTAIN_GUILD_EMBLEM" # Size = 20040
packetsType[3687] = "ZC_GUILD_EMBLEM_INFO" # Size = 41
packetsType[3688] = "CZ_REQUEST_GUILD_EMBLEM_INFO" # Size = 18
packetsType[3689] = "CZ_REQUEST_GUILD_INDEX" # Size = 18
packetsType[3690] = "ZC_NO_GUILD_INDEX" # Size = 14
packetsType[3691] = "CZ_REPORT_GUILDEMBLEM" # Size = 74
packetsType[3692] = "ZC_NXA_REQ_TICKET" # Size = 10
packetsType[3693] = "CZ_NXA_TICKET" # Size = 1034
packetsType[3694] = "CZ_NXA_REQ_BALANCE" # Size = 10
packetsType[3695] = "ZC_NXA_BALANCE" # Size = 40
packetsType[3696] = "CZ_NXA_REQ_ITEMLIST" # Size = 11
packetsType[3697] = "ZC_NXA_ITEMLIST" # Size = 0
packetsType[3698] = "CZ_NXA_REQ_PURCHASE" # Size = 15
packetsType[3699] = "ZC_NXA_PURCHASE" # Size = 1034
packetsType[3700] = "CZ_NXA_REQ_PICKUP_READY_ITEMS" # Size = 523
packetsType[3701] = "CZ_NXA_REQ_PURCHASE_CANCEL" # Size = 10
packetsType[3702] = "ZC_NXA_SELLITEMLIST" # Size = 0
packetsType[3472] = "CZ_MYPAGE_COMMENT_ADD" # Size = 278
packetsType[3473] = "CZ_MYPAGE_COMMENT_DELETE" # Size = 18
packetsType[3475] = "CZ_GET_TARGET_MYPAGE" # Size = 14
packetsType[3476] = "CZ_ON_MYPAGE_MODE" # Size = 14
packetsType[3477] = "CZ_RESET_SOCIAL_MODE" # Size = 10
packetsType[3474] = "CZ_GUESTPAGE_COMMENT_ADD" # Size = 278
packetsType[3478] = "CZ_GET_TARGET_GUESTPAGE" # Size = 14
packetsType[3479] = "CZ_ADD_SELLMODE_ITEM" # Size = 30
packetsType[3480] = "CZ_DELETE_SELLMODE_ITEM" # Size = 18
packetsType[3481] = "CZ_ON_SELLITEM_MODE" # Size = 14
packetsType[3486] = "CZ_ON_ITEMBUY_MODE" # Size = 0
packetsType[3482] = "ZC_MYPAGE_MAP" # Size = 0
packetsType[3483] = "ZC_GUESTPAGE_MAP" # Size = 0
packetsType[3484] = "ZC_ON_MYPAGE_MODE" # Size = 0
packetsType[3485] = "ZC_RESET_SOCIAL_MODE" # Size = 14
packetsType[3487] = "ZC_ON_BUYITEM_MODE" # Size = 0
packetsType[3512] = "CZ_STOP_ALLPC" # Size = 10
packetsType[3513] = "CZ_COMPLETE_PRELOAD" # Size = 14
packetsType[3514] = "CZ_MGAME_JOIN_CMD" # Size = 46
packetsType[3516] = "ZC_ATTACH_TO_OBJ" # Size = 53
packetsType[3517] = "ZC_DETACH_FROM_OBJ" # Size = 18
packetsType[3518] = "ZC_RUN_FROM" # Size = 18
packetsType[3519] = "ZC_LOOKAT_OBJ" # Size = 18
packetsType[3520] = "CZ_SKILL_CELL_LIST" # Size = 0
packetsType[3522] = "CZ_DIRECTION_PROCESS" # Size = 18
packetsType[3523] = "CZ_DIRECTION_MOVE_STATE" # Size = 0
packetsType[3524] = "ZC_TO_ALL_CLIENT" # Size = 0
packetsType[3525] = "ZC_TO_CLIENT" # Size = 0
packetsType[3526] = "CZ_REWARD_CMD" # Size = 14
packetsType[3527] = "CZ_PROPERTY_COMPARE" # Size = 16
packetsType[3528] = "ZC_PROPERTY_COMPARE" # Size = 0
packetsType[3529] = "ZC_PROPERTY_COMPARE_FOR_ACT" # Size = 0
packetsType[3531] = "ZC_SEND_CASH_VALUE" # Size = 0
packetsType[3603] = "ZC_RECOMMEND_PARTYMEMBER_INFO" # Size = 0
packetsType[3530] = "ZC_FACTION" # Size = 18
packetsType[3532] = "ZC_BEGIN_KILL_LOG" # Size = 10
packetsType[3533] = "ZC_END_KILL_LOG" # Size = 10
packetsType[3534] = "ZC_CLEAR_KILL_LOG" # Size = 10
packetsType[3535] = "CZ_NPC_AUCTION_CMD" # Size = 30
packetsType[3536] = "ZC_DIRECTION_APC" # Size = 30
packetsType[3537] = "ZC_BGMODEL_ANIM_INFO" # Size = 19
packetsType[3538] = "ZC_ATTACH_BY_KNOCKBACK" # Size = 42
packetsType[3539] = "CZ_OBJECT_MOVE" # Size = 30
packetsType[3540] = "CZ_CONTROL_OBJECT_ROTATE" # Size = 22
packetsType[3541] = "CZ_SUMMON_COMMAND" # Size = 18
packetsType[3542] = "CZ_VEHICLE_RIDE" # Size = 15
packetsType[3543] = "CZ_REQ_ACHIEVE_RANK_PAGE_INFO" # Size = 78
packetsType[3544] = "ZC_SPC_TRIGGER_EXEC" # Size = 34
packetsType[3545] = "CZ_REQ_MGAME_VIEW" # Size = 18
packetsType[3546] = "CZ_REQ_MGAME_CHAT" # Size = 0
packetsType[3547] = "CZ_TOURNAMENT_GIFT" # Size = 18
packetsType[3548] = "CZ_PARTY_INVITE_ACCEPT" # Size = 87
packetsType[3549] = "CZ_PARTY_INVITE_CANCEL" # Size = 91
packetsType[3550] = "CZ_PARTY_PROP_CHANGE" # Size = 147
packetsType[3551] = "CZ_REQ_MARKET_REGISTER" # Size = 40
packetsType[3552] = "CZ_REQ_MARKET_MINMAX_INFO" # Size = 18
packetsType[3553] = "CZ_REQ_MARKET_BUY" # Size = 0
packetsType[3554] = "CZ_REQ_MARKET_LIST" # Size = 138
packetsType[3555] = "CZ_REQ_MY_SELL_LIST" # Size = 14
packetsType[3556] = "CZ_REQ_CABINET_LIST" # Size = 10
packetsType[3557] = "CZ_REQ_GET_CABINET_ITEM" # Size = 26
packetsType[3558] = "CZ_REQ_CANCEL_MARKET_ITEM" # Size = 18
packetsType[3560] = "CZ_OBJ_RECORD_POS" # Size = 0
packetsType[3561] = "CZ_FORMATION_CMD" # Size = 32
packetsType[3562] = "CZ_REGISTER_AUTOSELLER" # Size = 0
packetsType[3559] = "CZ_INV_ITEM_LOCK" # Size = 19
packetsType[3563] = "CZ_OPEN_AUTOSELLER" # Size = 66
packetsType[3564] = "CZ_BUY_AUTOSELLER_ITEMS" # Size = 0
packetsType[3565] = "CZ_SELL_MY_AUTOSELLER_ITEMS" # Size = 0
packetsType[3566] = "CZ_PUZZLE_CRAFT" # Size = 0
packetsType[3567] = "CZ_PET_EQUIP" # Size = 34
packetsType[3568] = "CZ_PET_AUTO_ATK" # Size = 11
packetsType[3569] = "ZC_PET_AUTO_ATK" # Size = 11
packetsType[3570] = "ZC_FOUND_PARTY_LIST" # Size = 0
packetsType[3571] = "ZC_NEAR_PARTY_LIST" # Size = 0
packetsType[3572] = "ZC_RECOMMEND_PARTY_INFO" # Size = 0
packetsType[3573] = "CZ_REQUEST_SOME_PARTY" # Size = 90
packetsType[3574] = "CZ_REFRESH_MEMBERRECOMMEND_LIST" # Size = 10
packetsType[3575] = "ZC_TO_SOMEWHERE_CLIENT" # Size = 0
packetsType[3576] = "CZ_REVEAL_NPC_STATE" # Size = 14
packetsType[3577] = "CZ_CHANGE_CHANNEL" # Size = 12
packetsType[3578] = "CZ_REQ_CHANNEL_TRAFFICS" # Size = 12
packetsType[3579] = "CZ_BUY_PROPERTYSHOP_ITEM" # Size = 0
packetsType[3580] = "CZ_SKILL_USE_HEIGHT" # Size = 14
packetsType[3581] = "CZ_CHANGE_GUILD_NEUTRALITY" # Size = 10
packetsType[3582] = "CZ_SAVE_GUILD_BOARD" # Size = 110
packetsType[3583] = "CZ_DELETE_PARTY_EVENT" # Size = 20
packetsType[3584] = "CZ_PING" # Size = 10
packetsType[3585] = "ZC_PING" # Size = 10
packetsType[3586] = "CZ_REQ_REMAIN_NEXONCASH" # Size = 10
packetsType[3587] = "CZ_REQ_OPEN_INGAMESHOP_UI" # Size = 10
packetsType[3588] = "CZ_REQ_BUY_INGAMESHOP_ITEM" # Size = 78
packetsType[3589] = "CZ_REQ_BUY_ALL_INGAMESHOP_ITEM" # Size = 10
packetsType[3590] = "CZ_REQ_PICKUP_CASHITEM" # Size = 37
packetsType[3591] = "CZ_REQ_REFUND_CASHITEM" # Size = 33
packetsType[3592] = "ZC_XIGNCODE_BUFFER" # Size = 524
packetsType[3593] = "CZ_XIGNCODE_BUFFER" # Size = 524
packetsType[3594] = "CZ_SYSTEM_LOG_SAVE_TO_MONGODB" # Size = 280
packetsType[3595] = "CZ_CHANGE_TITLE" # Size = 74
packetsType[3596] = "CZ_PC_COMMENT_CHANGE" # Size = 0
packetsType[3597] = "CZ_AUTTOSELLER_BUYER_CLOSE" # Size = 18
packetsType[3598] = "CZ_REQ_ITEM_LIST" # Size = 11
packetsType[3599] = "CZ_REQ_ACC_WARE_VIS_LOG" # Size = 10
packetsType[3600] = "CZ_HIT_MISSILE" # Size = 14
packetsType[3601] = "CZ_I_NEED_PARTY" # Size = 23
packetsType[3602] = "CZ_PARTY_JOIN_BY_LINK" # Size = 19
packetsType[3604] = "CZ_PVP_ZONE_CMD" # Size = 26
packetsType[3605] = "CZ_PVP_CHAT" # Size = 0
packetsType[3606] = "CZ_CARDBATTLE_CMD" # Size = 26
packetsType[3607] = "CZ_REQ_UPDATE_CONTENTS_SESSION" # Size = 10
packetsType[3608] = "CZ_REQ_FRIENDLY_FIGHT" # Size = 15
packetsType[3609] = "CZ_HARDSKILL_POS_LIST" # Size = 0
packetsType[3610] = "CZ_CART_POSITION" # Size = 26
packetsType[3611] = "CZ_REQ_RIDE_CART" # Size = 18
packetsType[3612] = "CZ_DUMMYPC_SKILL_POS" # Size = 26
packetsType[3614] = "CZ_PARTY_MEMBER_SKILL_USE" # Size = 0
packetsType[3615] = "CZ_PARTY_MEMBER_SKILL_ACCEPT" # Size = 23
packetsType[3617] = "CZ_CHECK_PING" # Size = 10
packetsType[3623] = "CZ_PARTY_INVENTORY_LOAD" # Size = 12
packetsType[3625] = "CZ_REQ_MOVE_PARTYINV_TO_ACCOUNT" # Size = 0
packetsType[3626] = "CZ_PVP_COMMAND" # Size = 23
packetsType[3627] = "CZ_REQ_CancelGachaCube" # Size = 10
packetsType[3628] = "CZ_WAREHOUSE_TAKE_LIST" # Size = 0
packetsType[3629] = "CZ_SAVE_AUTO_MACRO" # Size = 0
packetsType[3630] = "CZ_REQUEST_LOAD_ITEM_BUY_LIMIT" # Size = 10
packetsType[3631] = "CZ_AUTO_STATE" # Size = 11
packetsType[3633] = "CZ_FIXED_NOTICE_SHOW" # Size = 10
packetsType[3634] = "CZ_SAGE_SKILL_GO_FRIEND" # Size = 90
packetsType[3632] = "CZ_RUN_GAMEEXIT_TIMER" # Size = 42
packetsType[3635] = "CZ_REQUEST_CHANGE_NAME" # Size = 66
packetsType[3636] = "CZ_REQUEST_CHANGE_PET_NAME" # Size = 42
packetsType[3640] = "ZC_HOLD_EXP_BOOK_TIME" # Size = 25
packetsType[3641] = "CZ_HOLD_EXP_BOOK_TIME" # Size = 14
packetsType[3637] = "CZ_CYOU_CTU_CLIENT_MSG" # Size = 1054
packetsType[3656] = "CZ_RUN_FUNCTION_DUMP" # Size = 0
packetsType[3657] = "ZC_RUN_FUNCTION_DUMP" # Size = 0
packetsType[3658] = "ZC_RUN_FUNCTION_DUMP_ERROR" # Size = 0
packetsType[3659] = "ZC_RUN_FUNCTION_DUMP_PRINT" # Size = 0
packetsType[3660] = "ZC_ATTACH_TO_SLOT" # Size = 26
packetsType[3669] = "CZ_REQ_GUILD_NEUTRALITY_ALARM" # Size = 14
packetsType[3664] = "CZ_SYNC_POS" # Size = 26
packetsType[3666] = "CZ_DISCONNECT_REASON_FOR_LOG" # Size = 0
packetsType[3675] = "CZ_LOAD_COMPLETE" # Size = 10
packetsType[3676] = "ZC_LOAD_COMPLETE" # Size = 10
packetsType[3677] = "CZ_ACCEPT_CHALLENGE_MODE" # Size = 14
packetsType[3678] = "CZ_ACCEPT_NEXT_LEVEL_CHALLENGE_MODE" # Size = 14
packetsType[3679] = "CZ_ACCEPT_STOP_LEVEL_CHALLENGE_MODE" # Size = 14
packetsType[3680] = "ZC_UPDATE_CHALLENGE_MODE_WARP_PORTAL_MARK" # Size = 23
packetsType[3639] = "ZC_CYOU_KICK_USER_EXIT_CLIENT" # Size = 10
packetsType[3703] = "CZ_REQ_PARTY_INFO" # Size = 10
packetsType[3704] = "CZ_REQ_RETURN_ORIGIN_SERVER" # Size = 10
packetsType[3705] = "CZ_ANS_GIVEUP_PREV_PLAYING_INDUN" # Size = 11


# Search "SkillAdd" or "AbilityList"
packetFunctionProfiler = 0x415960;

class JumpTableHandler:

    def __init__ (self, jumptableOffset, jumptableSize, jumptableIndex, jumptableAddress, defaultCase, className):
        self.jumptableOffset = jumptableOffset;
        self.jumptableSize = jumptableSize;
        self.jumptableIndex = jumptableIndex;
        self.jumptableAddress = jumptableAddress;
        self.defaultCase = defaultCase;
        self.className = className;

    def resolve (self, isZone):
        for n in range (self.jumptableSize):
            # Get jumptable entry
            namePacketFunctionSeen = 0;
            index = Byte (self.jumptableIndex + n);
            address = Dword (self.jumptableAddress + index*4);

            # Default case
            if address == self.defaultCase:
                continue;

            # Get the first call or the first call after the packetFunctionProfiler
            callOk = False;
            newPacketFunctionCalled = False;

            while callOk == False:
                if GetMnem (address) == "call":
                    if isZone == False:
                        callOk = True;
                    else:
                        callAddress = GetOperandValue (address, 0);
                        if callAddress == packetFunctionProfiler:
                            newPacketFunctionCalled = True;
                        elif newPacketFunctionCalled == True:
                            callOk = True;
                if callOk == False:
                    address = NextHead (address);

            # Get the name in the packets list
            name = packetsType[n+self.jumptableOffset];

            if name != None:
                callAddress = GetOperandValue (address, 0);
                if GetOpnd (address, 0) == "ds:delete":
                    continue;
                if callAddress < 0x400000:
                    continue;
                print "%x => %s" % (callAddress, self.className + "::" + name);
                MakeName (callAddress, self.className + "::" + name);

return;
# Barrack
jumptableOffset  = 13
jumptableSize    = 0x4F
jumptableIndex   = 0x44B178
jumptableAddress = 0x44B128
defaultCase      = 0x44B109
barrackHandler = JumpTableHandler (jumptableOffset, jumptableSize, jumptableIndex, jumptableAddress, defaultCase, "CBarrackNet");
barrackHandler.resolve (False);


# Zone : ProcessPacket
jumptableOffset  = 0xC2B
jumptableSize    = 0x175
jumptableIndex   = 0x41D044
jumptableAddress = 0x41CDF8
defaultCase      = 0x41CCBC
zoneHandler1 = JumpTableHandler (jumptableOffset, jumptableSize, jumptableIndex, jumptableAddress, defaultCase, "CNormalNet");
zoneHandler1.resolve (True);


# Zone : ProcessCommonPackets
jumptableOffset  = 0xBBE
jumptableSize    = 0x1D7
jumptableIndex   = 0x666840
jumptableAddress = 0x666658
defaultCase      = 0x666637
zoneHandler2 = JumpTableHandler (jumptableOffset, jumptableSize, jumptableIndex, jumptableAddress, defaultCase, "CNormalNet");
zoneHandler2.resolve (True);