//Coin sums


static void Main(string[] args)
        {
            int count = 1;//a L2.

            int sum = 200;
            int n1 = 100;
            int n2 = 50;
            int n3 = 20;
            int n4 = 10;
            int n5 = 5;
            int n6 = 2;
            int n7 = 1;

            for(int a1=sum/n1; a1>=0; a1--)
                for (int a2 = sum / n2; a2 >= 0; a2--)
                    for (int a3 = sum / n3; a3 >= 0; a3--)
                        for (int a4 = sum / n4; a4 >= 0; a4--)
                            for (int a5 = sum / n5; a5 >= 0; a5--)
                                for (int a6 = sum / n6; a6 >= 0; a6--)
                                    for (int a7 = sum / n7; a7 >= 0; a7--)
                                    {
                                        if (a1 * n1 + a2 * n2 + a3 * n3 + a4 * n4 + a5 * n5 + a6 * n6 + a7 * n7 == sum)
                                            count++;
                                    }


            Console.WriteLine("\nThe number of ways is {0}", count);            
            Console.ReadKey();
        }//end of Main()