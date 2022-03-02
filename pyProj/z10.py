#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    s1 = input("Put first text: ")
    s1 = s1.replace(' ', '')
    a = {i for i in s1.lower()}
    s2 = input("Put second text: ")
    s2 = s2.replace(' ', '')
    b = {i for i in s2.lower()}
    c = a.intersection(b)
    print(f"Intersection: {c}")
