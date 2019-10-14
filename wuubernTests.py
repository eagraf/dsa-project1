import implementation as imp
import event as e

def main():
	#Constructor test
	wu1 = imp.Wuubern(3,0)
	wu2 = imp.Wuubern(3,1)
	wu1.printAll()
	wu2.printAll()

	#insert event at wu1
	wu1.insert(e.Event("res_pend", 1, 0))
	wu1.printAll()

	#insert 2 events at wu2
	wu2.insert(e.Event("res_pend", 1, 1))
	wu2.insert(e.Event("res_conf", 2, 1))
	wu2.printAll()

	#send of message from wu2 to wu1
	np, oMC = wu2.send(wu1.mID)
	wu1.receive(oMC, wu2.mID, np)

	print("HERE")
	wu1.printAll()
	wu2.printAll()

	wu3 = imp.Wuubern(3,2)
	np, oMC = wu1.send(wu3.mID)
	wu3.receive(oMC, wu1.mID, np)
	wu3.printAll()

	ev = e.Event("res_pend", 1, 0)
	print("EHERE")

	print(ev)










main()