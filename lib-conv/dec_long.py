#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: Wellington Silva a.k.a. Well
Date: July 2017
Name: dec_long.py
Purpose: Class Encode/Decode with Decimal Long.
Description: Script Based on script CAL9000 by Chris Loomis from OWASP Project, posted at:
                     <https://www.owasp.org/index.php/Category:OWASP_CAL9000_Project>
Version: 1.0B
Licence: GPLv3
 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
 
 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 
 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses/>.

Other itens: Copyright (c) 2017, How2Security All rights reserved.
'''

class CodingDecLong:
    def __init__(self, mystring):
        self.mystring = mystring
	# Encode ASCII Decimal Long
        self.dec_long = { '&#00' : '', '&#32' : ' ', '&#33' : '!', '&#34' : '"', '&#35' : '#', '&#36' : '$', '&#37' : '%', '&#38' : '&', '&#39' : "'", '&#40' : '(', '&#41' : ')', '&#42' : '*', '&#43' : '+', '&#44' : ',', '&#45' : '-', '&#46' : '.', '&#47' : '/', '&#48' : '0', '&#49' : '1', '&#50' : '2', '&#51' : '3', '&#52' : '4', '&#53' : '5', '&#54' : '6', '&#55' : '7', '&#56' : '8', '&#57' : '9', '&#58' : ':', '&#59' : ';', '&#60' : '<', '&#61' : '=', '&#62' : '>', '&#63' : '?', '&#64' : '@', '&#65' : 'A', '&#66' : 'B', '&#67' : 'C', '&#68' : 'D', '&#69' : 'E', '&#70' : 'F', '&#71' : 'G', '&#72' : 'H', '&#73' : 'I', '&#74' : 'J', '&#75' : 'K', '&#76' : 'L', '&#77' : 'M', '&#78' : 'N', '&#79' : 'O', '&#80' : 'P', '&#81' : 'Q', '&#82' : 'R', '&#83' : 'S', '&#84' : 'T', '&#85' : 'U', '&#86' : 'V', '&#87' : 'W', '&#88' : 'X', '&#89' : 'Y', '&#90' : 'Z', '&#91' : '[', '&#92' : '\\', '&#93' : '[', '&#94' : '^', '&#95' : '_', '&#96' : '`', '&#97' : 'a', '&#98' : 'b', '&#99' : 'c', '&#100' : 'd', '&#101' : 'e', '&#102' : 'f', '&#103' : 'g', '&#104' : 'h', '&#105' : 'i', '&#106' : 'j', '&#107' : 'k', '&#108' : 'l', '&#109' : 'm', '&#110' : 'n', '&#111' : 'o', '&#112' : 'p', '&#113' : 'q', '&#114' : 'r', '&#115' : 's', '&#116' : 't', '&#117' : 'u', '&#118' : 'v', '&#119' : 'w', '&#120' : 'x', '&#121' : 'y', '&#122' : 'z', '&#123' : '{', '&#124' : '|', '&#125' : '}', '&#126' : '~', '&#160' : ' ', '&#161' : '¡', '&#162' : '¢', '&#163' : '£', '&#164' : '¤', '&#165' : '¥', '&#166' : '¦', '&#167' : '§', '&#168' : '¨', '&#169' : '©', '&#170' : 'ª', '&#171' : '«', '&#172' : '¬', '&#173' : '­', '&#174' : '®', '&#175' : '¯', '&#176' : '°', '&#177' : '±', '&#178' : '²', '&#179' : '³', '&#180' : '´', '&#181' : 'µ', '&#182' : '¶', '&#183' : '·', '&#184' : '¸', '&#185' : '¹', '&#186' : 'º', '&#187' : '»', '&#188' : '¼', '&#189' : '½', '&#190' : '¾', '&#191' : '¿', '&#192' : 'À', '&#193' : 'Á', '&#194' : 'Â', '&#195' : 'Ã', '&#196' : 'Ä', '&#197' : 'Å', '&#198' : 'Æ', '&#199' : 'Ç', '&#200' : 'È', '&#201' : 'É', '&#202' : 'Ê', '&#203' : 'Ë', '&#204' : 'Ì', '&#205' : 'Í', '&#206' : 'Î', '&#207' : 'Ï', '&#208' : 'Ð', '&#209' : 'Ñ', '&#210' : 'Ò', '&#211' : 'Ó', '&#212' : 'Ô', '&#213' : 'Õ', '&#214' : 'Ö', '&#215' : '×', '&#216' : 'Ø', '&#217' : 'Ù', '&#218' : 'Ú', '&#219' : 'Û', '&#220' : 'Ü', '&#221' : 'Ý', '&#222' : 'Þ', '&#223' : 'ß', '&#224' : 'à', '&#225' : 'á', '&#226' : 'â', '&#227' : 'ã', '&#228' : 'ä', '&#229' : 'å', '&#230' : 'æ', '&#231' : 'ç', '&#232' : 'è', '&#233' : 'é', '&#234' : 'ê', '&#235' : 'ë', '&#236' : 'ì', '&#237' : 'í', '&#238' : 'î', '&#239' : 'ï', '&#240' : 'ð', '&#241' : 'ñ', '&#242' : 'ò', '&#243' : 'ó', '&#244' : 'ô', '&#245' : 'õ', '&#246' : 'ö', '&#247' : '÷', '&#248' : 'ø', '&#249' : 'ù', '&#250' : 'ú', '&#251' : 'û', '&#252' : 'ü', '&#253' : 'ý', '&#254' : 'þ', '&#255' : 'ÿ' }

    def decoded(self):
        answer = self.mystring
        for i in self.mystring:
            for i, j in self.dec_long.iteritems():
                answer = answer.replace(i, j)
        return answer

    def encoded(self):
        answer = ''
        for i in self.mystring:
            for k in self.dec_long:
                if i in self.dec_long[k]:
                    answer += k
                    break
            else:
                answer += i
        return answer
