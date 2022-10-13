#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 19:20:56 2022

@author: josephbriggs
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # print('[][][][][]')

        max_window = len(s)+1
        # print(s)
        if max_window == 1:
            # print(s)
            return(s)

        for start,i in zip(range(0,max_window),range(max_window,0,-1)):
            for j in range(0,start):
                
                s_forward = s[j:j+i+1]
                s_backward = s_forward[::-1]
                # print('---')
                # print(s_forward)
                # print(s_backward)
                # print('---')
                if s_forward==s_backward:
                    return s_forward

if __name__ == "__main__":
    
    sln = Solution()

    
    assert(sln.longestPalindrome("babad")=="bab")
    assert(sln.longestPalindrome("cbbd")=="bb")
    assert(sln.longestPalindrome("a")=="a")
    assert(sln.longestPalindrome("ac")=="c")
    assert(sln.longestPalindrome("bb")=="bb")
    assert(sln.longestPalindrome("eabcb") == "bcb")
    assert(sln.longestPalindrome("qkajbumzdzkiplmbcpnhbzweoevrvbptpozhtrfntszvnwbdahvkykmezrwruhvvslngruvwqebudtfxgpbmwefczwrecpqjegxkqknpobzkemmtruidulnxgntjxcmxtwmlxhzmbqfqylwvzjyojhfawwuupiipvxjiyxkqvsxbhgzzegfkdihizvjoxzrmeorikzsdyphbujaqmykrfblneqmwwxsoonzsgvligqxrrumspylfvquklbanjhkudlprwoycpxdsueokruoofyubirbhbyfuvgllijywuqmkcsfjttbnmelrylivkefllepgxnoeummujbaoyvryukyoumvuxezegpwgmwsupjuaarvbtbfmisrifjadqjypmzipvjysgakvjhfeaqwpsqijvqibshctuabwqqsjwotjopahoaptmxkwerkjkmwiodgblhtnhykzjuaoluoyokroxuvqtkpggfanzabgjejdfsgybhxbscubdpufywbxgutheskuhixasnksoayjngvhfoxxclykfobrwxjwgefarzczvptlfrgrtrjcemaeihpukhbeoezgvrwxgyhpkkfvmfvquwtswkdwqqgrgasopladdnteulqofmjhewpghkibbrewnhdllfppctgkfkoedoiwqocnpvfviochrokrgrzthrvyhqfsrzyyvqwkhuzsrkfaympcdodkwaojnghzytkhf") == "piip")