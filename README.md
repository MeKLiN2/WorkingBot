# WorkingBot
chat bot connects and reads chat. you cannot type, they come out as terminal commands. maybe useful in future.

when the chat server pings, the bot does not pong back. could be dangerous.
bot account visible to others in room. proof of concept.
album:
https://imgur.com/a/iJGB1OD
single links:
https://i.imgur.com/hkjWU1H.png
https://i.imgur.com/GW7KOQ4.png
https://i.imgur.com/M9cxBwb.png
https://i.imgur.com/IlIfYDv.png

no captcha power. you should be able to connect if you havnt been on chat in a while, as the service usually only gives a captcha upon your fourth refresh.
if this happens and you are stuck, try another account, ip, wait till tomorrow, or login on the account name the bot is using and go to the chat room you want it to go to.
refresh four times until you get the captcha, and solve it for your bot. close the browser window and the chat (you can leave a tab open on the main tc page if you want your cookie to stay incase you need to rejoin it again later, it would be easier to keep this new private window open. the reason you use a new private window is to get fresh cookies if you are logged into the chat on a different account.

once the captcha is solved, the site will probably let you reconnect if you do it fast enough, with the bot. there is an occasional endpoint error which may just be debugging not knowing what to print.
the endpoint is retrieved from the api token and is always successful. the login part is a problem, because you can only login so many times per day. there must be a way to make the bot keep its login, and not run the first part of the script where it logs in, and just make it connect to a room, and if it isnt in the room, it still is 'active' in the terminal waiting to be told to join the room.

this is the code i had right after i got it to work, if you are looking for where i am now, probably adding this stuff to nortbot, or trying to get it to respond to ping as well as let me type to the chat through my terminal, which i will add to a different repository called mekbot
