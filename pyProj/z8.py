#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    ao = {'a', 'e', 'u', 'i', 'o', 'y'}
    s = input('Put your text: ')
    cnt = 0
    list = []
    for i in s:
        if i.lower() in ao:
            cnt += 1
            list.append(i)

    print(f"Number of vowels: {cnt} {list}")
