#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from chessNotation import solution


class TestBase(unittest.TestCase):
    # @unittest.skip
    def test_case1(self):
        case = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR"
        expected = "RP4pr/NP4pn/BP4pb/QP4pq/K2P2pk/BP4pb/NP4pn/RP4pr"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case2(self):
        case = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
        expected = "RP4pr/NP4pn/BP4pb/QP4pq/KP4pk/BP4pb/NP4pn/RP4pr"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case3(self):
        case = "2kr3r/pp1nbppp/3p1n2/q1pPp1B1/4P1b1/2N2N2/PPP1BPPP/R2Q2RK"
        expected = "RP2q1p1/1P4p1/1PN1p2k/Q3Ppnr/1B1Pp1b1/1PN2np1/RP1bB1p1/KP4pr"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case4(self):
        case = "rNBNn1nR/RN2BNbp/BN3Br1/B1BBp1Kb/npRrBrpb/QB2k1QR/q1nrn2r/bbNBN3"
        expected = "bqQnBBRr/b1Bp1NNN/Nn1RB2B/Br1rB2N/NnkBp1Bn/3r1BN1/2QpKrbn/1rRbb1pR"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case5(self):
        case = "bN2nrp1/n1nQn1n1/p1bPRPrb/n2Q1Nrb/Bn1nBRnB/Q1n1N1b1/qk1n1R2/Q1n2n1Q"
        expected = "QqQBnpnb/1k1n3N/n1n2bn1/1n1nQPQ1/2NB1Rnn/nR1RNP1r/2bnrrnp/Q2Bbb2"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case6(self):
        case = "PkpRnNnB/bqBkbb1k/K2n4/N1BbkP2/QB2kNQk/q1nRNnBB/pbp1RbN1/P1PR1Np1"
        expected = "PpqQNKbP/1b1B2qk/Ppn1B1Bp/R1R1bnkR/1RNkk1bn/NbnNP1bN/pNBQ3n/2Bk2kB"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case7(self):
        case = "N3rrB1/B4NR1/q1pNPb2/k1p1PQQK/nNb1bbr1/n2NP1K1/rb1bRn2/rp1B3p"
        expected = "rrnnkqBN/pb1N4/3bpp2/BbN2N2/1RPbPP1r/1n1bQbNr/2KrQ1RB/p3K3"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case8(self):
        case = "K1Rnrk11/n7/NKb1r1Qq/r1Q2b2/bKBrNBr1/BnpKKr1B/NB1RnNN1/r1RKQ1N1"
        expected = "rNBbrNnK/1BnK1K2/R1pBQb1R/KRKr3n/QnKN1r1r/1NrBb2k/NN1r1Q2/2B2q2"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case9(self):
        case = "p1rKBRkK/P2qqr1p/nbKnb12/RnrrBkbK/NPn1BN2/kb2B1BB/QQ1ppn2/r1Pn1nB1"
        expected = "rQkNRnPp/1QbPnb2/P2nrK1r/np2rnqK/1pBBBbqB/nn1Nk1rR/B1B1b2k/2B1K1pK"
        output = solution(case)
        self.assertEqual(output, expected)

    # @unittest.skip
    def test_case10(self):
        case = "k3KRBk/PNkqN12/pqNB1Qp1/N1nbrk1q/n2nK1Bp/BrRBN1Pk/K1pBKRRR/bP2R21"
        expected = (
            "bKBnNpPk/P1r2qN1/1pR1nNk1/1BBnbBq1/RKNKr1NK/1R2kQ1R/1RPB1p1B/1Rkpq2k"
        )
        output = solution(case)
        self.assertEqual(output, expected)
