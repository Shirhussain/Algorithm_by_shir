'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''

'''

this is the recursive tree visualization of the tree
https://www.mermaidchart.com/play?utm_source=mermaid_live_editor&utm_medium=toggle#pako:eNrVWM1u20YQfpWxg6CxITsWSceOALfgKkwiVJINkW4bJEFCU0uLMEUK_HHs_gC9NEABuwXqAAGCIOkh9x566S2HvomfII_Q2V2SWoqyHDfOwRaiiDOzO3_ffsvdH-adsE_nG_O7kT0agHXnUQD4d_06tAIv8WwfTJqkIyE1Lb1nPXw0__TD21c_w-Ki8Z3R3LZam12hWVwUZlZEaQMe1msKftSahh_1sVDdC22_Ac0BdfbAcyE-HA5pEnnO00fzj2Fp6UswulbvgbAV31wgfJ4co0_TMrag3gAvNvPBN6IwTBZy7x_evvgHmAQ2oIu53agvTCq8GAL8rxsGFE5fn0jqpu1jfKOIPgmjPo34zMs-dZMaH7kcebuDRJ5vy45sjIJGcQOY3QZ3qSygPTPNH4v8mnq7XZfzw0q36T71oQ5L0EMfX8TgDDy_H9EAnHA4siMvDgNhzEdnxXiTF0ORAy7cZz_KZTETGwt_h46SQQMUOW_ekXo5Bzj99c-pReLG6LaU4mxrVUy9vG_7zHZjQwzOn8tDOmmcwNDeo6BARJ00ir19Cg72Jl5eXi5qSXp6t3m_VM1MJEp09B5LJCSt7j3Y2mx1C4x27D0v2IXYG6Z-Ygc0TGPhoJFVGn-DLleWh59BgYcuY4Gbk4o5N8ntmaQMBEUvRT2Wk6kIUXSESBtngZ3IDpwB3AhTRB5iuU_jhTFCFH0SIqpewYiaY0SdhRH1XKirZairC7NRpV4IVeoFUKVOoEqdhaphGNFZ0GJlVPW6XFNJrkxtj8raQ-yYTRfTGNwwyitcrOjxhDj7ZJc0vV5uU0BrPPcZDdJmN4jNkNczoJItj7OJXw0gYTLgbuYk_enrXzCsnmFt97pg9baNxcWiOEJalEfOSanmpFypnEqtLRLNsno3Hs57JeaopJEGz7ygj_SCiJKUPDvQ4PT5H6COkbbZIa2ukVNB2bEyzbHyGR0XQuH4xcu8j6vIIJkSozO325ZZCoATIBYFF1WSRgHtiyCrFsrZFj0aIxkLMejdO-LHxqSZaCPDG1tyoizm9H6WkxsTKWF7LYNQwaReEExjUlJhUlJhUi1nUu3TmFQrM6l2DpNqF2JS7QJMqk0wqfbJTEpkJiWS_AwmJWcwqTaVSUmVScmVYlJSZVJSZVJypZiUTGNSMo1JySUzKZnmeBqTEuUzOi6EFSYlH8Ok5FwmJZfLpOQcJp18Jb3rBXg4xAPKDv5IvPyEkvNutdzsHfT_VFvl1ZYPK9_aeDLFl3dGC7wWKpEZ526rq7efZCWuYqHgdDk2clmx8eXCSZAf3nxccHPnR1ZSiPB--ysHzK2G0Geo0dmBu4oY3ApnAwY7fDl46eitLiepsxAjshHKapZCLvWAJ7mWJynUpfzGpLdwdgryfUBuFlesRE_72QGYd6_Ov1eK6O8bvU05avYsov39OUbLHqGz2TG6Fm5S4xsQbM5W27CMuVLorGLsOgRa5viyQ2ZSK0xwGblp4LA1lB1BYU3ebO0DiOWwZVLXsbE7440yorYzoH2IU8ehceymvn9Yst4NIy8ZDGGfRp7roWXCgssiO2Q1mFjmptenMMIDsi-2YScMEnqQCH2c7mTXRjiLmUSpg1WngNVCf0d_i8wJZWtVR7Y4_B4dFi74TVHP4HAXT_VCcZOFwP4ygSK-s8ebXFf8EFIV_2n4gfxNK7uyyov-FTwwzLlxhjToy3ZFKmytCJSINE5eieUjZMZ-6Ke8U6U8TEtvfs0SEbQw7XpKGAt9aSNXakpJqcpKtYaHxx8lgVbTStZa5Z2AvxLAvy9BOz_ZNt1FVZbpi-P8uZRb27hXXPlhEaIEtkIvSHJYnRyDESB24G6G4ULxBmklfy1kJcwVR--B8LduxEVh_A6N2ZKFb2w_Hb-KvIQm32FoRlFxrkF6FDuQmdBRLsQFep9GIXTCIQ2SM9NnsE4O_cJ9jA9UXGGC6_l-4xpVXcXt1-IkCvdo41r99tqtvpI9Lj3z-rgM1dGBPJrTghjsrNNbzu1isLq-TlVn5uDsPiAb77quSleK8e7qmrOyUjVXLmROLjY7-ejZS1tXXr51d5WuF4M0x3ZXV8oVUEYH8z_9BxzmSKE

or:https://www.mermaidchart.com/play?utm_source=mermaid_live_editor&utm_medium=toggle#pako:eNrNWM1u20YQfpWJAxSRITkWKVoKARfgKkwiVJIDSUkbxEXAUEuLCE0aJOXYaAvk0AZpkTZAEyBAUDRtUKDHHnrJrYe-iZ8gj9DZH5JLUf4R0EMMm97dmSVnvpn59uerNTea0jVzrdFo7IZuFHr-nrkbAgTOcTRPTfD8IzrdDbnYC6LH7syJU5hcR51k_nAvdg5mMIkpHafx3E3nMb2_u_bh7fO_oe_EexTGx_v7NI19lyvtrn3J3i1-JiPbRuXmZjEEcFX822U_-bBmFK189KrQKnWkUO-wZ6st_lhfCK5mM2Rjoc-VDA22mtBuQUdnv9jArqFx2Ye3r97BXSeY08SE5mZdM-p6p95q1w2tvtWst1v1ji4VX76AW9TfmyGCLQjoIQ0SKXn-DwwRcvYGA9IodQIuOPnlO7hNY4-6aXAMSQbbJQkZDacq4l0nCMap4z7iaL98A7wD1-lBOgMrdILjxE9KaI8nVvcz1O4zW6Bpgp_ksbnS3KwJTSHVTDiI6YMontL4CjqpGSWxrooRAL1Tg6-VIQSk1S7NaKkzECxDK89A8LaaNTUPSmIEtt0qz-joiHXpG4b6jWEU0jp71ODf19CBh05CwcWHiAIL0A8It_MIBnQ_io9NMCDhEHqxs19ovfoWJixEHHARMm8euqkfhVLn5M3vQNjbu-ztJn4roI4Hh07gTx2htzSCGLA0EdF7BvYRdedMmQ_7Seq7lehNxlz7p79gfZ0lShTvO6FL0QEWwsRcX5cGPXnHa63IP2Wc-5KnXyEY4ffjxD-khaOFsOReMaykHMJXjHej_QMn9hN03QRNV77u71MTdq6ENdjGf80sq_jLDhyXC2dC2KplIXjxFB0e0WQeoC_je4OBPRn1uuitCquAaDThEL15gjPsL-zunUlvZygEGToMGRPui-LN6xd_saFUMfvFBnYNTYZhaTnDzcgJTOjOKELhe0XdonXQaHwK9nAyuifC_CNaNZ7YtxeLL46itJbZhyn3HtgIosDiVJRmIfETCPEfS2-kjZeKmAVPLQOmvhFQL63zmRsxc0F9322HpXtKYwwV09vm38R6xwlMN-_n2cgd4q51rX6_KVz7NXNNKxdh9q6sVXazlECa6gaD02S0f_L9b7mf9cWBpTO2t7laSUpirJSZH-4h34LL05OySkwxGZKNjY3cOe4Sd46MrGH3lnAPGXt9vW_ftfvQlILe8GbmCsMcrIrfSIrSb2zVFFVSUUWylKrYKpCWJuRYa9YC2Pp5Xz0dbb2KHS6aiB0-z8AuEPwvIINPhFlk0azzPFzJLFzB0Sx8XtSsIpKapYRSoqfEEsWnBLNZcQAXLOkAttRoWtWMx5VM6mJrMZzSJmaebi1WT-vcL58OXasKHW5lEDp8lqHrs_VJQBZTx53RaSmeuqVVzDrPyZXMwv0UmoXPi5lVxBMBEwG1xnbLqtQmEzMR6o7tsRrRys4AxNbg5OnPuAu9Y6-qma1GbAROnv0pGttCI4-3sJJbPLInebT_YMuZPbkzGop4s0n5apY5qimOalVHtY_PUa1wVFviqFZxVGAiqmFnQHpDW5boq9dZ4hlIcFIGWc2WUi2rC0nqbM9hKuYXOpikZ-mc6WehxvboaJpYOJAqG8iWvfGSTYn0Tit7J9HPuhlgGa8reDFml3CpBeKl2aoFhzT2PZ9OFfnnjp8yQsSdoVi8M-UKLxKVF0mFF8kpvEiq7ITbckkD2CqtclXKwP261MVWhRdJwYukwovnfnklAsIzHRIQPlfjRVLhxXOdXMksPG2iWfhcmReJwoukyovk4-NFUvAiWcKL5BReJAovkiovko-PF0nBi2QJL5LlvEjKvEgWeZFUeJFUeZEdmc_jRUzS_50XW-0GbtfO4EVS5kVS5kWS8yKp8iJZwosjleuWESOJ0lm-3efuBnjkuaTaJNn4Rm9o9R9IS4rjNgd9yxRiaajFzpan87O8F6kiWjJWXpVUtdgxD7e3wTSmIcgrGOX0e9EQqR6SqodCWBpSlATmRQw4Cu0MBSEtAVBUTg2pKp3HIZ1WXFNPvplaUtESXOnNg-AY5uHjaI6n_MwZ1Tpu7i17tMPN5FcFrAeDnQEeVKEBfWt00-ZXjXDXHvVu9Ozrl0pGs9zt8pQ4Ah4TTFzl9q1QFHcncX5R4pYvSrjOwDmS10jT0rWISMP8DiojcnZblPrqddN7sHDxbBp4wJ-inrxFolPMGNelScIRyZFI0uOAivsN8Hwkr8tU9zRvWk_SOHpEzcvNa-2tqSa7jcf-FG3SD47U2dk2Vcz3PE-nm_l8z2i7m5tVde2i6sVmR07QqeEZ-YRrrtZ-WH0_Wc0csrI55KLmlGtDYtzxDNrJJ7VcxzM2yxhrZYx5SorJboduudfyyXqnQ3V3SYDWvvkPWf9o_w

or fib: call stack: https://www.mermaidchart.com/play?utm_source=mermaid_live_editor&utm_medium=toggle#pako:eNqtWN1u48YVfpWxAwSuE--SM6SiqEgKiqazBmzJleSiQd0YFDW0iJVIhaSyNoIAuUiDosgPkF0gwCJomiD3vehN7vou-wLJI-TMkEPOj-RogwjrFXnmnDPffN85I3I-3I-yGd3v7R8dHV2lUZbGyU3vKkVoEd5l67KH4uSWzq5SPhwvsifRPMxLNDkGn2I9vcnD1RydJNMxfX9N04j-7Wr_52-ffc9MWRpGUYLEyNX-31ne6jMO_gyeJwfWH9BbyK7sJwc2v0NI3OPq_jX4ewthYSXMimsrEVaHWQlYMXy7wuoyqwtWAt9dYe0waxesLstfp_j526f_RBdhWdI87aEgjOYoXS-nNEdJAUtdoixGq5x-kGTrApVPsno9NJ3JVPjhYjHJacXDZ__j94gZ0LjM11G5zlUiJqMgAN84mQKq1iw-D6uvK_ZRBlkALK65dtTgh02Yft-4VVH1BXAqfeE22UMpTXttXlUBSg704MEDsLH_pT9B9lffoUFWJhHtobOsLBi7OV3RsKQzxmYJlBV7wvnZJyJ1uAKfvAA9y2RJi8rhxfPvxJxi3K3HN4o0LsOy4Ao9_Re6oHmc5csQShR5abi4K5JCkegiGJ1w5y_-iw4Pg1sarcskS6ssvcPDGsPH36MRLdYL3jPTqsZEbbHBSVaGC14PRQ9htx3ohwUFe0HBbndE9bOR8_AWHdNVOe-hjpQIFtZDwwP8XsrmGB50hPhsdLwKIz4sBsXY8__89OOXsIDTlMZxEiXQk3fIW9C8bNYQ3K6ylKZlAkAZfWi2pqjMqkFZnVWeTRd02QoEah4ejrMFZwbyoeO7NFwmEbrIM-B8uUzSG0ULtgdMvNGEE_v8Y0bsXwP_cnI6HFQDApOfLVeQNb0RtFbmd7Jw0YNdJp2hTjmXtpuqZ2EudHT0NgoGk9G7ldKfM4ST4ALZIpOYAurrR5QCWx3p3p_T6DHwjl5dlH8EJf-EBkNp-HxdlCji2GhPdONrSityPyiS6LEQ0W7qiuPiCPsjb-A_sqv94v-A8Sz4S3AGe1s1cDp4R8A8Dx8DDWzrQRGvopogtsN4AoNk6_cEHDFrPRef1_fOzq7dipp_C2pwk8fgxjW5cXfmxhHckK3cYCbZqxUsx9NxNWsxcDnooJ5qhsKbMEn35Ckmc9i84V85pwhDrdRgGH8ykBBqvcoS8tYOCzSlsCtQacPaBLhmm1MpqYk9XU7smXqe5NmyZluR0u4pZVQZcU_wp4oJiRs1nb5GG2lzmbyZejo760mEnnirnkTSk3gGsGY9BjByr6AmFiyw2PdikaRy-pJWwJEuFpjuUcuR1eopVd1asK4Ty9kIRXShHM8OtxNiKkV2VmoHdhxJKeyZyKYik4EMv6RUtgBj3QtGkorIUjGWdK2Y7R6xiCkWNsSydbF40kYtrKvlwrC9nRRTLryzXDsw5FZy9b1xcG177YMJMwDgcSAyGchs6f7FN_-AmFEwuRwNkA2uCu1Ypp0vV-edG-8hHpvE2wbxlk58lZVPzZfX_63Lq4m3W-LfDcZ7961_C9sdiW1rO9uWCccy4Vi_C5yasIogThbEgWTXlUhPf4BMdS3lFF440kIRuF6KHGipgdbmQDFL1RnD8_7pIBDN8ezrOlZ9ZVMWoqwRm4ktLXFdLc19g5j0r7GKGLeIsb5U25MDd-NIzKIgItpS1ffQ7UslZmJbS6wulbRLdfrXREVMWsTEaFtP3S2nENremJvcVGo1f9dW27BzNA3S37VBtm4_NZi2Oj0umbjUqrgv-1mtn6XWlqcXrfc7Fa2nF62nFa0nK7lb0QrZlcSOVnvqacd2xK6ZGGuJVcROS6l77aiAnRawq5ce8ZRnKtxUHlwbj0JY-nH12x_XmpQjRPIZf_9U1nX_j6X0m3isFmHj--LTrzb80vkS7gpNc63hbnz5LMGvztJ0hb_J1TIB1Ynbmvbb2veN2vdlP6v1s7R8x-321_YSkXtJTKCWsr-hR4wG8PUG8LUG8OXZcTs7VrdET99rvV_Za7VobUPV2pB4UlHvtp_WDaCkdVVM6tni9h7sGmnV3nZVsG6DtSPez39oZxRYu3ohO9Uax4-Go4l_OeG9y87F4Jm1NrEZLi4nHjtjUdCKl2LxKJ_M2BkQe0e-01-Scxqt8yL5gCJ2QIeK5kyz9ZMPwfg2JZ8cHNgELeG9GsXrNOKv2vwoo30ObPFLNOy2D9WU8biT04F3dl1T2rYfNzO-_MuzzTxwUbsmOUxppJn1Y2QViGMCqZ-RZRN3ehSMhhzkl58CSHaHzofnwWACe-HJaX848Hz_lMt3FkyCPaPUjPPG6uyDHziqRLcnj9WeGt6Chuz5cqYcM_JBfi4ZsXNJNE9KfjYpnbnWWs_W6SxMS_n0BCY5D9O7PY0tLFWYa2SqW7HxIBs95CrFygkvgnXcLWh1dgi-8IrxCiUxjmevQ5Fmj2nvFfvNNzozXN8ePUlmsGCyupWjxQNjFR_HMaFWEx-7b0SWZbr3X8rderns1s7Zpc4REXRKaRvhOIR05Ai1EGvOurFLu02QE4Wxa6mcYZUzXq5VcNSlnejNJph0u5REGwjf_-gXcSXwPg

Example:

                    1
                    
            2                 2
            
        3      4          4       3
        
           5      6     6            5
        
Output: false

Example 2:
                    1

            2                 2

        3      4          4       3

             5   6      6   5         

Output: true

Example 3:          []

Output: true

Example 4:
                    1
Output: true

'''
'''
Constraints: Between 0 and 1000 nodes.

The input tree can be empty.
'''
'''
Diagram:

                    1

            2                 2

        3      4          4       5

           5      6     6            5



[1]
[2, 2]
[3, 4, 4, 5] false

                    1

            2                 2

        3      4          4       3

           5      6     6            5

queue: 3L, 4L, 4R, 3R

[1]
[2, 2]
[3, 4, 4, 3]
[null, 5, null, 6, 6, null, null, 5] false


                    1

            2                 2

        3      N            N       3

     5    N                       N   5
'''
'''
Pseudocode

while there are levels
   Create an array for each level, including nulls
   Return false if not palindrome
return True


create queue
enqueue root
while queue is not empty
   # Create an array for each level, including nulls
   if queue (treated as an array) is not a palindrome, return false
   for each element currently in queue
      dequeue the element
      if element is not null, add children (with nulls) to queue
return True

def helper(left, right):
   if left and right are null
      return true
   if left or right is null
      return false
   if left.val != right.val
      return false
   return helper(left.left, right.right) and helper(left.right, right.left)
      

def driver(node):
   if node is null
      return true
   return helper(node.left, node.right)
   
   
                   1

           2L                 2R

       3L      4L         4R       3R

          5L      6     6             5R

node:1

helper(2L, 2R) --> False
left: 2L
right: 2R

helper(3L, 3R) [& helper(4L, 4R)] --> False

helper(3L, 3R) --> False
left: 3L
Right: 3R

helper(null, 5R) [& helper(5L, null)] --> False

helper(null, 5R) --> False




      
'''

'''

'''
'''
symmetric3(root):
  [null, 3L, null, 2L, 5, 4L, 6, 1, 6, 4R, ...]


'''


def symmetric3(root):
    if root is None:
        return True
    return pre_order(root.left, root.right)

def pre_order(left, right):
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False 
    
    if left.val != right.val:
        return False 
    
    return pre_order(left.left, right.right) and pre_order(left.right, right.left)

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(symmetric3(root))