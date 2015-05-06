//Names scores



  static void Main(string[] args)
        {//C#方便之处:不用file open, file close, 不用exception handling. 
            ////method 1
            //string text = File.ReadAllText(@"D:\shao\csharp\names.txt");
            //Console.WriteLine("The text is: \n"+text);

            ////method 2
            //string[] lines = File.ReadAllLines(@"D:\shao\csharp\names.txt");
            //foreach (string line in lines)
            //{
            //    Console.WriteLine("\t" + line);
            //}

            string text = File.ReadAllText(@"d:\shao\csharp\names.txt");
            text = text.Replace("\"", "");
            string[] split = text.Split(new char[] { ','});
            Array.Sort<string>(split);

            int index = 0;
            int sumForLine = 0;
            int sum = 0;
            for (int i = 0; i < split.Length; i++)
            {
                index++;
                char[] cArray = split[i].ToCharArray();
                foreach (var c in cArray)
                {
                    sumForLine += c - 'A' + 1;
                }
                //Console.WriteLine(split[i].ToString());
                Console.WriteLine("{0}: {1}*{2}", split[i], sumForLine, index);
                sum += sumForLine * index;
                sumForLine = 0;
            }

            //another method of access an array
            //foreach (var line in split)
            //{
            //    index++;
            //    char[] cArray = line.Trim().ToCharArray();
            //    foreach (var c in cArray)
            //    {
            //        sumForLine += c - 'A' + 1;
            //    }
            //    //Console.WriteLine(split[i].ToString());
            //    Console.WriteLine("{0}: {1}*{2}", line, sumForLine, index);
            //    sum += sumForLine * index;
            //    sumForLine = 0;
            //}

            Console.WriteLine("The sum is {0}", sum);
        }//end of Main()