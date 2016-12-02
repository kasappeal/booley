# -*- coding: utf-8 -*-


def flatten(L):
    ret = []
    for i in L:
        if isinstance(i, list):
            ret.extend(flatten(i))
        else:
            ret.append(i)
    return ret