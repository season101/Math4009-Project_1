from ciphertext import cipher;
import string;

#To count chars and its count

inputChars = []

for each in cipher:
    inputChars.append(chr(each+65))

#print(len(inputChars))
'''
for j in range(65,91):
    print(str(chr(j))+" : "+str(inputChars.count(chr(j))))
'''

inputChars = str(inputChars)
#print(inputChars)

#only on first loop -> output = inputChars.translate(str.maketrans('', '', string.punctuation)).replace(" ","")
output = "THZXHDBHTTHZXTGETNVTGXRKXVTNHBWGXTGXDNTNVBHZQXDNBTGXONBYTHVKFFXDTGXVQNBIVEBYEDDHWVHFHKTDEIXHKVFHDTKBXHDTHTEAXEDOVEIENBVTEVXEHFTDHKZQXVEBYZCHLLHVNBIXBYTGXOTHYNXTHVQXXLBHOHDXEBYZCEVQXXLTHVECWXXBYTGXGXEDTEPGXEBYTGXTGHKVEBYBETKDEQVGHPAVTGETFQXVGNVGXNDTHNTNVEPHBVKOOETNHBYXSHKTQCTHZXWNVGXYTHYNXTHVQXXLTHVQXXLLXDPGEBPXTHYDXEOECTGXDXNVTGXDKZFHDNBTGETVQXXLHFYXETGWGETYDXEOVOECPHOXWGXBWXGESXVGKFFQXYHFFTGNVOHDTEQPHNQOKVTINSXKVLEKVXTGXDXNVTGXDXVLXPTTGETOEAXVPEQEONTCHFVHQHBIQNFXFHDWGHWHKQYZXEDTGXWGNLVEBYVPHDBVHFTNOXTGXHLLDXVVHDVWDHBITGXLDHKBYOEBVPHBTKOXQCTGXLEBIVHFYXVLNVXYQHSXTGXQEWVYXQECTGXNBVHQXBPXHFHFFNPXEBYTGXVLKDBVTGETLETNXBTOXDNTHFTGXKBWHDTGCTEAXVWGXBGXGNOVXQFONIGTGNVRKNXTKVOEAXWNTGEZEDXZHYANBWGHWHKQYFEDYXQVZXEDTHIDKBTEBYVWXETKBYXDEWXEDCQNFXZKTTGETTGXYDXEYHFVHOXTGNBIEFTXDYXETGTGXKBYNVPHSXDXYPHKBTDCFDHOTGHVXZHKDBBHTDESXQXDDXTKDBVLKJJQXVTGXWNQQEBYOEAXVKVDETGXDZXEDTGHVXNQQVWXGESXTGEBFQCTHHTGXDVTGETWXABHWBHTHFTGKVPHBVPNXBPXYHXVOEAXPHWEDYVEBYTGKVTGXBETNSXGKXHFDXVHQKTNHBNVHSXDWNTGTGXLEQXPEVTHFTGHKIGTEBYXBTXDLDNVXVHFIDXETLNTPGEBYOHOXBTWNTGTGNVDXIEDYTGXNDPKDDXBTVTKDBEWDCEBYQHVXTGXBEOXHFEPTNHBVHFTCHKBHWTGXFENDHLGXQNEBCOLGNBTGCHDNVHBVZXEQQOCVNBVDXOXOZXDXY"
temp = output.replace("E","/")
temp = temp.replace("Z","E")
temp = temp.replace("/","Z")
print(temp)