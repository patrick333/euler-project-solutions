//Quadratic primes



public static int N(int a, int b, int n)
        {
            return n * n + a * n + b;
        }

        static void Main(string[] args)
        {
            int maxCount = 0;
            int A = 0;
            int B = 0;
            for (int a = -999; a <= 999; a++)
            {
                for (int b = 2; b <= 999; b++)
                {
                    //Console.WriteLine("a={0}, b={1}", a,b);
                    int count = 0;
                    for (int n = 0; ; n++)
                    {
                        int result = N(a, b, n);
                        if (result < 2)
                            break;

                        if (!Helper.isPrime(result))
                        {
                            if (count > maxCount)
                            {
                                maxCount = count;
                                A = a;
                                B = b;
                                //Console.WriteLine("count={0}, A={1}, B={2} when a={3}, b={4}, n={5}", count, A, B, a, b, n);
                            }
                            
                            break;
                        }
                        else //is a prime
                        {
                            count++;
                        }
                    }


                }//end of b
            }

            Console.WriteLine("A and B are {0} and {1}. The product is {2} for count={3}", A, B, A*B, maxCount);
            Console.ReadKey();
        }//end of Main()