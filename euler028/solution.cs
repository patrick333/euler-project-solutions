//Number spiral diagonals

static void Main(string[] args)
        {
            uint first = 0;
            uint sec = 0;
            uint third = 0;
            uint last = 1;
            ulong sum=1;
            uint pace = 0;
            for (uint i = 3; i <= 1001; i += 2)
            {
                pace=i-1;
                first = last + pace;
                sec = first + pace;
                third = sec + pace;
                last = third + pace;
                sum += first + sec + third + last;
                Console.WriteLine("{0} {1} {2} {3}", first, sec, third, last);
            }

            Console.WriteLine(sum);
            Console.ReadKey();
        }//end of Main()

