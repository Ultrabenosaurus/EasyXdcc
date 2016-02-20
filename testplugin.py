# -*- coding: utf-8 -*-
__module_name__ = "tester"
__module_version__ = "x.x"
__module_description__ = "plugin for testing random shit"
__module_author__ = "Ultrabenosaurus <https://github.com/Ultrabenosaurus/EasyXdcc>"
import hexchat, os, time, pprint, platform

def info_main(word, word_eol, userdata):
    argc = len(word)

    if argc == 3:
        if("info" == word[1])
        print hexchat.get_info(word[2])
    else:
        print "tester: use a proper command"

    return hexchat.EAT_ALL

hexchat.hook_command("tester", main, help="/tester <cmd>")
