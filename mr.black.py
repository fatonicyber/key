
print('\nProses..')
sleep(1)
print(b+'\n[!] sabar ya sayang mwehehe..')
sleep(1)
try:
      os.mkdir('/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[!]Success !')
sleep(1)
print(b+'\n[!] Making setup file..')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
kontol = open('/data/dam.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
sleep(1)
print(a+'[!] Success !')
sleep(1)
print(b+'\n[!] Setting up..')
sleep(2)
os.system('termux-reload-settings')
print(a+'[!] Successfully !! ^^'+c+'\n\nhubungi 085691015635 untuk requests\natau pertanyaan, atau hubungi mhmdfatoni0304@gmail.com\nThanks :*\n\n')
