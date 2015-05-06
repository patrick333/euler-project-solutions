//Reciprocal cycles



//public static bool debug = false;
        public static bool debug = true;
        
        //public static int lengthR(int n)  //analysis on the divisor doesn't work.
        //{
        //    int r = 0;
        //    int d = 0;
        //    int Re = 0;
        //    bool[] D = new bool[10];//default: false.

        //    for (int j = 0; j <= 9; j++)
        //        D[j] = false;

        //    r = 1;
        //    Re = 0;

        //    if (debug) Console.Write("{0}\t", n);
        //    while (true)
        //    {
        //        r = r * 10;
        //        if (r >= n)
        //            break;
        //    }

        //    while (true)
        //    {               
        //        if (r % n == 0)
        //        {
        //            Re = 0;
        //            break;
        //        }
        //        else
        //        {
        //            d = r / n; if(debug) Console.Write("{0}={1}/{2} ", d, r,n);
        //            r = r % n;
        //            Re += 1;
        //            if(d==0){}
        //            else if (!D[d])
        //                D[d] = true;
        //            else
        //            {
        //                Re -= 1;
        //                break;
        //            }
        //        }//end of else

        //        r = r * 10;
        //    }

        //    if (debug) Console.WriteLine("The recurring length is {0}.", Re);
        //    return Re;
        //}

        public static int lengthR2(int n)  //analysis on the remainder
        {
            int[] RatP = new int[n];
            int p = 0;
            int r = 1;

            while (r != 0 &&RatP[r]==0)
            {
                RatP[r] = p; if (debug) Console.Write("RatP[{0}]={1} ", r, p);              
                r = r * 10;
                r=r%n;                  
                p++;
            }

            int Re = 0;
            if (r == 0)
                Re=0;
            else Re=p - RatP[r];

            if (debug) Console.WriteLine("Result for {0} is {1}", n, Re);
            return Re;
        }

        static void Main(string[] args)
        {
            int maxRe = 0;

            for (int i = 999; i >= 2; i--)
            {
                if (i <= maxRe)
                    break;

                int Re = lengthR2(i);
                if (Re > maxRe)
                    maxRe = Re;
            }
            //lengthR2(3);
            //lengthR2(4);
            //lengthR2(5);
            //lengthR2(7);

            //lengthR2(111);

            Console.WriteLine("The max recurring length is {0}. ", maxRe);
            Console.ReadKey();
        }//end of Main()