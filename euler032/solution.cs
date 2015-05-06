//Pandigital products


public static bool isPandigital(int a1, int b1, int n1)
        {
            int a = a1;
            int b = b1;
            int n = n1;
            bool[] isUsed=new bool[10];
            int d;
            while (a != 0)
            {
                d = a % 10;
                a = a / 10;
                if (isUsed[d] || d == 0)
                    return false;
                else
                    isUsed[d] = true;
            }

            while (b != 0)
            {
                d = b % 10;
                b = b / 10;
                if (isUsed[d] || d == 0)
                    return false;
                else
                    isUsed[d] = true;
            }

            while (n != 0)
            {
                d = n % 10;
                n = n / 10;                
                if (isUsed[d] || d == 0)
                    return false;
                else
                    isUsed[d] = true;
            }

            Console.Write("{0}*{1}={2} \t", a1,b1,n1);
            return true;
        }

        static void Main(string[] args)
        {
            int sum =0;

            bool[] hasCalculated = new bool[9999];
            for (int a = 1; a <= 9; a++)
            {
                for (int b = 1000; b <= 9999; b++)
                {
                    int product=a*b;
                    if (product > 9999)
                        break;

                    if (isPandigital(a, b, product) && hasCalculated[product] == false)
                    {
                        sum += product;
                        hasCalculated[product] = true;
                    }
                }
            }

            for (int a = 11; a <= 99; a++)
            {
                for (int b = 100; b <= 999; b++)
                {
                    int product = a * b;
                    if (product > 9999)
                        break;

                    if (isPandigital(a, b, product) && hasCalculated[product] == false)
                    {
                        sum += product;
                        hasCalculated[product] = true;
                    }
                }
            }

            Console.WriteLine("\nThe number of ways is {0}", sum);            
            Console.ReadKey();
        }//end of Main()
