# 05 Bytes

print("bytes(4):", bytes(4))

smileyBytes = bytes("🙄", "utf-8")
print("smileyBytes       :", smileyBytes)
print("smileyBytes decode:", smileyBytes.decode("utf-8"))

smileyBytes = bytearray("🙄", "utf-8")
print("smileyBytes array :", smileyBytes)

smileyBytes[3] = int("85", 16)
print("modify position 3 of smileyBytes")
print("smileyBytes decode:", smileyBytes.decode("utf-8"))
