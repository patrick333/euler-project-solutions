//Non-abundant sums


 //1. get the abandant numbers
 
    //int[] a=new int[];
    List<int> a = new List<int>();//a dynamic arry is needed!
    //a.Capacity = 28123; //not necessary
    for (int i = 1; i <= 28123; i++)
    {
        int sum = 0;
        for (int j = 2; j <= i / 2; j++)
        {
            if (i % j == 0)
                sum += j;
        }
        if (sum > i)
        {
            a.Add(i);
            //Console.Write(i+" ");
        }
    }

    //2. mark those who can be expressed of 2 abandant numbers.
    Console.WriteLine("Now step 2. ");
    bool[] numB = new bool[28123];//default: false. Need to remove: true.
    //var numVar = Enumerable.Range(1, 28123).ToArray();
    for (int ii = 0; ii <= a.Count - 1; ii++)
    {
        for (int jj = 0; jj <= a.Count - 1; jj++)
        {
            if (a[ii] + a[jj] <= 28123)
            {
                if (numB[a[ii] + a[jj] - 1] == false)
                {
                    numB[a[ii] + a[jj] - 1] = true;
                    //Console.WriteLine("Non-abundant sum: {0}", a[ii] + a[jj]);
                }
            }
        }
    }

    Console.WriteLine("Now step 3. ");
    int sumAllNonAbandants = 0;
    for (int i = 0; i <= 28123-1; i++)
    {
        if (numB[i] == false)
        {
            sumAllNonAbandants += i+1;
        }
    }

    Console.WriteLine("The sum is {0}", sumAllNonAbandants);
}//end of Main()
