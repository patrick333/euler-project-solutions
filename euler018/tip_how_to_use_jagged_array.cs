//jagged array in C#
    static void Main(string[] args)

        {

            int[,] a = new int[2, 2] {  {1,2}, {1,5}   };


            int[][] b = new int[3][];

            for(int i=0; i<b.Length;i++) {

                b[i] = new int[4];

            }


            Console.WriteLine(a[0,1]);

            Console.WriteLine(b[0][1]);

        }