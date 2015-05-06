//Amicable numbers


public static int d(int n)
        {
            int sum = 1;
            for (int i = 2; i <= n / 2; i++)
            {
                if (n % i == 0)
                    sum += i;
            }

            return sum;
        }

        static void Main(string[] args)
        {
            int sumA = 0;
            //in c++, bool b[]; in c#, bool[] b.    bool b[] is not legal!
            bool[] b=new bool[9999];//default will be false. 

            for (int i = 1; i <= 9999; i++)
            {
                int j = d(i);
                if (d(j) == i && i != j&& !b[i-1])
                {
                    b[i - 1] = true;
                    b[j - 1] = true;
                    sumA += i+j;                   
                    Console.Write("{0:d} and {1:d} \t", i, j);
                }
            }
            Console.WriteLine("The sum is {0:d4}", sumA);

        }//end of Main()