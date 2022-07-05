import subprocess
import time


#file1=open("CREATE1.txt","a")
start = time.time()
a=0
while a<=9999999999999999999999:
    print('===================================================================== T E S T 1  =======================================')
    print('=================================<<<< KYVE TESTNET TÜRKİYE  >>>>========================================================')
    print('===============================================================' 'TX=', a, '============================================')
    cmd = "kyved tx bank send kyve1w0rxvf6mq349cy03zwj69d2m534qyuymnvmwkl  kyve1ecdhlulwxgh2uxlnz286egyphswdzau0rtxzha 100000tkyve --chain-id korellia --fees 200tkyve --note KYVE-TÜRKİYE-TX---- --keyring-backend test -y"
    subprocess.Popen(cmd, shell=True)
    time.sleep(3)
    a=a+1  
