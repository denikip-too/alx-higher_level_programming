#!/usr/bin/python3
"""solves the N queens problem"""
import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board = [['' for col in range(n)] for row in range(n)]
    return board
