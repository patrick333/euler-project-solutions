//1000-digit Fibonacci number

static void Main(string[] args)
        {
            //BigInteger x=new BigInteger((long)1);
            //BigInteger y = new BigInteger((long)1);
            //BigInteger z = new BigInteger((long)0);
            ////for (int i = 3; i < 100; i++)
            //for (int i = 3; ; i++)
            //{
            //    z = x + y;  //overflow or underflow here!!!
            //    x = y;
            //    y = z;
            //    //Console.Write(z.dataLength + " ");//dataLength应是bytes的个数。
            //    //Console.Write(z.LongValue() + " ");
            //    Console.WriteLine("{0}:{1} ", i, z.ToString().Length);
            //    if ( z.ToString().Length>=1000 )
            //    {
            //        Console.WriteLine(i);
            //        break;
            //    }
            //}

            //length of nth fibonacci is n*log(g1)-0.5*log(5), where g1=1.61803399
            double a = Math.Log10(1.61803399);
            double b = 0.5 * Math.Log10(5);
            for (int i = 3; ; i++)
            {
                Console.Write("{0} ", i * a - b);
                if (i * a - b > 999.0)
                {
                    Console.WriteLine(i);
                    break;
                }
            }

        }//end of Main()

