//Digit fifth powers


//first, we need to find out how many digits should the number have: 2->6. 
        static void Main(string[] args)
        {
            int sum = 0;
            int x, a,b,c,d,e;
            for (int n = 2; n <= 355000; n++)
            {
                x = n / 100000;
                a = (n / 10000)%10;
                b = (n / 1000) % 10;
                c = (n / 100) % 10;
                d= (n / 10) % 10;
                e = n % 10;

                if (n == (int)(Math.Pow(x, 5)+Math.Pow(a, 5) + Math.Pow(b, 5) + Math.Pow(c, 5) + Math.Pow(d, 5) + Math.Pow(e, 5)))
                {
                    sum +=n;
                    Console.Write("{0}={1}, {2}, {3}, {4}, {5}, {6} \t", n, x, a, b, c, d, e);
                }
            }

            Console.WriteLine("\nThe sum is {0}", sum);            
            Console.ReadKey();
        }//end of Main()
