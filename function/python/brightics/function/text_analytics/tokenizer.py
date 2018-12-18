# coding: utf-8

import pandas as pd
import numpy as np
import re

def regexp_tokenizer(table, input_col, output_col_name='tokens', gaps=False, pattern="""\s+"""):
    out_table = table.copy()
    
    def _tokenizer(str_, gaps=gaps, pattern=pattern):
        if gaps is True:
            try:
                return re.findall(pattern, str_)
            except:
                return None
        else:
            try:
                return re.split(pattern, str_)
            except:
                return None
    
    out_table[output_col_name] = table[input_col].apply(lambda _: _tokenizer(_, gaps, pattern))
    return {'out_table': out_table}