alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
                , 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
                , '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '.', '?', '!', ' ']

posKey = []
posPlain = []


def Encrypt(W , choose):
    
    Key = toEnglish("تجربة") 
    if choose == 1 :
        Plain = toEnglish(W)
    else : 
        Plain = W


    enc = ""



    for i in range(len(Key)):
        for j in range(len(alpha)):
            if Key[i] == alpha[j]:
                posKey.append(j)
                break

    for i in range(len(Plain)):
        for j in range(len(alpha)):
            if Plain[i] == alpha[j]:
                posPlain.append(j)
                break

    j = 0

    for i in range(len(posPlain)):
        if j == len(posKey):
            j = 0
        enc += alpha[(posPlain[i] + posKey[j]) % len(alpha)]
        j += 1


    posKey.clear()
    posPlain.clear()


    if choose == 1 :
       return '#Start of Encrypted Message=' + ret(enc) + '=End of Encrypted Message#\n'
    else :
       return '#Start of Encrypted Message=' + enc + '=End of Encrypted Message#\n' 



def Decrypt(E , choose):


    Key = toEnglish("تجربة")

    if choose == 1 :
        Enc = toEnglish(E)
    else :
        Enc = E
    

    plain = ""
    for i in range(len(Key)):
        for j in range(len(alpha)):
            if Key[i] == alpha[j]:
                posKey.append(j)
                break

    for i in range(len(Enc)):
        for j in range(len(alpha)):
            if Enc[i] == alpha[j]:
                posPlain.append(j)
                break

    j = 0



    for i in range(len(Enc)):

        if j == len(posKey):
            j = 0

        plain += alpha[(posPlain[i] - posKey[j]) % len(alpha)]

        j += 1


    posKey.clear()
    posPlain.clear()

    if choose == 1 :
        return '#Start of Decrypted Message=' + ret(plain) + '=End of Decrypted Message#\n'
    else:
        return '#Start of Decrypted Message=' + plain + '=End of Decrypted Message#\n' 



def toEnglish (Key):
   
    arabic = ['ء', 'ا' ,'إ',
        'أ' , 'آ','ب' ,
        'ة' , 'ت', 'ث',
        'ج', 'ح', 'خ',
        'د', 'ذ', 'ر',
        'ز', 'س', 'ش',
        'ص', 'ض', 'ط',
        'ظ', 'ع', 'غ',
        'ف' , 'ق', 'ك',
        'ل', 'م', 'ن',
        'ه', 'ؤ', 'و',
        'ى', 'ئ', 'ي'
     , '٩', '٨', '٧', '٦', '٥', '٤', '٣', '٢', '١', '٠', 
     '؟', '!', '؛', ':', '(' , ')' , '.' , ',' , ' ' , 'ـ' , '"' , '^' , 'ً' , 'َ' , 'ِ' , 'ٍ' , 'ُ' , 'ٌ' , 'ْ' , 'ّ' , ' ' ]



   
    text = ""

    for i in range(len(Key)):
        for j in range(len(arabic)):
            if Key[i] == arabic[j]:
                text+= alpha[j]
                break

    return text


def ret (Key):
    arabic = ['ء', 'ا' ,'إ',
        'أ' , 'آ','ب' ,
        'ة' , 'ت', 'ث',
        'ج', 'ح', 'خ',
        'د', 'ذ', 'ر',
        'ز', 'س', 'ش',
        'ص', 'ض', 'ط',
        'ظ', 'ع', 'غ',
        'ف' , 'ق', 'ك',
        'ل', 'م', 'ن',
        'ه', 'ؤ', 'و',
        'ى', 'ئ', 'ي'
     , '٩', '٨', '٧', '٦', '٥', '٤', '٣', '٢', '١', '٠', 
     '؟', '!', '؛', ':', '(' , ')' , '.' , ',' , ' ' , 'ـ' , '"' , '^' , 'ً' , 'َ' , 'ِ' , 'ٍ' , 'ُ' , 'ٌ' , 'ْ' , 'ّ' , ' ' ]





    text = ""
    for i in range(len(Key)):
        for j in range(len(alpha)):
            if Key[i] == alpha[j]:
                text+= arabic[j]
                break

    return text





ch = 0 

while ch != 3 :
    ch = int(input('Please Choose \n1- Encrypt \n2- Decrypt \n3-exit\n'))

    if ch != 3 :
        language = int(input('Please Choose Language :\n1-Arabic \n2- English \n3-Back\n'))
        message = input('Please Enter The message :\n')

        if language == 1 :
            if ch == 1 :
                print(Encrypt(message , language))
            else :
                print(Decrypt(message , language))
        elif language == 2 :
            if ch == 1 :
                print(Encrypt(message , language))
            else :
                print(Decrypt(message , language))
       
