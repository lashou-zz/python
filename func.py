def count(num):
    c=0;
    while num>1:
        c+=num;
        num-=1;
    return c;

print(count(10));
