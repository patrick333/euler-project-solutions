//Factorial digit sum


  public static BigInteger factorial(int n)
        {
            BigInteger result = new BigInteger("1", 10);

            BigInteger temp;
            for (int i = n; i >=1; i--)
            {
                //Console.WriteLine(i.ToString());
                temp = new BigInteger((long)i);
                result = result * i;
            }

            return result;
        }

        public static int sumD(BigInteger b)
        {
            int sum = 0;
            BigInteger ten = new BigInteger((long)10);
            BigInteger zero = new BigInteger((long)0);
            while (b != zero)
            {
                sum = sum + (int)((b % ten).LongValue());
                b = b / ten;                
            }
            return sum;
        }

        static void Main(string[] args)
        {
            //Console.WriteLine(factorial(4));


            //Console.WriteLine(sumD(new BigInteger((long)59)));
            Console.WriteLine(sumD(factorial(100)));

        }//end of Main() 