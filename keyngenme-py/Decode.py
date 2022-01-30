import hashlib
import base64

bUsername_trial = b"MORTON"

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial

dynamicKey = ""

hexDigest = hashlib.sha256(bUsername_trial).hexdigest()

index = [4,5,3,6,2,7,1,8]

for i in index:
    dynamicKey = dynamicKey + hexDigest[i]

print(key_part_static1_trial + dynamicKey + key_part_static2_trial)
