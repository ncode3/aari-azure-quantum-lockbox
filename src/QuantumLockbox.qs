namespace QuantumLockbox {
    operation RandomBit() : Result {
        use q = Qubit();
        H(q);
        let bit = M(q);
        Reset(q);
        bit
    }

    operation RandomKey8() : Result[] {
        let b0 = RandomBit();
        let b1 = RandomBit();
        let b2 = RandomBit();
        let b3 = RandomBit();
        let b4 = RandomBit();
        let b5 = RandomBit();
        let b6 = RandomBit();
        let b7 = RandomBit();

        [b0, b1, b2, b3, b4, b5, b6, b7]
    }

    operation RandomKey16() : Result[] {
        let b0 = RandomBit();
        let b1 = RandomBit();
        let b2 = RandomBit();
        let b3 = RandomBit();
        let b4 = RandomBit();
        let b5 = RandomBit();
        let b6 = RandomBit();
        let b7 = RandomBit();
        let b8 = RandomBit();
        let b9 = RandomBit();
        let b10 = RandomBit();
        let b11 = RandomBit();
        let b12 = RandomBit();
        let b13 = RandomBit();
        let b14 = RandomBit();
        let b15 = RandomBit();

        [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15]
    }
}
