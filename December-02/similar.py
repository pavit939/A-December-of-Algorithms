def check(tri1,tri2,ang1,ang2):
    if((tri1[0]/tri2[0])==(tri1[1]/tri2[1])==(tri1[2]/tri2[2])):
        print("Similar triangle by SSS")
    elif((tri1[0]/tri2[0])==(tri1[1]/tri2[1]) or
         (tri1[1]/tri2[1])==(tri1[2]/tri2[2]) or
         (tri1[0]/tri2[0])==(tri1[2]/tri2[2]))or (ang1[1]==ang2[1]):
        print("Similar triangle by SAS")
    elif((ang1[0]==ang2[0]) or (ang1[0]==ang2[1]) or (ang1[0]==ang2[2]) or
         (ang1[1] == ang2[0]) or (ang1[1] == ang2[1]) or (ang1[1] == ang2[2]) or
         (ang1[2] == ang2[0]) or (ang1[2] == ang2[1]) or (ang1[2] == ang2[2])) or (tri1[1]==tri2[1]) :
        print("Similar triangle by ASA")
def main():
    s1 = input("Enter the side for trianlge 1:").split()
    s2 = input("Enter the side for triangle 2:").split()
    a1 = input("Enter the angle for triangle 1:").split()
    a2 = input("Enter the angle for triangle 2:").split()
    for i in range(0,3):
        side1 = list(map(int,s1))
    for i in range(0, 3):
        side2 = list(map(int,s2))
    for i in range(0,3):
        angle1 = list(map(int,a1))
    for i in range(0,3):
        angle2 = list(map(int,a2))
    check(side1,side2,angle1,angle2)
if __name__ == '__main__':
      main()
