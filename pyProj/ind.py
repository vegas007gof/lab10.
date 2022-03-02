#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    u = set("abcdefghijklmnopqrstuvwxyz")

    a = {"a", "b", "d", "i", "x"}
    b = {"d", "e", "h", "i", "n", "u"}
    c = {"e", "f", "m", "n"}
    d = {"a", "c", "h", "k", "r", "s", "w", "x"}

    bu = u.difference(b)
    x = (a.difference(c)).intersection(bu)
    print(f"x = {x}")

    ba = u.difference(a)
    y = (ba.intersection(d)).union(c.difference(b))
    print(f"y = {y}")
    