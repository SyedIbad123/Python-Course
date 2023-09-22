# Program to print multiplication table upto 20 in different files..

for i in range(2, 21):
    with open(f"tables/multiplication table of{i}.txt",'w') as f:
        for j in range(1,11):
            f.write(f"{i}X{j} = {i*j}")
            if j!= 10:
                f.write("\n")