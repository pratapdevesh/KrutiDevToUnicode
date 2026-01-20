import re

class KrutiDevConverter:
    def __init__(self):
        self.array_one_kd_to_uni = [
            "ñ", "Q+Z", "sas", "aa", ")Z", "ZZ", "‘", "’", "“", "”",
            "å", "ƒ", "„", "…", "†", "‡", "ˆ", "‰", "Š", "‹",
            "¶+", "d+", "[+k", "[+", "x+", "T+", "t+", "M+", "<+", "Q+", ";+", "j+", "u+",
            "Ùk", "Ù", "ä", "–", "—", "é", "™", "=kk", "f=k",
            "à", "á", "â", "ã", "ºz", "º", "í", "{k", "{", "=", "«",
            "Nî", "Vî", "Bî", "Mî", "<î", "|", "K", "}",
            "J", "Vª", "Mª", "<ªª", "Nª", "Ø", "Ý", "nzZ", "æ", "ç", "Á", "xz", "#", ":",
            "v‚", "vks", "vkS", "vk", "v", "b±", "Ã", "bZ", "b", "m", "Å", ",s", ",", "_",
            "ô", "d", "Dk", "D", "£", "[k", "[", "x", "Xk", "X", "Ä", "?k", "?", "³",
            "p", "Pk", "P", "N", "t", "Tk", "T", ">", "÷", "¥",
            "ê", "ë", "V", "B", "ì", "ï", "M+", "<+", "M", "<", ".k", ".",
            "r", "Rk", "R", "Fk", "F", ")", "n", "/k", "èk", "/", "Ë", "è", "u", "Uk", "U",
            "i", "Ik", "I", "Q", "¶", "c", "Ck", "C", "Hk", "H", "e", "Ek", "E",
            ";", "¸", "j", "y", "Yk", "Y", "G", "o", "Ok", "O",
            "'k", "'", "\"k", "\"", "l", "Lk", "L", "g",
            "È", "z",
            "Ì", "Í", "Î", "Ï", "Ñ", "Ò", "Ó", "Ô", "Ö", "Ø", "Ù", "Ük", "Ü",
            "‚", "¨", "ks", "©", "kS", "k", "h", "q", "w", "`", "s", "¢", "S",
            "a", "¡", "%", "W", "•", "·", "∙", "·", "~j", "~", "\\", "+", " ः",
            "^", "*", "Þ", "ß", "(", "¼", "½", "¿", "À", "¾", "A", "-", "&", "&", "Œ", "]", "~ ", "@",
            "ाे", "ाॅ", "ंै", "े्र", "अौ", "अो", "आॅ"
        ]

        self.array_two_kd_to_uni = [
            "॰", "QZ+", "sa", "a", "र्द्ध", "Z", "\"", "\"", "'", "'",
            "०", "१", "२", "३", "४", "५", "६", "७", "८", "९",
            "फ़्", "क़", "ख़", "ख़्", "ग़", "ज़्", "ज़", "ड़", "ढ़", "फ़", "य़", "ऱ", "ऩ",
            "त्त", "त्त्", "क्त", "दृ", "कृ", "न्न", "न्न्", "=k", "f=",
            "ह्न", "ह्य", "हृ", "ह्म", "ह्र", "ह्", "द्द", "क्ष", "क्ष्", "त्र", "त्र्",
            "छ्य", "ट्य", "ठ्य", "ड्य", "ढ्य", "द्य", "ज्ञ", "द्व",
            "श्र", "ट्र", "ड्र", "ढ्र", "छ्र", "क्र", "फ्र", "र्द्र", "द्र", "प्र", "प्र", "ग्र", "रु", "रू",
            "ऑ", "ओ", "औ", "आ", "अ", "ईं", "ई", "ई", "इ", "उ", "ऊ", "ऐ", "ए", "ऋ",
            "क्क", "क", "क", "क्", "ख", "ख", "ख्", "ग", "ग", "ग्", "घ", "घ", "घ्", "ङ",
            "च", "च", "च्", "छ", "ज", "ज", "ज्", "झ", "झ्", "ञ",
            "ट्ट", "ट्ठ", "ट", "ठ", "ड्ड", "ड्ढ", "ड़", "ढ़", "ड", "ढ", "ण", "ण्",
            "त", "त", "त्", "थ", "थ्", "द्ध", "द", "ध", "ध", "ध्", "ध्", "ध्", "न", "न", "न्",
            "प", "प", "प्", "फ", "फ्", "ब", "ब", "ब्", "भ", "भ्", "म", "म", "म्",
            "य", "य्", "र", "ल", "ल", "ल्", "ळ", "व", "व", "व्",
            "श", "श्", "ष", "ष्", "स", "स", "स्", "ह",
            "ीं", "्र",
            "द्द", "ट्ट", "ट्ठ", "ड्ड", "कृ", "भ", "्य", "ड्ढ", "झ्", "क्र", "त्त्", "श", "श्",
            "ॉ", "ो", "ो", "ौ", "ौ", "ा", "ी", "ु", "ू", "ृ", "े", "े", "ै",
            "ं", "ँ", "ः", "ॅ", "ऽ", "ऽ", "ऽ", "ऽ", "्र", "्", "?", "़", ":",
            "‘", "’", "“", "”", ";", "(", ")", "{", "}", "=", "।", ".", "-", "µ", "॰", ",", "् ", "/",
            "ो", "ॉ", "ैं", "्रे", "औ", "ओ", "ऑ"
        ]

        # UNICODE TO KRUTI DEV ARRAYS
        self.array_one_uni_to_kd = [
            "‘", "’", "“", "”", "(", ")", "{", "}", "=", "।", "?", "-", "µ", "॰", ",", ".", "् ",
            "०", "१", "२", "३", "४", "५", "६", "७", "८", "९", "x", "+", ";", "_",
            "फ़्", "क़", "ख़", "ग़", "ज़्", "ज़", "ड़", "ढ़", "फ़", "य़", "ऱ", "ऩ",
            "त्त्", "त्त", "क्त", "दृ", "कृ",
            "श्व", "ह्न", "ह्य", "हृ", "ह्म", "ह्र", "ह्", "द्द", "क्ष्", "क्ष", "त्र्", "त्र", "ज्ञ",
            "छ्य", "ट्य", "ठ्य", "ड्य", "ढ्य", "द्य", "द्व",
            "श्र", "ट्र", "ड्र", "ढ्र", "छ्र", "क्र", "फ्र", "द्र", "प्र", "ग्र", "रु", "रू",
            "्र",
            "ओ", "औ", "आ", "अ", "ई", "इ", "उ", "ऊ", "ऐ", "ए", "ऋ",
            "क्", "क", "क्क", "ख्", "ख", "ग्", "ग", "घ्", "घ", "ङ",
            "चै", "च्", "च", "छ", "ज्", "ज", "झ्", "झ", "ञ",
            "ट्ट", "ट्ठ", "ट", "ठ", "ड्ड", "ड्ढ", "ड", "ढ", "ण्", "ण",
            "त्", "त", "थ्", "थ", "द्ध", "द", "ध्", "ध", "न्", "न",
            "प्", "प", "फ्", "फ", "ब्", "ब", "भ्", "भ", "म्", "म",
            "य्", "य", "र", "ल्", "ल", "ळ", "व्", "व",
            "श्", "श", "ष", "ष्", "स", "स", "स्", "ह",
            "ऑ", "ॉ", "ो", "ौ", "ा", "ी", "ु", "ू", "ृ", "े", "ै",
            "ं", "ँ", "ः", "ॅ", "ऽ", "् ", "्", "़", "/"
        ]

        self.array_two_uni_to_kd = [
            "^", "*", "Þ", "ß", "¼", "½", "¿", "À", "¾", "A", "\\", "&", "&", "Œ", "]", "-", "~ ",
            "å", "ƒ", "„", "…", "†", "‡", "ˆ", "‰", "Š", "‹", "Û", "$", "(", "&",
            "¶+", "d+", "[k+", "x+", "T+", "t+", "M+", "<+", "Q+", ";+", "j+", "u+",
            "Ù", "Ùk", "ä", "–", "—",
            "Üo", "à", "á", "â", "ã", "ºz", "º", "í", "{", "{k", "«", "=", "K",
            "Nî", "Vî", "Bî", "Mî", "<î", "|", "}",
            "J", "Vª", "Mª", "<ªª", "Nª", "Ø", "Ý", "æ", "ç", "xz", "#", ":",
            "z",
            "vks", "vkS", "vk", "v", "bZ", "b", "m", "Å", ",s", ",", "_",
            "D", "d", "ô", "[", "[k", "X", "x", "?", "?k", "³",
            "pkS", "P", "p", "N", "T", "t", "÷", ">", "¥",
            "ê", "ë", "V", "B", "ì", "ï", "M", "<", ".", ".k",
            "R", "r", "F", "Fk", ")", "n", "è", "èk", "U", "u",
            "I", "i", "¶", "Q", "C", "c", "H", "Hk", "E", "e",
            "¸", ";", "j", "Y", "y", "G", "O", "o",
            "'", "'k", "\"", "\"k", "L", "l", "g", "g",
            "v‚", "‚", "ks", "kS", "k", "h", "q", "w", "`", "s", "S",
            "a", "¡", "%", "W", "•", "~ ", "~", "+", "@"
        ]

    def convert_to_unicode(self, text):
        if not text:
            return ""

        modified_substring = text

        # Global substitutions from array
        for i in range(len(self.array_one_kd_to_uni)):
           modified_substring = modified_substring.replace(self.array_one_kd_to_uni[i], self.array_two_kd_to_uni[i])
        
        # Special Glyph Handling
        modified_substring = modified_substring.replace("±", "Zं") # reph+anusvAr
        modified_substring = modified_substring.replace("Æ", "र्f") # reph + i

        # Positioning of 'i' matra (f)
        position_of_i = modified_substring.find("f")
        while position_of_i != -1:
            character_next_to_i = modified_substring[position_of_i + 1] if position_of_i + 1 < len(modified_substring) else ""
            character_to_be_replaced = "f" + character_next_to_i
            modified_substring = modified_substring.replace(character_to_be_replaced, character_next_to_i + "ि", 1) # Replace only first occurrence per finding
            # Need to search again from current position or restart? JS code searches from position_of_i + 1. 
            # In Python replace returns a new string.
            # We should probably be careful with the loop variable.
            # The JS logic: replace string, then search from pos+1. 
            # If we replaced "fK" with "Kि", the 'f' is gone from that spot. 
            # So next search should be successful.
            position_of_i = modified_substring.find("f", position_of_i + 1)
        
        # handling 'fa' (i + anusvar)
        modified_substring = modified_substring.replace("Ç", "fa")
        modified_substring = modified_substring.replace("É", "र्fa")
        
        position_of_i = modified_substring.find("fa")
        while position_of_i != -1:
            character_next_to_ip2 = modified_substring[position_of_i + 2] if position_of_i + 2 < len(modified_substring) else ""
            character_to_be_replaced = "fa" + character_next_to_ip2
            modified_substring = modified_substring.replace(character_to_be_replaced, character_next_to_ip2 + "िं", 1)
            position_of_i = modified_substring.find("fa", position_of_i + 2)

        modified_substring = modified_substring.replace("Ê", "ीZ")

        # Fixing 'chotee ee' on half-letters
        position_of_wrong_ee = modified_substring.find("ि्")
        while position_of_wrong_ee != -1:
            consonent_next_to_wrong_ee = modified_substring[position_of_wrong_ee + 2] if position_of_wrong_ee + 2 < len(modified_substring) else ""
            character_to_be_replaced = "ि्" + consonent_next_to_wrong_ee
            modified_substring = modified_substring.replace(character_to_be_replaced, "्" + consonent_next_to_wrong_ee + "ि", 1)
            position_of_wrong_ee = modified_substring.find("ि्", position_of_wrong_ee + 2)
        
        # Reph "Z" processing
        set_of_matras = "अ आ इ ई उ ऊ ए ऐ ओ औ ा ि ी ु ू ृ े ै ो ौ ं : ँ ॅ"
        position_of_R = modified_substring.find("Z")
        while position_of_R > 0:
            probable_position_of_half_r = position_of_R - 1
            character_at_probable_position_of_half_r = modified_substring[probable_position_of_half_r]
            
            while character_at_probable_position_of_half_r in set_of_matras:
                probable_position_of_half_r = probable_position_of_half_r - 1
                if probable_position_of_half_r < 0: break 
                character_at_probable_position_of_half_r = modified_substring[probable_position_of_half_r]
            
            previous_to_position_of_half_r = probable_position_of_half_r - 1
            if previous_to_position_of_half_r >= 0:
                character_previous_to_position_of_half_r = modified_substring[previous_to_position_of_half_r]
                while character_previous_to_position_of_half_r == "्":
                    probable_position_of_half_r = previous_to_position_of_half_r - 1
                    if probable_position_of_half_r < 0: break
                    character_at_probable_position_of_half_r = modified_substring[probable_position_of_half_r]
                    
                    previous_to_position_of_half_r = probable_position_of_half_r - 1
                    if previous_to_position_of_half_r < 0: break
                    character_previous_to_position_of_half_r = modified_substring[previous_to_position_of_half_r]

            character_to_be_replaced = modified_substring[probable_position_of_half_r : position_of_R]
            new_replacement_string = "र्" + character_to_be_replaced
            character_to_be_replaced_full = character_to_be_replaced + "Z"
            modified_substring = modified_substring.replace(character_to_be_replaced_full, new_replacement_string, 1)
            position_of_R = modified_substring.find("Z")

        return modified_substring

    def convert_to_krutidev(self, text):
        if not text:
            return ""
        
        modified_substring = text
        
        # Nukta Handling
        modified_substring = modified_substring.replace("त्र्य", "«य")
        modified_substring = modified_substring.replace("श्र्य", "Ü‍‍zय")
        modified_substring = modified_substring.replace("क़", "क़")
        modified_substring = modified_substring.replace("ख़‌", "ख़")
        modified_substring = modified_substring.replace("ग़", "ग़")
        modified_substring = modified_substring.replace("ज़", "ज़")
        modified_substring = modified_substring.replace("ड़", "ड़")
        modified_substring = modified_substring.replace("ढ़", "ढ़")
        modified_substring = modified_substring.replace("ऩ", "ऩ")
        modified_substring = modified_substring.replace("फ़", "फ़")
        modified_substring = modified_substring.replace("य़", "य़")
        modified_substring = modified_substring.replace("ऱ", "ऱ")

        # Matra positioning for 'i' (f)
        # JS loops backwards for this one, or just careful replacement
        position_of_f = modified_substring.find("ि")
        while position_of_f != -1:
            character_left_to_f = modified_substring[position_of_f - 1] if position_of_f - 1 >= 0 else ""
            if character_left_to_f:
                modified_substring = modified_substring.replace(character_left_to_f + "ि", "f" + character_left_to_f, 1)
                position_of_f = position_of_f - 1
            else:
                 # Should not happen ideally if text is valid
                 break

            while (position_of_f - 1 >= 0) and (modified_substring[position_of_f - 1] == "्") and (position_of_f != 0):
                # We need to handle moving 'f' further back over half letters
                # string_to_be_replaced logic from JS:
                # var string_to_be_replaced = modified_substring.charAt(position_of_f - 2) + "्";
                # modified_substring = modified_substring.replace(string_to_be_replaced + "f", "f" + string_to_be_replaced);
                
                string_to_be_replaced = modified_substring[position_of_f - 2] + "्"
                modified_substring = modified_substring.replace(string_to_be_replaced + "f", "f" + string_to_be_replaced, 1)
                position_of_f = position_of_f - 2
            
            position_of_f = modified_substring.find("ि", position_of_f + 1)
        
        # Reph (half-r) processing
        set_of_matras = "ािीुूृेैोौं:ँॅ"
        modified_substring += '  ' # Padding for safety as per JS
        
        position_of_half_R = modified_substring.find("र्")
        while position_of_half_R >= 0:
            probable_position_of_Z = position_of_half_R + 2
            character_at_probable_position_of_Z = modified_substring[probable_position_of_Z]
            
            while character_at_probable_position_of_Z in set_of_matras:
                probable_position_of_Z = probable_position_of_Z + 1
                if probable_position_of_Z >= len(modified_substring): break
                character_at_probable_position_of_Z = modified_substring[probable_position_of_Z]
            
            right_to_position_of_Z = probable_position_of_Z + 1
            if right_to_position_of_Z < len(modified_substring) and right_to_position_of_Z > 0:
                character_right_to_position_of_Z = modified_substring[right_to_position_of_Z]
                while character_right_to_position_of_Z == "्":
                    probable_position_of_Z = right_to_position_of_Z + 1
                    if probable_position_of_Z >= len(modified_substring): break
                    character_at_probable_position_of_Z = modified_substring[probable_position_of_Z]
                    
                    right_to_position_of_Z = probable_position_of_Z + 1
                    if right_to_position_of_Z >= len(modified_substring): break
                    character_right_to_position_of_Z = modified_substring[right_to_position_of_Z]
            
            string_to_be_replaced = modified_substring[position_of_half_R + 2 : probable_position_of_Z]
            # JS: modified_substring.replace("र्" + string_to_be_replaced, string_to_be_replaced + "Z");
            # Need to be careful to only replace this instance
            to_find = "र्" + string_to_be_replaced
            to_replace = string_to_be_replaced + "Z"
            modified_substring = modified_substring.replace(to_find, to_replace, 1)
            
            position_of_half_R = modified_substring.find("र्")

        modified_substring = modified_substring[:-2] # Remove padding

        # Array replacement
        for i in range(len(self.array_one_uni_to_kd)):
            modified_substring = modified_substring.replace(self.array_one_uni_to_kd[i], self.array_two_uni_to_kd[i])
            
        modified_substring = modified_substring.replace("Zksa", "ksZa")
        modified_substring = modified_substring.replace("~ Z", "Z~")
        modified_substring = modified_substring.replace("Zk", "kZ")
        modified_substring = modified_substring.replace("Zh", "Ê")
        
        return modified_substring
