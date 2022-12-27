class Searching:
    def __init__(self,info):
        self.ls=info
    def InsertionSort(self,myl):
        for i in range(len(self.ls)):
            j=i-1
            while j>=0 and self.ls[j]>self.ls[i]:
                self.ls[i],self.ls[j]=self.ls[j],self.ls[i]
                i=i-1
                j=j-1
        return self.ls
    def LinearSearch(self):
        req=int(input("Enter the roll number you are concerned with :-> "))
        for i in range(len(self.ls)):
            if req==self.ls[i]:
                return (" "+str(req)," was present and at the position :-> "+str(i+1))
        return (" "+str(req)," was not present.")
    def SentinelSeaech(self):
        req=int(input("Enter the roll number you are concerned with :-> "))
        last=self.ls[len(self.ls)-1]
        self.ls[len(self.ls)-1]=req
        i=0
        while(self.ls[i]!=req):
            i+=1
        self.ls[len(self.ls)-1]=last
        if i<(len(self.ls)-1) or req==self.ls[len(self.ls)-1]:
            return (" "+str(req)," was present and at the position :-> "+str(i+1))
        else:
            return  (" "+str(req)," was not present.")
    def BinarySearch(self):
        req=int(input("Enter the roll number you are concerned with :-> "))
        temp=self.InsertionSort(self.ls)
        start=0
        end=len(self.ls)-1
        while start<=end:
            mid=(start+end)//2
            if temp[mid]==req:
                return (" "+str(req)," was present and at the position :-> "+str(mid+1))
            elif temp[mid]>req:
                end=mid
            else:
                start=mid+1
        return  (" "+str(req)," was not present.")
    def FibonacciSearch(self):
        req=int(input("Enter the roll number you are concerned with :-> "))
        temp=self.InsertionSort(self.ls)
        f0=0
        f1=1
        f2=1
        size=len(self.ls)
        while f2<=size :
            f0=f1
            f1=f2
            f2=f0+f1
        offset=-1
        while f2>1 :
            ind=min(offset+f0,size-1)
            if temp[ind]>req:
                f2=f1
                f1=f0
                f0=f2-f1
                offset=ind
            elif temp[ind]<req:
                f2=f0
                f1=f1-f0
                f0=f2-f1
            else:
                return (" "+str(req)," was present and at the position :-> "+str(ind+1))
        if f1 and temp[size-1]==req:
            return (" "+str(req)," was present and at the position :-> "+str(size))
        return  (" "+str(req)," was not present.")
while True:
    chc=int(input("ENTER WHAT YOU WANT TO DO \n 1.TO GIVE THE INFO OF ROLL NUMBERS OF STUDENTS WHO ATTENDED \n 2.EXIT"))
    if chc==2:
        break
    elif chc==1:
        info=Searching(list(map(int,input("Enter the Roll Numbers of Students :-> ").split())))
        while True:
            chc=int(input("Enter your choice :-> \n 1.Linear Search \n 2.Sentinel Search \n 3.Binary Search \n 4.Fibonacci search \n 5.Exit"))
            if chc==5:
                break
            elif chc==1:
                print(info.LinearSearch())
            elif chc==2:
                print(info.SentinelSeaech())
            elif chc==3:
                print(info.BinarySearch())
            elif chc==4:
                print(info.FibonacciSearch())


        



        



            


            