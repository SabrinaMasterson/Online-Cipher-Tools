from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
#from django.template.defaulttags import register
#for just django
from .passDict_web import *
from .ciphEncode_web import *

import json



# Create your views here.
def tools_home(request):
    return render(request, 'tools.html')

def password_dictionary(request):

    if(request.method == "POST"):
        pass_input = request.POST['inputd']
        res_def = makeDef(pass_input)
        res_dict = makeDict(pass_input)
        data = {}
        data['def'] = res_def
        data['dict'] = res_dict
        #print(res_def)
        #return HttpResponse(json.dumps(data), content_type="application/json")
        return render(request, 'passdict.html', {'data':data})
        
    return render(request, 'passdict.html')

def cipher_encoding(request):

    if (request.method == "POST"):
        ciph_input = request.POST['inputc']
       
        if ciph_input == "":
            ciph_input == "The quick brown fox"
        #in case the input is empty

        ciph_shift = request.POST['shift']
        ciph_mult = request.POST['mult']
        ciph_type = request.POST['type']
        ciph1 = request.POST['dropdown1']
        ciph2 = request.POST['dropdown2']
        explanation1 = "Here's the location for the first cipher explanation."
        explanation2 = "Here's the location for the second cipher explanation."
        results = "empty"
        if (ciph1 == "Caesar"):
            explanation1 = "The Caesar cipher (famous for use by Julius Caesar) is a cipher that shifts the input text's letters in the alphabet by a number (the same for each letter). So a shift of 3 on the letters 'abc' shifts them over by three, to 'def'. " 
        elif (ciph1 == "Affine"):
            explanation1 = "Affine is very similar to the Caesar cipher, as it shifts over letters in the alphabet with a number, but with a twist: Affine also adds a multiplier, this multiples the letter to change it even further. The catch is that the multiplier must be a coprime of 26, the number of letters in the alphabet. Otherwise, it would go past this number, and there is no 27th letter in the alphabet. Here are some example coprimes of 26 for you to input: 1, 3, 5, 7, 9 11, 15, 17, 19, 21, 23, and 25."
        elif (ciph1 == "Atbash"):
            explanation1 = "Like the other shifting ciphers, Atbash cipher encodes by taking a letter, and choosing it's letter on the opposite side of the alphabet. So A becomes Z and B becomes Y, and so on. As such, no shift or multiplier is needed."
        elif (ciph1 == "Base64"):
            explanation1 = "Unlike the other shift ciphers, Base64 doesn't use a shift, instead it transforms letters from their ASCHII format to a 64-base representation. This means that instead of A-Z, it uses uppercase, lowercase, numbers from 0-9, and special charcters to define it's 'language'. There are additional bases as well, such as base32 and base16, which you can encode and decode with this cipher."
        elif(ciph1 == "Baconian"):
            explanation1 = "Unlike the other shift ciphers, Baconian replaces a letter with a series of five letters. These letters are a combination of a and b, and are set. so A will always equal 'aaaaa' and B will always equal 'aaaab'. It's essentially trading one alphabet for another, each with 26 'letters'. As a note, there is another version of this cipher, in which I and J, and U and V have the same 5-letter combinations, making a 24 alphabet for the encoding instead of 26."
        else:
            explanation1 = "Here's the location for the first cipher explanation."
        if (ciph2 == "Caesar"):
            explanation2 = "The Caesar cipher (famous for use by Julius Caesar) is a cipher that shifts the input text's letters in the alphabet by a number (the same for each letter). So a shift of 3 on the letters 'abc' shifts them over by three, to 'def'. " 
        elif (ciph2 == "Affine"):
            explanation2 = "Affine is very similar to the Caesar cipher, as it shifts over letters in the alphabet with a number, but with a twist: Affine also adds a multiplier, this multiples the letter to change it even further. The catch is that the multiplier must be a coprime of 26, the number of letters in the alphabet. Otherwise, it would go past this number, and there is no 27th letter in the alphabet. Here are some example coprimes of 26 for you to input: 1, 3, 5, 7, 9 11, 15, 17, 19, 21, 23, and 25."
        elif (ciph2 == "Atbash"):
            explanation2 = "Like the other shifting ciphers, Atbash cipher encodes by taking a letter, and choosing it's letter on the opposite side of the alphabet. So A becomes Z and B becomes Y, and so on. As such, no shift or multiplier is needed."
        elif (ciph2 == "Base64"):
            explanation2 = "Unlike the other shift ciphers, Base64 doesn't use a shift, instead it transforms letters from their ASCHII format to a 64-base representation. This means that instead of A-Z, it uses uppercase, lowercase, numbers from 0-9, and special charcters to define it's 'language'. There are additional bases as well, such as base32 and base16, which you can encode and decode with this cipher."
        elif(ciph2 == "Baconian"):
            explanation2 = "Unlike the other shift ciphers, Baconian replaces a letter with a series of five letters. These letters are a combination of a and b, and are set. so A will always equal 'aaaaa' and B will always equal 'aaaab'. It's essentially trading one alphabet for another, each with 26 'letters'. As a note, there is another version of this cipher, in which I and J, and U and V have the same 5-letter combinations, making a 24 alphabet for the encoding instead of 26."
        else:
            explanation2 = "Here's the location for the second cipher explanation."
        if 'encode' in request.POST:
            #encode chosen
            if (ciph1 == "Caesar" and ciph2 == "None"):
                results = encryptCaesar(ciph_input, int(ciph_shift))
            elif (ciph1 == "Affine" and ciph2 == "None"):
                results = encryptAffine(ciph_input, int(ciph_mult), int(ciph_shift))
            elif (ciph1 == "Atbash" and ciph2 == "None"):
                results = encryptAtbash(ciph_input)
            elif (ciph1 == "Base64" and ciph2 == "None"):
                results = encryptBase64(ciph_input, int(ciph_type))
            elif (ciph1 == "Baconian" and ciph2 == "None"):
                results = encryptBaconian(ciph_input)
            #for cipher 1
            elif (ciph2 == "Caesar" and ciph1 == "None"):
                results = encryptCaesar(ciph_input, int(ciph_shift))
            elif (ciph2 == "Affine" and ciph1 == "None"):
                results = encryptAffine(ciph_input, int(ciph_mult), int(ciph_shift))
            elif (ciph2 == "Atbash" and ciph1 == "None"):
                results = encryptAtbash(ciph_input)
            elif (ciph2 == "Base64" and ciph1 == "None"):
                results = encryptBase64(ciph_input, int(ciph_type))
            elif (ciph2 == "Baconian" and ciph1 == "None"):
                results = encryptBaconian(ciph_input)
            #for cipher 2
            elif(ciph1 != "None" and ciph2 != "None"):
                if (ciph1 == ciph2):
                    results = "You cannot combine the same ciphers together"
                else:
                    results = combine_ciphs(ciph_input, "e", ciph1, ciph2, ciph_shift, ciph_mult, ciph_type)
            #for combinations
            else:
                results = "Please choose a cipher"
        else:
            #decode chosen
            if (ciph1 == "Caesar" and ciph2 == "None"):
                results = decryptCaesar(ciph_input, int(ciph_shift))
                
            elif (ciph1 == "Affine" and ciph2 == "None"):
                results = decryptAffine(ciph_input, int(ciph_mult), int(ciph_shift))
            elif (ciph1 == "Atbash" and ciph2 == "None"):
                results = decryptAtbash(ciph_input)
            elif (ciph1 == "Base64" and ciph2 == "None"):
                results = decryptBase64(ciph_input, int(ciph_type))
            elif (ciph1 == "Baconian" and ciph2 == "None"):
                results = decryptBaconian(ciph_input)
            #for cipher 1
            elif (ciph2 == "Caesar" and ciph1 == "None"):
                results = decryptCaesar(ciph_input, int(ciph_shift))
            elif (ciph2 == "Affine" and ciph1 == "None"):
                results = decryptAffine(ciph_input, int(ciph_mult), int(ciph_shift))
            elif (ciph2 == "Atbash" and ciph1 == "None"):
                results = decryptAtbash(ciph_input)
            elif (ciph2 == "Base64" and ciph1 == "None"):
                results = decryptBase64(ciph_input, int(ciph_type))
            elif (ciph2 == "Baconian" and ciph1 == "None"):
                results = decryptBaconian(ciph_input)
            #for cipher 2
            elif(ciph1 != "None" and ciph2 != "None"):
                if (ciph1 == ciph2):
                    results = "You cannot combine the same ciphers together"
                else:
                    results = combine_ciphs(ciph_input, "d", ciph1, ciph2, ciph_shift, ciph_mult, ciph_type)
            #for combinations
            else:
                results = "Please choose a cipher"
        data = {}
        data['res'] = results
        data['ex1'] = explanation1
        data['ex2'] = explanation2
        return render(request, 'ciphencode.html', {'data':data})
    return render(request, 'ciphencode.html')



