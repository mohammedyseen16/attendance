def cntgloves(arr, n) :

    count = 0;

    arr.sort();
    i = 0;
    while i < (n-1) :

        if (arr[i] == arr[i + 1]) :
            count += 1;

            i = i + 2;

        else :
            i += 1                                   

    return count;


if __name__ == "__main__" :
 a=int(input(''))
 arr = [int(i) for i in input().split()]
 n = len(arr)

 print(cntgloves(arr, n))


