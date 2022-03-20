def phoneNumberMnemonics(phoneNumber):
    # Write your code here.
    lst = []
    op = ""
    helper(phoneNumber, op, lst, )
    print(len(lst))
    return lst

keyAssociation={
		1: (1,),
		2: ("a","b","c"),
		3: ("d","e""f"),
		4: ("g","h","i"),
		5: ("j","k","l"),
		6: ("m","n","o"),
		7: ("p","q","r","s"),
		8: ("t","u","v"),
		9: ("w","x","y","z"),
		0: (0,)
	}
def helper(inp, op, lst):
	if not inp:
		lst.append(op)
		return
	print(keyAssociation[int(inp[0])])
	for val in keyAssociation[int(inp[0])]:
		op1 = "{}{}".format(op,val)
		helper(inp[1:], op1, lst)
	
	return


if __name__ == "__main__":
    phoneNumber="1905"
    print(phoneNumberMnemonics(phoneNumber))