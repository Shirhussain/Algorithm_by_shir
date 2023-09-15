""" 
all construct:

def(abcdef, [ab, abc, cd, def, abcd, ef, c])


                                    abcdef
                        /ab         abc|     abcd\
                    cdef              def       ef 
            /cd     c|                def|      ef|
            ef      def                ''         ''
            ef|      def|
            ''         '' 
            
            
result = [
    [ab,cd,ef],
    [ab, c, def],
    [abc,def],
    [abcd,ef]
]          


def all_construct(purple, [purp, p, ur, le, purpl])


                                        purple
                                    /purp   p|  purpl\
                                le        urple       e
                                le|         ur|       []
                                ''          ple|     
                                [[]]          p| 
                                                le
                                                |le
                                                ''
                                                [[]]

"""
