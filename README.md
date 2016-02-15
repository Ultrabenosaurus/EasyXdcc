EasyXdcc
========

XDCC download manager with support for simultaneous queues on different channels, servers and bots, as well as saving/loading queue state.

## Credit

This is not my work, I just found it and made some modifications. The site seems to be down even though the file is still accessible and searching for an hour today looking for an updated version returned nothing helpful, so I decided to host it here.

The original is by [Bouliere Tristan](boulieretristan@aliceadsl.fr) and can be found in the [XChat plugin repository](http://xchat.org/cgi-bin/search.pl?str=easyxdcc&cat=0&Submit=Search).

## Install

Simply copy `EasyXdcc.py` to your IRC client's plugins folder. Original version designed for XChat 2, my version is tested and working in HexChat 2.10.1. May or may not work in any other client.

Some lines near the bottom of the file need to be toggled depending on your OS, they are commented so check them before using.

Confirm it is loaded and active in your client's plugin manager.

## Usage

Make sure you have joined a channel with access to the bot you want files from, then use one of the following commands:

* `/XDCC ADD [bot_name] [n°_pack]`
* `/XDCC ADDL [bot_name] [n°_pack_beg] [n°_pack_end]`
* `/XDCC ADDM [bot_name] [n°_pack_1] [n°_pack_2] [...]`

You can use `/XDCC QUEUE` or `/XDCC QUEUE [bot_name]` to view the current queue.

If it doesn't start downloading stuff for you automatically enter `/XDCC START` to get things going.

## All Commands

```
 Queue a pack :
 /XDCC ADD [bot_name] [n°_pack]
 
 Queue a pack list :
 /XDCC ADDL [bot_name] [n°_pack_beg] [n°_pack_end]
 
 Queue non-sequential pack list :
 /XDCC ADDM [bot_name] [n°_pack_1] [n°_pack_2] [...]
 
 See pack queue :
 /XDCC QUEUE
 
 See pack queue for a bot :
 /XDCC QUEUE [bot_name]
 
 Withdraw a pack from queue :
 /XDCC RMP [bot_name] [n°pack]
 
 Withdraw a pack list from queue :
 /XDCC RMPL [bot_name] [n°pack_beg] [N°pack_end]
 
 Withdraw a non-sequential pack list from queue :
 /XDCC RMPM [bot_name] [n°_pack_1] [n°_pack_2] [...]
 
 Withdraw a bot from queue :
 /XDCC RMBOT [bot_name]
 
 Stop EasyXdcc :
 /XDCC STOP
 
 Start EasyXdcc :
 /XDCC START
 
 Save Queue :
 /XDCC SAVE
 
 Load Queue :
 /XDCC LOAD
 
 Delete saved Queue file :
 /XDCC PURGE
 ```
