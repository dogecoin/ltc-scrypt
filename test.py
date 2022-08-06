import ltc_scrypt

teststart = '000000203a297b4b7685170d7644b43e5a6056234cc2414edde454a87580e1967d14c1078c13ea916117b0608732f3f65c2e03b81322efc0a62bcee77d8a9371261970a58a5a715da80e031b02560ad8'

testbin = bytes.fromhex(teststart)
hash_bin_scrypt = ltc_scrypt.getPoWHash(testbin)
print("ltc_scrypt", hash_bin_scrypt.hex())
