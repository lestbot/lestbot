
import ch
import random
import sys
import os
import re
import time
import json
import urllib
import traceback
import __future__
import shelve
from time import localtime, strftime
from urllib.request import urlopen
import urllib.request as urlreq
from urllib.request import urlopen
from xml.etree import cElementTree as ET
from urllib.request import unquote
from random import choice
if sys.version_info[0] > 2:
  import urllib.request as urlreq
else:
  import urllib2 as urlreq
import re

################################
lockdown = False
activated = True
################################

def getUptime():
  """
 Returns the number of seconds since the programs started.
 """
  #do return startTime if you want the process start time
  
  return time.time() - startTime

################################
##File Stuff##

startTime = time.time()

pd = dict()
wordtodaytime = dict()
wife = dict()
ping = dict()
oco = dict()
family = dict()
pdf = dict()
waifu = dict()


########################################
########## BLACKLIST ###################

dictionary = dict()
f = open("definitions.txt", "r") # read-only
for line in f.readlines():
  try:
    if len(line.strip())>0:
      word, definition, name = json.loads(line.strip())
      dictionary[word] = json.dumps([definition, name])
  except:
    print("[ERROR]Cant load definition: %s" % line)
f.close()

########################################
########## BLACKLIST ###################

blacklist = dict()
try:
  f = open("blacklist.txt", "r")
  blacklist = eval(f.read())
  f.close()
except:pass

########################################
########## RANK ########################

developer = []
file = open("developer.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    developer.append(name.strip())
print("[INF]Loading Developer...")
file.close()

########################################

admin = []
file = open("admin.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    admin.append(name.strip())
print("[INF]Loading Admin...")
file.close()

########################################

mod = []
file = open("mod.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    mod.append(name.strip())
print("[INF]Loading Mod...")
file.close()

#######################################

assistant = []
file = open("assistant.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    assistant.append(name.strip())
print("[INF]Loading Assistant...")
file.close()

########################################


registered = []
file = open("registered.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    registered.append(name.strip())
print("[INF]Loading Registered...")
file.close()

########################################

blacklist = []
file = open("blacklist.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    blacklist.append(name.strip())
print("[INF]Loading Blacklist...")
file.close()

########################################

whitelist = []
file = open("whitelist.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    whitelist.append(name.strip())
print("[INF]Loading Whitelist...")
file.close()

########################################
############# STATUS ROOM ##############

rooms = []
file = open("rooms.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    rooms.append(name.strip())
print("[INF]Loading Rooms...")
file.close()

#########################################

locks = []
file = open("locks.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    locks.append(name.strip())
print("[INF]Loading Locks...")
file.close()

#########################################
########### SN Notifs ###################

sasaran = dict()
f = open ("notes.txt", "r") #read-only
print("[INF]Loading Notes...")
time.sleep(1)
for line in f.readlines():
  try:
    if len(line.strip())>0:
      to, body, sender = json.loads(line.strip())
      sasaran[to] = json.dumps([body, sender])
  except:
    print("[Error] Notes load fails : %s" % line)
f.close()
 
notif = []
f = open("notif.txt", "r")
print("[INF]Loading Notifs...")
for name in f.readlines():
  if len(name.strip())>0: notif.append(name.strip())
f.close

#########################################
################# NICK ##################

nicks=dict()
f=open ("nicks.txt","r")#r=read w=right
for line in f.readlines():#loop through eachlinimporte and read each line
    try:#try code
        if len(line.strip())>0:#strip the whitespace checkgreater than 0
            user , nick = json.loads(line.strip())
            nicks[user] = json.dumps(nick)
    except:
        print("[Error]Can't load nick %s" % line)
f.close()

def myanimelistanime(args):
  try:
    s = args.split(" ", 1)
    args = s[1]
    val = s[0]
    try:
      val = int(val)
    except:
      args = " ".join(s)
      val = 1
  except:
      args = args
      val = 1
  val = val - 1
  if val < 0:
    val = 0
    anime = mal.anime(args, 0, val)
  else: return "Anime: %s" % anime
     
 
def myanimelistanime(args):
  try:
    s = args.split(" ", 1)
    args = s[1]
    val = s[0]
    try:
      val = int(val)
    except:
      args = " ".join(s)
      val = 1
  except:
      args = args
      val = 1
  val = val - 1
  if val < 0:
    val = 0
  anime = mal.anime(args, 0, val)
  return anime

def sntonick(username):
    user = username.lower()
    if user in nicks:
        nick = json.loads(nicks[user])
        return nick
    else:
        return user

def pars(args):
  args=args.lower()
  if args in name:return name    

def roompars(args):
  args = args.lower()
  if args in name:return name

########################################
############# GOOGLE ###################

def gis(cari):
  argss = cari
  args = argss.split()
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (x12; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request("https://www.google.com.br/search?hl=en&authuser=0&site=imghp&tbm=isch&source=hp&biw=1366&bih=623&q=" + "+".join(args), headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','').replace('http://','gis:').replace('https://','gis:').replace('.jpg','.jpg:end').replace('.gif','.gif:end').replace('.png','.png:end')
  anjay = re.findall('<div class="rg_meta">(.*?)</div>', resp)
  setter = list()
  la = "".join(anjay)
  a = re.findall('"ou":"gis:(.*?):end","ow"', la)
  q = 1
  for result in a:
    if ".jpg" in result or ".gif" in result or ".png" in result:
     if "vignette" not in result and "mhcdn.net" not in result and "alicdn.com" not in result and "gambardanfoto.com" not in result and "squarespace.com" not in result and "polyvore.com" not in result and "wikia.nocookie" not in result and "blogspot.com" not in result and "wordpress.com" not in result and "minionnation.co.uk" not in result and "twimg.com" not in result and "ohmymag.com" not in result and "waterfrontcinema.co.uk" not in result and "funmobility.netdna-ssl.com" not in result and "images-amazon.com" not in result and "upload.wikimedia.org" not in result: 
      setter.append('(%s) http://%s' % (q, result))
      q += 1
  return "<br/>"+"<br/>".join(setter[0:4])

def tube(args):
  search = args.split()
  url = urlreq.urlopen("https://www.googleapis.com/youtube/v3/search?q=%s&part=snippet&key=AIzaSyBSnh-sIjd97_FmQVzlyGbcaYXuSt_oh84" % "+".join(search))
  udict = url.read().decode('utf-8')
  data = json.loads(udict)
  rest = []
  for f in data["items"]:
    rest.append(f)
  
  d = random.choice(rest)
  link = "http://www.youtube.com/watch?v=" + d["id"]["videoId"]
  videoid = d["id"]["videoId"]
  title = d["snippet"]["title"]
  uploader = d["snippet"]["channelTitle"]
  descript = d["snippet"]['description']
  count    = d["snippet"]["publishedAt"]
  return "Resultado: %s <br/><br/><br/><br/><br/><br/><br/><br/><font color='#ffcc00'> %s </font><br/><font color='#ff0000'> Canal </font>:  %s <br/><font color='#ff0000'> Publicado em </font>: %s<br/><font color='#ff0000'> Descrição </font>:<i> %s ...</i><br/> " % (link, title, uploader, count, descript[:200])

def gs(args):
  args = args.split()
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (x12; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request("https://www.google.com.br/search?q=" + "+".join(args), headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','').replace('http://','gs:').replace('https://','gs:')
  anjay = re.findall('<h3 class="r">(.*?)</h3>', resp)
  setter = list()
  la = "".join(anjay)
  a = re.findall('<a href="gs:(.*?)" onmousedown="(.*?)">(.*?)</a>', la)
  q = 1
  for link, fak, title in a:
      setter.append("<br/>(%s) %s : http://%s" % (q, title.capitalize(), link))
      q += 1
  return "".join(setter[0:4])

def rainbow(word):
    length = len(word)
    #set rgb values
    r = 255 #rgb value set to red by default
    g = 0
    b = 0
    sub = int(765/length)
    counter = 0
    string = ""
    for x in range(0, length):
        letter = word[counter]
        s = "<f x12%02X%02X%02X='0'>%s" % (r, g, b, letter)
        string = string+s
        counter+=1
        if (r == 255) and (g >= 0) and (b == 0): #if all red
            g = g+sub
            if g > 255: g = 255
        if (r > 0) and (g == 255) and (b == 0): #if some red and all green
            r = r-sub #reduce red to fade from yellow to green
            if r<0: r = 0 #if red gets lower than 0, set it back to 0
        if (r == 0) and (g == 255) and (b >= 0):
            b = b+sub
            if b>255:
                b = 255
                trans = True
        if (r == 0) and (g > 0) and (b == 255):
            g = g-sub
            if g<0: g = 0
        if (r >= 0) and (g == 0) and (b == 255):
            r = r+sub
            if r>255: r = 255
    return string


##End##
########################################


#############################################################
##========================Variables========================##

botname = "MayuBot" #Put your bot name here

botpassword = "daniel157" #Put your bot password here

cek_mods = dict() #Don't mess with this variable. This one is related with *mods command.

error = ("Expectation failed.")    #Error message

command_list = ['help','wl/register','uwl/unregister','bl/blacklist','chain','ubl/unblacklist','unchain','rank','setrank','pm','broadcast','say','reverse/rsay','find','multichat','ban','unban','join','leave','lock','unlock','rooms','save','mods','activate','restrict','lockdown','wake']

prefix = "-" ##You set the prefix here

##===========================End===========================##
#############################################################
  
#setting colors
  
class TestBot(ch.RoomManager):
  def onInit(self):
    self.setNameColor("A498AC")
    self.setFontColor("A498AC")
    self.setFontFace("Comic")
    self.setFontSize(12)
    self.enableBg()  
    self.enableRecording()

  def saveAll(self):
    room = self._Room
    f = open("blacklist.txt", "w")
    f.write("\n".join(blacklist))
    f.close()
    f = open("developer.txt", "w")
    f.write("\n".join(developer))
    f.close()
    f = open("admin.txt", "w")
    f.write("\n".join(admin))
    f.close()
    f = open("mod.txt", "w")
    f.write("\n".join(mod))
    f.close()
    f = open("assistant.txt", "w")
    f.write("\n".join(assistant))
    f.close()
    f = open("registered.txt", "w")
    f.write("\n".join(registered))
    f.close()
    f = open("rooms.txt", "w")
    f.write("\n".join(self.roomnames))
    f.close()


  def findUser(self, args):
          stuff = urllib.request.urlopen("http://" + args + ".chatango.com/").read().decode()
          if "buyer" in stuff:
                  return "<f x12FF0000='1'>%s <f x12A498AC='1'>é um usuário." % args.title()
          elif "group" in stuff:
                  return "<f x12FF0000='1'> %s <f x12A498AC='1'>é um chat, é o seu link interno é: <f x12FF0000='1'>%s" % (args.title(), ch.getServer(args))
          elif not "buyer" in stuff or not "group" in stuff:
                  return "%s isso existe?" % args.title()

  def getAccess(self, room, user):
    vroom = room
    if user.name in developer and not user.name in blacklist: return 6
    elif user.name in admin and not user.name in blacklist: return 5
    elif user.name in mod and not user.name in blacklist: return 4
    elif user.name in assistant and not user.name in blacklist: return 3
    elif user.name in registered and not user.name in blacklist: return 2
    elif user.name not in whitelist and not user.name in blacklist: return 1
    elif user.name in blacklist: return -1
    else: return 0

  def roomUsers():
      usrs = []
      gay = []
      prop = 0
      prop = prop + len(room._userlist) - 1
      for i in room._userlist:
        i = str(i)
        usrs.append(i)
      while prop >= 0:
        j = usrs[prop].replace("<User: ", "")
        i = j.replace(">", "")
        gay.append(i)
        prop = prop - 1
      return gay
     
  def getParticipant(arg):
      rname = self.getRoom(arg)
      usrs = []
      gay = []
      finale = []
      prop = 0
      prop = prop + len(rname._userlist) - 1
      for i in rname._userlist:
        i = str(i)
        usrs.append(i)
      while prop >= 0:
        j = usrs[prop].replace("<User: ", "")
        i = j.replace(">", "")
        gay.append(i)
        prop = prop - 1
      for j in gay:
        if j not in finale:
          finale.append(j)
      return finale
         
  def pars(args):
    args=args.lower()
    for name in room.usernames:
      if args in name:return name    

  def roompars(args):
    args = args.lower()
    for name in self.roomnames:
      if args in name:return name
#############################################  
##connecting and disconnecting crap##
  
  def onConnect(self, room):
    print("[+] Mad Hatter Connected to "+room.name)
    for i in cek_mods: #Di onJoin
      if len(cek_mods[i]) > 1:
        rmm, rmd = json.loads(cek_mods[i])
        self.getRoom(rmm).message("<br/>||<font color='#87ceeb'><b>OWNER</b></font>: <b>"+ (self.getRoom(rmd).ownername) +"</b> <br/>||<b>Mods</b>: "+", ".join(self.getRoom(rmd).modnames), True)
        self.leaveRoom(rmd)
        cek_mods.pop(i)
      return
    
  def onReconnect(self, room):
    print("[+] Mad Hatter Reconnected to "+room.name)
    
  def onDisconnect(self, room):
    print("[+] Mad Hatter Disconnected from "+room.name)
    
  def onBan(self, room, user, target):
    print(user.name+" got banned in "+room.name)
    

  def onConnectFail(self, room):
    print("[ERR] Room Not Found")
    for i in cek_mods: #Di onJoin
      if len(cek_mods[i]) > 1:
        rmm, rmd = json.loads(cek_mods[i])
        self.getRoom(rmm).message("Such room doesn't exist")
        cek_mods.pop(i)
      return

  

##End##
#############################################

#############################################
##setting up commands##
  
  def onMessage(self, room, user, message):
   try:
    if user == self.user:
        return
    global activated
    global lockdown
    global lock
    global developer
    global admin
    global mod
    global assistant
    try:
      if room.getLevel(self.user) > 0:
        print("[%s]- [MSG] - [Rank %s] - [%s] - [%s] - [%s: %s]" % (time.strftime("%d/%m/%y- %H:%M:%S", time.localtime(time.time())), self.getAccess(room, user), room.name, message.ip, user.name.title(), message.body))
      else:
        print("[%s]- [MSG] - [Rank %s] - [%s] - [User_IP: Null] %s: %s" % (time.strftime("%d/%m/%y- %H:%M:%S", time.localtime(time.time())), self.getAccess(room, user), room.name, user.name.title(), message.body))
    except:
      pass

########################################################################### MSG NOTIFICAÇÃO #####################################################################################

    if user.name in notif and user.name in sasaran:
      room.message("<br/>Olá <f x12FF0000='1'> "+user.name+"   <f x12A498AC='1'> você possui uma mensagem não lida em minha [<f x12FF0000='0'>C<f x12FF2F00='0'>A<f x12FF5E00='0'>I<f x12FF8D00='0'>X<f x12FFBC00='0'>A<f x12FFEB00='0'> <f x12D0FF00='0'>D<f x12A1FF00='0'>E<f x1272FF00='0'> <f x1243FF00='0'>E<f x1214FF00='0'>N<f x1200FF2F='0'>T<f x1200FF5E='0'>R<f x1200FF8D='0'>A<f x1200FFBC='0'>D<f x1200FFEB='0'>A <f x12A498AC='1'>] para ler sua mensagem digite -rn", True)
      notif.remove(user.name)

##################################################################################################################################################################################



    if user.name.startswith("#") or user.name.startswith("!"):return
    if self.user == user: return
    if user.name in blacklist: return
    if self.getAccess(room, user) > 0:
      if not activated and self.getAccess(room, user) > 1: return #return, if not activated and user rank is less than 4.
      if "Mayu" == message.body.lower() or "mayu" == message.body.lower() or "@mayubot" == message.body.lower() or "@MayuBot" == message.body.lower() :
        rank = self.getAccess(room, user)
        if rank == 1:
           room.message(random.choice(["%s" % "Olá usuário "+sntonick(user.name)+" seu nick não se encontra em meu banco de dados, para usufruir do bot de um -wl. \(^o^)/"]), True)
        if rank == 2:
           room.message(random.choice(["%s" % "Oi "+sntonick(user.name) ,"Olá "+sntonick(user.name),"Hi "+sntonick(user.name)]), True)
        if rank == 3:
           room.message(random.choice(["%s" % "Oi "+sntonick(user.name) ,"Olá "+sntonick(user.name),"Hi "+sntonick(user.name)]), True)
        if rank == 4:
           room.message(random.choice(["%s" % "Oi "+sntonick(user.name) ,"Olá "+sntonick(user.name),"Hi "+sntonick(user.name)]), True)
        if rank == 5:
           room.message(random.choice(["%s" % "Oi "+sntonick(user.name) ,"Olá "+sntonick(user.name),"Hi "+sntonick(user.name)]), True)
        if rank == 6:
          room.message("Olá "+sntonick(user.name)+"-sama", True)
      if "afk" == message.body.lower() or "Afk"== message.body.lower():
        rank = self.getAccess(room, user)
        if rank == 1:
           room.message(random.choice(["%s" % "Até "+sntonick(user.name) ,"Já vai "+sntonick(user.name)+"?","Você irá voltar "+sntonick(user.name)+"?"]), True)
        if rank == 2:
           room.message(random.choice(["%s" % "Até "+sntonick(user.name) ,"Já vai "+sntonick(user.name)+"?","Você irá voltar "+sntonick(user.name)+"?"]), True)
        if rank == 3:
           room.message(random.choice(["%s" % "Até "+sntonick(user.name) ,"Já vai "+sntonick(user.name)+"?","Você irá voltar "+sntonick(user.name)+"?"]), True)
        if rank == 4:
           room.message(random.choice(["%s" % "Até "+sntonick(user.name) ,"Já vai "+sntonick(user.name)+"?","Você irá voltar "+sntonick(user.name)+"?"]), True)
        if rank == 5:
           room.message(random.choice(["%s" % "Até "+sntonick(user.name) ,"Já vai "+sntonick(user.name)+"?","Você irá voltar "+sntonick(user.name)+"?"]), True)
        if rank == 6:
          room.message("volte logo "+sntonick(user.name)+"-sama", True)
      if "offline" == message.body.lower() or "off" == message.body.lower() or "Off" == message.body.lower():
        rank = self.getAccess(room, user)
        if rank == 2:
           room.message(random.choice(["%s" % "Até "+sntonick(user.name) ,"Já vai "+sntonick(user.name)+"?","Você irá voltar "+sntonick(user.name)+"?"]), True)
        if rank == 3:
           room.message(random.choice(["%s" % "Até "+sntonick(user.name) ,"Já vai "+sntonick(user.name)+"?","Você irá voltar "+sntonick(user.name)+"?"]), True)
        if rank == 4:
           room.message(random.choice(["%s" % "Até "+sntonick(user.name) ,"Já vai "+sntonick(user.name)+"?","Você irá voltar "+sntonick(user.name)+"?"]), True)
        if rank == 5:
           room.message(random.choice(["%s" % "Até "+sntonick(user.name) ,"Já vai "+sntonick(user.name)+"?","Você irá voltar "+sntonick(user.name)+"?"]), True)
        if rank == 6:
          room.message("volte logo "+sntonick(user.name)+"-sama", True)
         
    ##Commands | You design great commands for your bot in this part
      if message.body[0] == "=" or  message.body[0] == "<" or  message.body[0] == "+" or message.body[0] == "-" or message.body[0] == "|" : #prefix usage in this line (for this case I use "*" as prefix)
        data = message.body[1:].split(" ", 1) #This part splits message body into [0]prefix and [1:]data ([1:] <- this means the message body's second character and after) and data will be split into 2 (cmd(data[0]), args(data[1])) which is very usefull. (Many thanks to TryHardHusky)
        if len(data) == 2: #If there are more than 1 data (This is where we will get args)
          cmd, args = data[0], data[1] #the first data (data[0]) will be the cmd (specified command) and the next data will be args (it doesn't matter how many word next to the cmd, It'd eventually be args)
        else: #If there is only 1 data (No args)
          cmd, args = data[0], "" #the arg will simply be "" (Empty)
        cmd == cmd.lower()

######################################################################################################################################################
#################################################################### SN/RN MESSAGE ######################################################################


        if cmd == "sn" and len(args) and self.getAccess(room, user) >= 2:
          try:
            to, body = args.split(" ", 1)
            sender = user.name
            if to in developer or to in admin or to in assistant or to in whitelist or to in registered:
              sasaran[to] = json.dumps([body, sender])
              room.message("[MSG]Enviada")
              notif.append(to)
            else: room.message("O usuário <f x12FF0000='1'>"+to+"<f x12A498AC='1'> não está registrado.", True)
            #if user.name : room.message( kamu dapat sn dari .... silahkan gunakan cmd 'sn read ) kek gitu aja
          except: room.message("Fail !!")
 
        if cmd == "rn" and self.getAccess(room, user) >= 2:
          try:
            if user.name in sasaran:
              body, sender = json.loads(sasaran[user.name])
              room.message(" <br/><br/><br/>[<f x12FF0000='0'>C<f x12FF2F00='0'>A<f x12FF5E00='0'>I<f x12FF8D00='0'>X<f x12FFBC00='0'>A<f x12FFEB00='0'> <f x12D0FF00='0'>D<f x12A1FF00='0'>E<f x1272FF00='0'> <f x1243FF00='0'>E<f x1214FF00='0'>N<f x1200FF2F='0'>T<f x1200FF5E='0'>R<f x1200FF8D='0'>A<f x1200FFBC='0'>D<f x1200FFEB='0'>A <f x12A498AC='1'>] <br/> <f x12A498AC='1'>Usuário : <f x12FF0000='1'>"+user.name+"<br/>  <f x12A498AC='1'>Remetente : <f x12FF0000='1'>"+sender+"<br/>  <f x12A498AC='1'>Mensagem : <f x12FFCC00='1'>"+body, True)
              del sasaran[user.name]
              notif.remove(to)
          except: return
          else: room.message("<f x12FF0000='1'>"+user.name+" <f x12A498AC='1'> você não tem mensagens :|", True)

######################################################################################################################################################
############################################################### UNLOCK/LOCK BOT ######################################################################

        if cmd == "lock" and self.getAccess(room, user) >= 4:
          self.getRoom("mayubotchat").message("<f x12A498AC='1'><br/><br/>[<f x12FF0000='0'>S<f x12FF4C00='0'>T<f x12FF9800='0'>A<f x12FFE400='0'>T<f x12B3FF00='0'>U<f x1267FF00='0'>S<f x12BFF00='0'> <f x1200FF4C='0'>C<f x1200FF98='0'>M<f x1200FFE4='0'>D<f x12A498AC='1'>]<f x12A498AC='1'><br/><br/><br/><b>Usuário</b>: <f x12FF0000='1'>%s <f x12A498AC='1'><br/><b>Chat</b>: <f x12FF0000='1'>%s  <f x12A498AC='1'><br/><b>Comando</b>: <f x12FF0000='1'>%s <f x12A498AC='1'><br/><b>IP</b>: <f x12FF0000='1'>%s" % (user.name, room.name, cmd, message.ip), True)    
          if args in locks:
            room.message("Este chat já está <f x12FF0000='1'> bloqueado ", True)
            return
          if args in self.roomnames:
            if self.getAccess(room, user) > 0: 
              locks.append(args)
              room.message("O chat <f x12FF0000='1'> %s   <f x12A498AC='1'> foi <f x12FF0000='1'> bloqueado " % args, True)
            else:room.message("Mestre você não tem permissão para executar essa ação. :|")
          if args == "":
            if room.name in locks:
              room.message("Este chat já está <f x12FF0000='1'> [TRANCADO] ", True)
              return
            locks.append(room.name)
            room.message("O chat <f x12FF0000='1'> %s   <f x12A498AC='1'> foi <f x12FF0000='1'> bloqueado " % room.name, True)
          if args not in self.roomnames:
            if args == "": return
            room.message("O travamento não esta disponível no chat <f x12FF0000='1'> %s ."% args, True)
            return


        if cmd == "unlock" and self.getAccess(room, user) >= 4:
          self.getRoom("mayubotchat").message("<f x12A498AC='1'><br/><br/>[<f x12FF0000='0'>S<f x12FF4C00='0'>T<f x12FF9800='0'>A<f x12FFE400='0'>T<f x12B3FF00='0'>U<f x1267FF00='0'>S<f x12BFF00='0'> <f x1200FF4C='0'>C<f x1200FF98='0'>M<f x1200FFE4='0'>D<f x12A498AC='1'>]<f x12A498AC='1'><br/><br/><br/><b>Usuário</b>: <f x12FF0000='1'>%s <f x12A498AC='1'><br/><b>Chat</b>: <f x12FF0000='1'>%s  <f x12A498AC='1'><br/><b>Comando</b>: <f x12FF0000='1'>%s <f x12A498AC='1'><br/><b>IP</b>: <f x12FF0000='1'>%s" % (user.name, room.name, cmd, message.ip), True)    
          if args in self.roomnames:
            if args in locks:
              if self.getAccess(room, user) > 0:
                locks.remove(args)
                room.message("O chat <f x12FF0000='1'> %s   <f x12A498AC='1'> foi <f x1233FF33='1'> desbloqueado " % args, True)
              else: room.message("*warning*  Mestre você não tem permissão para executar essa ação. *warning* ")
            else:
              room.message("Este chat já está <f x1233FF33='1'> desbloqueado ", True)
              return
          if args == "":
            if room.name in locks:
              locks.remove(room.name)
              self.getRoom("mayubotchat").message("<f x12A498AC='1'><br/><br/>[<f x12FF0000='0'>S<f x12FF4C00='0'>T<f x12FF9800='0'>A<f x12FFE400='0'>T<f x12B3FF00='0'>U<f x1267FF00='0'>S<f x12BFF00='0'> <f x1200FF4C='0'>C<f x1200FF98='0'>M<f x1200FFE4='0'>D<f x12A498AC='1'>]<f x12A498AC='1'><br/><br/><br/><b>Usuário</b>: <f x12FF0000='1'>%s <f x12A498AC='1'><br/><b>Chat</b>: <f x12FF0000='1'>%s  <f x12A498AC='1'><br/><b>Comando</b>: <f x12FF0000='1'>%s <f x12A498AC='1'><br/><b>IP</b>: <f x12FF0000='1'>%s" % (user.name, room.name, cmd, message.ip), True)    
            else:
              room.message("O chat <f x12FF0000='1'> %s   <f x12A498AC='1'> foi <f x1233FF33='1'> desbloqueado " % room.name, True)
              return
          if args not in self.roomnames:
            if args == "": return
            room.message("O destravamento não esta disponível no chat <f x12FF0000='1'> %s ."% args, True)
            return

######################################################################################################################################################
########################################################### BOT HABILITADO / DESABILITADO ############################################################

        if cmd == "sleep" and self.getAccess(room, user) >= 5:
         if self.getAccess(room, user) > 0: 
          if lockdown: return
          room.message(" <f x12A498AC='1'> O bot foi <f x12FF0000='1'> [DESATIVADO]  ", True)
          self.getRoom("mayubotchat").message("<f x12A498AC='1'><br/><br/>[<f x12FF0000='0'>S<f x12FF4C00='0'>T<f x12FF9800='0'>A<f x12FFE400='0'>T<f x12B3FF00='0'>U<f x1267FF00='0'>S<f x12BFF00='0'> <f x1200FF4C='0'>C<f x1200FF98='0'>M<f x1200FFE4='0'>D<f x12A498AC='1'>]<f x12A498AC='1'><br/><br/><br/><b>Usuário</b>: <f x12FF0000='1'>%s <f x12A498AC='1'><br/><b>Chat</b>: <f x12FF0000='1'>%s  <f x12A498AC='1'><br/><b>Comando</b>: <f x12FF0000='1'>%s <f x12A498AC='1'><br/><b>IP</b>: <f x12FF0000='1'>%s" % (user.name, room.name, cmd, message.ip), True)    
          lockdown = True

        if cmd == "wakeup" and self.getAccess(room, user) >= 5:
         if self.getAccess(room, user) > 0: 
           if not lockdown: return
           room.message("<f x12A498AC='1'> O bot foi <f x1233FF33='1'> [ATIVADO] ", True)
           self.getRoom("mayubotchat").message("<f x12A498AC='1'><br/><br/>[<f x12FF0000='0'>S<f x12FF4C00='0'>T<f x12FF9800='0'>A<f x12FFE400='0'>T<f x12B3FF00='0'>U<f x1267FF00='0'>S<f x12BFF00='0'> <f x1200FF4C='0'>C<f x1200FF98='0'>M<f x1200FFE4='0'>D<f x12A498AC='1'>]<f x12A498AC='1'><br/><br/><br/><b>Usuário</b>: <f x12FF0000='1'>%s <f x12A498AC='1'><br/><b>Chat</b>: <f x12FF0000='1'>%s  <f x12A498AC='1'><br/><b>Comando</b>: <f x12FF0000='1'>%s <f x12A498AC='1'><br/><b>IP</b>: <f x12FF0000='1'>%s" % (user.name, room.name, cmd, message.ip), True)    
           lockdown = False

######################################################################################################################################################
############################################### DELISGAR BOT #########################################################################################
           
        if cmd == "shutdown" and self.getAccess(room, user) >= 6:
            self.saveAll()
            room.message("Bye *waves*")
            self.setTimeout(3, self.stop, )


######################################################################################################################################################
######################################################### REGISTRO  BOT ##############################################################################


        elif cmd == "wl":
          if args == "":
            rank = self.getAccess(room, user)
            if rank == 1:
              registered.append(user.name)
              room.message(user.name+" registrado com sucesso, caso tenha duvida de um -cmds", True)
            if rank == 2:
              room.message(user.name+" já está registrado, caso tenha duvida de um -cmds", True)
        
          else:
              rank = self.getAccess(room, ch.User(args))
              if rank == 1:
                registered.append(args)
                room.message(args+" registrado com sucesso, caso tenha duvida de um -cmds", True)
              if rank == 2:
                room.message(args+" já está registrado, caso tenha duvida de um -cmds", True)

######################################################################################################################################################
########################################################## DEFINITION ######################################################################################

        elif cmd == "define" or cmd == "df" and len(args) and self.getAccess(room, user) >= 2:
           try:
             try:
               word, definition = args.split(" as ",1)
               word = word.lower()
             except:
               word = args
               definition = ""
             if len(word.split()) > 4:
               room.message("Fail")
               return
             elif len(definition) > 0:
               if word in dictionary:
                 room.message("%s defined already" % user.name.capitalize())
               else:
                 dictionary[word] = json.dumps([definition, user.name])
                 f =open("definitions.txt", "w")
                 for word in dictionary:
                   definition, name = json.loads(dictionary[word])
                   f.write(json.dumps([word, definition, name])+"\n")
                 f.close
                 room.message("Definição foi salva :|")
             else:
              if word in dictionary:
                 definition, name = json.loads(dictionary[word])
                 room.message("<br/><br/><br/> ID :  <f x12FF0000='1'>  %s  <br/> <f x12A498AC='1'>   Palavra chave :   <f x12990099='1'>  %s  <br/> <f x12A498AC='1'>  Definição: <f x12FF6600='1'>  %s " % (name, word, definition),True)
              else:
                 room.message("<f x12FF0000='1'>"+args+" <f x12A498AC='1'> não está definido.", True)
           except:
             room.message("Tem algo errado :|")

        if (cmd == "undefine" or cmd == "undef" or cmd == "udf") and len(args) and self.getAccess(room, user) >= 5:
         if self.getAccess(room, user) > 0:
          try:
            word = args
            if word in dictionary:
              definition, name = json.loads(dictionary[word])
              if self.getAccess(room, user) > 0:
                del dictionary[word]
                room.message(" <f x12A498AC='1'>A definição <f x12FF0000='1'>"+word+" <f x12A498AC='1'> foi removido do banco de dados.", True)
                return
              else:
                room.message("<f x12FF0000='1'>Usuário  %s   <f x12A498AC='1'> você não está autorizado a remover essa definição :| " % user.name, True)
                return
            else:
              room.message(" %s  is not yet defined you can define it by typing  define %s: meaning " % args, True)
          except:
            room.message("*warning*  Mestre você não tem permissão para executar essa ação. *warning* ")
            return
  
        elif cmd == "mydf" and self.getAccess(room, user) >= 2:
          arr = []
          for i in dictionary:
            if user.name in dictionary[i]:
              arr.append(i)
          if len(arr) > 0:
            room.message("<f x12FF0000='1'> "+user.name+"    <f x12A498AC='1'> você tem <f x12FF0000='1'>  "+str(len(arr))+"   <f x12A498AC='1'> definições adicionada em meu sistema é elas são :  <f x12FF0000='1'>  %s  "% (', '.join(sorted(arr))), True)
          else:
            room.message("Não existe definições salva no sistema.")

######################################################################################################################################################
########################################################## MESSAGENS TIME ############################################################################

        if cmd =="wordtoday" or cmd=="wt" and self.getAccess(room, user) >= 2:
            if self.getAccess(room, user) > 0:
              if user.name in wordtodaytime:
                w = json.loads(wordtodaytime[user.name])
                if time.time() < w:
                  w = int(w) - int(time.time())
                  minute = 60
                  hour = minute * 60
                  day = hour * 24
                  days =  int(w / day)
                  hours = int((w % day) / hour)
                  minutes = int((w % hour) / minute)
                  seconds = int(w % minute)
                  string = ""
                  if days > 0:
                    string += str(days) + " " + (days == 1 and " <f x12A498AC='1'>day" or " <f x12A498AC='1'>days" ) + "<f x12FF0000='1'> "
                  if len(string) > 0 or hours > 0:
                    string += str(hours) + " " + (hours == 1 and " <f x12A498AC='1'>hour" or " <f x12A498AC='1'>horas" ) + "<f x12FF0000='1'> "
                  if len(string) > 0 or minutes > 0:
                    string += str(minutes) + " " + (minutes == 1 and " <f x12A498AC='1'>minuto" or " <f x12A498AC='1'>minutos" ) + " <f x12A498AC='1'><f x12FF0000='1'> "
                  string += str(seconds) + " " + (seconds == 1 and " <f x12A498AC='1'>segundo" or " <f x12A498AC='1'>segundos" )
                  room.message("Para usar o comando novamente aguarde :  <f x12FF0000='1'>%s (~^o^)~ "% string,True)
                  return
              if self.getAccess(room, user) > 0:
                x=(random.choice(["tristeza","felicidade","yaoi","yuri","trap","gg","mal","idiota","jailson","yuri","waifu","rico","lindo","feio","gostoso","bom","gay","keep calm","arrogante","doçe","special","oppai","morte","anjo","caralho","nub","sol","amor","nude","velho","carinho","sexo",'rei',"impotent","cancêr"]))
                zee = rainbow(x)
                room.message("Caro usuário <f x12FF0000='1'>"+sntonick(user.name)+" <f x12A498AC='1'> sua palavra é : <f x12FF0000='1'> "+str(zee), True)
                wordtodaytime[user.name] = json.dumps(time.time()+1200)


        if cmd =="waifu" and self.getAccess(room, user) >= 2:
            if self.getAccess(room, user) > 0:
              if user.name in waifu:
                w = json.loads(waifu[user.name])
                if time.time() < w:
                  w = int(w) - int(time.time())
                  minute = 60
                  hour = minute * 60
                  day = hour * 24
                  days =  int(w / day)
                  hours = int((w % day) / hour)
                  minutes = int((w % hour) / minute)
                  seconds = int(w % minute)
                  string = ""
                  if days > 0:
                    string += str(days) + " " + (days == 1 and " <f x12A498AC='1'>day" or " <f x12A498AC='1'>days" ) + "<f x12FF0000='1'> "
                  if len(string) > 0 or hours > 0:
                    string += str(hours) + " " + (hours == 1 and " <f x12A498AC='1'>hora" or " <f x12A498AC='1'>horas" ) + "<f x12FF0000='1'> "
                  if len(string) > 0 or minutes > 0:
                    string += str(minutes) + " " + (minutes == 1 and " <f x12A498AC='1'>minuto" or " <f x12A498AC='1'>minutos" ) + " <f x12A498AC='1'><f x12FF0000='1'> "
                  string += str(seconds) + " " + (seconds == 1 and " <f x12A498AC='1'>segundo" or " <f x12A498AC='1'>segundos" )
                  room.message("Para usar o comando novamente aguarde :  <f x12FF0000='1'>%s          (~^o^)~ "% string,True)
                  return
              if self.getAccess(room, user) > 0:
                x=(random.choice(["<br/>http://i.imgur.com/n3sPgJW.jpg<br/><f x12A498AC='1'>Personagem: <f x12FF0000='1'>Meguimi <br/><f x12A498AC='1'>Anime: <f x12FF0000='1'>Konosuba","<br/>http://i.imgur.com/U2FrAbJ.jpg<br/><f x12A498AC='1'>Personagem: <f x12FF0000='1'>Victorique <br/><f x12A498AC='1'>Anime: <f x12FF0000='1'>Gosick","<br/>http://i.imgur.com/fNsVi39.png<br/><f x12A498AC='1'>Personagem: <f x12FF0000='1'>vert neptunia <br/><f x12A498AC='1'>Anime: <f x12FF0000='1'>(?)","<br/>http://i.imgur.com/Xv5gHYv.jpg<br/><f x12A498AC='1'>Personagem: <f x12FF0000='1'>Kou Yagami <br/><f x12A498AC='1'>Anime: <f x12FF0000='1'>New game","<br/>https://66.media.tumblr.com/fff138cc0081579f0b3c1520f314b5d0/tumblr_nnw5j4ZxCk1tydz8to1_500.gif<br/><f x12A498AC='1'>Personagem: <f x12FF0000='1'>Hestia <br/><f x12A498AC='1'>Anime: <f x12FF0000='1'>Dungeon","<br/>http://i.imgur.com/xRiELxE.jpg<br/><f x12A498AC='1'>Personagem: <f x12FF0000='1'>Shinobu <br/><f x12A498AC='1'>Anime: <f x12FF0000='1'>Monogatari Series","<brhttp://i.imgur.com/VtFeG4H.jpg<br/><f x12A498AC='1'>Personagem: <f x12FF0000='1'>Hare <br/><f x12A498AC='1'>Anime: <f x12FF0000='1'>Guity crown","<br/>http://i.imgur.com/ZA7NP3N.jpg <br/><f x12A498AC='1'>Personagem: <f x12FF0000='1'>Excell <br/><f x12A498AC='1'>Anime: <f x12FF0000='1'>Kuro kami","<br/>http://i.imgur.com/3SiSIKp.jpg<br/><f x12A498AC='1'>Personagem: <f x12FF0000='1'>Kuro <br/><f x12A498AC='1'>Anime: <f x12FF0000='1'>Kuro kami","<br/>http://i.imgur.com/5L8Giys.png<br/><f x12A498AC='1'>Personagem: <f x12FF0000='1'>Kirino <br/><f x12A498AC='1'>Anime: <f x12FF0000='1'>Oreimo","<br/>http://i.imgur.com/kMiYfKu.jpg<br/><f x12A498AC='1'>Personagem: <f x12FF0000='1'>Yuno <br/><f x12A498AC='1'>Anime: <f x12FF0000='1'>Mirai nikki"]))
                room.message("Caro usuário "+sntonick(user.name)+"<f x12A498AC='1'> sua waifu é : <f x12FF0000='1'>  "+str(x)+"</font> ",True)
                waifu[user.name] = json.dumps(time.time()+1800)


        if cmd =="pdf" and self.getAccess(room, user) >= 2:
            if self.getAccess(room, user) > 0:
              if user.name in pdf:
                w = json.loads(pdf[user.name])
                if time.time() < w:
                  w = int(w) - int(time.time())
                  minute = 60
                  hour = minute * 60
                  day = hour * 24
                  days =  int(w / day)
                  hours = int((w % day) / hour)
                  minutes = int((w % hour) / minute)
                  seconds = int(w % minute)
                  string = ""
                  if days > 0:
                    string += str(days) + " " + (days == 1 and " <f x12A498AC='1'>day" or " <f x12A498AC='1'>days" ) + "<f x12FF0000='1'> "
                  if len(string) > 0 or hours > 0:
                    string += str(hours) + " " + (hours == 1 and " <f x12A498AC='1'>hora" or " <f x12A498AC='1'>horas" ) + "<f x12FF0000='1'> "
                  if len(string) > 0 or minutes > 0:
                    string += str(minutes) + " " + (minutes == 1 and " <f x12A498AC='1'>minuto" or " <f x12A498AC='1'>minutos" ) + " <f x12A498AC='1'><f x12FF0000='1'> "
                  string += str(seconds) + " " + (seconds == 1 and " <f x12A498AC='1'>segundo" or " <f x12A498AC='1'>segundos" )
                  room.message("Para usar o comando novamente aguarde :  <f x12FF0000='1'>%s (~^o^)~ "% string,True)
                  return
              if self.getAccess(room, user) > 0:
                x=(random.choice(["Aiiii que delicia cara! http://i2.ytimg.com/vi/QBPgWoOpS5Q/mqdefault.jpg",
"O problema era na mangueira. http://i2.kym-cdn.com/photos/images/original/000/424/243/792.jpg",
"Não cara, No salame pode não. http://i.ytimg.com/vi/DHc9lnBHhME/mqdefault.jpg",
"Trabalhando e relaxando. http://lh3.googleusercontent.com/-9Kp9lq9fhls/Vwr1CYowkqI/AAAAAAAAFwI/eDG0okXfNqQiZHl7NPUj2RLALSn8LZFDw/w250-h167/zw7tlrG.gif",
"Arrochando os parafusos, queimando uma rosquinha, que delicia. http://i0.kym-cdn.com/photos/images/original/000/525/317/4c8.jpg",
"Senti firmeza demacol. http://i.ytimg.com/vi/JA0w7_Tjyas/hqdefault.jpg",
"Era essa peça q vc queria? http://i.ytimg.com/vi/qu8hJFF9DXw/hqdefault.jpg",
"Nossa assim você me mata. http://i.makeagif.com/media/6-21-2015/oiaVvf.gif"]))
                room.message("Caro usuário "+sntonick(user.name)+"<f x12A498AC='1'> sua frase é : <f x12FF0000='1'>  "+str(x)+"</font> ",True)
                pdf[user.name] = json.dumps(time.time()+1800)

        if cmd =="family" and self.getAccess(room, user) >= 2:
            if self.getAccess(room, user) > 0:
              if user.name in family:
                w = json.loads(family[user.name])
                if time.time() < w:
                  w = int(w) - int(time.time())
                  minute = 60
                  hour = minute * 60
                  day = hour * 24
                  days =  int(w / day)
                  hours = int((w % day) / hour)
                  minutes = int((w % hour) / minute)
                  seconds = int(w % minute)
                  string = ""
                  if days > 0:
                    string += str(days) + " " + (days == 1 and " <f x12A498AC='1'>day" or " <f x12A498AC='1'>days" ) + "<f x12FF0000='1'> "
                  if len(string) > 0 or hours > 0:
                    string += str(hours) + " " + (hours == 1 and " <f x12A498AC='1'>hora" or " <f x12A498AC='1'>horas" ) + "<f x12FF0000='1'> "
                  if len(string) > 0 or minutes > 0:
                    string += str(minutes) + " " + (minutes == 1 and " <f x12A498AC='1'>minuto" or " <f x12A498AC='1'>minutos" ) + " <f x12A498AC='1'><f x12FF0000='1'> "
                  string += str(seconds) + " " + (seconds == 1 and " <f x12A498AC='1'>segundo" or " <f x12A498AC='1'>segundos" )
                  room.message("Para usar o comando novamente aguarde :  <f x12FF0000='1'>%s (~^o^)~ "% string,True)
                  return
              if self.getAccess(room, user) > 0:
                day= random.choice(room.usernames)
                dia= random.choice(room.usernames)
                room.message("A familia do(a) <f x12FF0000='1'>  ["+user.name+"]  <f x12A498AC='1'> é: <br/> O pai é : <f x12FF0000='1'>"+user.name+"  <f x12A498AC='1'> sua mulher é : <f x12FF0000='1'>"+day+" <f x12A498AC='1'> seu filho é : <f x12FF0000='1'> "+dia, True)
                family[user.name] = json.dumps(time.time()+1800)

######################################################################################################################################################
########################################################## BLACKLIST #################################################################################
        


        if cmd.lower() == "bl" and self.getAccess(room, user) >= 5:
              if len(args) > 0:
                if "!anon" in args:
                    room.message("Anons are unable to be blacklisted.")
                    return
                else:
                      if args not in blacklist:
                        blacklist.append(args)
                        self.getRoom("mayubotchat").message("<f x12A498AC='1'><br/><br/>[<f x12FF0000='0'>S<f x12FF4C00='0'>T<f x12FF9800='0'>A<f x12FFE400='0'>T<f x12B3FF00='0'>U<f x1267FF00='0'>S<f x12BFF00='0'> <f x1200FF4C='0'>C<f x1200FF98='0'>M<f x1200FFE4='0'>D<f x12A498AC='1'>]<f x12A498AC='1'><br/><br/><br/><b>Usuário</b>: <f x12FF0000='1'>%s <f x12A498AC='1'><br/><b>Chat</b>: <f x12FF0000='1'>%s  <f x12A498AC='1'><br/><b>Comando</b>: <f x12FF0000='1'>%s - %s  <f x12A498AC='1'><br/><b>IP</b>: <f x12FF0000='1'>%s" % (user.name, room.name, cmd, args, message.ip), True)    
                        rank = self.getAccess(room, user)
                        if rank == 5:
                          room.message("<br/><br/> <f x12FE9A2E='1'> [5 - Admin]  : <f x12FF0000='1'>  "+user.name+"  <br/> <f x12FF0000='1'>  "+args+"   <f x12A498AC='1'> você está na <f x12FF0000='1'> [BLACKLIST]    <f x12A498AC='1'>agora", True)
                        if rank == 6:
                          room.message("<br/><br/> <f x12FE2EF7='1'> [6 - Developer]  : <f x12FF0000='1'>  "+user.name+"  <br/> <f x12FF0000='1'>  "+args+"   <f x12A498AC='1'> você está na <f x12FF0000='1'> [BLACKLIST]    <f x12A498AC='1'>agora", True)
                      else:
                        rank = self.getAccess(room, user)
                        if rank == 5:
                          room.message("<br/><br/> <f x12FE9A2E='1'> [5 - Admin]   : <f x12FF0000='1'>  "+user.name+"  <br/>  <f x12A498AC='1'>o usuário <f x12FF0000='1'>  "+args+"   <f x12A498AC='1'> já está na <f x12FF0000='1'> [BLACKLIST] ", True)
                        if rank == 6:
                          room.message("<br/><br/> <f x12FE2EF7='1'> [6 - Developer]  : <f x12FF0000='1'>  "+user.name+"  <br/>  <f x12A498AC='1'>o usuário <f x12FF0000='1'>  "+args+"   <f x12A498AC='1'> já está na <f x12FF0000='1'> [BLACKLIST] ", True)
              else:
                rank = self.getAccess(room, user)
                if rank == 5:
                  room.message("<br/><br/> <f x12FE9A2E='1'> [5 - Admin] : <f x12FF0000='1'>  "+user.name+"  <br/> <f x12A498AC='1'>eu preciso de um <f x12FF0000='1'>[NICK]", True)
                if rank == 6:
                  room.message("<br/><br/> <f x12FE2EF7='1'> [6 - Developer]  : <f x12FF0000='1'>  "+user.name+"  <br/> <f x12A498AC='1'>eu preciso de um <f x12FF0000='1'>[NICK]", True)


        if cmd.lower() == "ubl" and self.getAccess(room, user) >= 5:
              if len(args) > 0:
                if "!anon" in args:
                    room.message("Anons are unable to be blacklisted.")
                    return
                else:
                      if args in blacklist:
                        blacklist.remove(args)
                        self.getRoom("mayubotchat").message("<f x12A498AC='1'><br/><br/>[<f x12FF0000='0'>S<f x12FF4C00='0'>T<f x12FF9800='0'>A<f x12FFE400='0'>T<f x12B3FF00='0'>U<f x1267FF00='0'>S<f x12BFF00='0'> <f x1200FF4C='0'>C<f x1200FF98='0'>M<f x1200FFE4='0'>D<f x12A498AC='1'>]<f x12A498AC='1'><br/><br/><br/><b>Usuário</b>: <f x12FF0000='1'>%s <f x12A498AC='1'><br/><b>Chat</b>: <f x12FF0000='1'>%s  <f x12A498AC='1'><br/><b>Comando</b>: <f x12FF0000='1'>%s - %s  <f x12A498AC='1'><br/><b>IP</b>: <f x12FF0000='1'>%s" % (user.name, room.name, cmd, args, message.ip), True)    
                        room.message("<br/><br/> <f x126666CC='1'> [Desenvolvedor]  : <f x12FF0000='1'>  "+user.name+"  <br/> <f x12FF0000='1'>  "+args+"   <f x12A498AC='1'> você foi removido da <f x12FF0000='1'> [BLACKLIST] ", True)
                      else:
                        room.message("<br/><br/> <f x126666CC='1'> [Desenvolvedor]  : <f x12FF0000='1'>  "+user.name+"  <br/>  <f x12A498AC='1'>o usuário <f x12FF0000='1'>  "+args+"   <f x12A498AC='1'> não está na <f x12FF0000='1'> [BLACKLIST] ", True)
              else:
                  room.message("<br/><br/> <f x126666CC='1'> [Desenvolvedor]  : <f x12FF0000='1'>  "+user.name+"  <br/> <f x12A498AC='1'>eu preciso de um <f x12FF0000='1'>[NICK]", True)

        if cmd == "blist":
         if self.getAccess(room, user) > 5:
            room.message("<br/><br/><f x12FF0000='1'> [BLACKLIST] :   <f x12A498AC='1'><br/> [%s] " % (", ".join(blacklist)), True)

######################################################################################################################################################
########################################################## BAN USER ######################################################################################

        if cmd == "ban" or cmd == "banir" and self.getAccess(room, user) >= 4:
          if self.getAccess(room, user) > 0:
            if self.getAccess(room, user) > 0:
              room.banUser(ch.User(args))
              room.message(" O usuário   <f x12FF0000='1'>  "+args.title()+"   <f x12A498AC='1'>  foi banido.", True)
            else:
              room.message("Desculpe eu não possuo (mod) aqui :(")
          else:
            room.message(" *warning* Mestre você não tem permissão para executar essa ação. *warning* ")
            
        if cmd == "uban" or cmd == "desbanir" and self.getAccess(room, user) >= 4:
          if args == "": return
          args = args.lower()
          if self.getAccess(room, user) > 0:
            if self.getAccess(room, user) > 0:
              if ch.User(args) not in room._getBanlist():
                room.message(" O usuário   <f x12FF0000='1'>  "+args.title()+"   <f x12A498AC='1'>  não está banido   ", True)
                return
              room.unban(ch.User(args))
              room.message(" Foi retirado o ban do   <f x12FF0000='1'>  "+args.title()+"   <f x12A498AC='1'>  , não abuse das regra novamente, é previna o ban.  ", True)
            else:
              room.message("Desculpe eu não possuo (mod) aqui :(")
          else:
            room.message("*warning*  Mestre você não tem permissão para executar essa ação. *warning* ", True)

      	
##########################################################################################################################################
################################################## ROOMS #################################################################################  

        if cmd == "join" and self.getAccess(room, user) >= 3:
           if args == "": return
           if args in self.roomnames:
            room.message("<f x12A498AC='1'> Opa já estou <f x1233FF33='1'>Online", True)
           else:
             self.joinRoom(args)
             self.getRoom("mayubotchat").message("<f x12A498AC='1'><br/><br/>[<f x12FF0000='0'>S<f x12FF4C00='0'>T<f x12FF9800='0'>A<f x12FFE400='0'>T<f x12B3FF00='0'>U<f x1267FF00='0'>S<f x12BFF00='0'> <f x1200FF4C='0'>C<f x1200FF98='0'>M<f x1200FFE4='0'>D<f x12A498AC='1'>]<f x12A498AC='1'><br/><br/><br/><b>Usuário</b>: <f x12FF0000='1'>%s <f x12A498AC='1'><br/><b>Chat</b>: <f x12FF0000='1'>%s  <f x12A498AC='1'><br/><b>Comando</b>: <f x12FF0000='1'>%s - %s  <f x12A498AC='1'><br/><b>IP</b>: <f x12FF0000='1'>%s" % (user.name, room.name, cmd, args, message.ip), True)    
             room.message("  Entrei em :  <f x12FF0000='1'>  "+args.title(),True)

        if cmd == "leave" and self.getAccess(room, user) >= 5:
            if args == "":
              room.message("Estou saindo. *waves*")
              self.getRoom("mayubotchat").message("<f x12A498AC='1'><br/><br/>[<f x12FF0000='0'>S<f x12FF4C00='0'>T<f x12FF9800='0'>A<f x12FFE400='0'>T<f x12B3FF00='0'>U<f x1267FF00='0'>S<f x12BFF00='0'> <f x1200FF4C='0'>C<f x1200FF98='0'>M<f x1200FFE4='0'>D<f x12A498AC='1'>]<f x12A498AC='1'><br/><br/><br/><b>Usuário</b>: <f x12FF0000='1'>%s <f x12A498AC='1'><br/><b>Chat</b>: <f x12FF0000='1'>%s  <f x12A498AC='1'><br/><b>Comando</b>: <f x12FF0000='1'>%s - %s  <f x12A498AC='1'><br/><b>IP</b>: <f x12FF0000='1'>%s" % (user.name, room.name, cmd, room.name, message.ip), True)    
              self.setTimeout(2, self.leaveRoom, room.name)
            else:
              self.leaveRoom(args)
              self.getRoom("mayubotchat").message("<f x12A498AC='1'><br/><br/>[<f x12FF0000='0'>S<f x12FF4C00='0'>T<f x12FF9800='0'>A<f x12FFE400='0'>T<f x12B3FF00='0'>U<f x1267FF00='0'>S<f x12BFF00='0'> <f x1200FF4C='0'>C<f x1200FF98='0'>M<f x1200FFE4='0'>D<f x12A498AC='1'>]<f x12A498AC='1'><br/><br/><br/><b>Usuário</b>: <f x12FF0000='1'>%s <f x12A498AC='1'><br/><b>Chat</b>: <f x12FF0000='1'>%s  <f x12A498AC='1'><br/><b>Comando</b>: <f x12FF0000='1'>%s - %s  <f x12A498AC='1'><br/><b>IP</b>: <f x12FF0000='1'>%s" % (user.name, room.name, cmd, args, message.ip), True)    
              room.message(" Estou saindo do :  <f x12FF0000='1'>  "+args.title(),True)

        elif cmd == "rooms" and self.getAccess(room, user) >= 2: 
          j = [] 
          for i in self.roomnames: 
            j.append(i+"<f x12FF0000='1'> (%s)" % str(self.getRoom(i).usercount)) 
            j.sort() 
          room.message("[ <f x12A498AC='1'> Online em (<f x12FF0000='1'>%s<f x12A498AC='1'>)  <f x12A498AC='1'> chat's] : <f x12FF0000='1'>  "%(len(self.roomnames))+", ".join(j), True)


        elif cmd == "lockstatus" and self.getAccess(room, user) >= 2:
          if room.name not in locks:
            roomlock = "<f x1233FF33='1'>Desloqueado"
            room.message("<br/><br/><br/><f x12FF0000='1'>[ ★ LOCKSTATUS ★] <br/><f x12A498AC='1'>[Chat]: "+roomlock+"<br/><f x12A498AC='1'>[SimSimi]: <f x12FF0000='1'>Bloqueado ", True)
          if room.name in locks : 
            roomlock = "<f x12FF0000='1'>Bloqueado"
            room.message("<br/><br/><br/><f x12FF0000='1'>[ ★ LOCKSTATUS ★] <br/><f x12A498AC='1'>[Chat]: "+roomlock+"<br/><f x12A498AC='1'>[SimSimi]: <f x12FF0000='1'>Bloqueado ", True)
##########################################################################################################################################
################################################## SYSTEN ################################################################################ 
            
        if cmd == "save" and self.getAccess(room, user) >= 5:
          self.saveAll()
          room.message("Atualizado... *blush*")

        if cmd == "shutdown":      
         if self.getAccess(room, user) >= 6:
          self.saveAll()
          room.message("Tchau *waves*")
          self.setTimeout(3, self.stop, )

        if cmd == "restart":      
         if self.getAccess(room, user) >= 5:
            for room in self.rooms:
                time.sleep(2)
                room.reconnect()
   
        if cmd == "e"and self.getAccess(room, user) >= 6: #DO NOT MESS WITH THIS COMMAND IF YOU DON'T KNOW WHAT YOU'RE DOING (This is a vital command)
         if user.name == "lsabela":
          ret = eval(args)
          if ret == None:
           room.message("Done.")
           return
          room.message(str(ret))
         else:
              room.message("*warning*  Mestre você não tem permissão para executar essa ação. *warning* ")
         

##########################################################################################################################################
################################################## SAY ################################################################################# 

        if cmd == "say" and self.getAccess(room, user) >= 2:
            if args:
              room.message(args, True)
            else:
              room.message("What to say ?")
              
        if cmd == "reverse" or cmd == "rsay" and self.getAccess(room, user) >= 2: #Reversed arguments
          if args:
            room.message(args[::-1])
          else:
            room.message("Fook off"[::-1])

##########################################################################################################################################
################################################## CMDS/RANK #############################################################################            

        elif cmd == "cmds":
          if args == "":
            rank = self.getAccess(room, user)
            if rank == 1:
              room.message("<br/><br/><br/><br/><br/> <f x12FF0000='1'>            [ ★ CMDS ★]<br/> <f x12A498AC='1'> Usuário: <f x12FF0000='1'>"+user.name+" <f x12A498AC='1'> <br/> Rank:  <f x12A498AC='1'> [1 - Whitelist] <f x12FF0040='1'>"+"<br/> ★  [Lista de Comandos] ★ "+"<br/><f x12A498AC='1'> [Usuário <f x12FF0000='1'>"+user.name+"<f x12A498AC='1'> não constar em meu sistema que você esta registrado, para se registrar é liberar seus comandos digite -wl para usufruir do bot (^o^)/ ]", True)
            if rank == 2:
              room.message("<br/><br/><br/><br/><br/> <f x12FF0000='1'>            [ ★ CMDS ★]<br/> <f x12A498AC='1'> Usuário: <f x12FF0000='1'>"+user.name+" <f x12A498AC='1'> <br/> Rank:  <f x1200A3EF='1'> [2 - Registered] <f x12FF0040='1'>"+"<br/> ★  [Lista de Comandos] ★ "+"<br/><f x12FA5882='1'>  [sn,rn,lockstatus,df,mydf,wt,family,waifu,waifu2,pdf,join,rooms,say,rsay,rank,level,ranker,nick,mynick,seenick,gs,gis,yt,yt2,about,profile,sut,server,cso,find,bgtime,cs,dice,users,people,rr,ms,timelocal,isdown,check,myip,pg,mc,relaxar,fuder,kiss,kisses,suck,eat,kill,hug,rb,rb2]", True)
            if rank == 3:
              room.message("<br/><br/><br/><br/><br/> <f x12FF0000='1'>            [ ★ CMDS ★]<br/> <f x12A498AC='1'> Usuário: <f x12FF0000='1'>"+user.name+" <f x12A498AC='1'> <br/> Rank:  <f x12A9D0F5='1'> [3 - Assistant] <f x12FF0040='1'>"+"<br/> ★  [Lista de Comandos] ★ "+"<br/><f x12FA5882='1'>  [sn,rn,lockstatus,df,mydf,wt,family,waifu,waifu2,pdf,join,rooms,say,rsay,rank,level,ranker,nick,mynick,seenick,gs,gis,yt,yt2,about,profile,sut,server,cso,find,bgtime,cs,dice,users,people,rr,ms,timelocal,isdown,check,myip,pg,mc,relaxar,fuder,kiss,kisses,suck,eat,kill,hug,rb,rb2]", True)
            if rank == 4:
              room.message("<br/><br/><br/><br/><br/> <f x12FF0000='1'>            [ ★ CMDS ★]<br/> <f x12A498AC='1'> Usuário: <f x12FF0000='1'>"+user.name+" <f x12A498AC='1'> <br/> Rank:   <f x129F81F7='1'> [4 - Mod] <f x12FF0040='1'>"+"<br/> ★  [Lista de Comandos]   ★ "+"<br/><f x12FA5882='1'>  [sn,rn,lock,unlock,lockstatus,df,mydf,wt,family,waifu,waifu2,pdf,ban,uban,join,rooms,say,rsay,rank,level,ranker,nick,mynick,seenick,gs,gis,yt,yt2,mods,ping,about,profile,sut,server,cso,find,bgtime,cs,dice,users,people,rr,ms,timelocal,isdown,check,myip,pg,mc,relaxar,fuder,kiss,kisses,suck,eat,kill,hug,rb,rb2]", True)
            if rank == 5:
              room.message("<br/><br/><br/><br/><br/> <f x12FF0000='1'>            [ ★ CMDS ★]<br/> <f x12A498AC='1'> Usuário: <f x12FF0000='1'>"+user.name+" <f x12A498AC='1'> <br/> Rank:  <f x12FE9A2E='1'> [5 - Admin] <f x12FF0040='1'>"+"<br/> ★  [Lista de Comandos]   ★ "+"<br/><f x12FA5882='1'> [sn,rn,lock,unlock,lockstatus,sleep,wakeup,df,udf,mydf,wt,family,waifu,waifu2,pdf,bl,ubl,blist,ban,uban,join,leave,rooms,save,restart,say,rsay,rank,level,ranker,nick,mynick,seenick,gs,gis,yt,yt2,msg,fax,broadcast,mods,bg,ping,about,profile,sut,server,cso,find,bgtime,cs,dice,users,people,rr,ms,timelocal,isdown,check,myip,pg,mc,relaxar,fuder,kiss,kisses,suck,eat,kill,hug,rb,rb2]", True)
            if rank == 6:
              room.message("<br/><br/><br/><br/><br/> <f x12FF0000='1'>            [ ★ CMDS ★]<br/> <f x12A498AC='1'> Usuário: <f x12FF0000='1'>"+user.name+" <f x12A498AC='1'> <br/> Rank:  <f x12FE2EF7='1'> [6 - Developer] <f x12FF0040='1'>"+"<br/> ★  [Lista de Comandos]   ★ "+"<br/><f x12FA5882='1'>[sn,rn,lock,unlock,lockstatus,sleep,wakeup,shutdown,df,udf,mydf,wt,family,waifu,waifu2,pdf,bl,ubl,blist,ban,uban,join,leave,rooms,save,restart,shutdown,say,rsay,rank,level,ranker,setrank,nick,mynick,seenick,gs,gis,yt,yt2,msg,fax,broadcast,mods,bg,ping,about,profile,sut,server,cso,find,bgtime,cs,dice,users,people,rr,ms,timelocal,isdown,check,myip,pg,mc,relaxar,fuder,kiss,kisses,suck,eat,kill,hug,rb,rb2]", True)

        elif cmd == "rank":
          if args == "":
            rank = self.getAccess(room, user)
            if rank == 1:
              room.message("<br/><br/><br/> <f x12FF0000='1'>            [ ★ RANK ★]<br/>  <f x12A498AC='1'>Usuário: <f x12FF0000='1'>"+user.name+" <f x12A498AC='1'><br/>Rank: <f x12A498AC='1'> [1 - Whitelist] <f x12FF0040='1'>", True)
            if rank == 2:
              room.message("<br/><br/><br/> <f x12FF0000='1'>            [ ★ RANK ★]<br/>  <f x12A498AC='1'>Usuário: <f x12FF0000='1'>"+user.name+" <f x12A498AC='1'><br/>Rank: <f x1200A3EF='1'> [2 - Registered] <f x12FF0040='1'>", True)
            if rank == 3:
              room.message("<br/><br/><br/> <f x12FF0000='1'>            [ ★ RANK ★]<br/>  <f x12A498AC='1'>Usuário: <f x12FF0000='1'>"+user.name+" <f x12A498AC='1'><br/>Rank: <f x12A9D0F5='1'> [3 - Assistant] <f x12FF0040='1'>", True)
            if rank == 4:
              room.message("<br/><br/><br/> <f x12FF0000='1'>            [ ★ RANK ★]<br/>  <f x12A498AC='1'>Usuário: <f x12FF0000='1'>"+user.name+" <f x12A498AC='1'><br/>Rank: <f x129F81F7='1'> [4 - Mod] <f x12FF0040='1'>", True)
            if rank == 5:
              room.message("<br/><br/><br/> <f x12FF0000='1'>            [ ★ RANK ★]<br/>  <f x12A498AC='1'>Usuário: <f x12FF0000='1'>"+user.name+" <f x12A498AC='1'><br/>Rank: <f x12FE9A2E='1'> [5 - Admin] <f x12FF0040='1'>", True)
            if rank == 6:
              room.message("<br/><br/><br/> <f x12FF0000='1'>            [ ★ RANK ★]<br/>  <f x12A498AC='1'>Usuário: <f x12FF0000='1'>"+user.name+" <f x12A498AC='1'><br/>Rank: <f x12FE2EF7='1'> [6 - Developer] <f x12FF0040='1'>", True)
        
          else:
              rank = self.getAccess(room, ch.User(args))
              if rank == 0:
                room.message("<br/><br/><br/> <f x12FF0000='1'>            [ ★ RANK ★]<br/>  <f x12A498AC='1'>Usuário: <f x12FF0000='1'>"+args+" <f x12A498AC='1'><br/>Rank: <f x1281BEF7='1'> [0 - Unranked] <f x12FF0040='1'>", True)
              if rank == 1:
                room.message("<br/><br/><br/> <f x12FF0000='1'>            [ ★ RANK ★]<br/>  <f x12A498AC='1'>Usuário: <f x12FF0000='1'>"+args+" <f x12A498AC='1'><br/>Rank: <f x12A498AC='1'> [1 - Whitelist] <f x12FF0040='1'>", True)
              if rank == 2:
                room.message("<br/><br/><br/> <f x12FF0000='1'>            [ ★ RANK ★]<br/>  <f x12A498AC='1'>Usuário: <f x12FF0000='1'>"+args+" <f x12A498AC='1'><br/>Rank: <f x1200A3EF='1'> [2 - Registered] <f x12FF0040='1'>", True)
              if rank == 3:
                room.message("<br/><br/><br/> <f x12FF0000='1'>            [ ★ RANK ★]<br/>  <f x12A498AC='1'>Usuário: <f x12FF0000='1'>"+args+" <f x12A498AC='1'><br/>Rank: <f x12A9D0F5='1'> [3 - Assistant] <f x12FF0040='1'>", True)
              if rank == 4:
                room.message("<br/><br/><br/> <f x12FF0000='1'>            [ ★ RANK ★]<br/>  <f x12A498AC='1'>Usuário: <f x12FF0000='1'>"+args+" <f x12A498AC='1'><br/>Rank: <f x129F81F7='1'> [4 - Mod] <f x12FF0040='1'>", True)
              if rank == 5:
                room.message("<br/><br/><br/> <f x12FF0000='1'>            [ ★ RANK ★]<br/>  <f x12A498AC='1'>Usuário: <f x12FF0000='1'>"+args+" <f x12A498AC='1'><br/>Rank: <f x12FE9A2E='1'> [5 - Admin] <f x12FF0040='1'>", True)
              if rank == 6:
                room.message("<br/><br/><br/> <f x12FF0000='1'>            [ ★ RANK ★]<br/>  <f x12A498AC='1'>Usuário: <f x12FF0000='1'>"+args+" <f x12A498AC='1'><br/>Rank: <f x12FE2EF7='1'> [6 - Developer] <f x12FF0040='1'>", True)

        if cmd == "ranker" and self.getAccess(room, user) >= 2:
            room.message("<br/><br/><f x12FF0000='1'>            [ ★ RANK ALL ★] "+"<br/><f x12FE2EF7='1'> [Developer] :   <f x12A498AC='1'> %s " % (", ".join(developer))+"<br/><f x12FE9A2E='1'> [Admin] :   <f x12A498AC='1'> %s " % (", ".join(admin))+"<br/><f x129F81F7='1'> [Mod] :   <f x12A498AC='1'> %s " % (", ".join(mod))+"<br/><f x12A9D0F5='1'> [Assistant] :   <f x12A498AC='1'> %s " % (", ".join(assistant)), True)

        if cmd == "setrank" and self.getAccess(room, user) >= 6:
          if args != "":
#           try:
            args = args.lower()
            target, rank = args.split(" ", 1)
            target = str(target)
            rank = int(rank)
            available_rank = [-1,1,2,3,4,5,6]
            if not rank in available_rank:
              room.message("Digite um rank correspondente")
              return
            if rank == 1:
              if target in whitelist:
                room.message("<f x12FF0000='1'>  "+target.title()+"   <f x12A498AC='1'> foi promovido a    <f x12A498AC='1'> [1 - Whitelist]    <f x12A498AC='1'>  agora. ",True)
                return
              if target in blacklist:
                blacklist.pop(target)
              if target in admin:
                admin.remove(target)
              if target in developer:
                developer.remove(target)
              if target in mod:
                mod.remove(target)
              if target in assistant:
                assistant.remove(target)
              if target in admin:
                admin.remove(target)
              if target in registered:
                registered.remove(target)
              whitelist.append(target)
              room.message("<f x12FF0000='1'>  "+target.title()+"   <f x12A498AC='1'> foi promovido a    <f x12A498AC='1'> [1 - Whitelist]    <f x12A498AC='1'>  agora. ", True)
            if rank == 2:
              if target in registered:
                room.message("<f x12FF0000='1'>  "+target.title()+"   <f x12A498AC='1'> foi promovido a <f x1200A3EF='1'> [Registered]    <f x12A498AC='1'>  agora. ",True)
                return
              if target in blacklist:
                blacklist.pop(target)
              if target in admin:
                admin.remove(target)
              if target in developer:
                developer.remove(target)
              if target in mod:
                mod.remove(target)
              if target in assistant:
                assistant.remove(target)
              if target in admin:
                admin.remove(target)
              if target in whitelist:
                whitelist.remove(target)
              registered.append(target)
              room.message("<f x12FF0000='1'>  "+target.title()+"   <f x12A498AC='1'> foi promovido a <f x1200A3EF='1'> [2 - Registered]    <f x12A498AC='1'>  agora. ", True)
            if rank == 3:
              if not user.name == "sxdanielxd": return #put your name there (if user.name == "yourname" and user.name == "anothername":) To prevent other Owners(in this case is Co-Owners) to set user's rank to Co-Owner.
              if target in assistant:
                room.message("<f x12FF0000='1'>  "+target.title()+"   <f x12A498AC='1'> foi promovido a    <f x12A9D0F5='1'> [3 - Assistant]    <f x12A498AC='1'>  agora. ",True)
                return
              if target in blacklist:
                blacklist.pop(target)
              if target in admin:
                admin.remove(target)
              if target in developer:
                developer.remove(target)
              if target in mod:
                mod.remove(target)
              if target in registered:
                registered.remove(target)
              if target in admin:
                admin.remove(target)
              if target in whitelist:
                whitelist.remove(target)
              assistant.append(target)
              room.message("<f x12FF0000='1'>  "+target.title()+"   <f x12A498AC='1'> foi promovido a    <f x12A9D0F5='1'> [3 - Assistant]    <f x12A498AC='1'>  agora. ", True)
            if rank == 4:
              if target in mod:
                room.message("<f x12FF0000='1'>  "+target.title()+"   <f x12A498AC='1'> foi promovido a    <f x129F81F7='1'> [4 - Mod]    <f x12A498AC='1'>  agora. ",True)
                return
              if target in blacklist:
                blacklist.pop(target)
              if target in admin:
                admin.remove(target)
              if target in developer:
                developer.remove(target)
              if target in assistant:
                assistant.remove(target)
              if target in registered:
                registered.remove(target)
              if target in admin:
                admin.remove(target)
              if target in whitelist:
                whitelist.remove(target)
              mod.append(target)
              room.message("<f x12FF0000='1'>  "+target.title()+"   <f x12A498AC='1'> foi promovido a    <f x129F81F7='1'> [4 - Mod]    <f x12A498AC='1'>  agora. ", True)
            if rank == 5:
              if target in admin:
                room.message("<f x12FF0000='1'>  "+target.title()+"   <f x12A498AC='1'> foi promovido a    <f x12FE9A2E='1'> [5 - Admin]   <f x12A498AC='1'>  agora. ",True)
                return
              if target in blacklist:
                blacklist.pop(target)
              if target in admin:
                admin.remove(target)
              if target in developer:
                developer.remove(target)
              if target in assistant:
                assistant.remove(target)
              if target in registered:
                registered.remove(target)
              if target in mod:
                mod.remove(target)
              if target in whitelist:
                whitelist.remove(target)
              admin.append(target)
              room.message("<f x12FF0000='1'>  "+target.title()+"   <f x12A498AC='1'> foi promovido a    <f x12FE9A2E='1'> [5 - Admin]    <f x12A498AC='1'>  agora. ", True)
            if rank == 6:
              if not user.name == "timmingyukamochida": return #put your name there (if user.name == "yourname" and user.name == "anothername":) To prevent other Owners(in this case is Co-Owners) to set user's rank to Co-Owner.
              if target in developer:
                room.message("<f x12FF0000='1'>  "+target.title()+"   <f x12A498AC='1'> foi promovido a    <f x12FE2EF7='1'> [6 - Developer]   <f x12A498AC='1'>  agora. ",True)
                return
              if target in blacklist:
                blacklist.pop(target)
              if target in admin:
                admin.remove(target)
              if target in admin:
                admin.remove(target)
              if target in assistant:
                assistant.remove(target)
              if target in registered:
                registered.remove(target)
              if target in mod:
                mod.remove(target)
              if target in whitelist:
                whitelist.remove(target)
              developer.append(target)
              room.message("<f x12FF0000='1'>  "+target.title()+"   <f x12A498AC='1'> foi promovido a   <f x12FE2EF7='1'> [6 - Developer]    <f x12A498AC='1'>  agora. ", True)
            if rank == -1:
              if target in blacklist:
                room.message(target.title()+" is already blacklisted.<br/>Reason: %s"% blacklist[target])
                return
              blacklist.update({target:"Annoying reason."})
              room.message(" <f x12FF0000='1'>  "+target.title()+"   <f x12A498AC='1'> ,você está na   <f x12FF0000='1'> [-1 - BLACKLIST]    <f x12A498AC='1'>  agora. ", True)

##########################################################################################################################################
################################################################# NICKS ##################################################################

        elif cmd == "nick" and self.getAccess(room, user) >= 2:
            if args:
                nick = args 
                user = user.name 
                nicks[user] = json.dumps(nick)
                room.message("<f x12FF0000='1'> "+user+"   <f x12A498AC='1'> apartir de agora irei chama-lo de <f x12FF0000='1'> "+str(args)+" ", True)
                try: 
                    print("[SAVING] NICKS...")
                    f = open("nicks.txt", "w")
                    for user in nicks:
                        nick = json.loads(nicks[user])
                        f.write(json.dumps([user,nick]) + "\n")
                except:
                       room.message("Erro ao criar nick.");return
            else:
              room.message("<f x12FF0000='1'>"+user.name+" <f x12A498AC='1'> para usar esse comando digite .nick+ o nome que você quer se chamado.", True)

        elif cmd == "mynick" and self.getAccess(room, user) >= 2:
          user=user.name.lower()
          if user in nicks :
            nick = json.loads(nicks[user])
            room.message("<f x12FF0000='1'> "+user+" <f x12A498AC='1'> seu atual nick é :<f x12FF0000='1'> "+nick,True)
          else:
            room.message("<f x12FF0000='1'>"+user+" <f x12A498AC='1'> você não possui nick. :D ", True)

        elif cmd == "seenick" and self.getAccess(room, user) >= 2:
          try:
            if args in nicks:
              room.message("O nick da <f x12FF0000='1'>"+args+" <f x12A498AC='1'> é :<f x12FF0000='1'>"+sntonick(args), True)
            else:
              room.message("O usuário <f x12FF0000='1'>"+args+" <f x12A498AC='1'> não tem um nick :|", True)
          except:
            return

##########################################################################################################################################
######################################################## GOOGLE ##########################################################################

        if cmd == "gs" and self.getAccess(room, user) >= 2: 
            room.message("Search Google for : ( <f x12FF0000='1'>"+args+"  <f x12A498AC='1'> ) <br/><br/>"+gs(args),True) 

        if cmd == "gis" and self.getAccess(room, user) >= 2:
            room.message("Search Google image for : ( <f x12FF0000='1'>"+args+" <f x12A498AC='1'> ) <br/><br/>"+gis(args),True) 

        if cmd == "youtube" or cmd == "yt2" and self.getAccess(room, user) >= 2:
          if args:
               room.message(tube(args),True)

        if cmd == "yt" and self.getAccess(room, user) >= 2:
         len(args) > 0
         s_result = "";
         sarr = args;
         for i in range(0, len(sarr)):
           if(ord(sarr[i]) < 128):
                 s_result += sarr[i]
         site= "https://www.googleapis.com/youtube/v3/search?part=id&q=" + s_result.replace(" ", "%20")  + "&type=video&key=AIzaSyAA_MhpqTqMG3su4BSt4k7_AyozaEkG_p4"
         response = urlopen(site).read()
         json_response = json.loads(response.decode())
         if(len(json_response["items"]) > 0):
             vId = json_response["items"][0]["id"]["videoId"]
             room.message("https://www.youtube.com/watch?v=" + vId)

##########################################################################################################################################
######################################################## MSG #############################################################################

        if cmd == "msg" and self.getAccess(room, user) >= 5:
         if self.getAccess(room, user) > 0:
            name, body = args.split(" ", 1)
            self.getRoom(name).message(body)
            room.message("[FAX]Enviado.")

        if cmd == "bc" or cmd == "broadcast" and self.getAccess(room, user) >= 5:
         if self.getAccess(room, user) > 0:
           r = room.name
           l = "http://ch.besaba.com/chat/html5/?"+r+"!"
           for room in self.rooms:
               room.message(" <br/><br/><br/><f x12A498AC='1'>[<f x12FF0000='0'>B<f x12FF5500='0'>R<f x12FFAA00='0'>O<f x12AAFF00='0'>A<f x1255FF00='0'>D<f x1200FF55='0'>C<f x1200FFAA='0'>A<f x1200AAFF='0'>S<f x120055FF='0'>T<f x12A498AC='1'>] <br/> <f x12A498AC='1'>Usuário : <f x12FF0000='1'>"+user.name+"<br/>  <f x12A498AC='1'>Chat : <f x12FF0000='1'>"+r+"<br/>  <f x12A498AC='1'>Mensagem : <f x12FFCC00='1'>"+args+"<br/>  <f x12A498AC='1'>Link : <f x12CC66CC='1'>"+l, True)
         else:
               room.message("*warning*  Mestre você não tem permissão para executar essa ação. *warning* ")
        if cmd == "fax" or cmd == "Fax" and self.getAccess(room, user) >= 5:
         if self.getAccess(room, user) > 2:
           try:
             name, body = args.split(" ", 1)
             l = "http://ch.besaba.com/chat/html5/?"+room.name+"!"
             if name in self.roomnames :
               self.getRoom(name).message("<br/><br/><br/><f x12A498AC='1'>[<f x12FF0000='0'>M<f x12FF6D00='0'>S<f x12FFDA00='0'>G<f x1292FF00='0'> <f x1225FF00='0'>F<f x1200FF6D='0'>A<f x1200FFDA='0'>X<f x12A498AC='1'>] <br/> <f x12A498AC='1'>Usuário : <f x12FF0000='1'> %s <br/>  <f x12A498AC='1'>Chat : <f x12FF0000='1'> %s <br/>  <f x12A498AC='1'>Mensagem : <f x12FFCC00='1'> %s <br/>  <f x12A498AC='1'>Link : <f x12CC66CC='1'> %s " % (user.name, room.name, body, l),True)
               room.message("[FAX]Enviado")
             else:
               room.message("Não estou online nesse chat :|")
           except:room.message("error")
         else:
               room.message("*warning*  Mestre você não tem permissão para executar essa ação. *warning* ")

        if cmd == "pm" and len(args) > 1 and self.getAccess(room, user) >= 2:
            name, msg = args.split(" ", 1)
            self.pm.message(ch.User(name.lower()), msg+" - from "+user.name)
            room.message('Sent to <font size="15"><font color="#FF9966"><b>%s</b></font></font>' % name, True)


##########################################################################################################################################
################################################## ROOMS RANK ############################################################################

        elif cmd == "level" and self.getAccess(room, user) >= 2 :
          if args == "":
            level = room.getLevel(user)
            if level == 1:
              title = "Moderator"
            if level == 2:
              title = "OWNER"
            if level == 0:
              title = "Slave"
            room.message("Your room level is: %s [%s]" %(level,title))
          else:
            level = room.getLevel(ch.User(args))
            if level == 1:
              title = "Moderator"
            if level == 2:
              title = "OWNER"
            if level == 0:
              title = "Slave"
            room.message("%s's room level is: %s [%s]" %(args.title(), level, title))
 
        elif cmd == "mods" and self.getAccess(room, user) >= 4:
          args = args.lower()
          if args == "":
            room.message("<br/>||<font color='#87ceeb'><b>OWNER</b></font>: <u>"+ (room.ownername) +"</u> <br/>||<b>Mods</b>: "+", ".join(room.modnames), True)
            return
          if args in self.roomnames:
              modask = self.getRoom(args).modnames
              owner = self.getRoom(args).ownername
              room.message("<br/>||<font color='#87ceeb'><b>OWNER</b></font>: <u>"+ (owner) +"</u> <br/>||<b>Mods</b>: "+", ".join(modask), True)
          else:
             self.joinRoom(args)
             cek_mods[user.name] = json.dumps([room.name,args])
  

##########################################################################################################################################
################################################## CHATANGO SPECIAL ######################################################################
        
 

        elif cmd=="about" and self.getAccess(room, user) >= 2:
           try:
             args=args.lower()
             stuff=str(urlreq.urlopen("http://"+args+".chatango.com").read().decode("utf-8"))
             crap,mini=stuff.split("<span class=\"profile_text\"><!-- google_ad_section_start -->",1)
             mini,crap=mini.split("<!-- google_ad_section_end --></span>",1)
             mini=mini.replace("<img","<!")
             prodata = '<br/>'+mini
             room.message(prodata,True)
           except:
             room.message(""+args+" não existe o.o ")

        elif cmd=="cso" and args != "" and self.getAccess(room, user) >= 2:
          offline = None
          url = urlreq.urlopen("http://"+args+".chatango.com").read().decode()
          if not "buyer" in url:
            room.message(args+" does not exist on chatango.")
          else:
            url2 = urlreq.urlopen("http://"+args+".chatango.com").readlines()
            for line in url2:
              line = line.decode('utf-8')
              if "leave a message for" in line.lower():
                print(line)
                offline = True
            if offline:
              room.message(random.choice([" %s " % args+" está <f x10FF0000='1'> Offline "]), True)
            if not offline:
              room.message(random.choice([" %s " % args+" está <f x1033CC00='1'> Online "]), True)


        elif cmd=="profile" and args != "":
          try:
            args=args.lower()
            stuff=str(urlreq.urlopen("http://"+args+".chatango.com").read().decode("utf-8"))
            crap, age = stuff.split('<span class="profile_text"><strong>Age:</strong></span></td><td><span class="profile_text">', 1)
            age, crap = age.split('<br /></span>', 1)
            crap, gender = stuff.split('<span class="profile_text"><strong>Gender:</strong></span></td><td><span class="profile_text">', 1)
            gender, crap = gender.split(' <br /></span>', 1)
            if gender == 'M':
                gender = 'Masculino'
            elif gender == 'F':
                gender = 'Feminino'
            else:
                gender = '?'
            crap, location = stuff.split('<span class="profile_text"><strong>Location:</strong></span></td><td><span class="profile_text">', 1)
            location, crap = location.split(' <br /></span>', 1)
            crap,mini=stuff.split("<span class=\"profile_text\"><!-- google_ad_section_start -->",1)
            mini,crap=mini.split("<!-- google_ad_section_end --></span>",1)
            mini=mini.replace("<img","<!")
            picture = '<a href="http://fp.chatango.com/profileimg/' + args[0] + '/' + args[1] + '/' + args + '/full.jpg" style="z-index:59" target="_blank">http://fp.chatango.com/profileimg/' + args[0] + '/' + args[1] + '/' + args + '/full.jpg</a>'
            rank = self.getAccess(room, ch.User(args))
          except:
            df = ' não existe. :|'
          offline = None
          url = urlreq.urlopen("http://"+args+".chatango.com").read().decode()
          if not "buyer" in url:
            room.message(args+df)
          else:
            url2 = urlreq.urlopen("http://"+args+".chatango.com").readlines()
            for line in url2:
              line = line.decode('utf-8')
              if "leave a message for" in line.lower():
                offline = True
            rank = self.getAccess(room, ch.User(args))
            if offline:
             if rank == 0:
                 room.message("<br/><br/>[<f x13FF0000='0'>P<f x13FF6D00='0'>R<f x13FFDA00='0'>O<f x1392FF00='0'>F<f x1325FF00='0'>I<f x1300FF6D='0'>L<f x1300FFDA='0'>E<f x13A498AC='1'>]<br/>"+picture+"<br/> <f x13A498AC='1'>Usuário: <f x13FF0000='1'>"+args+"<br/><f x13A498AC='1'>Sexo: <f x13FF0000='1'>"+gender+"<br/><f x13A498AC='1'>Idade: <f x13FF0000='1'>"+age+"<br/><f x13A498AC='1'> País: <f x13FF0000='1'>"+location+" <f x13A498AC='1'><br/>Rank: <f x1381BEF7='1'> [0 - Unranked] <f x13FF0040='1'>"+"<br/><f x13A498AC='1'> Status:<f x13FF0000='1'> Offline"+"<br/> <f x13A498AC='1'> Perfil completo: <f x136666CC='1'> http://barrykun.com/?"+args+"<f x13A498AC='1'> ou <f x136666CC='1'> http://"+args+".chatango.com", True)
             if rank == 1:
                 room.message("<br/><br/>[<f x13FF0000='0'>P<f x13FF6D00='0'>R<f x13FFDA00='0'>O<f x1392FF00='0'>F<f x1325FF00='0'>I<f x1300FF6D='0'>L<f x1300FFDA='0'>E<f x13A498AC='1'>]<br/>"+picture+"<br/> <f x13A498AC='1'>Usuário: <f x13FF0000='1'>"+args+"<br/><f x13A498AC='1'>Sexo: <f x13FF0000='1'>"+gender+"<br/><f x13A498AC='1'>Idade: <f x13FF0000='1'>"+age+"<br/><f x13A498AC='1'> País: <f x13FF0000='1'>"+location+" <f x13A498AC='1'><br/>Rank: <f x13A498AC='1'> [1 - Whitelist] <f x13FF0040='1'>"+"<br/><f x13A498AC='1'> Status:<f x13FF0000='1'> Offline"+"<br/> <f x13A498AC='1'> Perfil completo: <f x136666CC='1'> http://barrykun.com/?"+args+"<f x13A498AC='1'> ou <f x136666CC='1'> http://"+args+".chatango.com", True)
             if rank == 2:
                 room.message("<br/><br/>[<f x13FF0000='0'>P<f x13FF6D00='0'>R<f x13FFDA00='0'>O<f x1392FF00='0'>F<f x1325FF00='0'>I<f x1300FF6D='0'>L<f x1300FFDA='0'>E<f x13A498AC='1'>]<br/>"+picture+"<br/> <f x13A498AC='1'>Usuário: <f x13FF0000='1'>"+args+"<br/><f x13A498AC='1'>Sexo: <f x13FF0000='1'>"+gender+"<br/><f x13A498AC='1'>Idade: <f x13FF0000='1'>"+age+"<br/><f x13A498AC='1'> País: <f x13FF0000='1'>"+location+" <f x13A498AC='1'><br/>Rank: <f x1300A3EF='1'> [2 - Registered] <f x13FF0040='1'>"+"<br/><f x13A498AC='1'> Status:<f x13FF0000='1'> Offline"+"<br/> <f x13A498AC='1'> Perfil completo: <f x136666CC='1'> http://barrykun.com/?"+args+"<f x13A498AC='1'> ou <f x136666CC='1'> http://"+args+".chatango.com", True)
             if rank == 3:
                 room.message("<br/><br/>[<f x13FF0000='0'>P<f x13FF6D00='0'>R<f x13FFDA00='0'>O<f x1392FF00='0'>F<f x1325FF00='0'>I<f x1300FF6D='0'>L<f x1300FFDA='0'>E<f x13A498AC='1'>]<br/>"+picture+"<br/> <f x13A498AC='1'>Usuário: <f x13FF0000='1'>"+args+"<br/><f x13A498AC='1'>Sexo: <f x13FF0000='1'>"+gender+"<br/><f x13A498AC='1'>Idade: <f x13FF0000='1'>"+age+"<br/><f x13A498AC='1'> País: <f x13FF0000='1'>"+location+" <f x13A498AC='1'><br/>Rank: <f x13A9D0F5='1'> [3 - Assistant] <f x13FF0040='1'>"+"<br/><f x13A498AC='1'> Status:<f x13FF0000='1'> Offline"+"<br/> <f x13A498AC='1'> Perfil completo: <f x136666CC='1'> http://barrykun.com/?"+args+"<f x13A498AC='1'> ou <f x136666CC='1'> http://"+args+".chatango.com", True)
             if rank == 4:
                 room.message("<br/><br/>[<f x13FF0000='0'>P<f x13FF6D00='0'>R<f x13FFDA00='0'>O<f x1392FF00='0'>F<f x1325FF00='0'>I<f x1300FF6D='0'>L<f x1300FFDA='0'>E<f x13A498AC='1'>]<br/>"+picture+"<br/> <f x13A498AC='1'>Usuário: <f x13FF0000='1'>"+args+"<br/><f x13A498AC='1'>Sexo: <f x13FF0000='1'>"+gender+"<br/><f x13A498AC='1'>Idade: <f x13FF0000='1'>"+age+"<br/><f x13A498AC='1'> País: <f x13FF0000='1'>"+location+" <f x13A498AC='1'><br/>Rank: <f x139F81F7='1'> [4 - Mod] <f x13FF0040='1'>"+"<br/><f x13A498AC='1'> Status:<f x13FF0000='1'> Offline"+"<br/> <f x13A498AC='1'> Perfil completo: <f x136666CC='1'> http://barrykun.com/?"+args+"<f x13A498AC='1'> ou <f x136666CC='1'> http://"+args+".chatango.com", True)
             if rank == 5:
                 room.message("<br/><br/>[<f x13FF0000='0'>P<f x13FF6D00='0'>R<f x13FFDA00='0'>O<f x1392FF00='0'>F<f x1325FF00='0'>I<f x1300FF6D='0'>L<f x1300FFDA='0'>E<f x13A498AC='1'>]<br/>"+picture+"<br/> <f x13A498AC='1'>Usuário: <f x13FF0000='1'>"+args+"<br/><f x13A498AC='1'>Sexo: <f x13FF0000='1'>"+gender+"<br/><f x13A498AC='1'>Idade: <f x13FF0000='1'>"+age+"<br/><f x13A498AC='1'> País: <f x13FF0000='1'>"+location+" <f x13A498AC='1'><br/>Rank: <f x13FE9A2E='1'> [5 - Admin] <f x13FF0040='1'>"+"<br/><f x13A498AC='1'> Status:<f x13FF0000='1'> Offline"+"<br/> <f x13A498AC='1'> Perfil completo: <f x136666CC='1'> http://barrykun.com/?"+args+"<f x13A498AC='1'> ou <f x136666CC='1'> http://"+args+".chatango.com", True)
             if rank == 6:
                 room.message("<br/><br/>[<f x13FF0000='0'>P<f x13FF6D00='0'>R<f x13FFDA00='0'>O<f x1392FF00='0'>F<f x1325FF00='0'>I<f x1300FF6D='0'>L<f x1300FFDA='0'>E<f x13A498AC='1'>]<br/>"+picture+"<br/> <f x13A498AC='1'>Usuário: <f x13FF0000='1'>"+args+"<br/><f x13A498AC='1'>Sexo: <f x13FF0000='1'>"+gender+"<br/><f x13A498AC='1'>Idade: <f x13FF0000='1'>"+age+"<br/><f x13A498AC='1'> País: <f x13FF0000='1'>"+location+" <f x13A498AC='1'><br/>Rank: <f x13FE2EF7='1'> [6 - Developer] <f x13FF0040='1'>"+"<br/><f x13A498AC='1'> Status:<f x13FF0000='1'> Offline"+"<br/> <f x13A498AC='1'> Perfil completo: <f x136666CC='1'> http://barrykun.com/?"+args+"<f x13A498AC='1'> ou <f x136666CC='1'> http://"+args+".chatango.com", True)
            rank = self.getAccess(room, ch.User(args))
            if not offline:
             if rank == 0:
                 room.message("<br/><br/>[<f x13FF0000='0'>P<f x13FF6D00='0'>R<f x13FFDA00='0'>O<f x1392FF00='0'>F<f x1325FF00='0'>I<f x1300FF6D='0'>L<f x1300FFDA='0'>E<f x13A498AC='1'>]<br/>"+picture+"<br/> <f x13A498AC='1'>Usuário: <f x13FF0000='1'>"+args+"<br/><f x13A498AC='1'>Sexo: <f x13FF0000='1'>"+gender+"<br/><f x13A498AC='1'>Idade: <f x13FF0000='1'>"+age+"<br/><f x13A498AC='1'> País: <f x13FF0000='1'>"+location+" <f x13A498AC='1'><br/>Rank: <f x1381BEF7='1'> [0 - Unranked] <f x13FF0040='1'>"+"<br/><f x13A498AC='1'> Status:<f x1333FF33='1'> Online"+"<br/> <f x13A498AC='1'> Perfil completo: <f x136666CC='1'> http://barrykun.com/?"+args+"<f x13A498AC='1'> ou <f x136666CC='1'> http://"+args+".chatango.com", True)
             if rank == 1:
                 room.message("<br/><br/>[<f x13FF0000='0'>P<f x13FF6D00='0'>R<f x13FFDA00='0'>O<f x1392FF00='0'>F<f x1325FF00='0'>I<f x1300FF6D='0'>L<f x1300FFDA='0'>E<f x13A498AC='1'>]<br/>"+picture+"<br/> <f x13A498AC='1'>Usuário: <f x13FF0000='1'>"+args+"<br/><f x13A498AC='1'>Sexo: <f x13FF0000='1'>"+gender+"<br/><f x13A498AC='1'>Idade: <f x13FF0000='1'>"+age+"<br/><f x13A498AC='1'> País: <f x13FF0000='1'>"+location+" <f x13A498AC='1'><br/>Rank: <f x13A498AC='1'> [1 - Whitelist] <f x13FF0040='1'>"+"<br/><f x13A498AC='1'> Status:<f x1333FF33='1'> Online"+"<br/> <f x13A498AC='1'> Perfil completo: <f x136666CC='1'> http://barrykun.com/?"+args+"<f x13A498AC='1'> ou <f x136666CC='1'> http://"+args+".chatango.com", True)
             if rank == 2:
                 room.message("<br/><br/>[<f x13FF0000='0'>P<f x13FF6D00='0'>R<f x13FFDA00='0'>O<f x1392FF00='0'>F<f x1325FF00='0'>I<f x1300FF6D='0'>L<f x1300FFDA='0'>E<f x13A498AC='1'>]<br/>"+picture+"<br/> <f x13A498AC='1'>Usuário: <f x13FF0000='1'>"+args+"<br/><f x13A498AC='1'>Sexo: <f x13FF0000='1'>"+gender+"<br/><f x13A498AC='1'>Idade: <f x13FF0000='1'>"+age+"<br/><f x13A498AC='1'> País: <f x13FF0000='1'>"+location+" <f x13A498AC='1'><br/>Rank: <f x1300A3EF='1'> [2 - Registered] <f x13FF0040='1'>"+"<br/><f x13A498AC='1'> Status:<f x1333FF33='1'> Online"+"<br/> <f x13A498AC='1'> Perfil completo: <f x136666CC='1'> http://barrykun.com/?"+args+"<f x13A498AC='1'> ou <f x136666CC='1'> http://"+args+".chatango.com", True)
             if rank == 3:
                 room.message("<br/><br/>[<f x13FF0000='0'>P<f x13FF6D00='0'>R<f x13FFDA00='0'>O<f x1392FF00='0'>F<f x1325FF00='0'>I<f x1300FF6D='0'>L<f x1300FFDA='0'>E<f x13A498AC='1'>]<br/>"+picture+"<br/> <f x13A498AC='1'>Usuário: <f x13FF0000='1'>"+args+"<br/><f x13A498AC='1'>Sexo: <f x13FF0000='1'>"+gender+"<br/><f x13A498AC='1'>Idade: <f x13FF0000='1'>"+age+"<br/><f x13A498AC='1'> País: <f x13FF0000='1'>"+location+" <f x13A498AC='1'><br/>Rank: <f x13A9D0F5='1'> [3 - Assistant] <f x13FF0040='1'>"+"<br/><f x13A498AC='1'> Status:<f x1333FF33='1'> Online"+"<br/> <f x13A498AC='1'> Perfil completo: <f x136666CC='1'> http://barrykun.com/?"+args+"<f x13A498AC='1'> ou <f x136666CC='1'> http://"+args+".chatango.com", True)
             if rank == 4:
                 room.message("<br/><br/>[<f x13FF0000='0'>P<f x13FF6D00='0'>R<f x13FFDA00='0'>O<f x1392FF00='0'>F<f x1325FF00='0'>I<f x1300FF6D='0'>L<f x1300FFDA='0'>E<f x13A498AC='1'>]<br/>"+picture+"<br/> <f x13A498AC='1'>Usuário: <f x13FF0000='1'>"+args+"<br/><f x13A498AC='1'>Sexo: <f x13FF0000='1'>"+gender+"<br/><f x13A498AC='1'>Idade: <f x13FF0000='1'>"+age+"<br/><f x13A498AC='1'> País: <f x13FF0000='1'>"+location+" <f x13A498AC='1'><br/>Rank: <f x139F81F7='1'> [4 - Mod] <f x13FF0040='1'>"+"<br/><f x13A498AC='1'> Status:<f x1333FF33='1'> Online"+"<br/> <f x13A498AC='1'> Perfil completo: <f x136666CC='1'> http://barrykun.com/?"+args+"<f x13A498AC='1'> ou <f x136666CC='1'> http://"+args+".chatango.com", True)
             if rank == 5:
                 room.message("<br/><br/>[<f x13FF0000='0'>P<f x13FF6D00='0'>R<f x13FFDA00='0'>O<f x1392FF00='0'>F<f x1325FF00='0'>I<f x1300FF6D='0'>L<f x1300FFDA='0'>E<f x13A498AC='1'>]<br/>"+picture+"<br/> <f x13A498AC='1'>Usuário: <f x13FF0000='1'>"+args+"<br/><f x13A498AC='1'>Sexo: <f x13FF0000='1'>"+gender+"<br/><f x13A498AC='1'>Idade: <f x13FF0000='1'>"+age+"<br/><f x13A498AC='1'> País: <f x13FF0000='1'>"+location+" <f x13A498AC='1'><br/>Rank: <f x13FE9A2E='1'> [5 - Admin] <f x13FF0040='1'>"+"<br/><f x13A498AC='1'> Status:<f x1333FF33='1'> Online"+"<br/> <f x13A498AC='1'> Perfil completo: <f x136666CC='1'> http://barrykun.com/?"+args+"<f x13A498AC='1'> ou <f x136666CC='1'> http://"+args+".chatango.com", True)
             if rank == 6:
                 room.message("<br/><br/>[<f x13FF0000='0'>P<f x13FF6D00='0'>R<f x13FFDA00='0'>O<f x1392FF00='0'>F<f x1325FF00='0'>I<f x1300FF6D='0'>L<f x1300FFDA='0'>E<f x13A498AC='1'>]<br/>"+picture+"<br/> <f x13A498AC='1'>Usuário: <f x13FF0000='1'>"+args+"<br/><f x13A498AC='1'>Sexo: <f x13FF0000='1'>"+gender+"<br/><f x13A498AC='1'>Idade: <f x13FF0000='1'>"+age+"<br/><f x13A498AC='1'> País: <f x13FF0000='1'>"+location+" <f x13A498AC='1'><br/>Rank: <f x13FE2EF7='1'> [6 - Developer] <f x13FF0040='1'>"+"<br/><f x13A498AC='1'> Status:<f x1333FF33='1'> Online"+"<br/> <f x13A498AC='1'> Perfil completo: <f x136666CC='1'> http://barrykun.com/?"+args+"<f x13A498AC='1'> ou <f x136666CC='1'> http://"+args+".chatango.com", True)


        if cmd == ("find") and len(args) > 0 and self.getAccess(room, user) >= 2:
          name = args.split()[0].lower()
          if not ch.User(name).roomnames:
            room.message("Não consigo encontra-lo :(")
          else:
            room.message("Sr(a) %s está atualmente nos seguintes chats :  %s  " % (args, ", ".join(ch.User(name).roomnames)), True)

        if cmd== "bg" or cmd == "background"and self.getAccess(room, user) >= 5:
         if args == "on":
             room.setBgMode(1)
             room.message("BG On", True)
         if args == "off":
            room.setBgMode(0)
            room.message("BG Off" ,True)

        if cmd=="bgtime" and len(args) > 0 and self.getAccess(room, user) >= 2:
            try:
                args=args.lower()
                bgimg = "http://fp.chatango.com/profileimg/%s/%s/%s/msgbg.jpg" % (args[0], args[1], args)
                pic = "http://fp.chatango.com/profileimg/%s/%s/%s/full.jpg" % (args[0], args[1], args)
                if len(args.split(" ", -1)) != 1:
                    return
                if len(args) == 1:
                    f_args, s_args = args, args
                elif len(args) > 1:
                    f_args, s_args = args[0], args[1]
 
                def getBgtime(args):
                    expired = True
                    url = ("http://st.chatango.com/profileimg/" + f_args + "/" + s_args + "/" + args + "/mod1.xml")
                    f = urllib.request.urlopen(url)
                    data = f.read().decode("utf-8")
                    e = ET.XML(data)
                    bg = e.findtext("d")
                    bg = int(urllib.request.unquote(bg))
                    if bg - int(time.time()) < 0:
                      total_seconds = int(time.time())-bg
                    else:
                      total_seconds = bg-int(time.time())
                      expired = False
 
                    # Helper vars:
                    MINUTE  = 60
                    HOUR    = MINUTE * 60
                    DAY     = HOUR * 24
 
                   # Get the days, hours, etc:
                    days    = int( total_seconds / DAY )
                    hours   = int( ( total_seconds % DAY ) / HOUR )
                    minutes = int( ( total_seconds % HOUR ) / MINUTE )
                    seconds = int( total_seconds % MINUTE )
 
                    # Build up the pretty string (like this: "N days, N hours, N minutes, N seconds")
                    string = ""
                    if days > 0 or days < 0:
                        string += str(days) + " " + (days == 1 and " <f x12A498AC='1'>dia" or " <f x12A498AC='1'>dias" ) + "<f x12FF0000='1'> "
                    if len(string) > 0 or hours > 0:
                        string += str(hours) + " " + (hours == 1 and " <f x12A498AC='1'>hora" or " <f x12A498AC='1'>horas" ) + "<f x12FF0000='1'> "
                    if len(string) > 0 or minutes > 0:
                        string += str(minutes) + " " + (minutes == 1 and " <f x12A498AC='1'>minuto" or " <f x12A498AC='1'>minutos" ) + "<f x12FF0000='1'> "
                    string += str(seconds) + " " + (seconds == 1 and " <f x12A498AC='1'>segundo" or " <f x12A498AC='1'>segundos" )
                    if expired == True:
                      return "<f x12FF0000='1'>Expirada"
                    elif expired == False:
                      return " "+string
                room.message("<br/><br/><f x12A498AC='1'>[<f x12FF0000='0'>B<f x12FF5500='0'>G<f x12FFAA00='0'> <f x12AAFF00='0'>S<f x1255FF00='0'>T<f x1200FF55='0'>A<f x1200FFAA='0'>T<f x1200AAFF='0'>U<f x120055FF='0'>S<f x12A498AC='1'>] <br/>Usuário:<f x12FF0000='1'> " + args.title() +"<br/><f x12A498AC='1'>Imagem background: <br/>"+bgimg+"<br/><f x12A498AC='1'> Tempo restante:  <f x12FF0000='1'>" + getBgtime(args), True)
            except:
                room.message("<br/><br/><f x12A498AC='1'>[<f x12FF0000='0'>B<f x12FF5500='0'>G<f x12FFAA00='0'> <f x12AAFF00='0'>S<f x1255FF00='0'>T<f x1200FF55='0'>A<f x1200FFAA='0'>T<f x1200AAFF='0'>U<f x120055FF='0'>S<f x12A498AC='1'>] <br/>Usuário:<f x12FF0000='1'> " + args.title() +"<br/><f x12A498AC='1'>Imagem background: <br/>"+bgimg+"<br/><f x12A498AC='1'> Tempo restante: <f x12FF0000='1'>Expirada", True)

##########################################################################################################################################
################################################## CMD NORMAIS ###########################################################################

        if cmd == "cs" or cmd =="currentstats" and self.getAccess(room, user) >= 2:
          a = len(self.roomnames)
          b = len(developer)
          c = len(admin)
          d = len(mod)
          e = len(assistant)
          f = len(registered)
          g = len(nicks)
          h = len(blacklist)
          room.message("<br/><br/><br/>  <f x12A498AC='1'> ★ Banco de dados ★"+"<br/>  <f x12A498AC='1'> Developer: <f x12FF0000='1'> "+str(b)+"<br/>  <f x12A498AC='1'> Admin: <f x12FF0000='1'> "+str(c)+"<br/>  <f x12A498AC='1'> Mod: <f x12FF0000='1'> "+str(d)+"<br/>  <f x12A498AC='1'> Assistant: <f x12FF0000='1'> "+str(e)+"<br/>  <f x12A498AC='1'> Registered: <f x12FF0000='1'> "+str(f)+"<br/>  <f x12A498AC='1'> Blacklist: <f x12FF0000='1'> "+str(h)+"<br/>  <f x12A498AC='1'> Chat: <f x12FF0000='1'>"+str(a)+"<br/>  <f x12A498AC='1'> Nick: <f x12FF0000='1'>"+str(g) ,True)

        if cmd == "dice" and self.getAccess(room, user) >= 2:
          die1=random.randint(1,6)
          die2=random.randint(1,6)
          room.message("Eu rolei os dados e consegui um : "+str(die1)+" , "+str(die2))


        if cmd =="users" and self.getAccess(room, user) >= 2:
           d=str(room.usercount)
           room.message("<f x12A498AC='1'>Há <f x12FF0000='1'> <b>"+d+"</b> <f x12A498AC='1'> usuários <f x1233FF33='1'>online<f x12A498AC='1'>, é os usuários registrados são : <f x12FF0000='1'><b>%s</b>" % ", ".join(room.usernames),True)

        if cmd == "ping" and self.getAccess(room, user) >= 4:
           if args == "":
            usrs = []
            gay = []
            finale = []
            prop = 0
            prop = prop + len(room._userlist) - 1
            for i in room._userlist:
              i = str(i)
              usrs.append(i)
            while prop >= 0:
              j = usrs[prop].replace("<User: ", "")
              i = j.replace(">", "")
              gay.append(i)
              prop = prop - 1
            for i in gay:
              if i not in finale:
                finale.append(i)
            if len(finale) > 40:
              room.message("@%s"% (" @".join(finale[:41])), True)
            if len(finale) <=40 :
              room.message("@%s"% (" @".join(finale)), True)
           if args != "":
             if args not in self.roomnames:
               room.message("I'm not there.")
               self.getRoom("mayubotchat").message("<br/><br/><b>Nama</b>: %s <br/><b>Rooms</b>: %s  <br/><b>Commmand</b>: %s <br/><b>IP</b>: %s" % (user.name, room.name, cmd, message.ip), True)    
               return
        
        elif cmd == "people" and self.getAccess(room, user) >= 2:
         if args == "":
          usrs = []
          gay = []
          finale = []
          prop = 0
          prop = prop + len(room._userlist) - 1
          for i in room._userlist:
            i = str(i)
            usrs.append(i)
          while prop >= 0:
            j = usrs[prop].replace("<User: ", "")
            i = j.replace(">", "")
            gay.append(i)
            prop = prop - 1
          for i in gay:
            if i not in finale:
              finale.append(i)
          if len(finale) > 40:
            room.message("<f x12FF0000='1'>Há  %s <f x12000099='1'> usuário registrado online nesse chat é eles são : <f x123366FF='1'>%s"% (len(finale),", ".join(finale)), True)
          if len(finale) <=40 :
            room.message("<f x12A498AC='1'>Já passaram <f x12FF0000='1'>  %s   <f x12A498AC='1'>usuário registrado nesse chat é eles são : <f x12FF0000='1'>%s"% (len(finale),", ".join(finale)), True)
         if args != "":
           if args not in self.roomnames:
             room.message("I'm not there.")
             return
           users = getParticipant(str(args))
           if len(users) > 40:
             room.message("<font color='#9999FF'> 40 </font> of  %s   current users in  %s : %s"% (len(users), args.title(), ", ".join(users[:41])), True)
           if len(users) <=40:
             room.message("<f xFF0000='1'>Há <f xFF0000='1'> %s  <f x000099='1'>usuários nesse chat <f x3366FF='1'> %s : %s"% (len(users), args.title(), ", ".join(users)), True)

        if cmd == "rr" and self.getAccess(room, user) >= 2:
            room.message(random.choice(["%s" % "<f x12FF0000='1'>  BANNG!!  <f x12FF0000='1'> "+user.name+" , <f x12A498AC='1'>  você  <f x12FF0000='1'> morreu!! ","<f x12FF0000='1'> *click*  <f x12FF0000='1'> "+user.name+" <f x12A498AC='1'> você  <f x1233FF33='1'> sobreviveu<f x12A498AC='1'>!! "]), True)

        elif cmd == "sut" and self.getAccess(room, user) >= 2:
          minute = 60
          hour = minute * 60
          day = hour * 24
          days =  int(getUptime() / day)
          hours = int((getUptime() % day) / hour)
          minutes = int((getUptime() % hour) / minute)
          seconds = int(getUptime() % minute)
          string = ""
 
          if days > 0:
 
            string += str(days) + " " + (days == 1 and " <f x12A498AC='1'>dia" or " <f x12A498AC='1'>dias" ) + "<f x12FF0000='1'> "
 
          if len(string) > 0 or hours > 0:
 
            string += str(hours) + " " + (hours == 1 and " <f x12A498AC='1'>hora" or " <f x12A498AC='1'>horas" ) + "<f x12FF0000='1'> "
 
          if len(string) > 0 or minutes > 0:
 
            string += str(minutes) + " " + (minutes == 1 and " <f x12A498AC='1'>minuto" or " <f x12A498AC='1'>minutos" ) + "<f x12FF0000='1'> "
 
          string += str(seconds) + " " + (seconds == 1 and " <f x12A498AC='1'>segundo" or " <f x12A498AC='1'>segundos" )
          room.message("Bot online a<f x12A498AC='1'>: <f x12FF0000='1'>%s" % string, True)

        elif cmd == "server" and self.getAccess(room, user) >= 2:
          minute = 60
          hour = minute * 60
          day = hour * 24
          days =  int(getUptime() / day)
          hours = int((getUptime() % day) / hour)
          minutes = int((getUptime() % hour) / minute)
          seconds = int(getUptime() % minute)
          string = ""
 
          if days > 0:
 
            string += str(days) + " " + (days == 1 and " <f x12A498AC='1'>dia" or " <f x12A498AC='1'>dias" ) + "<f x12FF0000='1'> "
 
          if len(string) > 0 or hours > 0:
 
            string += str(hours) + " " + (hours == 1 and " <f x12A498AC='1'>hora" or " <f x12A498AC='1'>horas" ) + "<f x12FF0000='1'> "
 
          if len(string) > 0 or minutes > 0:
 
            string += str(minutes) + " " + (minutes == 1 and " <f x12A498AC='1'>minuto" or " <f x12A498AC='1'>minutos" ) + "<f x12FF0000='1'> "
 
          string += str(seconds) + " " + (seconds == 1 and " <f x12A498AC='1'>segundo" or " <f x12A498AC='1'>segundos" )
          z=(random.choice(["701","721","710","701","781","761","731","733","732","782",]))
          x=(random.choice(["1","2","3","4","5"]))
          room.message("<br/><br/><br/><f x12A498AC='1'>[<f x12FF0000='0'>I<f x12FF2800='0'>N<f x12FF5000='0'>F<f x12FF7800='0'>O<f x12FFA000='0'>R<f x12FFC800='0'>M<f x12FFF000='0'>A<f x12D7FF00='0'>Ç<f x12AFFF00='0'>Ã<f x1287FF00='0'>O<f x125FFF00='0'> <f x1237FF00='0'>S<f x120FFF00='0'>E<f x1200FF28='0'>R<f x1200FF50='0'>V<f x1200FF78='0'>I<f x1200FFA0='0'>D<f x1200FFC8='0'>O<f x1200FFF0='0'>R<f x12A498AC='1'>]<br/><f x12A498AC='1'>Versão bot: <f x12FF0000='1'>2.0.1  <br/><f x12A498AC='1'>Versão sistema : <f x12FF0000='1'>Python 3.5.2 <br/><f x12A498AC='1'>Memoria: <f x12FF0000='1'>"+str(z)+"<f x12A498AC='1'>MB/<f x12FF0000='1'>32<f x12A498AC='1'>GB (Free: <f x12FF0000='1'>31<f x12A498AC='1'>GB) [<f x12FF0000='1'>1<f x12A498AC='1'>% ] <br/>Latencia: <f x12FF0000='1'>"+str(x)+"<f x12A498AC='1'>ms <br/>Servidor online: <f x12FF0000='1'>24<f x12A498AC='1'> dias<br/> Bot online: <f x12FF0000='1'>%s" % string, True)

        if cmd == "ms" or cmd == "lag" and self.getAccess(room, user) >= 2:
            room.message(random.choice(["%s" % "42ms","32ms","41ms","62ms","85ms","42ms","10ms","25ms","95ms"]), True)

        elif cmd=="timelocal" and self.getAccess(room, user) >= 2:
             room.message(strftime("A hora atual é : "+"%H:%M:%S", localtime()))     

        if cmd == "myip" and self.getAccess(room, user) >= 2:
            room.message("<f x12FF0000='1'>  "+user.name+"    <f x12A498AC='1'>   seu atual ip é   <f x12FF0000='1'>  "+message.ip+" ", True)
        
        elif cmd=="isdown" and self.getAccess(room, user) >= 2:
          if len(args)>0:
            for line in urlreq.urlopen("http://www.downforeveryoneorjustme.com/"+args):
              decoder=line.decode("UTF-8")
              if "It's just you." in decoder:
                room.message("O site <f x12FF0000='1'>"+args+"<f x12A498AC='1'> está <f x1233FF33='1'>[ONLINE]", True)
                break
              if "It's not just you!" in decoder:
                room.message("O site <f x12FF0000='1'>"+args+"<f x12A498AC='1'> está <f x12FF0000='1'>[OFFLINE]", True)
                break
              if "doesn't look like a site on the interwho." in decoder:
                room.message("O link do site: <f x12FF0000='1'>"+args+"<f x12A498AC='1'> está <f x126633FF='1'>inválido", True)
                break
              else:
                 continue
          else:
            room.message("Este é o comando (isdown) Para usá-lo, digite <isdown + [O url do site]")

##########################################################################################################################################
################################################## CMD ARGS ##############################################################################

        if cmd == "pg" and self.getAccess(room, user) >= 2:
             if not args == "":
                              room.message(random.choice(["Sim","Não","De jeito nenhum","Mais do que provável","Nunca","Descubra você mesmo","Sem duvida","Como eu vou saber?","Eu me recuso a comentar sobre isso.","Isso é meio óbvio."]))
             else:
                              room.message("Este é o comando (pergunta) Para usá-lo, digite .pg+[Sua pergunta aqui]")
        if cmd == "barry" and self.getAccess(room, user) >= 2:
             if not args == "":
                               room.message(random.choice(["http://barrykun.com/?"+args]))
             else:
                               room.message("Este é o comando (barry) Para usá-lo, digite .barry+[O nick do profile]")
        if cmd == "mc" and self.getAccess(room, user) >= 2:
            if not args == "":
                            room.message(random.choice(["http://ch.besaba.com/chat/html5/?"+args]))
            else:
                            room.message("Este é o comando (mc) Para usá-lo, digite .mc+[O nome do chat]")
        if cmd == "relaxar" :
            if not args == "":
                            room.message(random.choice(["%s" % "Iai vamos relaxar? https://pbs.twimg.com/media/CDrx3lQW0AAEJ4o.jpg @"+args]), True)
            else:
                            room.message(random.choice(["%s" % "Iai vamos relaxar? https://pbs.twimg.com/media/CDrx3lQW0AAEJ4o.jpg @"+user.name]), True)

        if cmd == "fuder" and self.getAccess(room, user) >= 2:
            if not args == "":
                            room.message(random.choice(["%s" % "Oi amor, vamos fuder? ( ͡° ͜ʖ ͡°) @"+args]), True)
            else:
                            room.message(random.choice(["%s" % "Oi amor, vamos fuder? ( ͡° ͜ʖ ͡°) @"+user.name]), True)
        if cmd == "kiss" and self.getAccess(room, user) >= 2:
            if not args == "":
                            room.message(random.choice(["%s" % "https://i.imgur.com/eyJifvl.gif  @"+args]), True)
            else:
                            room.message(random.choice(["%s" % "https://i.imgur.com/eyJifvl.gif @"+user.name]), True)

        elif cmd == "check" and self.getAccess(room, user) >= 2:
                  room.message(self.findUser(args), True)

##suck
        if cmd == "suck" and self.getAccess(room, user) >= 2:
            room.message(" <f x12FF0000='1'>"+user.name+"<f x12A498AC='1'>-senpai está chupando <f x12FF0000='1'>"+random.choice(room.usernames)+"<f x12A498AC='1'>-san Bem gostoso :o", True)
         
##eat
        if cmd == "eat" and self.getAccess(room, user) >= 2:
            room.message("Ohh Nãão!!! "+user.name+"<f x12A498AC='1'> está comendo <f x12FF0000='1'>"+random.choice(room.usernames)+" u////u", True)
         
##kills
        if cmd == "kill" and self.getAccess(room, user) >= 2:
            room.message(" <f x12FF0000='1'>"+user.name+"<f x12A498AC='1'> acabou de matar <f x12FF0000='1'>"+random.choice(room.usernames)+" :@", True)
 
        if cmd == "hug" and self.getAccess(room, user) >= 2:
            if args:
              room.message("*Abraçando <f x12FF0000='1'>" + args+"*")
            else:
              room.message("*Abraço <f x12FF0000='1'>"+random.choice(room.usernames)+"*",True)
##kiss
        if cmd == "kisses" and self.getAccess(room, user) >= 2:
            if args:
              room.message("*Beijando <f x12FF0000='1'>" + args+"*", True)
            else:
              room.message("*Beijo <f x12FF0000='1'>"+random.choice(room.usernames)+"*", True)##########################################################################################################################################
        if cmd == "waifu2" and self.getAccess(room, user) >= 2:
            die1=random.randint(1,100)
            die2=random.randint(1,100)
            die3=random.randint(1,100)
            die4=random.randint(1,100)
            room.message("<f x12FF0000='1'>"+user.name+"<f x12A498AC='1'> sua waifu vai ser <f x12FF0000='1'>"+random.choice(room.usernames)+"<f x12A498AC='1'> vocês vão se beijar <f x12FF0000='1'>"+str(die1)+"<f x12A498AC='1'> vezes ao dia e vai levar <f x12FF0000='1'>"+str(die2)+"<f x12A498AC='1'> chute em um mês e tem <f x12FF0000='1'>"+str(die3)+"% <f x12A498AC='1'> de chance pra ficar com sua waifu e <f x12FF0000='1'>"+str(die4)+"% <f x12A498AC='1'>chance de <f x12FF0000='1'>"+random.choice(room.usernames)+"<f x12A498AC='1'> ser amante.", True)



##########################################################################################################################################
################################################## CMD RB ################################################################################
 
        elif cmd == "rb" and self.getAccess(room, user) >= 2:
              if args == "":
                rain = rainbow('Rainbow!')
                room.message(rain,True)
              else:
                rain = rainbow(args)
                room.message(rain,True)

        elif cmd == "rb2" and self.getAccess(room, user) >= 2:
              if args == "":
                rain = rainbow('Rainbow!')
                room.message(rain)
              else:
                rain = rainbow(args)
                room.message(rain)

################################################## FINAL #################################################################################


   except Exception as e:
         try:
          et, ev, tb = sys.exc_info()
          lineno = tb.tb_lineno
          fn = tb.tb_frame.f_code.co_filename
          room.message("[Error] %s Line %i - %s"% (fn, lineno, str(e)))
          return
         except:
          room.message("Undescribeable error detected !!")
          return

  



  def onFloodWarning(self, room):
    time.sleep(2)
    room.reconnect()



def hexc(e):
  et, ev, tb = sys.exc_info()
  if not tb: print(str(e))
  while tb:
    lineno = tb.tb_lineno
    fn = tb.tb_frame.f_code.co_filename
    tb = tb.tb_next
  print("(%s:%i) %s" % (fn, lineno, str(e)))
  
if __name__ == "__main__":
   try:
     TestBot.easy_start(rooms, botname, botpassword)
   except KeyboardInterrupt:
     print("Console initiated a kill.")
   except Exception as e:
     hexc(e)
