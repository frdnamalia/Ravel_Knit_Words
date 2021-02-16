print("="*50)
print("---Ravelling & Knitting Words---\n")
print("by Fardhina Amalia")

print("="*50)
print("==Ravelling Words==")
def ravel(x):
    i=0
    jum=len(x)
    temp=''
    for j in range (jum+1):
        for i in range(j):
            temp+= x[i]
    temp+='' 
    return temp

print(ravel('Purwadhika'))
print(ravel('Digital'))
print(ravel('Coding'))
print(ravel('School'))

print("="*50)
print("==Knitting Words==")


# [1,1+2,1+2+3,1+2+3+4,1+2+3+4+5]
def knit(x):
    jum=len(x) #6
    baris=[]
    num=0
    hasil=''
    for i in range(jum):
        if num<jum: 
            num+=i
            baris.append(num)
        elif num==jum:
            break
    # print(baris)
    y=(len(baris)-1)
    x=list(x)
    final=jum-y
    hasil=x[final:]
    hasil="".join(hasil)
    return hasil

print(knit('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))
print(knit('DDiDigDigiDigitDigitaDigital'))
print(knit('CCoCodCodiCodinCoding'))
print(knit('SScSchSchoSchooSchool'))



