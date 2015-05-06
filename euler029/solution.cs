//Distinct powers


//from http://www.mathblog.dk/project-euler-29-distinct-terms-sequence-ab/. In fact, this is not precise, the solution. 
        //An analysis in mathmatics should be at least needed to say why double precision is OK. 
        public static void BruteForce()
        {
            Stopwatch clock = Stopwatch.StartNew();

            List<double> set = new List<double>();//或用SortedSet<double>

            for (int a = 2; a <= 100; a++)
            {
                for (int b = 2; b <= 100; b++)
                {
                    double result = Math.Pow(a, b);
                    //Console.Write("{0} ", result);
                    if (!set.Contains(result))
                    {
                        set.Add(result);
                    }
                }
            }

            clock.Stop();
            Console.WriteLine("The number of distinct terms are {0}", set.Count);
            Console.WriteLine("Solution took {0} ms", clock.ElapsedMilliseconds);
        }

        public static void forceWithBigInteger()
        {
            Stopwatch clock = Stopwatch.StartNew();
            List<BigInteger> set = new List<BigInteger>();

            BigInteger result;
            BigInteger temp;
            for (int a = 2; a <= 100; a++)
            {
                for (int b = 2; b <= 100; b++)
                {
                    result = new BigInteger((long)0);
                    temp=new BigInteger((long)1);
                    for (int i = 1; i <= b; i++)
                    {
                        temp *= new BigInteger(a);
                    }
                    result += temp;                    

                    if (!set.Contains(result))
                    {
                        set.Add(result);
                    }
                }
            }

            Console.WriteLine("The number of distinct terms are {0}", set.Count);
            Console.WriteLine("Solution took {0} ms", clock.ElapsedMilliseconds);
        }

        static void Main(string[] args)
        {
            BruteForce();
            forceWithBigInteger();
            
            Console.ReadKey();
        }//end of Main()